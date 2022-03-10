from qcodes.instrument.base import Instrument, Parameter
from typing import Dict, Optional, Sequence
from config import *
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
            n = declare(int)
            I = declare(fixed)
            Q = declare(fixed)
            I_stream = declare_stream()
            Q_stream = declare_stream()

            with for_(n,0,n<100,n+1):
                measure('readout_pulse_0_2', 'Q1_readout', None, demod.full('cos', I), demod.full('sin', Q))
                save(I, I_stream)
                save(Q, Q_stream)


            with stream_processing():
                I_stream.buffer(1).average().save('I')
                Q_stream.buffer(1).average().save('Q')

        self.dumbpulse = dumbpulse

        self.add_parameter(name='pulse_meas',
                           label='pulse_meas',
                           unit='Vh',
                           get_cmd=get_pulse)

    def run_dumbpulse(self):
        self.job = self.qm.execute(self.dumbpulse)

    def get_pulse(self):
        I_handle = self.job.result_handles.get('I')
        Q_handle = self.job.result_handles.get('Q')
        Q_handle.wait_for_all_values()
        I_handle.wait_for_all_values()
        results_I = I_handle.fetch_all()
        results_Q = Q_handle.fetch_all()
        # job.halt()
        return results_I**2 + results_Q**2
