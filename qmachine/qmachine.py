from qm.qua import wait_for_trigger,reset_phase,program,update_frequency,for_,stream_processing,declare,declare_stream,wait,measure,play,save,fixed,demod,ramp,amp,if_,elif_,else_,align, ramp_to_zero
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
import time as time
import numpy as np
from qcodes.instrument.base import Instrument
from qcodes.instrument.parameter import Parameter, ParameterWithSetpoints
from typing import Dict, Optional, Sequence
from qcodes.utils.validators import Numbers, Arrays

class QMachine(Instrument):

    def __init__(self, name, config,close_others=False,n_slices=100,single_averages=50,map_size=(50,50),map_averages=1, **kwargs):
        super().__init__(name, **kwargs)
        
        self.map_size=map_size
        self.map_averages=map_averages
        self.config=config
        self.readout_length=config['pulses']['readout_pulse_0_2']['length']
        # self.buffered_acq_id = self.buffered_acq(map_size,averages)
        self.qmm = QuantumMachinesManager(host='192.168.15.128',port=80)
        #qmm.close_all_quantum_machines()
        self.qm = self.qmm.open_qm(config, close_other_machines=close_others)

        self.single_pulse_id = self.single_value_measurement(single_averages)
        self.time_pulse_id = self.sliced_measurement(num_of_slices=n_slices,readout_length=self.readout_length)


        self.add_parameter(name="x_axis",
                            unit="s",
                            label="time",
                            parameter_class=GeneratedSetPoints,
                            startparam=0,
                            stopparam=self.readout_length*1e-9,
                            numpointsparam=n_slices,
                            vals=Arrays(shape=(n_slices,)),
                            )

        self.add_parameter(name="x_axis_buff",
                            unit="a.u.",
                            label="voltage ",
                            parameter_class=GeneratedSetPoints,
                            startparam=0,
                            stopparam=1,
                            numpointsparam=self.map_size[0],
                            vals=Arrays(shape=(self.map_size[0],)),
                            )
        
        self.add_parameter(name="y_axis_buff",
                            unit="a.u.",
                            label="voltage ",
                            parameter_class=GeneratedSetPoints,
                            startparam=0,
                            stopparam=1,
                            numpointsparam=self.map_size[1],
                            vals=Arrays(shape=(self.map_size[1],)),
                            )

        self.add_parameter(name='buffered_acq_phase',
                           label='Buffered_acq_phase',
                           unit='Vh',
                           vals=Arrays(shape=(self.map_size[0],self.map_size[1])), 
                           setpoints=(self.x_axis_buff,self.y_axis_buff),
                           parameter_class=buffered_pulse_class_phase)

        self.add_parameter(name='buffered_acq_amp',
                           label='Buffered_acq_amp',
                           unit='Vh',
                           vals=Arrays(shape=(self.map_size[0],self.map_size[1])), 
                           setpoints=(self.x_axis_buff,self.y_axis_buff),
                           parameter_class=buffered_pulse_class_amp)

        self.add_parameter(name='time_pulse_meas',
                           label='Time Pulse Meas',
                           unit='Vh',
                           vals=Arrays(shape=(n_slices,)),
                           setpoints=(self.x_axis,),
                           parameter_class=pulse_class)

        self.add_parameter(name='single_pulse_meas_amp',
                           label='single pulse meas amplitude',
                           unit='Vh',
                           get_cmd=self.get_single_pulse)

        self.add_parameter(name='single_pulse_meas_phase',
                           label='single pulse meas phase',
                           unit='a.u.',
                           get_cmd=self.get_single_pulse_phase)

    def prepare_buffered_acq(self,map_size,averages=1):
        self.map_size=map_size
        self.average=averages

        self.y_axis_buff.vals=Arrays(shape=(map_size[1],))
        self.y_axis_buff.num_points_param=map_size[1]
        
        self.x_axis_buff.vals=Arrays(shape=(map_size[0],))
        self.x_axis_buff.num_points_param=map_size[0]

        self.buffered_acq_phase.vals=Arrays(shape=(map_size[0],map_size[1]))
        self.buffered_acq_amp.vals=Arrays(shape=(map_size[0],map_size[1]))
        
        self.buffered_acq_id=self.buffered_acq(map_size,averages)

    def get_single_pulse(self):
        p_job = self.qm.queue.add_compiled(self.single_pulse_id)
        job=p_job.wait_for_execution()
        I_handle = job.result_handles.get('I')
        Q_handle = job.result_handles.get('Q')
        Q_handle.wait_for_all_values()
        I_handle.wait_for_all_values()
        results_I = I_handle.fetch_all()
        results_Q = Q_handle.fetch_all()
        job.halt()
        return np.sqrt(results_I**2 + results_Q**2)

    def get_single_pulse_phase(self):
        p_job = self.qm.queue.add_compiled(self.single_pulse_id)
        job=p_job.wait_for_execution()
        I_handle = job.result_handles.get('I')
        Q_handle = job.result_handles.get('Q')
        Q_handle.wait_for_all_values()
        I_handle.wait_for_all_values()
        results_I = I_handle.fetch_all()
        results_Q = Q_handle.fetch_all()
        job.halt()
        return np.arctan2(results_Q,results_I)

    def start_buffered_acq(self,):
        p_job = self.qm.queue.add_compiled(self.buffered_acq_id)
        self.buffered_acq_job=p_job.wait_for_execution()
        
    def get_buffered_acq_phase(self,job=None):
        job = self.buffered_acq_job
        I_handle = job.result_handles.get('I')
        Q_handle = job.result_handles.get('Q')
        Q_handle.wait_for_all_values()
        I_handle.wait_for_all_values()
        results_I = I_handle.fetch_all()
        results_Q = Q_handle.fetch_all()
        job.halt()
        return np.arctan2(results_Q,results_I)

    def get_buffered_acq_amp(self,job=None):
        job = self.buffered_acq_job
        I_handle = job.result_handles.get('I')
        Q_handle = job.result_handles.get('Q')
        Q_handle.wait_for_all_values()
        I_handle.wait_for_all_values()
        results_I = I_handle.fetch_all()
        results_Q = Q_handle.fetch_all()
        job.halt()
        return np.sqrt(results_Q**2+results_I**2)

    def buffered_acq(self,map_size,averages): 
        with program() as buff_pulse:
            avg=declare(int)
            n=declare(int) 
            I = declare(fixed)
            Q = declare(fixed)
            I_stream = declare_stream()
            Q_stream = declare_stream()
            # i = declare(int)
            total_pixels=int(np.prod(map_size))
            with for_(avg,0,avg<int(averages),avg+1):
                wait_for_trigger('bottom_right_DQD_readout')
                with for_(n, 0, n<total_pixels, n+1):
                    measure('readout_pulse_0_2', 'bottom_right_DQD_readout', None, demod.full('cos', I), demod.full('sin', Q))

                    save(I,I_stream)
                    save(Q,Q_stream)

                
            with stream_processing():
                I_stream.buffer(*map_size).save('I')
                Q_stream.buffer(*map_size).save('Q')
        # I_stream.save('I')
        # Q_stream.save('Q')
    
    
        return self.qm.compile(buff_pulse)

    def sliced_measurement(self,num_of_slices,readout_length):
        # num_of_slices = int(50)
        # readout_length=config['pulses']['readout_pulse_0_2']['length']
        # print(readout_length)
        slice_length = int((readout_length//4)/num_of_slices)  #//4 makes it into clock cycles
        # N = 1 
        # total_pulse_time = readout_length*N
        # N_time_pulse = N*num_of_slices

        with program() as time_pulse:
            # n=declare(int)
            I = declare(fixed,size=num_of_slices)
            Q = declare(fixed,size=num_of_slices)
            I_stream = declare_stream()
            Q_stream = declare_stream()
            i = declare(int)
            # with for_(n, 0, n<int(N), n+1):
            measure('readout_pulse_0_2', 'bottom_right_DQD_readout', None, demod.sliced('cos', I, slice_length, 'out1'), demod.sliced('sin', Q, slice_length, 'out1'))
            with for_(i, 0, i<num_of_slices, i+1):
                save(I[i], I_stream)
                save(Q[i], Q_stream)

                    
            with stream_processing():
                I_stream.buffer(num_of_slices).save('I')
                Q_stream.buffer(num_of_slices).save('Q')

        return self.qm.compile(time_pulse)

    def single_value_measurement(self,num_of_averages):
        # num_of_averages=1000
        with program() as single_pulse:
            n=declare(int) 
            I = declare(fixed)
            Q = declare(fixed)
            I_stream = declare_stream()
            Q_stream = declare_stream()
            # i = declare(int)
            with for_(n, 0, n<num_of_averages, n+1):
                measure('readout_pulse_0_2', 'bottom_right_DQD_readout', None, demod.full('cos', I), demod.full('sin', Q))
                save(I,I_stream)
                save(Q,Q_stream)

                    
            with stream_processing():
                I_stream.buffer(1).average().save('I')
                Q_stream.buffer(1).average().save('Q')
                # I_stream.save('I')
                # Q_stream.save('Q')

        return self.qm.compile(single_pulse)



    def get_time_pulse(self):
        p_job = self.qm.queue.add_compiled(self.time_pulse_id)
        job=p_job.wait_for_execution()
        I_handle = job.result_handles.get('I')
        Q_handle = job.result_handles.get('Q')
        Q_handle.wait_for_all_values()
        I_handle.wait_for_all_values()
        results_I = I_handle.fetch_all()
        results_Q = Q_handle.fetch_all()
        job.halt()
        return results_I**2 + results_Q**2


        
class pulse_class(ParameterWithSetpoints):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_raw(self):
        return self.root_instrument.get_time_pulse()

class buffered_pulse_class_phase(ParameterWithSetpoints):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_raw(self):
        return self.root_instrument.get_buffered_acq_phase()

class buffered_pulse_class_amp(ParameterWithSetpoints):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_raw(self):
        return self.root_instrument.get_buffered_acq_amp()
        

class GeneratedSetPoints(Parameter):
    """
    A parameter that generates a setpoint array from start, stop and num points
    parameters.
    """

    def __init__(self, startparam, stopparam, numpointsparam, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._startparam = startparam
        self._stopparam = stopparam
        self._numpointsparam = numpointsparam

    def get_raw(self):
        return np.linspace(self._startparam, self._stopparam, self._numpointsparam)
