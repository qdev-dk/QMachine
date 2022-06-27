
# Single QUA script generated at 2022-06-27 15:17:42.943784
# QUA library version: 0.3.6

from qm.qua import *

with program() as prog:
    v1 = declare(fixed, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(int, )
    a1 = declare(fixed, value=[2749.0, 2748.747474747475, 2748.4949494949497, 2748.242424242424, 2747.989898989899, 2747.7373737373737, 2747.4848484848485, 2747.2323232323233, 2746.979797979798, 2746.7272727272725, 2746.4747474747473, 2746.222222222222, 2745.969696969697, 2745.717171717172, 2745.4646464646466, 2745.212121212121, 2744.959595959596, 2744.7070707070707, 2744.4545454545455, 2744.2020202020203, 2743.949494949495, 2743.6969696969695, 2743.4444444444443, 2743.191919191919, 2742.939393939394, 2742.686868686869, 2742.4343434343436, 2742.181818181818, 2741.929292929293, 2741.6767676767677, 2741.4242424242425, 2741.1717171717173, 2740.919191919192, 2740.6666666666665, 2740.4141414141413, 2740.161616161616, 2739.909090909091, 2739.656565656566, 2739.40404040404, 2739.151515151515, 2738.89898989899, 2738.6464646464647, 2738.3939393939395, 2738.1414141414143, 2737.8888888888887, 2737.6363636363635, 2737.3838383838383, 2737.131313131313, 2736.878787878788, 2736.626262626263, 2736.373737373737, 2736.121212121212, 2735.868686868687, 2735.6161616161617, 2735.3636363636365, 2735.1111111111113, 2734.8585858585857, 2734.6060606060605, 2734.3535353535353, 2734.10101010101, 2733.848484848485, 2733.59595959596, 2733.343434343434, 2733.090909090909, 2732.838383838384, 2732.5858585858587, 2732.3333333333335, 2732.080808080808, 2731.8282828282827, 2731.5757575757575, 2731.3232323232323, 2731.070707070707, 2730.818181818182, 2730.5656565656564, 2730.313131313131, 2730.060606060606, 2729.808080808081, 2729.5555555555557, 2729.3030303030305, 2729.050505050505, 2728.7979797979797, 2728.5454545454545, 2728.2929292929293, 2728.040404040404, 2727.787878787879, 2727.5353535353534, 2727.282828282828, 2727.030303030303, 2726.777777777778, 2726.5252525252527, 2726.2727272727275, 2726.020202020202, 2725.7676767676767, 2725.5151515151515, 2725.2626262626263, 2725.010101010101, 2724.757575757576, 2724.5050505050503, 2724.252525252525, 2724.0])
    a2 = declare(fixed, value=[2749.0, 2748.747474747475, 2748.4949494949497, 2748.242424242424, 2747.989898989899, 2747.7373737373737, 2747.4848484848485, 2747.2323232323233, 2746.979797979798, 2746.7272727272725, 2746.4747474747473, 2746.222222222222, 2745.969696969697, 2745.717171717172, 2745.4646464646466, 2745.212121212121, 2744.959595959596, 2744.7070707070707, 2744.4545454545455, 2744.2020202020203, 2743.949494949495, 2743.6969696969695, 2743.4444444444443, 2743.191919191919, 2742.939393939394, 2742.686868686869, 2742.4343434343436, 2742.181818181818, 2741.929292929293, 2741.6767676767677, 2741.4242424242425, 2741.1717171717173, 2740.919191919192, 2740.6666666666665, 2740.4141414141413, 2740.161616161616, 2739.909090909091, 2739.656565656566, 2739.40404040404, 2739.151515151515, 2738.89898989899, 2738.6464646464647, 2738.3939393939395, 2738.1414141414143, 2737.8888888888887, 2737.6363636363635, 2737.3838383838383, 2737.131313131313, 2736.878787878788, 2736.626262626263, 2736.373737373737, 2736.121212121212, 2735.868686868687, 2735.6161616161617, 2735.3636363636365, 2735.1111111111113, 2734.8585858585857, 2734.6060606060605, 2734.3535353535353, 2734.10101010101, 2733.848484848485, 2733.59595959596, 2733.343434343434, 2733.090909090909, 2732.838383838384, 2732.5858585858587, 2732.3333333333335, 2732.080808080808, 2731.8282828282827, 2731.5757575757575, 2731.3232323232323, 2731.070707070707, 2730.818181818182, 2730.5656565656564, 2730.313131313131, 2730.060606060606, 2729.808080808081, 2729.5555555555557, 2729.3030303030305, 2729.050505050505, 2728.7979797979797, 2728.5454545454545, 2728.2929292929293, 2728.040404040404, 2727.787878787879, 2727.5353535353534, 2727.282828282828, 2727.030303030303, 2726.777777777778, 2726.5252525252527, 2726.2727272727275, 2726.020202020202, 2725.7676767676767, 2725.5151515151515, 2725.2626262626263, 2725.010101010101, 2724.757575757576, 2724.5050505050503, 2724.252525252525, 2724.0])
    a3 = declare(fixed, value=[1.0, 1.2525252525252526, 1.5050505050505052, 1.7575757575757576, 2.0101010101010104, 2.262626262626263, 2.515151515151515, 2.7676767676767677, 3.0202020202020203, 3.272727272727273, 3.5252525252525255, 3.777777777777778, 4.03030303030303, 4.282828282828283, 4.5353535353535355, 4.787878787878788, 5.040404040404041, 5.292929292929293, 5.545454545454546, 5.7979797979797985, 6.050505050505051, 6.303030303030304, 6.555555555555556, 6.808080808080809, 7.0606060606060606, 7.313131313131313, 7.565656565656566, 7.818181818181818, 8.070707070707071, 8.323232323232324, 8.575757575757576, 8.828282828282829, 9.080808080808081, 9.333333333333334, 9.585858585858587, 9.83838383838384, 10.090909090909092, 10.343434343434344, 10.595959595959597, 10.84848484848485, 11.101010101010102, 11.353535353535355, 11.606060606060607, 11.85858585858586, 12.111111111111112, 12.363636363636365, 12.616161616161618, 12.86868686868687, 13.121212121212121, 13.373737373737374, 13.626262626262626, 13.878787878787879, 14.131313131313131, 14.383838383838384, 14.636363636363637, 14.88888888888889, 15.141414141414142, 15.393939393939394, 15.646464646464647, 15.8989898989899, 16.151515151515152, 16.404040404040405, 16.656565656565657, 16.90909090909091, 17.161616161616163, 17.414141414141415, 17.666666666666668, 17.91919191919192, 18.171717171717173, 18.424242424242426, 18.67676767676768, 18.92929292929293, 19.181818181818183, 19.434343434343436, 19.68686868686869, 19.93939393939394, 20.191919191919194, 20.444444444444446, 20.6969696969697, 20.94949494949495, 21.202020202020204, 21.454545454545457, 21.70707070707071, 21.959595959595962, 22.212121212121215, 22.464646464646467, 22.71717171717172, 22.969696969696972, 23.222222222222225, 23.474747474747478, 23.72727272727273, 23.979797979797983, 24.232323232323235, 24.484848484848488, 24.73737373737374, 24.989898989898993, 25.242424242424242, 25.494949494949495, 25.747474747474747, 26.0])
    a4 = declare(fixed, value=[1.0, 1.2525252525252526, 1.5050505050505052, 1.7575757575757576, 2.0101010101010104, 2.262626262626263, 2.515151515151515, 2.7676767676767677, 3.0202020202020203, 3.272727272727273, 3.5252525252525255, 3.777777777777778, 4.03030303030303, 4.282828282828283, 4.5353535353535355, 4.787878787878788, 5.040404040404041, 5.292929292929293, 5.545454545454546, 5.7979797979797985, 6.050505050505051, 6.303030303030304, 6.555555555555556, 6.808080808080809, 7.0606060606060606, 7.313131313131313, 7.565656565656566, 7.818181818181818, 8.070707070707071, 8.323232323232324, 8.575757575757576, 8.828282828282829, 9.080808080808081, 9.333333333333334, 9.585858585858587, 9.83838383838384, 10.090909090909092, 10.343434343434344, 10.595959595959597, 10.84848484848485, 11.101010101010102, 11.353535353535355, 11.606060606060607, 11.85858585858586, 12.111111111111112, 12.363636363636365, 12.616161616161618, 12.86868686868687, 13.121212121212121, 13.373737373737374, 13.626262626262626, 13.878787878787879, 14.131313131313131, 14.383838383838384, 14.636363636363637, 14.88888888888889, 15.141414141414142, 15.393939393939394, 15.646464646464647, 15.8989898989899, 16.151515151515152, 16.404040404040405, 16.656565656565657, 16.90909090909091, 17.161616161616163, 17.414141414141415, 17.666666666666668, 17.91919191919192, 18.171717171717173, 18.424242424242426, 18.67676767676768, 18.92929292929293, 19.181818181818183, 19.434343434343436, 19.68686868686869, 19.93939393939394, 20.191919191919194, 20.444444444444446, 20.6969696969697, 20.94949494949495, 21.202020202020204, 21.454545454545457, 21.70707070707071, 21.959595959595962, 22.212121212121215, 22.464646464646467, 22.71717171717172, 22.969696969696972, 23.222222222222225, 23.474747474747478, 23.72727272727273, 23.979797979797983, 24.232323232323235, 24.484848484848488, 24.73737373737374, 24.989898989898993, 25.242424242424242, 25.494949494949495, 25.747474747474747, 26.0])
    a5 = declare(fixed, value=[-0.0347633450224, -0.034772153698090225, -0.034780962373780464, -0.0347897710494707, -0.03479857972516094, -0.034807388400851166, -0.03481619707654139, -0.034825005752231644, -0.03483381442792187, -0.03484262310361211, -0.03485143177930235, -0.034860240454992586, -0.03486904913068281, -0.034877857806373064, -0.03488666648206329, -0.03489547515775353, -0.03490428383344377, -0.034913092509134006, -0.03492190118482423, -0.03493070986051447, -0.03493951853620471, -0.03494832721189493, -0.034957135887585186, -0.03496594456327541, -0.03497475323896565, -0.03498356191465589, -0.03499237059034613, -0.03500117926603635, -0.03500998794172658, -0.03501879661741683, -0.035027605293107056, -0.035036413968797295, -0.035045222644487534, -0.03505403132017777, -0.035062839995868, -0.03507164867155825, -0.035080457347248475, -0.035089266022938714, -0.03509807469862895, -0.03510688337431918, -0.03511569205000942, -0.035124500725699656, -0.035133309401389895, -0.03514211807708012, -0.03515092675277036, -0.0351597354284606, -0.03516854410415084, -0.03517735277984106, -0.035186161455531315, -0.03519497013122154, -0.035203778806911765, -0.03521258748260202, -0.03522139615829224, -0.03523020483398248, -0.03523901350967272, -0.03524782218536296, -0.035256630861053184, -0.03526543953674344, -0.03527424821243366, -0.03528305688812389, -0.03529186556381414, -0.035300674239504365, -0.035309482915194604, -0.03531829159088484, -0.03532710026657508, -0.03533590894226531, -0.035344717617955546, -0.035353526293645784, -0.03536233496933602, -0.03537114364502625, -0.0353799523207165, -0.035388760996406726, -0.03539756967209695, -0.035406378347787204, -0.03541518702347743, -0.03542399569916767, -0.03543280437485791, -0.035441613050548146, -0.03545042172623837, -0.035459230401928624, -0.03546803907761885, -0.035476847753309074, -0.03548565642899931, -0.03549446510468955, -0.03550327378037979, -0.035512082456070015, -0.03552089113176027, -0.03552969980745049, -0.03553850848314073, -0.03554731715883097, -0.03555612583452121, -0.035564934510211435, -0.035573743185901674, -0.03558255186159191, -0.03559136053728214, -0.03560016921297239, -0.035608977888662616, -0.035617786564352855, -0.035626595240043094, -0.03563540391573333])
    a6 = declare(fixed, value=[0.013823764812000004, 0.013830981431191929, 0.013838198050383839, 0.013845414669575763, 0.013852631288767688, 0.013859847907959598, 0.013867064527151522, 0.013874281146343447, 0.013881497765535357, 0.013888714384727281, 0.013895931003919205, 0.013903147623111116, 0.01391036424230304, 0.013917580861494964, 0.013924797480686875, 0.0139320140998788, 0.013939230719070723, 0.013946447338262634, 0.013953663957454558, 0.013960880576646469, 0.013968097195838393, 0.013975313815030317, 0.013982530434222228, 0.013989747053414152, 0.013996963672606062, 0.014004180291797987, 0.01401139691098991, 0.014018613530181821, 0.014025830149373746, 0.014033046768565656, 0.01404026338775758, 0.014047480006949505, 0.014054696626141415, 0.01406191324533334, 0.014069129864525264, 0.014076346483717174, 0.014083563102909098, 0.014090779722101023, 0.014097996341292947, 0.014105212960484857, 0.014112429579676782, 0.014119646198868692, 0.014126862818060616, 0.014134079437252527, 0.014141296056444451, 0.014148512675636375, 0.014155729294828286, 0.01416294591402021, 0.01417016253321212, 0.014177379152404045, 0.014184595771595969, 0.01419181239078788, 0.014199029009979804, 0.014206245629171728, 0.014213462248363638, 0.014220678867555563, 0.014227895486747487, 0.014235112105939397, 0.014242328725131322, 0.014249545344323246, 0.014256761963515156, 0.01426397858270708, 0.014271195201899005, 0.014278411821090915, 0.01428562844028284, 0.014292845059474764, 0.014300061678666674, 0.014307278297858599, 0.014314494917050509, 0.014321711536242433, 0.014328928155434358, 0.014336144774626268, 0.014343361393818192, 0.014350578013010103, 0.014357794632202027, 0.014365011251393951, 0.014372227870585862, 0.014379444489777786, 0.014386661108969696, 0.01439387772816162, 0.014401094347353545, 0.014408310966545455, 0.01441552758573738, 0.014422744204929304, 0.014429960824121228, 0.014437177443313139, 0.014444394062505063, 0.014451610681696987, 0.014458827300888898, 0.014466043920080822, 0.014473260539272732, 0.014480477158464657, 0.014487693777656581, 0.014494910396848491, 0.014502127016040416, 0.014509343635232326, 0.01451656025442425, 0.01452377687361616, 0.014530993492808085, 0.01453821011200001])
    with for_(v5,0,v5<100,v5+1):
        align("gate_36", "gate_29", "bottom_right_DQD_readout")
        play("CW"*amp(-0.07149319999999999), "gate_36", duration=a1[v5])
        play("CW"*amp(0.061776899999999996), "gate_29", duration=a2[v5])
        measure("readout_pulse_10us", "bottom_right_DQD_readout", None, demod.full("cos", v1, "out1"), demod.full("sin", v2, "out1"))
        r1 = declare_stream()
        save(v1, r1)
        r2 = declare_stream()
        save(v2, r2)
        align("gate_36", "gate_29")
        play("CW"*amp(2.61617668), "gate_36", duration=a3[v5])
        play("CW"*amp(-2.1433359000000003), "gate_29", duration=a4[v5])
        align("gate_36", "gate_29", "bottom_right_DQD_readout")
        play("CW"*amp(-2.61617668), "gate_36", duration=2500)
        play("CW"*amp(2.1433359000000003), "gate_29", duration=2500)
        measure("readout_pulse_10us", "bottom_right_DQD_readout", None, demod.full("cos", v3, "out1"), demod.full("sin", v4, "out1"))
        r3 = declare_stream()
        save(v3, r3)
        r4 = declare_stream()
        save(v4, r4)
        align("gate_36", "gate_29")
        play("CW"*amp(2.5591947999999998), "gate_36", duration=2500)
        play("CW"*amp(-2.210571), "gate_29", duration=2500)
        align("gate_36", "gate_29")
        play(ramp(-2.7805456e-05), "gate_36", duration=2500)
        play(ramp(2.6714580999999998e-05), "gate_29", duration=2500)
        align("gate_36", "gate_29")
        play("CW"*amp(a5[v5]*10.0), "gate_36", duration=7500)
        play("CW"*amp(a6[v5]*10.0), "gate_29", duration=7500)
        align("gate_36", "gate_29")
        ramp_to_zero("gate_36", 1)
        ramp_to_zero("gate_29", 1)
    with stream_processing():
        r1.save_all("I_1")
        r2.save_all("Q_1")
        r3.save_all("I_2")
        r4.save_all("Q_2")


config = {
    'version': 1,
    'controllers': {
        'con1': {
            'analog_outputs': {
                '1': {
                    'offset': 0.0,
                },
                '3': {
                    'offset': 0.0,
                },
                '2': {
                    'offset': 0.0,
                },
            },
            'digital_outputs': {
                '1': {},
            },
            'analog_inputs': {
                '1': {
                    'offset': 0.21164,
                },
                '2': {
                    'offset': 0.0,
                },
            },
        },
    },
    'elements': {
        'Q1_R': {
            'singleInput': {
                'port': ('con1', 3),
            },
            'intermediate_frequency': 0.0,
            'hold_offset': {
                'duration': 100,
            },
            'operations': {
                'CW': 'CW',
            },
        },
        'Q1_L': {
            'singleInput': {
                'port': ('con1', 2),
            },
            'intermediate_frequency': 0.0,
            'hold_offset': {
                'duration': 100,
            },
            'operations': {
                'CW': 'CW',
            },
        },
        'Q1_readout': {
            'singleInput': {
                'port': ('con1', 1),
            },
            'intermediate_frequency': 156390000,
            'operations': {
                'readout_pulse_0_2': 'readout_pulse_0_2',
                'readout_pulse_0_1': 'readout_pulse_0_1',
                'readout_pulse_0_05': 'readout_pulse_0_05',
                'readout_pulse_0_01': 'readout_pulse_0_01',
                'readout_pulse_0_0001': 'readout_pulse_0_0001',
            },
            'outputs': {
                'out1': ('con1', 1),
            },
            'time_of_flight': 368,
            'smearing': 0,
        },
        'Q2_readout': {
            'singleInput': {
                'port': ('con1', 1),
            },
            'intermediate_frequency': 129291200,
            'operations': {
                'readout_pulse_0_05': 'readout_pulse_0_05',
                'readout_pulse_0_2': 'readout_pulse_0_2',
            },
            'outputs': {
                'out1': ('con1', 1),
            },
            'time_of_flight': 368,
            'smearing': 0,
        },
    },
    'pulses': {
        'CW': {
            'operation': 'control',
            'length': 100,
            'waveforms': {
                'single': 'const_wf',
            },
        },
        'readout_pulse_0_2': {
            'operation': 'measurement',
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_0_1': {
            'operation': 'measurement',
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_1',
            },
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_0_05': {
            'operation': 'measurement',
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_05',
            },
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_0_01': {
            'operation': 'measurement',
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_01',
            },
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_0_001': {
            'operation': 'measurement',
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_001',
            },
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_0_0001': {
            'operation': 'measurement',
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_0001',
            },
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'digital_marker': 'ON',
        },
    },
    'waveforms': {
        'const_wf': {
            'type': 'constant',
            'sample': 0.1,
        },
        'zero_wf': {
            'type': 'constant',
            'sample': 0.0,
        },
        'readout_wf_0_2': {
            'type': 'constant',
            'sample': 0.2,
        },
        'readout_wf_0_1': {
            'type': 'constant',
            'sample': 0.1,
        },
        'readout_wf_0_05': {
            'type': 'constant',
            'sample': 0.05,
        },
        'readout_wf_0_01': {
            'type': 'constant',
            'sample': 0.01,
        },
        'readout_wf_0_001': {
            'type': 'constant',
            'sample': 0.001,
        },
        'readout_wf_0_0001': {
            'type': 'constant',
            'sample': 0.0001,
        },
    },
    'digital_waveforms': {
        'ON': {
            'samples': [(1, 0)],
        },
    },
    'integration_weights': {
        'cos': {
            'cosine': [(1.0, 10000)],
            'sine': [(0.0, 10000)],
        },
        'sin': {
            'cosine': [(0.0, 10000)],
            'sine': [(1.0, 10000)],
        },
    },
}

loaded_config = {
    'version': 1,
    'controllers': {
        'con1': {
            'type': 'opx1',
            'analog_outputs': {
                '1': {
                    'offset': 0.0,
                    'filter': {
                        'feedforward': [],
                        'feedback': [],
                    },
                    'delay': 0,
                },
                '3': {
                    'offset': 0.0,
                    'filter': {
                        'feedforward': [],
                        'feedback': [],
                    },
                    'delay': 0,
                },
                '2': {
                    'offset': 0.0,
                    'filter': {
                        'feedforward': [],
                        'feedback': [],
                    },
                    'delay': 0,
                },
            },
            'analog_inputs': {
                '1': {
                    'offset': 0.21164,
                    'gain_db': 0,
                },
                '2': {
                    'offset': 0.0,
                    'gain_db': 0,
                },
            },
            'digital_outputs': {
                '1': {},
            },
        },
    },
    'oscillators': {},
    'elements': {
        'Q1_R': {
            'digitalInputs': {},
            'digitalOutputs': {},
            'intermediate_frequency': 0,
            'operations': {
                'CW': 'CW',
            },
            'singleInput': {
                'port': ('con1', 3),
            },
            'hold_offset': {
                'duration': 100,
            },
        },
        'Q1_L': {
            'digitalInputs': {},
            'digitalOutputs': {},
            'intermediate_frequency': 0,
            'operations': {
                'CW': 'CW',
            },
            'singleInput': {
                'port': ('con1', 2),
            },
            'hold_offset': {
                'duration': 100,
            },
        },
        'Q1_readout': {
            'digitalInputs': {},
            'digitalOutputs': {},
            'outputs': {
                'out1': ('con1', 1),
            },
            'time_of_flight': 368,
            'smearing': 0,
            'intermediate_frequency': 156390000,
            'operations': {
                'readout_pulse_0_2': 'readout_pulse_0_2',
                'readout_pulse_0_1': 'readout_pulse_0_1',
                'readout_pulse_0_05': 'readout_pulse_0_05',
                'readout_pulse_0_01': 'readout_pulse_0_01',
                'readout_pulse_0_0001': 'readout_pulse_0_0001',
            },
            'singleInput': {
                'port': ('con1', 1),
            },
        },
        'Q2_readout': {
            'digitalInputs': {},
            'digitalOutputs': {},
            'outputs': {
                'out1': ('con1', 1),
            },
            'time_of_flight': 368,
            'smearing': 0,
            'intermediate_frequency': 129291200,
            'operations': {
                'readout_pulse_0_05': 'readout_pulse_0_05',
                'readout_pulse_0_2': 'readout_pulse_0_2',
            },
            'singleInput': {
                'port': ('con1', 1),
            },
        },
    },
    'pulses': {
        'CW': {
            'length': 100,
            'waveforms': {
                'single': 'const_wf',
            },
            'operation': 'control',
        },
        'readout_pulse_0_2': {
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'operation': 'measurement',
        },
        'readout_pulse_0_1': {
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_1',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'operation': 'measurement',
        },
        'readout_pulse_0_05': {
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_05',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'operation': 'measurement',
        },
        'readout_pulse_0_01': {
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_01',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'operation': 'measurement',
        },
        'readout_pulse_0_001': {
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_001',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'operation': 'measurement',
        },
        'readout_pulse_0_0001': {
            'length': 10000,
            'waveforms': {
                'single': 'readout_wf_0_0001',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos',
                'sin': 'sin',
            },
            'operation': 'measurement',
        },
    },
    'waveforms': {
        'const_wf': {
            'sample': 0.1,
            'type': 'constant',
        },
        'zero_wf': {
            'sample': 0.0,
            'type': 'constant',
        },
        'readout_wf_0_2': {
            'sample': 0.2,
            'type': 'constant',
        },
        'readout_wf_0_1': {
            'sample': 0.1,
            'type': 'constant',
        },
        'readout_wf_0_05': {
            'sample': 0.05,
            'type': 'constant',
        },
        'readout_wf_0_01': {
            'sample': 0.01,
            'type': 'constant',
        },
        'readout_wf_0_001': {
            'sample': 0.001,
            'type': 'constant',
        },
        'readout_wf_0_0001': {
            'sample': 0.0001,
            'type': 'constant',
        },
    },
    'digital_waveforms': {
        'ON': {
            'samples': [(1, 0)],
        },
    },
    'integration_weights': {
        'cos': {
            'cosine': [(1.0, 10000)],
            'sine': [(0.0, 10000)],
        },
        'sin': {
            'cosine': [(0.0, 10000)],
            'sine': [(1.0, 10000)],
        },
    },
    'mixers': {},
}

