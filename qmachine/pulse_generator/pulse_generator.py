# from config import config
from qm.qua import program,for_,stream_processing,declare,declare_stream,wait,measure,play,save,fixed,demod,ramp,amp,if_,elif_,else_,align, ramp_to_zero
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from qm import generate_qua_script

import pandas
import numpy as np
import matplotlib.pyplot as plt
import pprint

from xarray import corr

class Pulser():
    def __init__(self,config,measpulse = 'readout_pulse_10us') -> None:
        self.config=config

        self.channels=['ch1','ch2']
        
        self.channel_dict={'ch1':'gate_36' , 'ch2':'gate_29', 'm11':'bottom_right_DQD_readout' , 'm22':'bottom_right_DQD_readout'}
        self.meas_dict={'full':demod.full , 'sliced':demod.sliced}

        self.action_dict={'hold':self._make_wait , 'step':self._make_step , 'ramp':self._make_ramp, 'meas':self._make_meas,'ramp_to_zero':self._make_ramp_to_zero}
        
        self.cw_conversion=1/config['waveforms']['const_wf']['sample']
        self.readout_length=config['pulses'][measpulse]['length']
        print(f'readout length: {self.readout_length}ns')

        # self.open_qm(config)

    def simulate_pulse(self,pulsing_sequence,simulation_time,close_others=False):
        if not hasattr(self,'qm'):
            self.open_qm(self.config,close_others)
        fig,ax=None,None
        job = self.qm.simulate(pulsing_sequence, SimulationConfig(simulation_time))
        samples = job.get_simulated_samples()
        samples.con1.plot()
        # fig,ax=self._plot_simulated_pulse(samples)
        return job, samples ,(fig,ax)

    def seq_to_py(self,seq,filename):
        with open(filename,'w') as file:
            print(generate_qua_script(seq,self.config) , file = file)
    
    def _plot_simulated_pulse(self,samples,meas_channel=1):
        fig,ax=plt.subplots()
        ax2=ax.twinx()
        measurement_on_points=np.where(samples.con1.analog[str(meas_channel)]!=0)
        ax.plot(samples.con1.analog['3'],label='ch2')
        ax.plot(samples.con1.analog['2'],label='ch1')
        # ax.hlines(0,0,len(samples.con1.analog['3']))
        # fig.canvas.draw()
        # y_ticks=ax.get_yticklabels()
        # ax.set_yticklabels([float(y_tick.get_text())*1e3 for y_tick in y_ticks])
        # ax.set_ylabel('mV')
        ax2.plot(measurement_on_points,np.ones(len(measurement_on_points)),'.')
        ax2.set_ylim(0,1.05)
        fig.legend()
        plt.show()
        return fig,ax
        
        


    def open_qm(self,config,close_others=False):
        #load the quantum machine this should probably only be done when simulating/performing the pulse
        self.config=config
        self.qmm = QuantumMachinesManager(host='192.168.15.128',port=80)
        if close_others:
            self.qmm.close_all_quantum_machines()
        self.qm = self.qmm.open_qm(config,close_other_machines=False)
        print(f"quantum machine opened with channels {list(self.config['elements'].keys())}")
        print(f"default value for CW is: {self.config['waveforms']['const_wf']['sample']}")
        self.cw_conversion=1/self.config['waveforms']['const_wf']['sample']


    def build_seq(self,actions,buffer_size=0):
        temp_actions=actions.copy()
        with program() as sequence:
            # self.cw_conversion_dec =declare(fixed,value=self.cw_conversion)
            if 'm11' in temp_actions['channels'] or 'm12' in temp_actions['channels']: #changes here FB why m2?
                temp_actions = self._declare_measurements(temp_actions)

            if 'looped' in temp_actions.keys(): #changes here
                loop_indexes,temp_actions = self._declare_loops(temp_actions) #declare loop variables and return dict with loop indexes. and arrays to be looped over.       
                self._run_loops(loop_indexes=loop_indexes,actions=temp_actions,loop_nr=0) #run_loops will run a single with for_ loop and call itself within this loop. run_loops also will can _run_all_actions.
            else:
                self._run_all_actions(temp_actions) #if no loops are to be done it will just run all the actions.

            self._do_stream_processing(temp_actions,buffer_size)
        return sequence, temp_actions

    def _run_loops(self,loop_indexes,actions,loop_nr=0):
        #check if we are still supposed to loop more
        if loop_nr<len(loop_indexes): 
            loop_index=loop_indexes[str(loop_nr)]
            with for_(loop_index,0,loop_index<actions['looped'][int(loop_nr)],loop_index+1): #setup the loop
                loop_nr+=1
                self._run_loops(loop_indexes,actions,loop_nr) #call itself again going a loop deeper each time.
        else: #if no more looping.
            self._run_all_actions(actions,loop_indexes)

    def _run_all_actions(self,actions,loop_indexes=None): #this will just run all the actions
        for step,row_actions in actions['steps'].items():
            align(*[self.channel_dict[channel] for channel in row_actions.keys()])
            for key,channel_actions in row_actions.items(): #key should be changed to channel here
                if ('ch' in key or 'm' in key):
                    if channel_actions['looped']: #if a variable is looped it will have the different values it takes declared as an array on the OPX, this will tell python what that OPX variable is.
                        channel_actions['action_variables'][channel_actions['looper']]=channel_actions['loop_param'][loop_indexes[channel_actions['loop_index']]]

                    self._perform_action(channel_actions) 

    def _declare_loops(self,actions):
        loop_indexes={str(i):declare(int) for i in range(len(actions['looped']))} #declares all the loop indexes

        for step,row_actions in actions['steps'].items():
            for key,channel_actions in row_actions.items():
                if 'ch' in key:
                    if channel_actions['looped']: #declare only looped parameters
                        channel_actions['loop_param']=declare(fixed,value=channel_actions['action_variables'][channel_actions['looper']])
        return loop_indexes,actions

    def _declare_measurements(self,actions):
        k=1
        for step,row_actions in actions['steps'].items():
            for key,channel_actions in row_actions.items():
                # print(key) 
                if 'm' in key:
                    # print('m here')
                    if channel_actions['action_variables']['type']=='sliced':
                        # print('and here')
                        slice_length=self.readout_length/4/channel_actions["action_variables"]["slices"]
                        if not slice_length.is_integer():
                            raise Exception(f'readout length, {self.readout_length}, and number of slices, {channel_actions["action_variables"]["slices"]}, are incompatible, slice_length=readout_length/4/slices must be an integer')
                        slice_length=int(slice_length)
                        print(f'slice length (chunk size in qua terms)={slice_length}')

                        channel_actions['action_variables']['slice_length']=slice_length
                        channel_actions['action_variables']['save_I']=declare(fixed,size=channel_actions["action_variables"]["slices"]) #declare save variables
                        channel_actions['action_variables']['save_Q']=declare(fixed,size=channel_actions["action_variables"]["slices"])

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

        else:
            measure(variables['pulse'],self.channel_dict[channel],None,
                    self.meas_dict[variables['type']]('cos',variables['save_I'],variables['analog_output']), 
                    self.meas_dict[variables['type']]('sin',variables['save_Q'],variables['analog_output']))

            save(variables['save_I'],variables['save_I_stream'])
            save(variables['save_Q'],variables['save_Q_stream'])

    def _do_stream_processing(self,actions,buffer_size):
        with stream_processing():
            for step,row_actions in actions['steps'].items():
                for key,channel_actions in row_actions.items():
                    if 'm' in key:
                        if buffer_size!=0:
                            #some more things to be implemented: averaging, figure out buffer size rework
                            channel_actions['action_variables']['save_I_stream'].buffer(*channel_actions['action_variables']['buffer_size']).save_all(channel_actions['action_variables']['I_name']) #
                            channel_actions['action_variables']['save_Q_stream'].buffer(*channel_actions['action_variables']['buffer_size']).save_all(channel_actions['action_variables']['Q_name'])
                        else:
                            channel_actions['action_variables']['save_I_stream'].save_all(channel_actions['action_variables']['I_name']) #
                            channel_actions['action_variables']['save_Q_stream'].save_all(channel_actions['action_variables']['Q_name'])
class Pulse_builder():
    def __init__(self,dividers):
        self.dividers=dividers
        

    def make_dict(self,df,measpulse='readout_pulse_10us',averages=0,zero_offset=True,ramp_to_zero=True):
        df = df.copy()
        self.channels = [i for i in df.columns.values if 'ch' in i or 'm11' in i or 'm22' in i]
        self.current_position = {channel:[0] for channel in self.channels if 'ch' in channel}
        self.next_loop_index = {}

        self.actions_dict = {'steps':{},'channels':self.channels,'looped':[]}
        if averages!=0:
            self.actions_dict['looped'].append(averages)

        df['time'] = df['time'].map(lambda x : int(x/4*1000)) #time from us to clockcycles
        for channel in self.channels:
            if 'ch' in channel:
                self.next_loop_index[channel] = 0
                if averages!=0:
                    self.next_loop_index[channel]+=1
                df[channel] = df[channel].map(self._str_to_float)
                df[channel] = df[channel].map(self._apply_dividers(channel))

        self.in_loop = {ch : False for ch in self.channels}
        self.containts_loops = {ch : False for ch in self.channels}
        self.measpulse = measpulse

        for index,row in df.iterrows():
            self.actions_dict['steps'][str(index+1)]=self._identify_actions(row)

        if zero_offset:
            index+=2
            self.actions_dict['steps'][str(index)]={}
            for channel in self.channels:
                if 'ch' in channel:
                    self.actions_dict['steps'][str(index)][channel]=self._zero_avg_action(df,channel,correction_length=30000)

        if ramp_to_zero:
            index+=1
            self.actions_dict['steps'][str(index)]={}
            for channel in self.channels:
                if 'ch' in channel:
                    self.actions_dict['steps'][str(index)][channel]=self._ramp_to_zero_action(channel)

        if any(list(self.containts_loops.values())):
            if zero_offset:
                print('WARNING: Making zero offset is only done with innermost loop.') 
        
        return self.actions_dict, df

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
        return {'action':'hold' , 'channel':channel , 'action_variables':{'time':time},'looped':looped}

    def _step_action(self,channel,value,time,looped=False,looped_variable='step_value',loop_index=0):
        return {'action':'step' , 'channel':channel , 'action_variables':{'time':time,'step_value':value},'looped':looped,'looper':looped_variable,'loop_index':str(loop_index)}

    def _ramp_action(self,channel,rate,time,looped=False):
        return {'action':'ramp' , 'channel':channel , 'action_variables':{'time':time,'rate':rate},'looped':looped}

    def _meas_action(self,channel,type='full',pulse='readout_pulse_10us',looped=False,buffer_size=16,slices=100,analog_output='out1'):
        return {'action':'meas' , 'channel':channel , 'action_variables':{'type':type , 'pulse':pulse,'buffer_size':buffer_size,'slices':slices,'analog_output':analog_output},'looped':looped}

    def _ramp_to_zero_action(self,channel,time=1):
        return {'action':'ramp_to_zero','channel':channel,'action_variables':{'time':time},'looped':False}

    def _zero_avg_action(self,df,channel,correction_length=30000):
        corr_value = self._make_zero_avg(df,channel,correction_length)
        corr_value = corr_value - self.current_position[channel][-1]
        return {'action':'step','channel':channel,'action_variables':{'time':int(correction_length/4),'step_value':corr_value},'looper':'step_value','looped':self.containts_loops[channel],'loop_index':str(len(self.actions_dict['looped'])-1)}

    def _identify_actions(self,row):
        actions={}
        for channel in self.channels:
            action=self._channel_action(row[channel],channel)
            if not action=='do_nothing':
                actions[channel]=self._get_variables(action,row,channel)
        return actions

    def _channel_action(self,input,channel):
        if 'm' in channel:
            if input:
                return 'meas' 
            else:
                return 'do_nothing'
        else:
            if len(input)==1: #step or hold
                if self.in_loop:
                    return 'step'
                if input[0]==self.current_position[channel][-1]:
                    return 'hold'
                else:
                    return 'step' 

            elif len(input)==2: #ramp
                return 'ramp' 

            elif len(input)==3:
                return 'loop' 


    def _get_variables(self,action,row,channel):
        if action=='hold':
            return self._hold_action(channel,row['time'])

        if action=='step':
            if self.in_loop[channel]:
                return self._looped_return_step(row,channel)
            step=row[channel][0]-self.current_position[channel][-1]
            self.current_position[channel].append(row[channel][0]) #update position
            return self._step_action(channel,step,row['time'])

        if action=='ramp':
            rate=(row[channel][1]-self.current_position[channel][-1])/(row['time']*4) #times 4 to account for clockcycles to ns
            self.current_position[channel].append(row[channel][1])
            return self._ramp_action(channel,rate,row['time'])

        if action=='meas':
            # print(f'{row},{channel}')
            if channel=='m11':
                mtype = 'full'
            elif channel=='m22':
                # print('h')
                mtype = 'sliced'

            return self._meas_action(channel,mtype,self.measpulse,)

        if action=='loop':
            startvalue=row[channel][0]-self.current_position[channel][-1]
            endvalue=row[channel][1]-self.current_position[channel][-1]
            steps=row[channel][2]
            if len(self.actions_dict['looped'])<=self.next_loop_index[channel]:
                self.actions_dict['looped'].append(int(steps))
            self.in_loop[channel]=True
            self.containts_loops[channel]=True
            values = np.linspace(startvalue,endvalue,int(steps))
            self.current_position[channel].append(values)
            return self._step_action(channel,values,row['time'],looped='True',loop_index=self.next_loop_index[channel])

    def _looped_return_step(self,row,channel):
        values = row[channel][0]-self.current_position[channel][-1]
        self.current_position[channel].append(row[channel][0])
        self.next_loop_index[channel]+=1
        self.in_loop[channel]=False
        return self._step_action(channel,values,row['time'],looped='True',loop_index=self.next_loop_index[channel]-1)

    def _make_zero_avg(self,df,channel,correction_length=30000):
        correction_length=correction_length/4
        total_offset=0
        for index,row in df.iterrows():
            if len(row[channel])==1:
                total_offset+=row[channel][0]*row['time']
            if len(row[channel])==2:
                total_offset+=(row[channel][1]+row[channel][0])/2*row['time'] #ramp
            if len(row[channel])==3:
                total_offset+=np.linspace(row[channel][0],row[channel][1],int(row[channel][2]))*row['time']

        # print(f'{channel} correction: {-total_offset/correction_length}')
        return -total_offset/correction_length
