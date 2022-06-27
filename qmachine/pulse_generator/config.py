import numpy as np
#router ip 192.168.15.128

readout_length = 10000

Q1_readout_frequency = 156390000
Q2_readout_frequency = 129291200

#(156759540.0, 129291200.0)

config = {

    "version": 1,

    "controllers": {
        "con1": {

            "analog_outputs": {
                1: {"offset": 0.0},  # Readout
                3: {"offset": 0.0},  # Q1_R BNC12/j9
                2: {"offset": 0.0},  # Q1_L BNC10/j8
            },

            "digital_outputs": {
                1: {},
            },

            "analog_inputs": {
                1: {"offset": 0.21164},
                2: {"offset": 0.0},
            },

        }
    },

    "elements": {

        "Q1_R": {
            "singleInput": {
                "port": ("con1", 3)
            },
            'intermediate_frequency': 0e6,
            'hold_offset':{'duration': 100},
            'operations': {
                'CW': "CW",
            },
        },

        "Q1_L": {
            "singleInput": {
                "port": ("con1", 2)
            },
            'intermediate_frequency': 0e6,
            'hold_offset':{'duration': 100},
            'operations': {
                'CW': "CW",
            },
        },

        # "Q2_R": {
        #     "singleInput": {
        #         "port": ("con1", 4)
        #     },
        #     'intermediate_frequency': 0e6,
        #     'operations': {
        #         'CW': "CW",
        #     },
        # },

        # "Q2_L": {
        #     "singleInput": {
        #         "port": ("con1", 5)
        #     },
        #     'intermediate_frequency': 0e6,
        #     'operations': {
        #         'CW': "CW",
        #     },
        # },

        "Q1_readout": {
            "singleInput": {
              "port": ("con1", 1)
              },
            "intermediate_frequency": Q1_readout_frequency,
            "operations": {
                "readout_pulse_0_2": "readout_pulse_0_2",
                "readout_pulse_0_1": "readout_pulse_0_1",
                "readout_pulse_0_05": "readout_pulse_0_05",
                "readout_pulse_0_01": "readout_pulse_0_01",
                "readout_pulse_0_0001": "readout_pulse_0_0001",
            },
            "outputs": {"out1": ("con1", 1)},
            "time_of_flight": 180+190-2,
            "smearing": 0,
        },

        "Q2_readout": {
            "singleInput": {
                "port": ("con1", 1)
            },
            "intermediate_frequency": Q2_readout_frequency,
            "operations": {
                "readout_pulse_0_05": "readout_pulse_0_05",
                "readout_pulse_0_2": "readout_pulse_0_2",
            },
            "outputs": {"out1": ("con1", 1)},
            "time_of_flight": 180+190-2,
            "smearing": 0,
        },

    },

    "pulses": {

        "CW": {
            "operation": "control",
            "length": 100,
            "waveforms": {"single": "const_wf"},
        },

        "readout_pulse_0_2": {
            "operation": "measurement",
            "length": readout_length,
            "waveforms": {"single": "readout_wf_0_2"},
            "integration_weights": {
                "cos": "cos",
                "sin": "sin",
            },
            'digital_marker': 'ON'
        },
        "readout_pulse_0_1": {
            "operation": "measurement",
            "length": readout_length,
            "waveforms": {"single": "readout_wf_0_1"},
            "integration_weights": {
                "cos": "cos",
                "sin": "sin",
            },
            'digital_marker': 'ON'
        },
        "readout_pulse_0_05": {
            "operation": "measurement",
            "length": readout_length,
            "waveforms": {"single": "readout_wf_0_05"},
            "integration_weights": {
                "cos": "cos",
                "sin": "sin",
            },
            'digital_marker': 'ON'
        },
        "readout_pulse_0_01": {
            "operation": "measurement",
            "length": readout_length,
            "waveforms": {"single": "readout_wf_0_01"},
            "integration_weights": {
                "cos": "cos",
                "sin": "sin",
            },
            'digital_marker': 'ON'
        },
        "readout_pulse_0_001": {
            "operation": "measurement",
            "length": readout_length,
            "waveforms": {"single": "readout_wf_0_001"},
            "integration_weights": {
                "cos": "cos",
                "sin": "sin",
            },
            'digital_marker': 'ON'
        },
        "readout_pulse_0_0001": {
            "operation": "measurement",
            "length": readout_length,
            "waveforms": {"single": "readout_wf_0_0001"},
            "integration_weights": {
                "cos": "cos",
                "sin": "sin",
            },
            'digital_marker': 'ON'
        },



    },

    "waveforms": {

        "const_wf": {"type": "constant", "sample": 0.25}, #previously this "sample": 0.05*7.063 

        "zero_wf": {"type": "constant", "sample": 0.0},
        
        "readout_wf_0_2": {"type": "constant", "sample": 0.2},

        "readout_wf_0_1": {"type": "constant", "sample": 0.1},

        "readout_wf_0_05": {"type": "constant", "sample": 0.05},

        "readout_wf_0_01": {"type": "constant", "sample": 0.01},

        "readout_wf_0_001": {"type": "constant", "sample": 0.001},

        "readout_wf_0_0001": {"type": "constant", "sample": 0.0001},

    },

    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]}
    },

    "integration_weights": {

        "cos": {
            "cosine": [(1.0, readout_length)],
            "sine": [(0.0, readout_length)],
        },

        "sin": {
            "cosine": [(0.0, readout_length)],
            "sine": [(1.0, readout_length)],
        },

    },

}