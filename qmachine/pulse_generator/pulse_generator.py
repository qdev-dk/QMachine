# from config import config
from qm.qua import program,for_,stream_processing,declare,declare_stream,wait,measure,play,save,fixed,demod,ramp,amp,if_,elif_,else_,align
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig

import pandas
import numpy as np
import matplotlib.pyplot as plt
import pprint

class Pulser():
    def __init__(self,config) -> None:
        self.config=config

        self.channels=['ch1','ch2']
        
        self.channel_dict={'ch1':'Q1_L' , 'ch2':'Q1_R', 'm1':'Q2_readout'}
        self.meas_dict={'full':demod.full , 'sliced':demod.sliced}

        self.action_dict={'hold':self._make_wait , 'step':self._make_step , 'ramp':self._make_ramp, 'meas':self._make_meas}
        self.cw_conversion=1
        self.readout_length=config['pulses']['readout_pulse_0_2']['length']
        print(f'readout length: {self.readout_length}ns')

        # self.open_qm(config)

    def simulate_pulse(self,pulsing_sequence,simulation_time):
        if not hasattr(self,'qm'):
            self.open_qm(self.config)
        job = self.qm.simulate(pulsing_sequence, SimulationConfig(simulation_time))
        samples = job.get_simulated_samples()
        samples.con1.plot()
        # self._plot_simulated_pulse(samples)
        return job
    
    def _plot_simulated_pulse(self,samples,meas_channel=1):
        fig,ax=plt.subplots()
        ax2=ax.twinx()
        measurement_on_points=np.where(samples.con1.analog[str(meas_channel)]!=0)
        ax.plot(samples.con1.analog['3'])
        ax.plot(samples.con1.analog['2'])
        ax2.plot(measurement_on_points,np.ones(len(measurement_on_points)),'.')
        ax2.set_ylim(0,1.05)
        
        


    def open_qm(self,config):
        #load the quantum machine this should probably only be done when simulating/performing the pulse
        self.config=config
        self.qmm = QuantumMachinesManager(host='192.168.15.128',port=80)
        self.qmm.close_all_quantum_machines()
        self.qm = self.qmm.open_qm(config)
        print(f"quantum machine opened with channels {list(self.config['elements'].keys())}")
        print(f"default value for CW is: {self.config['waveforms']['const_wf']['sample']}")
        self.cw_conversion=1/self.config['waveforms']['const_wf']['sample']


    def build_seq(self,actions):
        temp_actions=actions.copy()
        with program() as sequence:
            if 'm1' in temp_actions['channels'] or 'm2' in temp_actions['channels']: #changes here
                temp_actions = self._declare_measurements(temp_actions)

            if 'looped' in temp_actions.keys(): #changes here
                loop_indexes,temp_actions = self._declare_loops(temp_actions) #declare loop variables and return dict with loop indexes. and arrays to be looped over.       
                self._run_loops(loop_indexes=loop_indexes,actions=temp_actions,loop_nr=0) #run_loops will run a single with for_ loop and call itself within this loop. run_loops also will can _run_all_actions.
            else:
                self._run_all_actions(temp_actions) #if no loops are to be done it will just run all the actions.

            self._do_stream_processing(temp_actions)
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
                if 'm' in key:
                    if channel_actions['action_variables']['type']=='sliced':
                        slice_length=int(self.readout_length/4/channel_actions["action_variables"]["slices"])
                        print(f'slice length={slice_length}')
                        channel_actions['action_variables']['slice_length']=slice_length
                        channel_actions['action_variables']['save_I']=declare(fixed,size=slice_length) #declare save variables
                        channel_actions['action_variables']['save_Q']=declare(fixed,size=slice_length)

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
        play('CW'*amp(variables['step_value']), self.channel_dict[channel], duration=variables['time'])

    def _make_meas(self,channel,variables):
        #this measure syntax only works for 'type'='full', will have to rewrite with if statements for 'sliced' and 'raw_adc' once that is implemented
        if variables['type']=='sliced':
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

    def _do_stream_processing(self,actions):
        with stream_processing():
            for step,row_actions in actions['steps'].items():
                for key,channel_actions in row_actions.items():
                    if 'm' in key:
                        # pprint.pprint(channel_actions)
                        #some more things to be implemented: averaging
                        # print(channel_actions['action_variables']['buffer_size'])
                        channel_actions['action_variables']['save_I_stream'].buffer(*channel_actions['action_variables']['buffer_size']).save(channel_actions['action_variables']['I_name'])
                        channel_actions['action_variables']['save_Q_stream'].buffer(*channel_actions['action_variables']['buffer_size']).save(channel_actions['action_variables']['Q_name'])


#below is legacy for now, will return to it when above is done.
class pulse_generator():
    def __init__(self,config):
        self.config=config
        self.position={'ch1':0,'ch2':0}

  
        self.channels=['ch1','ch2']
        
        self.channel_dict={'ch1':'Q1_L' , 'ch2':'Q1_R'}

        self.action_dict={'hold':self._make_wait , 'step':self._make_step , 'ramp':self._make_ramp, 'loop':self._make_step}

        self.open_qm(config)

        
    def make_pulse_from_df(self,df):
        self.other_cols=[i for i in df.columns.values if 'ch' not in i]
        dfcopy=df.copy(deep=True)
        dfcopy['time']=dfcopy['time'].apply(lambda x : int(x//4)) #converts time to clockcycles of the fpga (4ns)

        
        actions={ch : {} for ch in self.channels}
        for channel in self.channels:
            channel_df=dfcopy[[channel]+self.other_cols].copy(deep=True)

            for index,row in channel_df.iterrows():
                if isinstance(row[channel],(float,int)):
                    row[channel]=[row[channel]]
                actions[channel][str(index)]=self._identify_actions(row,channel)

                self._update_position(row,channel)
                # print(f'my position is now {self.position}')
                # print(f"this row {row[self.channels].values} was assigned this action {actions[-1][0][0],actions[-1][1][0]}")
        loops=self._check_loop(actions)
        if loops['found']:
            self._fix_loop_channel(loops['where'],actions)
        # return actions
        return self._build_seq(actions) , actions
        
    def simulate_pulse(self,pulsing_sequence,simulation_time):
        if not hasattr(self,'qm'):
            self.open_qm(self.config)
        job = self.qm.simulate(pulsing_sequence, SimulationConfig(simulation_time))
        samples = job.get_simulated_samples()
        samples.con1.plot()


    def open_qm(self,config):
        #load the quantum machine this should probably only be done when simulating/performing the pulse
        self.config=config
        self.qmm = QuantumMachinesManager(host='192.168.15.128',port=80)
        self.qmm.close_all_quantum_machines()
        self.qm = self.qmm.open_qm(config)
        print(f"quantum machine opened with channels {list(self.config['elements'].keys())}")
        print(f"default value for CW is: {self.config['waveforms']['const_wf']['sample']}")
        self.cw_conversion=1/self.config['waveforms']['const_wf']['sample']
    


    def _build_seq(self,actions):
        # loop_present=False
        # for ac in actions:
        #     for a in ac:
        #         if a[0]=='loop':
        #             loop_present=True
        #             loop_variables=a[2]
        #             print('loop_present')    

        with program() as sequence:
            #declare things
            # if loop_present:
            #     print('im here')
            #     self._make_the_loop(loop_variables,actions)
            # else:
            for i in range(len(actions['ch1'])):
                for ch in self.channels:
                    self._perform_action(actions[ch][str(i)])
        return sequence
    
 
    def _perform_action(self,action):
        self.action_dict[action['action']](action['channel'],action['action_variables'])

    
    def _update_position(self,row,channel):
        if len(row[channel])==3: #loop
            print('loop not implemented yet')

        elif len(row[channel])==2: #ramp move
            self.position[channel]=row[channel][1]
            
        else: #step or hold
            self.position[channel]=row[channel][0]

    def _check_loop(self,actions):
        loops={'where':{ch:[] for ch in self.channels}, 'found':False}
        for channel,di in actions.items():
            for step,di2 in di.items():
                if di2['action']=='loop':
                    loops[channel].append(step)
                    loops['found']=True
                
        return loops
    
    def _fix_loop_channel(self,where,actions):
        print('fix the loop channel')

    def _make_wait(self,channel,variables):
        wait(variables['time'],self.channel_dict[channel])

    def _make_ramp(self,channel,variables):
        print(f'rate is {variables["rate"]}V/ns with time {variables["time"]*4}ns')
        play(ramp(variables['rate']), self.channel_dict[channel], duration=variables['time'])

    def _make_step(self,channel,variables):
        play('CW'*amp(self.cw_conversion*variables['step_value']), self.channel_dict[channel], duration=variables['time'])

    def _identify_actions(self,row,channel):
        # actions={}
        action=self._channel_action(channel,row[channel])
        action_variables=self._get_variables(action,row,channel)
        action={'action':action , 'channel':channel, 'action_variables':action_variables}
        return action

    def _get_variables(self,action,row,channel):
        if action=='hold':
            return {'time':row['time']}

        if action=='step':
            step=row[channel][0]-self.position[channel]
            return {'time':row['time'] , 'step_value':step}

        if action=='ramp':
            rate=(row[channel][1]-self.position[channel])/(row['time']*4) #times 4 to account for clockcycles to ns
            return {'rate':rate , 'time': row['time']}

        if action=='loop':
            startvalue=row[channel][0]-self.position[channel]
            endvalue=row[channel][1]-self.position[channel]
            steps=row[channel][2]
            stepsize=(endvalue-startvalue)/steps
            return {'time': row['time'] , 'stepsize':stepsize , 'start':startvalue, 'end':endvalue , 'steps':steps}


    def _channel_action(self,channel,input):
        if len(input)==1: #step or hold
            if input[0]==self.position[channel]:
                return 'hold'
            else:
                return 'step'    

        elif len(input)==2: #ramp
            return 'ramp'

        elif len(input)==3:
            return 'loop'