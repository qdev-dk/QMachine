from qcodes.instrument.base import Instrument
from qcodes.instrument.parameter import Parameter, ParameterWithSetpoints
from typing import Dict, Optional, Sequence
from qcodes.utils.validators import Numbers, Arrays
from qmachine.config import *
from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig

class QMachine(Instrument):

    def __init__(self, name, host, port, **kwargs):
        super().__init__(name, **kwargs)
        self.qmm = QuantumMachinesManager(host=host, port=port)
        self.qmm.close_all_quantum_machines()
        self.qm = self.qmm.open_qm(config)
        self.job = None


        with program() as dumbpulse:
            nn = declare(int)
            n = declare(int)
            I = declare(fixed)
            Q = declare(fixed)
            I_stream = declare_stream()
            Q_stream = declare_stream()
            with for_(nn,0,nn<2,nn+1):
                #pause()
                with for_(n,0,n<100,n+1):
                    measure('readout_pulse_0_2', 'Q1_readout', None, demod.full('cos', I), demod.full('sin', Q))
                    save(I, I_stream)
                    save(Q, Q_stream)


            with stream_processing():
                I_stream.buffer(1).average().save('I')
                Q_stream.buffer(1).average().save('Q')
            
            self.dumbpulse = dumbpulse

            ramp_time = 10e3//4  #//4 turns ns into clock cycles
            sweep_width = 50  #mV
            attenuation_L12 = 8.891
            rate = (sweep_width*attenuation_L12)*1e-3/(4*ramp_time)

            num_of_slices = 100
            slice_length = int(ramp_time//num_of_slices)

            da = 0.01


        with program() as twodscan:
            #From here
            a = declare(fixed)
            n = declare(int)
            I = declare(fixed, size=num_of_slices)
            Q = declare(fixed, size=num_of_slices)
            I_stream = declare_stream()
            Q_stream = declare_stream()
            i = declare(int)

            with for_(n, 0, n<2e3, n+1):  #number of averages
                with for_(a, 0.0, a < 1.0 - da*0.5, a + da):  #adding the '- da*0.5 ' makes it unequivocal that the last value is not included. this is important for looping over fixed/floating values. *0.5 is way faster than /2, as division adds a 400ns overhead.
                    # reset_phase('Q1_readout')  #legacy
                    play('CW'*amp(a), 'Q1_L', duration=ramp_time)
                    #wait(500, 'Q1_R')  #legacy
                    #wait(500, 'Q1_readout')  #legacy
                    play(ramp(rate), 'Q1_R', duration=ramp_time)
                    measure('readout_pulse_0_2', 'Q1_readout', None, demod.sliced('cos', I, slice_length, 'out1'), demod.sliced('sin', Q, slice_length, 'out1'))
                    with for_(i, 0, i<num_of_slices, i+1):
                        save(I[i], I_stream)
                        save(Q[i], Q_stream)
                    #wait(4000)  #legacy
            with stream_processing():
                I_stream.buffer(100,100).average().save('I')
                Q_stream.buffer(100,100).average().save('Q')
        self.twodscan = twodscan

        self.add_parameter(name='pulse_meas',
                           label='pulse_meas',
                           unit='Vh',
                           get_cmd=self.get_pulse)

        self.add_parameter("x_axis",
                            unit="Hz",
                            label="X Axis",
                            parameter_class=GeneratedSetPoints,
                            startparam=0,
                            stopparam=1,
                            numpointsparam=100,
                            vals=Arrays(shape=(100,)),
                            )

        self.add_parameter("y_axis",
                            unit="Hz",
                            label="Y Axis",
                            parameter_class=GeneratedSetPoints,
                            startparam=0,
                            stopparam=1,
                            numpointsparam=100,
                            vals=Arrays(shape=(100,)),
                            )

        self.add_parameter(name='scan2d',
                           label='scan2d',
                           unit='Vh',
                           vals=Arrays(shape=(100,100)),
                           setpoints=(self.x_axis, self.y_axis),
                           parameter_class=scan2d)
                        

    def run_dumbpulse(self):
        self.job = self.qm.execute(self.dumbpulse)

    def get_pulse(self):
        #self.job = self.qm.execute(self.dumbpulse)
        self.job.resume()
        I_handle = self.job.result_handles.get('I')
        Q_handle = self.job.result_handles.get('Q')
        Q_handle.wait_for_all_values()
        I_handle.wait_for_all_values()
        results_I = I_handle.fetch_all()
        results_Q = Q_handle.fetch_all()
        # job.halt()
        return results_I**2 + results_Q**2

    def get_scan2d(self):
        self.job = self.qm.execute(self.twodscan)
        I_handle = self.job.result_handles.get('I')
        Q_handle = self.job.result_handles.get('Q')
        I_handle.wait_for_all_values()
        Q_handle.wait_for_all_values()
        results_I = I_handle.fetch_all()
        results_Q = Q_handle.fetch_all()
        amplitude = results_I**2 + results_Q**2
        return amplitude

class scan2d(ParameterWithSetpoints):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_raw(self):
        return self.root_instrument.get_scan2d()


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