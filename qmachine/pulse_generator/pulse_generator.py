# from config import config
from copy import deepcopy
from qm.qua import program, for_, assign, reset_phase, stream_processing, switch_, case_, declare, declare_stream, wait, measure, play, save, fixed, demod, ramp, amp, if_, elif_, else_, align, ramp_to_zero
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from qm import generate_qua_script
from operator import itemgetter
from qualang_tools.bakery import baking

from functools import partial
import pandas
import numpy as np
import matplotlib.pyplot as plt
import pprint

from xarray import corr
from time import perf_counter

class Pulser():
    def __init__(self, config, measpulse='readout_pulse_10us', channel_dict = {'ch1': 'gate_36', 'ch2': 'gate_29', 'meas': 'bottom_right_DQD_readout'}) -> None:
        self.config = config
        self.channels = ['ch1', 'ch2']
        self.channel_dict = channel_dict
        self.meas_dict = {'full': demod.full, 'sliced': demod.sliced}
        self.action_dict = {'hold': self._make_wait,
                            'step': self._make_step,
                            'ramp': self._make_ramp,
                            'meas': self._make_meas,
                            'ramp_to_zero': self._make_ramp_to_zero,
                            'baked_waveform': self._build_arbitrary_waveform}

        self.cw_conversion = 1/config['waveforms']['const_wf']['sample']
        self.readout_length = config['pulses'][measpulse]['length']
        print(f'readout length: {self.readout_length}ns')
        self.measpulse = measpulse

    def simulate_pulse(self, pulsing_sequence, simulation_time, close_others=False):
        if not hasattr(self, 'qm'):
            self.open_qm(self.config, close_others)
        fig, ax = None, None
        job = self.qm.simulate(pulsing_sequence, SimulationConfig(simulation_time))
        samples = job.get_simulated_samples()
        samples.con1.plot()
        # fig,ax=self._plot_simulated_pulse(samples)
        return job, samples, (fig, ax)

    def seq_to_py(self, seq, filename):
        with open(filename, 'w') as file:
            print(generate_qua_script(seq, self.config), file=file)

    def _plot_simulated_pulse(self, samples, meas_channel=1):
        fig, ax = plt.subplots()
        ax2 = ax.twinx()
        measurement_on_points = np.where(samples.con1.analog[str(meas_channel)] != 0)
        ax.plot(samples.con1.analog['3'], label='ch2')
        ax.plot(samples.con1.analog['2'], label='ch1')
        # ax.hlines(0,0,len(samples.con1.analog['3']))
        # fig.canvas.draw()
        # y_ticks=ax.get_yticklabels()
        # ax.set_yticklabels([float(y_tick.get_text())*1e3 for y_tick in y_ticks])
        # ax.set_ylabel('mV')
        ax2.plot(measurement_on_points, np.ones(len(measurement_on_points)), '.')
        ax2.set_ylim(0, 1.05)
        fig.legend()
        plt.show()
        return fig, ax

    def open_qm(self, config, close_others=False):
        # load the quantum machine this should probably only be done when simulating/performing the pulse
        self.config = config
        self.qmm = QuantumMachinesManager(host='192.168.15.128', port=80)
        if close_others:
            self.qmm.close_all_quantum_machines()
        self.qm = self.qmm.open_qm(config, close_other_machines=False)
        print(f"quantum machine opened with channels {list(self.config['elements'].keys())}")
        print(f"default value for CW is: {self.config['waveforms']['const_wf']['sample']}")
        self.cw_conversion = 1 / self.config['waveforms']['const_wf']['sample']

    def build_seq(self, actions, buffer_size=0, average=False):
        temp_actions = deepcopy(actions)

        with program() as sequence:
            # self.cw_conversion_dec =declare(fixed,value=self.cw_conversion)
            if 'meas' in temp_actions['channels']:  # changes here FB why m2?
                temp_actions = self._declare_measurements(temp_actions)

            if 'looped' in temp_actions.keys():  # changes here
                self.loops = temp_actions['looped']
                loop_indexes, temp_actions = self._declare_loops(temp_actions)  # declare loop variables and return dict with loop indexes. and arrays to be looped over.       
                self._run_loops(loop_indexes=loop_indexes, actions=temp_actions, loop_nr=0)  # run_loops will run a single with for_ loop and call itself within this loop. run_loops also will can _run_all_actions.
            else:
                self._run_all_actions(temp_actions)  # if no loops are to be done it will just run all the actions.

            self._do_stream_processing(temp_actions, buffer_size, average)
        return sequence, temp_actions

    def _run_loops(self, loop_indexes, actions, loop_nr=0):
        # check if we are still supposed to loop more
        if loop_nr < len(loop_indexes):
            loop_index = loop_indexes[str(loop_nr)]
            with for_(loop_index, 0, loop_index < actions['looped'][int(loop_nr)], loop_index+1):  # setup the loop
                loop_nr += 1
                self._run_loops(loop_indexes, actions, loop_nr)  # call itself again going a loop deeper each time.
        else:  # if no more looping.
            self._run_all_actions(actions, loop_indexes)

    def _run_all_actions(self, actions, loop_indexes=None):  # this will just run all the actions
        for step, row_actions in actions['steps'].items():
            align(*[self.channel_dict[channel] for channel in row_actions.keys()])
            for key, channel_actions in row_actions.items():  # key should be changed to channel here
                if ('ch' in key or 'm' in key):
                    if channel_actions['looped']:  # if a variable is looped it will have the different values it takes declared as an array on the OPX, this will tell python what that OPX variable is.
                        if isinstance(channel_actions['loop_index'], list):
                            if channel_actions['action'] == 'step':  # this case is likely only relevant for the corrD pulse with multiple loops.
                                actual_index = declare(int, value = 0)
                                assign(actual_index,
                                       (loop_indexes[channel_actions['loop_index'][0]] * self.loops[int(channel_actions['loop_index'][0])] +
                                        loop_indexes[channel_actions['loop_index'][1]]))
                                # channel_actions['action_variables'][channel_actions['looper']] = channel_actions['loop_param'][channel_actions['looper']][list_of_indexes[0]*loop_indexes[0][1]+list_of_indexes[1]]
                                self._assign_looper(channel_actions['looper'],channel_actions,loop_index=actual_index)
                            elif isinstance(channel_actions['looper'], list):  # this should be the general case
                                waveform_loop = False
                                for i, looper in enumerate(channel_actions['looper']):
                                    if looper == 'waveform':
                                        waveform_loop = True
                                        waveform_loop_index = i
                                        continue
                                    else:
                                        self._assign_looper(looper, channel_actions, loop_indexes[channel_actions['loop_index'][i]])
                                
                                if waveform_loop:
                                    # print('here2')
                                    with switch_(loop_indexes[channel_actions['loop_index'][waveform_loop_index]], unsafe=True):
                                        for j in range(actions['looped'][int(channel_actions['loop_index'][waveform_loop_index])]):
                                            with case_(j):
                                                self._assign_looper('waveform', channel_actions, j)
                                                # channel_actions['action_variables']['waveform'] = channel_actions['loop_param']['waveform'][j]
                                                self._perform_action(channel_actions)
                                    continue
                        else:
                            # print('here')
                            if channel_actions['action'] == 'baked_waveform':  # handling baked waveform looping
                                # print('hhh')
                                with switch_(loop_indexes[channel_actions['loop_index']], unsafe=True):
                                    for j in range(actions['looped'][int(channel_actions['loop_index'])]):
                                        with case_(j):
                                            # channel_actions['action_variables'][channel_actions['looper']] = channel_actions['loop_param'][j]
                                            self._assign_looper('waveform', channel_actions, j)
                                            self._perform_action(channel_actions)
                                continue
                            else:  # regular single loop and non baked waveform.
                                self._assign_looper(channel_actions['looper'], channel_actions, loop_indexes[channel_actions['loop_index']])
                                # channel_actions['action_variables'][channel_actions['looper']] = channel_actions['loop_param'][loop_indexes[channel_actions['loop_index']]]
                    # print(channel_actions['action'])
                    self._perform_action(channel_actions)

    def _assign_looper(self, looper, channel_actions, loop_index):
        if channel_actions['action'] == 'baked_waveform' and looper == 'step_value':
            # print('hkhk')
            channel_actions['action_variables']['step_value_ch1'] = channel_actions['loop_param'][looper]['ch1'][loop_index]
            channel_actions['action_variables']['step_value_ch2'] = channel_actions['loop_param'][looper]['ch2'][loop_index]
        else:
            channel_actions['action_variables'][looper] = channel_actions['loop_param'][looper][loop_index]


    def _declare_loops(self, actions):
        loop_indexes = {str(i): declare(int) for i in range(len(actions['looped']))}  # declares all the loop indexes
        for step, row_actions in actions['steps'].items():
            for key, channel_actions in row_actions.items():
                if 'ch' in key:
                    if channel_actions['looped']:  # declare only looped parameters
                        if isinstance(channel_actions['looper'], list):
                            for looper in channel_actions['looper']:
                                self._declare_single_loop(looper, channel_actions)
                        else:
                            self._declare_single_loop(channel_actions['looper'], channel_actions)
        return loop_indexes, actions

    def _declare_single_loop(self, looper, channel_actions):
        if 'loop_param' not in channel_actions:
            channel_actions['loop_param'] = {}

        if looper == 'time':
            channel_actions['loop_param'][looper] = declare(int, value=channel_actions['action_variables'][looper])
        elif looper == 'waveform':  # for arbitrary waveforms being looped
            channel_actions['loop_param'][looper] = channel_actions['action_variables'][looper]
        elif channel_actions['action'] == 'baked_waveform' and looper == 'step_value':
            channel_actions['loop_param'][looper] = {'ch1': declare(fixed, value=channel_actions['action_variables']['step_value_ch1']),
                                                     'ch2': declare(fixed, value=channel_actions['action_variables']['step_value_ch2'])}
        else:
            channel_actions['loop_param'][looper] = declare(fixed, value=channel_actions['action_variables'][looper])

    def _declare_measurements(self, actions):
        k = 1
        for step, row_actions in actions['steps'].items():
            for key, channel_actions in row_actions.items():
                if 'meas' in key:
                    if channel_actions['action_variables']['type'] == 'sliced':
                        slice_length = self.readout_length / 4 / channel_actions["action_variables"]["slices"]
                        if not slice_length.is_integer():
                            raise Exception(f'readout length, {self.readout_length}, and number of slices, {channel_actions["action_variables"]["slices"]}, are incompatible, slice_length=readout_length/4/slices must be an integer')
                        slice_length = int(slice_length)
                        print(f'slice length (chunk size in qua terms)={slice_length}')

                        channel_actions['action_variables']['slice_length'] = slice_length
                        channel_actions['action_variables']['save_I'] = declare(fixed, size = channel_actions["action_variables"]["slices"]) #declare save variables
                        channel_actions['action_variables']['save_Q'] = declare(fixed, size = channel_actions["action_variables"]["slices"])

                        channel_actions['action_variables']['save_I_stream']=declare_stream() #declare streams
                        channel_actions['action_variables']['save_Q_stream']=declare_stream()

                        channel_actions['action_variables']['I_name']=f'I_{k}'
                        channel_actions['action_variables']['Q_name']=f'Q_{k}'
                        if not hasattr(self,'sliced_indexer'):
                            self.sliced_indexer=declare(int)
                        # pprint.pprint(channel_actions)

                    else:
                        channel_actions['action_variables']['save_I']=declare(fixed) #declare save variables
                        channel_actions['action_variables']['save_Q']=declare(fixed)

                        channel_actions['action_variables']['save_I_stream']=declare_stream() #declare streams
                        channel_actions['action_variables']['save_Q_stream']=declare_stream()

                        channel_actions['action_variables']['I_name']=f'I_{k}'
                        channel_actions['action_variables']['Q_name']=f'Q_{k}'
                    k+=1
        return actions
                    

                    
    def _perform_action(self,action):
        self.action_dict[action['action']](action['channel'],action['action_variables'])

    #the different actions implemented, this is where the QUA functions are being ran.
    def _make_wait(self,channel,variables):
        wait(variables['time'],self.channel_dict[channel])

    def _make_ramp(self,channel,variables):
        # print(f'rate is {variables["rate"]}V/ns with time {variables["time"]*4}ns')
        play(ramp(variables['rate']), self.channel_dict[channel], duration=variables['time'])

    def _make_step(self,channel,variables):
        #amp argument is limited to -2 to 2, cw conversion should likely be applied outside of this function, precalculating everything will reduce opx load.
        play('CW'*amp(variables['step_value']*self.cw_conversion), self.channel_dict[channel], duration=variables['time'])

    def _make_ramp_to_zero(self,channel,variables):
        ramp_to_zero(self.channel_dict[channel],variables['time'])

    def _build_arbitrary_waveform(self,channel,variables):
        # if not variables['step_value']==1:
        amp_array = [(self.channel_dict['ch1'],variables['step_value_ch1']),(self.channel_dict['ch2'],variables['step_value_ch2'])]
        # print(amp_array)
        # amp_array = [(gate,variables['step_value']) for gate,value in itemgetter(*self.channels)(self.channel_dict)]
        variables['waveform'].run(amp_array=amp_array)
        # else:
            # variables['waveform'].run()

    def _make_meas(self,channel,variables):
        if variables['type']=='sliced':
            # pprint.pprint(variables)
            measure(variables['pulse'],self.channel_dict[channel],None,
                    self.meas_dict[variables['type']]('cos',variables['save_I'],variables['slice_length'],variables['analog_output']), 
                    self.meas_dict[variables['type']]('sin',variables['save_Q'],variables['slice_length'],variables['analog_output']))
            # pprint.pprint(variables)
            with for_(self.sliced_indexer,0,self.sliced_indexer<variables['slices'],self.sliced_indexer+1):
                save(variables['save_I'][self.sliced_indexer],variables['save_I_stream'])
                save(variables['save_Q'][self.sliced_indexer],variables['save_Q_stream'])
                wait(10) #this is added to account for the stream saving rate. 

        else:
            measure(variables['pulse'],self.channel_dict[channel],None,
                    self.meas_dict[variables['type']]('cos',variables['save_I'],variables['analog_output']), 
                    self.meas_dict[variables['type']]('sin',variables['save_Q'],variables['analog_output']))

            save(variables['save_I'],variables['save_I_stream'])
            save(variables['save_Q'],variables['save_Q_stream'])
        reset_phase(self.channel_dict[channel])

    def _do_stream_processing(self,actions,buffer_size,average=False):
        with stream_processing():
            for step,row_actions in actions['steps'].items():
                for key,channel_actions in row_actions.items():
                    if 'm' in key:
                        if buffer_size!=0:
                            #some more things to be implemented: averaging, figure out buffer size rework
                            if not average:
                                channel_actions['action_variables']['save_I_stream'].buffer(*buffer_size).save_all(channel_actions['action_variables']['I_name']) #
                                channel_actions['action_variables']['save_Q_stream'].buffer(*buffer_size).save_all(channel_actions['action_variables']['Q_name'])
                            if average:
                                channel_actions['action_variables']['save_I_stream'].buffer(*buffer_size).average().save(channel_actions['action_variables']['I_name']) #
                                channel_actions['action_variables']['save_Q_stream'].buffer(*buffer_size).average().save(channel_actions['action_variables']['Q_name'])
                        
                        else:
                            channel_actions['action_variables']['save_I_stream'].save_all(channel_actions['action_variables']['I_name']) #
                            channel_actions['action_variables']['save_Q_stream'].save_all(channel_actions['action_variables']['Q_name'])

class Pulse_builder():
    def __init__(self,dividers, channel_dict={'ch1': 'gate_36', 'ch2': 'gate_29', 'meas': 'bottom_right_DQD_readout'}):
        self.dividers=dividers
        self.channel_dict = channel_dict 
        

    def make_dict(self,df,config=None,measpulse='readout_pulse_10us',averages=0,zero_offset=True,ramp_to_zero=True,correction_length=30):
        if config != None:
            self.config = config

        self.original_df = deepcopy(df)
        # print(self.original_df)
        df = deepcopy(df)
        

        self.channels = ['ch1','ch2','meas','time'] #time must be last see (!1)
        self.current_position = {channel:[0] for channel in self.channels if 'ch' in channel}
        

        self.actions_dict = {'steps':{},'channels':self.channels,'looped':[]}
        if averages!=0:
            self.actions_dict['looped'].append(averages)

        df['time'] = df['time'].map(self._str_time_to_int) #time from us to clockcycles

        if averages!=0:
                df['loops'] = df['loops'].map(lambda x : int(x)+1 if not np.isnan(x) else np.nan)

        for channel in self.channels:
            if 'ch' in channel:
                df[channel] = df[channel].map(self._str_to_float)
                df[channel] = df[channel].map(self._apply_dividers(channel))

        self.new_loops_to_int = partial(self._loops_nan_to_int,averages=averages)
        df['loops'] = df['loops'].map(self.new_loops_to_int)
        df['meas'] = df['meas'].map(lambda x : int(x))

        self.in_loop = {ch : False for ch in self.channels}
        self.contains_loops = {ch : False for ch in self.channels}
        self.measpulse = measpulse

        for index,row in df.iterrows():
            self.actions_dict['steps'][str(index+1)]=self._identify_actions(row)

        if zero_offset:
            index=int(list(self.actions_dict['steps'].keys())[-1])+1
            self.actions_dict['steps'][str(index)]={}
            for channel in self.channels:
                if 'ch' in channel:
                    self.actions_dict['steps'][str(index)][channel]=self._zero_avg_action(df,channel,correction_length=(correction_length*1e3))

        if ramp_to_zero:
            index=int(list(self.actions_dict['steps'].keys())[-1])+1
            self.actions_dict['steps'][str(index)]={}
            for channel in self.channels:
                if 'ch' in channel:
                    self.actions_dict['steps'][str(index)][channel]=self._ramp_to_zero_action(channel)

        if any(list(self.contains_loops.values())):
            if zero_offset:
                print('WARNING: Making zero offset is only tested properly with 1 loop max') 
        
        return self.actions_dict, df

    def _str_time_to_int(self,input):
        # print(input)
        if isinstance(input,float):
            input=[int(input*1000/4)]
            return input
        input = input.split(',')
        input = [float(i) for i in input]
        # print(input)
        for i,n in enumerate(input):
            if i<2:
                input[i]=int(n*1000/4)
                # print(input[i])
            if i>=2:
                input[i]=int(n)
        return input

    def _loops_nan_to_int(self,input,averages=0):
        if averages != 0:
            if isinstance(input,(list,np.ndarray)):
                return [int(inp+1) for inp in input]
            elif np.isnan(input):
                return np.nan
            else: 
                return int(input+1)
        else:
            if isinstance(input,(list,np.ndarray)):
                return [int(inp) for inp in input]
            elif np.isnan(input):
                return np.nan
            else: 
                return int(input)



    def _str_to_float(self,input):
        input = input.split(',')
        input = [float(i) for i in input]
        return input

    def _apply_dividers(self,channel):
        def application(input):
            for i,n in enumerate(input):
                if i<2:
                    input[i]=n*self.dividers[channel]
            return input
        return application

    def _hold_action(self,channel,time,looped=False):
        return {'action':'hold',
                'channel':channel,
                'action_variables':{'time':time},
                'looped':looped}

    def _step_action(self,channel,value,time,looped=False,looped_variable='step_value',loop_index=-1):
        return {'action':'step',
                'channel':channel,
                'action_variables':{'time':time,'step_value':value},
                'looped':looped,
                'looper':looped_variable,
                'loop_index':str(int(loop_index))}

    def _ramp_action(self,channel,rate,time,looped=False):
        return {'action':'ramp',
                'channel':channel,
                'action_variables':{'time':time,'rate':rate},
                'looped':looped}

    def _meas_action(self,channel,type='full',pulse='readout_pulse_10us',looped=False,slices=100,analog_output='out1'):
        return {'action':'meas',
                'channel':channel,
                'action_variables':{'type':type,
                                    'pulse':pulse,
                                    'slices':slices,
                                    'analog_output':analog_output},
                'looped':looped}

    def _ramp_to_zero_action(self,channel,time=1):
        return {'action':'ramp_to_zero',
                'channel':channel,
                'action_variables':{'time':time},
                'looped':False}

    def _baked_action(self, channel, baked_waveform, looped=False, step_value_ch1=1, step_value_ch2=1, looped_variable='waveform',loop_index=0):
        if isinstance(loop_index, list):
            loop_index = [str(int(i)) for i in loop_index]
        else:
            loop_index = str(int(loop_index))
        return {'action':'baked_waveform',
                'channel':channel,
                'action_variables':{'waveform':baked_waveform,
                                    'step_value_ch1':step_value_ch1,
                                    'step_value_ch2':step_value_ch2},
                'looped':looped,
                'looper':looped_variable,
                'loop_index':loop_index}

    def _zero_avg_action(self,df,channel,correction_length=30000):
        corr_value,avg_loop_indexes = self._make_zero_avg(df,channel,correction_length)
        corr_value = corr_value - self.current_position[channel][-1]

        if isinstance(avg_loop_indexes, list):
            if len(avg_loop_indexes)==1:
                loop_index = str(int(avg_loop_indexes[0]))
            else:
                loop_index = [str(int(i)) for i in avg_loop_indexes]
        else:
            loop_index = str(int(avg_loop_indexes))

        if len(avg_loop_indexes)==0 or (corr_value == corr_value[0]).all():
            corr_value = corr_value[0]

        

        return {'action':'step',
                'channel':channel,
                'action_variables':
                    {'time':int(correction_length/4),
                    'step_value':corr_value},
                'looper':'step_value',
                'looped':self.contains_loops[channel] or self.contains_loops['time'],
                'loop_index':loop_index}

    def _identify_actions(self, row):
        actions = {}

        #first check for baked waveform
        if self._channel_action(row['time'],'time') == 'baked_waveform':
            return self._get_variables('baked_waveform',row,'time',actions)

        for channel in self.channels: # time has to be the last to be checked, it changes the time values for all channels (!1)
            action = self._channel_action(row[channel], channel)
            if not action == 'do_nothing':
                if action == 'baked_waveform':
                    actions = self._get_variables(action,row,channel,actions)
                elif action != 'time_loop':
                    actions[channel] = self._get_variables(action, row, channel, actions)
                if action == 'time_loop':
                    actions = self._get_variables(action, row, channel, actions)
        return actions

    def _channel_action(self, input, channel):
        if channel == 'meas':
            if input > 0:
                return 'meas' 
            else:
                return 'do_nothing'

        elif channel == 'time':
            if (np.array(input) < 4).any():
                return 'baked_waveform'
            if len(input) == 3:
                return 'time_loop'
            else:
                return 'do_nothing'

        else:
            if len(input) == 1: #step or hold
                if self.in_loop:
                    return 'step'
                if input[0] == self.current_position[channel][-1]:
                    return 'hold'
                else:
                    return 'step' 

            elif len(input) == 2: #ramp
                return 'ramp' 

            elif len(input) == 3:
                return 'loop' 


    def _get_variables(self,action,row,channel,actions):
        if action=='hold':
            return self._hold_action(channel,row['time'][0])

        if action=='step':
            if self.in_loop[channel]:
                if np.isnan(row['loops']):
                    raise Exception('loop not specified on return step, will have to fix it later, for now, specify in row')
                # print(action,channel,row)
                #this is likely a bit of a cut corner and if there are segments occuring inbetween finishing the loop, it is not correct
                return self._looped_return_step(row,channel)
            step=row[channel][0]-self.current_position[channel][-1]
            self.current_position[channel].append(row[channel][0]) #update position
            return self._step_action(channel,step,row['time'][0])

        if action=='ramp':
            rate=(row[channel][1]-self.current_position[channel][-1])/(row['time'][0]*4) #times 4 to account for clockcycles to ns
            self.current_position[channel].append(row[channel][1])
            return self._ramp_action(channel,rate,row['time'][0])

        if action=='meas':
            if row[channel]==1:
                mtype = 'full'
            elif row[channel]>1:
                mtype = 'sliced'

            return self._meas_action(channel, mtype, pulse=self.measpulse, slices=row[channel])

        if action=='loop': 
            if np.isnan(row['loops']):
                raise Exception(f'looped action with no specified loop index in row:{row.Index}')
            startvalue = row[channel][0]-self.current_position[channel][-1]
            endvalue = row[channel][1]-self.current_position[channel][-1]
            steps = row[channel][2]
            if len(self.actions_dict['looped'])<=row['loops']:
                self.actions_dict['looped'].append(int(steps))
            self.in_loop[channel]=True
            self.contains_loops[channel]=True
            values = np.linspace(startvalue,endvalue,int(steps))
            self.current_position[channel].append(np.linspace(row[channel][0],row[channel][1],int(row[channel][2])))
            return self._step_action(channel,values,row['time'][0],looped='True',loop_index=row['loops'])

        if action=='time_loop':
            # step = str(row[0])
            values = (np.linspace(row['time'][0]*4,row['time'][1]*4,row['time'][2],dtype=int)//4).tolist()
            if self.in_loop['time']: #for now i assume only 1 time loop
                self.in_loop[channel]=False
                loop_index = row['loops']
            else:
                self.actions_dict['looped'].append(row['time'][2])
                self.in_loop[channel]=True
                self.contains_loops[channel]=True
                loop_index = row['loops']

                # self.next_loop_index[channel] +=1

            actions=self._add_time_loop(values,'ch1',loop_index,actions)
            actions=self._add_time_loop(values,'ch2',loop_index,actions)
            return actions
        
        if action == 'baked_waveform':
            looped=False
            looped_variable = []
            if not hasattr(self,'config'):
                raise Exception('config must be provided if baked waveforms are needed.')
            waveforms, step_value_ch1, step_value_ch2 = self._bake_waveforms(self.config, row)
            if isinstance(waveforms, list):
                looped=True
                looped_variable.append('waveform')
                self.actions_dict['looped'].append(len(waveforms))

            if isinstance(step_value_ch1, (list, np.ndarray)) or isinstance(step_value_ch2, (list, np.ndarray)):
                looped=True
                looped_variable.append('step_value')
                self.actions_dict['looped'].append(len(step_value_ch1))
            actions = {}
            actions['ch1']=self._baked_action('ch1', waveforms, looped=looped, step_value_ch1=step_value_ch1, step_value_ch2=step_value_ch2, looped_variable=looped_variable, loop_index=row['loops'])
            return actions
                    
                
    def _add_time_loop(self,values,channel,loop_index,actions):
        actions[channel]['looper']='time'
        actions[channel]['looped']=True
        actions[channel]['loop_index']=str(int(loop_index))
        actions[channel]['action_variables']['time']=values
        return actions
        
        

    def _looped_return_step(self,row,channel):
        values = row[channel][0]-self.current_position[channel][-1]
        self.current_position[channel].append(row[channel][0])
        # self.next_loop_index[channel]+=1
        self.in_loop[channel]=False
        return self._step_action(channel,values,row['time'][0],looped='True',loop_index=row['loops'])

    def _make_zero_avg(self,df,channel,correction_length=30000):
        total_offset=0
        correction_length=correction_length/4
        offset_shape=None
        averaging_loop_indexes = []
        
        for index,row in df.iterrows():
            if not isinstance(total_offset,(float,int)):
                offset_shape = total_offset.shape

            if len(row['time'])==1:
                time=np.array(row['time'][0])
            elif len(row['time'])==3:
                time=np.linspace(*row['time'])
                if isinstance(row['loops'], list):
                    averaging_loop_indexes.append(row['loops'][0])    
                else:
                    averaging_loop_indexes.append(row['loops'])
                # if offset_shape!=None:
                #     time = time[np.newaxis,:]


            if len(row[channel])==1:
                total_offset+=row[channel][0]*time
            if len(row[channel])==2:
                total_offset+=(row[channel][1]+row[channel][0])/2*time #ramp
            if len(row[channel])==3:
                if isinstance(row['loops'], list):
                    averaging_loop_indexes.append(row['loops'][1])    
                else:
                    averaging_loop_indexes.append(row['loops'])
                    
                if not isinstance(time,(float,int)):
                    value = np.linspace(row[channel][0],row[channel][1],int(row[channel][2]))
                    mtime,mvalue=np.meshgrid(time,value,indexing='ij')
                    total_offset += mtime*mvalue
                else:
                    total_offset+=np.linspace(row[channel][0],row[channel][1],int(row[channel][2]))*time

        # print(f'{channel} correction: {-total_offset/correction_length}')
        # print(averaging_loop_indexes)
        return (-total_offset/correction_length).flatten(),averaging_loop_indexes


    def _bake_waveforms(self,config,row):
        start_timing = perf_counter()
        if len(row['ch1']) > 1:
            self.contains_loops['ch1']=True
            ch1_step_values = (np.linspace(row['ch1'][0],row['ch1'][1],int(row['ch1'][2])) - self.current_position['ch1'][-1])*4  # *4 to account for the base height of the waveform
        else:
            ch1_step_values = (row['ch1'][0]-self.current_position['ch1'][-1])*4 

        if len(row['ch2']) > 1:
            self.contains_loops['ch2']=True
            ch2_step_values = (np.linspace(row['ch2'][0],row['ch2'][1],int(row['ch2'][2])) - self.current_position['ch2'][-1])*4  # *4 to account for the base height of the waveform
        else:
            ch2_step_values = (row['ch2'][0]-self.current_position['ch2'][-1])*4 

        
        original_time = self.original_df['time'].iloc[int(row.name)]
        # print(original_time)
        original_time = original_time.split(',')
        original_time = [float(ti) for ti in original_time]
        
        if len(row['time']) == 1:
            time = int(original_time[0]*1000)
            if not time % 4 == 0 or time>16:
                print(f'Padding left is enabled for baked waveform with time {time}ns')
            with baking(config, padding_method = 'left') as baked_waveforms:
                waveform = [0.25] * time + [0]

                b.add_op('ch1_pulse', self.channel_dict['ch1'], waveform)
                b.add_op('ch2_pulse', self.channel_dict['ch2'], waveform)

                b.play('ch1_pulse', self.channel_dict['ch1'])
                b.play('ch2_pulse', self.channel_dict['ch2'])
                
        else:
            self.contains_loops['time']=True
            start_time = int(original_time[0]*1000)
            stop_time = int(original_time[1]*1000)
            steps = int(original_time[2])
            # print(start_time,stop_time,steps)
            stepsize = (stop_time-start_time) // steps
            base_length = stop_time + 4 - (stop_time % 4) 
            baked_waveforms = []
            for t in np.arange(start_time, stop_time, stepsize):
                with baking(config, padding_method = 'none') as b:
                    waveform = [0] * (base_length - t - 1) + [0.25] * t + [0]
                    # waveform_ch2 = [0] * (base_length - t - 1) + [0.25] * t + [0]

                    b.add_op('ch1_pulse', self.channel_dict['ch1'], waveform)
                    b.add_op('ch2_pulse', self.channel_dict['ch2'], waveform)

                    b.play('ch1_pulse', self.channel_dict['ch1'])
                    b.play('ch2_pulse', self.channel_dict['ch2'])

                baked_waveforms.append(b)
                # print(waveform)
        print(f'Baking waveforms took: {perf_counter()-start_timing:.2f}s')
        return baked_waveforms, ch1_step_values, ch2_step_values

            
