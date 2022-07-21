
# Single QUA script generated at 2022-07-21 09:17:21.686782
# QUA library version: 0.3.7

from qm.qua import *

with program() as prog:
    v1 = declare(fixed, )
    v2 = declare(fixed, )
    a1 = declare(fixed, size=100)
    a2 = declare(fixed, size=100)
    v3 = declare(int, )
    v4 = declare(int, )
    with for_(v4,0,v4<200,v4+1):
        align("gate_36", "gate_29", "bottom_right_DQD_readout")
        play("CW"*amp(-0.02859728), "gate_36", duration=2500)
        play("CW"*amp(0.02471076), "gate_29", duration=2500)
        measure("readout_pulse_10us", "bottom_right_DQD_readout", None, demod.full("cos", v1, "out1"), demod.full("sin", v2, "out1"))
        r1 = declare_stream()
        save(v1, r1)
        r2 = declare_stream()
        save(v2, r2)
        align("gate_36")
        with if_(v4==0):
            align("gate_36", "gate_29")
            play("baked_Op_201", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_201", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==1):
            align("gate_36", "gate_29")
            play("baked_Op_202", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_202", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==2):
            align("gate_36", "gate_29")
            play("baked_Op_203", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_203", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==3):
            align("gate_36", "gate_29")
            play("baked_Op_204", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_204", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==4):
            align("gate_36", "gate_29")
            play("baked_Op_205", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_205", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==5):
            align("gate_36", "gate_29")
            play("baked_Op_206", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_206", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==6):
            align("gate_36", "gate_29")
            play("baked_Op_207", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_207", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==7):
            align("gate_36", "gate_29")
            play("baked_Op_208", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_208", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==8):
            align("gate_36", "gate_29")
            play("baked_Op_209", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_209", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==9):
            align("gate_36", "gate_29")
            play("baked_Op_210", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_210", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==10):
            align("gate_36", "gate_29")
            play("baked_Op_211", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_211", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==11):
            align("gate_36", "gate_29")
            play("baked_Op_212", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_212", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==12):
            align("gate_36", "gate_29")
            play("baked_Op_213", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_213", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==13):
            align("gate_36", "gate_29")
            play("baked_Op_214", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_214", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==14):
            align("gate_36", "gate_29")
            play("baked_Op_215", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_215", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==15):
            align("gate_36", "gate_29")
            play("baked_Op_216", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_216", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==16):
            align("gate_36", "gate_29")
            play("baked_Op_217", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_217", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==17):
            align("gate_36", "gate_29")
            play("baked_Op_218", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_218", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==18):
            align("gate_36", "gate_29")
            play("baked_Op_219", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_219", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==19):
            align("gate_36", "gate_29")
            play("baked_Op_220", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_220", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==20):
            align("gate_36", "gate_29")
            play("baked_Op_221", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_221", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==21):
            align("gate_36", "gate_29")
            play("baked_Op_222", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_222", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==22):
            align("gate_36", "gate_29")
            play("baked_Op_223", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_223", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==23):
            align("gate_36", "gate_29")
            play("baked_Op_224", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_224", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==24):
            align("gate_36", "gate_29")
            play("baked_Op_225", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_225", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==25):
            align("gate_36", "gate_29")
            play("baked_Op_226", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_226", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==26):
            align("gate_36", "gate_29")
            play("baked_Op_227", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_227", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==27):
            align("gate_36", "gate_29")
            play("baked_Op_228", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_228", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==28):
            align("gate_36", "gate_29")
            play("baked_Op_229", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_229", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==29):
            align("gate_36", "gate_29")
            play("baked_Op_230", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_230", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==30):
            align("gate_36", "gate_29")
            play("baked_Op_231", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_231", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==31):
            align("gate_36", "gate_29")
            play("baked_Op_232", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_232", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==32):
            align("gate_36", "gate_29")
            play("baked_Op_233", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_233", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==33):
            align("gate_36", "gate_29")
            play("baked_Op_234", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_234", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==34):
            align("gate_36", "gate_29")
            play("baked_Op_235", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_235", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==35):
            align("gate_36", "gate_29")
            play("baked_Op_236", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_236", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==36):
            align("gate_36", "gate_29")
            play("baked_Op_237", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_237", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==37):
            align("gate_36", "gate_29")
            play("baked_Op_238", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_238", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==38):
            align("gate_36", "gate_29")
            play("baked_Op_239", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_239", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==39):
            align("gate_36", "gate_29")
            play("baked_Op_240", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_240", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==40):
            align("gate_36", "gate_29")
            play("baked_Op_241", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_241", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==41):
            align("gate_36", "gate_29")
            play("baked_Op_242", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_242", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==42):
            align("gate_36", "gate_29")
            play("baked_Op_243", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_243", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==43):
            align("gate_36", "gate_29")
            play("baked_Op_244", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_244", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==44):
            align("gate_36", "gate_29")
            play("baked_Op_245", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_245", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==45):
            align("gate_36", "gate_29")
            play("baked_Op_246", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_246", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==46):
            align("gate_36", "gate_29")
            play("baked_Op_247", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_247", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==47):
            align("gate_36", "gate_29")
            play("baked_Op_248", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_248", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==48):
            align("gate_36", "gate_29")
            play("baked_Op_249", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_249", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==49):
            align("gate_36", "gate_29")
            play("baked_Op_250", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_250", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==50):
            align("gate_36", "gate_29")
            play("baked_Op_251", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_251", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==51):
            align("gate_36", "gate_29")
            play("baked_Op_252", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_252", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==52):
            align("gate_36", "gate_29")
            play("baked_Op_253", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_253", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==53):
            align("gate_36", "gate_29")
            play("baked_Op_254", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_254", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==54):
            align("gate_36", "gate_29")
            play("baked_Op_255", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_255", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==55):
            align("gate_36", "gate_29")
            play("baked_Op_256", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_256", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==56):
            align("gate_36", "gate_29")
            play("baked_Op_257", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_257", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==57):
            align("gate_36", "gate_29")
            play("baked_Op_258", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_258", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==58):
            align("gate_36", "gate_29")
            play("baked_Op_259", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_259", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==59):
            align("gate_36", "gate_29")
            play("baked_Op_260", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_260", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==60):
            align("gate_36", "gate_29")
            play("baked_Op_261", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_261", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==61):
            align("gate_36", "gate_29")
            play("baked_Op_262", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_262", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==62):
            align("gate_36", "gate_29")
            play("baked_Op_263", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_263", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==63):
            align("gate_36", "gate_29")
            play("baked_Op_264", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_264", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==64):
            align("gate_36", "gate_29")
            play("baked_Op_265", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_265", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==65):
            align("gate_36", "gate_29")
            play("baked_Op_266", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_266", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==66):
            align("gate_36", "gate_29")
            play("baked_Op_267", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_267", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==67):
            align("gate_36", "gate_29")
            play("baked_Op_268", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_268", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==68):
            align("gate_36", "gate_29")
            play("baked_Op_269", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_269", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==69):
            align("gate_36", "gate_29")
            play("baked_Op_270", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_270", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==70):
            align("gate_36", "gate_29")
            play("baked_Op_271", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_271", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==71):
            align("gate_36", "gate_29")
            play("baked_Op_272", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_272", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==72):
            align("gate_36", "gate_29")
            play("baked_Op_273", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_273", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==73):
            align("gate_36", "gate_29")
            play("baked_Op_274", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_274", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==74):
            align("gate_36", "gate_29")
            play("baked_Op_275", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_275", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==75):
            align("gate_36", "gate_29")
            play("baked_Op_276", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_276", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==76):
            align("gate_36", "gate_29")
            play("baked_Op_277", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_277", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==77):
            align("gate_36", "gate_29")
            play("baked_Op_278", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_278", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==78):
            align("gate_36", "gate_29")
            play("baked_Op_279", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_279", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==79):
            align("gate_36", "gate_29")
            play("baked_Op_280", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_280", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==80):
            align("gate_36", "gate_29")
            play("baked_Op_281", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_281", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==81):
            align("gate_36", "gate_29")
            play("baked_Op_282", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_282", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==82):
            align("gate_36", "gate_29")
            play("baked_Op_283", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_283", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==83):
            align("gate_36", "gate_29")
            play("baked_Op_284", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_284", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==84):
            align("gate_36", "gate_29")
            play("baked_Op_285", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_285", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==85):
            align("gate_36", "gate_29")
            play("baked_Op_286", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_286", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==86):
            align("gate_36", "gate_29")
            play("baked_Op_287", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_287", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==87):
            align("gate_36", "gate_29")
            play("baked_Op_288", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_288", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==88):
            align("gate_36", "gate_29")
            play("baked_Op_289", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_289", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==89):
            align("gate_36", "gate_29")
            play("baked_Op_290", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_290", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==90):
            align("gate_36", "gate_29")
            play("baked_Op_291", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_291", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==91):
            align("gate_36", "gate_29")
            play("baked_Op_292", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_292", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==92):
            align("gate_36", "gate_29")
            play("baked_Op_293", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_293", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==93):
            align("gate_36", "gate_29")
            play("baked_Op_294", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_294", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==94):
            align("gate_36", "gate_29")
            play("baked_Op_295", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_295", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==95):
            align("gate_36", "gate_29")
            play("baked_Op_296", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_296", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==96):
            align("gate_36", "gate_29")
            play("baked_Op_297", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_297", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==97):
            align("gate_36", "gate_29")
            play("baked_Op_298", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_298", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==98):
            align("gate_36", "gate_29")
            play("baked_Op_299", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_299", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==99):
            align("gate_36", "gate_29")
            play("baked_Op_300", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_300", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==100):
            align("gate_36", "gate_29")
            play("baked_Op_301", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_301", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==101):
            align("gate_36", "gate_29")
            play("baked_Op_302", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_302", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==102):
            align("gate_36", "gate_29")
            play("baked_Op_303", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_303", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==103):
            align("gate_36", "gate_29")
            play("baked_Op_304", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_304", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==104):
            align("gate_36", "gate_29")
            play("baked_Op_305", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_305", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==105):
            align("gate_36", "gate_29")
            play("baked_Op_306", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_306", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==106):
            align("gate_36", "gate_29")
            play("baked_Op_307", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_307", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==107):
            align("gate_36", "gate_29")
            play("baked_Op_308", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_308", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==108):
            align("gate_36", "gate_29")
            play("baked_Op_309", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_309", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==109):
            align("gate_36", "gate_29")
            play("baked_Op_310", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_310", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==110):
            align("gate_36", "gate_29")
            play("baked_Op_311", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_311", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==111):
            align("gate_36", "gate_29")
            play("baked_Op_312", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_312", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==112):
            align("gate_36", "gate_29")
            play("baked_Op_313", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_313", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==113):
            align("gate_36", "gate_29")
            play("baked_Op_314", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_314", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==114):
            align("gate_36", "gate_29")
            play("baked_Op_315", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_315", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==115):
            align("gate_36", "gate_29")
            play("baked_Op_316", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_316", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==116):
            align("gate_36", "gate_29")
            play("baked_Op_317", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_317", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==117):
            align("gate_36", "gate_29")
            play("baked_Op_318", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_318", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==118):
            align("gate_36", "gate_29")
            play("baked_Op_319", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_319", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==119):
            align("gate_36", "gate_29")
            play("baked_Op_320", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_320", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==120):
            align("gate_36", "gate_29")
            play("baked_Op_321", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_321", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==121):
            align("gate_36", "gate_29")
            play("baked_Op_322", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_322", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==122):
            align("gate_36", "gate_29")
            play("baked_Op_323", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_323", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==123):
            align("gate_36", "gate_29")
            play("baked_Op_324", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_324", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==124):
            align("gate_36", "gate_29")
            play("baked_Op_325", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_325", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==125):
            align("gate_36", "gate_29")
            play("baked_Op_326", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_326", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==126):
            align("gate_36", "gate_29")
            play("baked_Op_327", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_327", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==127):
            align("gate_36", "gate_29")
            play("baked_Op_328", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_328", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==128):
            align("gate_36", "gate_29")
            play("baked_Op_329", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_329", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==129):
            align("gate_36", "gate_29")
            play("baked_Op_330", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_330", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==130):
            align("gate_36", "gate_29")
            play("baked_Op_331", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_331", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==131):
            align("gate_36", "gate_29")
            play("baked_Op_332", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_332", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==132):
            align("gate_36", "gate_29")
            play("baked_Op_333", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_333", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==133):
            align("gate_36", "gate_29")
            play("baked_Op_334", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_334", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==134):
            align("gate_36", "gate_29")
            play("baked_Op_335", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_335", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==135):
            align("gate_36", "gate_29")
            play("baked_Op_336", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_336", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==136):
            align("gate_36", "gate_29")
            play("baked_Op_337", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_337", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==137):
            align("gate_36", "gate_29")
            play("baked_Op_338", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_338", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==138):
            align("gate_36", "gate_29")
            play("baked_Op_339", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_339", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==139):
            align("gate_36", "gate_29")
            play("baked_Op_340", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_340", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==140):
            align("gate_36", "gate_29")
            play("baked_Op_341", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_341", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==141):
            align("gate_36", "gate_29")
            play("baked_Op_342", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_342", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==142):
            align("gate_36", "gate_29")
            play("baked_Op_343", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_343", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==143):
            align("gate_36", "gate_29")
            play("baked_Op_344", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_344", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==144):
            align("gate_36", "gate_29")
            play("baked_Op_345", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_345", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==145):
            align("gate_36", "gate_29")
            play("baked_Op_346", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_346", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==146):
            align("gate_36", "gate_29")
            play("baked_Op_347", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_347", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==147):
            align("gate_36", "gate_29")
            play("baked_Op_348", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_348", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==148):
            align("gate_36", "gate_29")
            play("baked_Op_349", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_349", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==149):
            align("gate_36", "gate_29")
            play("baked_Op_350", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_350", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==150):
            align("gate_36", "gate_29")
            play("baked_Op_351", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_351", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==151):
            align("gate_36", "gate_29")
            play("baked_Op_352", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_352", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==152):
            align("gate_36", "gate_29")
            play("baked_Op_353", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_353", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==153):
            align("gate_36", "gate_29")
            play("baked_Op_354", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_354", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==154):
            align("gate_36", "gate_29")
            play("baked_Op_355", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_355", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==155):
            align("gate_36", "gate_29")
            play("baked_Op_356", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_356", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==156):
            align("gate_36", "gate_29")
            play("baked_Op_357", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_357", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==157):
            align("gate_36", "gate_29")
            play("baked_Op_358", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_358", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==158):
            align("gate_36", "gate_29")
            play("baked_Op_359", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_359", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==159):
            align("gate_36", "gate_29")
            play("baked_Op_360", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_360", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==160):
            align("gate_36", "gate_29")
            play("baked_Op_361", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_361", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==161):
            align("gate_36", "gate_29")
            play("baked_Op_362", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_362", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==162):
            align("gate_36", "gate_29")
            play("baked_Op_363", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_363", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==163):
            align("gate_36", "gate_29")
            play("baked_Op_364", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_364", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==164):
            align("gate_36", "gate_29")
            play("baked_Op_365", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_365", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==165):
            align("gate_36", "gate_29")
            play("baked_Op_366", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_366", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==166):
            align("gate_36", "gate_29")
            play("baked_Op_367", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_367", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==167):
            align("gate_36", "gate_29")
            play("baked_Op_368", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_368", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==168):
            align("gate_36", "gate_29")
            play("baked_Op_369", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_369", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==169):
            align("gate_36", "gate_29")
            play("baked_Op_370", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_370", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==170):
            align("gate_36", "gate_29")
            play("baked_Op_371", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_371", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==171):
            align("gate_36", "gate_29")
            play("baked_Op_372", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_372", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==172):
            align("gate_36", "gate_29")
            play("baked_Op_373", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_373", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==173):
            align("gate_36", "gate_29")
            play("baked_Op_374", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_374", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==174):
            align("gate_36", "gate_29")
            play("baked_Op_375", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_375", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==175):
            align("gate_36", "gate_29")
            play("baked_Op_376", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_376", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==176):
            align("gate_36", "gate_29")
            play("baked_Op_377", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_377", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==177):
            align("gate_36", "gate_29")
            play("baked_Op_378", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_378", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==178):
            align("gate_36", "gate_29")
            play("baked_Op_379", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_379", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==179):
            align("gate_36", "gate_29")
            play("baked_Op_380", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_380", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==180):
            align("gate_36", "gate_29")
            play("baked_Op_381", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_381", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==181):
            align("gate_36", "gate_29")
            play("baked_Op_382", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_382", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==182):
            align("gate_36", "gate_29")
            play("baked_Op_383", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_383", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==183):
            align("gate_36", "gate_29")
            play("baked_Op_384", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_384", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==184):
            align("gate_36", "gate_29")
            play("baked_Op_385", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_385", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==185):
            align("gate_36", "gate_29")
            play("baked_Op_386", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_386", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==186):
            align("gate_36", "gate_29")
            play("baked_Op_387", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_387", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==187):
            align("gate_36", "gate_29")
            play("baked_Op_388", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_388", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==188):
            align("gate_36", "gate_29")
            play("baked_Op_389", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_389", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==189):
            align("gate_36", "gate_29")
            play("baked_Op_390", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_390", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==190):
            align("gate_36", "gate_29")
            play("baked_Op_391", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_391", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==191):
            align("gate_36", "gate_29")
            play("baked_Op_392", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_392", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==192):
            align("gate_36", "gate_29")
            play("baked_Op_393", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_393", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==193):
            align("gate_36", "gate_29")
            play("baked_Op_394", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_394", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==194):
            align("gate_36", "gate_29")
            play("baked_Op_395", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_395", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==195):
            align("gate_36", "gate_29")
            play("baked_Op_396", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_396", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==196):
            align("gate_36", "gate_29")
            play("baked_Op_397", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_397", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==197):
            align("gate_36", "gate_29")
            play("baked_Op_398", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_398", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==198):
            align("gate_36", "gate_29")
            play("baked_Op_399", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_399", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        with elif_(v4==199):
            align("gate_36", "gate_29")
            play("baked_Op_400", "gate_36")
            frame_rotation_2pi(0.0, "gate_36")
            play("baked_Op_400", "gate_29")
            frame_rotation_2pi(0.0, "gate_29")
        align("gate_36", "gate_29", "bottom_right_DQD_readout")
        play("CW"*amp(-1.046470672), "gate_36", duration=3750)
        play("CW"*amp(0.8573343600000001), "gate_29", duration=3750)
        measure("readout_pulse_10us", "bottom_right_DQD_readout", None, demod.sliced("cos", a1, 25, "out1"), demod.sliced("sin", a2, 25, "out1"))
        with for_(v3,0,v3<100,v3+1):
            r3 = declare_stream()
            save(a1[v3], r3)
            r4 = declare_stream()
            save(a2[v3], r4)
            wait(10, )
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
                    'offset': -0.0072,
                },
                '2': {
                    'offset': -0.0072,
                },
            },
            'digital_outputs': {
                '2': {},
            },
            'analog_inputs': {
                '2': {
                    'offset': 0,
                },
            },
        },
    },
    'elements': {
        'gate_29': {
            'singleInput': {
                'port': ('con1', 3),
            },
            'intermediate_frequency': 0.0,
            'hold_offset': {
                'duration': 24,
            },
            'operations': {
                'CW': 'CW',
                'baked_Op_0': 'gate_29_baked_pulse_0',
                'baked_Op_1': 'gate_29_baked_pulse_1',
                'baked_Op_2': 'gate_29_baked_pulse_2',
                'baked_Op_3': 'gate_29_baked_pulse_3',
                'baked_Op_4': 'gate_29_baked_pulse_4',
                'baked_Op_5': 'gate_29_baked_pulse_5',
                'baked_Op_6': 'gate_29_baked_pulse_6',
                'baked_Op_7': 'gate_29_baked_pulse_7',
                'baked_Op_8': 'gate_29_baked_pulse_8',
                'baked_Op_9': 'gate_29_baked_pulse_9',
                'baked_Op_10': 'gate_29_baked_pulse_10',
                'baked_Op_11': 'gate_29_baked_pulse_11',
                'baked_Op_12': 'gate_29_baked_pulse_12',
                'baked_Op_13': 'gate_29_baked_pulse_13',
                'baked_Op_14': 'gate_29_baked_pulse_14',
                'baked_Op_15': 'gate_29_baked_pulse_15',
                'baked_Op_16': 'gate_29_baked_pulse_16',
                'baked_Op_17': 'gate_29_baked_pulse_17',
                'baked_Op_18': 'gate_29_baked_pulse_18',
                'baked_Op_19': 'gate_29_baked_pulse_19',
                'baked_Op_20': 'gate_29_baked_pulse_20',
                'baked_Op_21': 'gate_29_baked_pulse_21',
                'baked_Op_22': 'gate_29_baked_pulse_22',
                'baked_Op_23': 'gate_29_baked_pulse_23',
                'baked_Op_24': 'gate_29_baked_pulse_24',
                'baked_Op_25': 'gate_29_baked_pulse_25',
                'baked_Op_26': 'gate_29_baked_pulse_26',
                'baked_Op_27': 'gate_29_baked_pulse_27',
                'baked_Op_28': 'gate_29_baked_pulse_28',
                'baked_Op_29': 'gate_29_baked_pulse_29',
                'baked_Op_30': 'gate_29_baked_pulse_30',
                'baked_Op_31': 'gate_29_baked_pulse_31',
                'baked_Op_32': 'gate_29_baked_pulse_32',
                'baked_Op_33': 'gate_29_baked_pulse_33',
                'baked_Op_34': 'gate_29_baked_pulse_34',
                'baked_Op_35': 'gate_29_baked_pulse_35',
                'baked_Op_36': 'gate_29_baked_pulse_36',
                'baked_Op_37': 'gate_29_baked_pulse_37',
                'baked_Op_38': 'gate_29_baked_pulse_38',
                'baked_Op_39': 'gate_29_baked_pulse_39',
                'baked_Op_40': 'gate_29_baked_pulse_40',
                'baked_Op_41': 'gate_29_baked_pulse_41',
                'baked_Op_42': 'gate_29_baked_pulse_42',
                'baked_Op_43': 'gate_29_baked_pulse_43',
                'baked_Op_44': 'gate_29_baked_pulse_44',
                'baked_Op_45': 'gate_29_baked_pulse_45',
                'baked_Op_46': 'gate_29_baked_pulse_46',
                'baked_Op_47': 'gate_29_baked_pulse_47',
                'baked_Op_48': 'gate_29_baked_pulse_48',
                'baked_Op_49': 'gate_29_baked_pulse_49',
                'baked_Op_50': 'gate_29_baked_pulse_50',
                'baked_Op_51': 'gate_29_baked_pulse_51',
                'baked_Op_52': 'gate_29_baked_pulse_52',
                'baked_Op_53': 'gate_29_baked_pulse_53',
                'baked_Op_54': 'gate_29_baked_pulse_54',
                'baked_Op_55': 'gate_29_baked_pulse_55',
                'baked_Op_56': 'gate_29_baked_pulse_56',
                'baked_Op_57': 'gate_29_baked_pulse_57',
                'baked_Op_58': 'gate_29_baked_pulse_58',
                'baked_Op_59': 'gate_29_baked_pulse_59',
                'baked_Op_60': 'gate_29_baked_pulse_60',
                'baked_Op_61': 'gate_29_baked_pulse_61',
                'baked_Op_62': 'gate_29_baked_pulse_62',
                'baked_Op_63': 'gate_29_baked_pulse_63',
                'baked_Op_64': 'gate_29_baked_pulse_64',
                'baked_Op_65': 'gate_29_baked_pulse_65',
                'baked_Op_66': 'gate_29_baked_pulse_66',
                'baked_Op_67': 'gate_29_baked_pulse_67',
                'baked_Op_68': 'gate_29_baked_pulse_68',
                'baked_Op_69': 'gate_29_baked_pulse_69',
                'baked_Op_70': 'gate_29_baked_pulse_70',
                'baked_Op_71': 'gate_29_baked_pulse_71',
                'baked_Op_72': 'gate_29_baked_pulse_72',
                'baked_Op_73': 'gate_29_baked_pulse_73',
                'baked_Op_74': 'gate_29_baked_pulse_74',
                'baked_Op_75': 'gate_29_baked_pulse_75',
                'baked_Op_76': 'gate_29_baked_pulse_76',
                'baked_Op_77': 'gate_29_baked_pulse_77',
                'baked_Op_78': 'gate_29_baked_pulse_78',
                'baked_Op_79': 'gate_29_baked_pulse_79',
                'baked_Op_80': 'gate_29_baked_pulse_80',
                'baked_Op_81': 'gate_29_baked_pulse_81',
                'baked_Op_82': 'gate_29_baked_pulse_82',
                'baked_Op_83': 'gate_29_baked_pulse_83',
                'baked_Op_84': 'gate_29_baked_pulse_84',
                'baked_Op_85': 'gate_29_baked_pulse_85',
                'baked_Op_86': 'gate_29_baked_pulse_86',
                'baked_Op_87': 'gate_29_baked_pulse_87',
                'baked_Op_88': 'gate_29_baked_pulse_88',
                'baked_Op_89': 'gate_29_baked_pulse_89',
                'baked_Op_90': 'gate_29_baked_pulse_90',
                'baked_Op_91': 'gate_29_baked_pulse_91',
                'baked_Op_92': 'gate_29_baked_pulse_92',
                'baked_Op_93': 'gate_29_baked_pulse_93',
                'baked_Op_94': 'gate_29_baked_pulse_94',
                'baked_Op_95': 'gate_29_baked_pulse_95',
                'baked_Op_96': 'gate_29_baked_pulse_96',
                'baked_Op_97': 'gate_29_baked_pulse_97',
                'baked_Op_98': 'gate_29_baked_pulse_98',
                'baked_Op_99': 'gate_29_baked_pulse_99',
                'baked_Op_100': 'gate_29_baked_pulse_100',
                'baked_Op_101': 'gate_29_baked_pulse_101',
                'baked_Op_102': 'gate_29_baked_pulse_102',
                'baked_Op_103': 'gate_29_baked_pulse_103',
                'baked_Op_104': 'gate_29_baked_pulse_104',
                'baked_Op_105': 'gate_29_baked_pulse_105',
                'baked_Op_106': 'gate_29_baked_pulse_106',
                'baked_Op_107': 'gate_29_baked_pulse_107',
                'baked_Op_108': 'gate_29_baked_pulse_108',
                'baked_Op_109': 'gate_29_baked_pulse_109',
                'baked_Op_110': 'gate_29_baked_pulse_110',
                'baked_Op_111': 'gate_29_baked_pulse_111',
                'baked_Op_112': 'gate_29_baked_pulse_112',
                'baked_Op_113': 'gate_29_baked_pulse_113',
                'baked_Op_114': 'gate_29_baked_pulse_114',
                'baked_Op_115': 'gate_29_baked_pulse_115',
                'baked_Op_116': 'gate_29_baked_pulse_116',
                'baked_Op_117': 'gate_29_baked_pulse_117',
                'baked_Op_118': 'gate_29_baked_pulse_118',
                'baked_Op_119': 'gate_29_baked_pulse_119',
                'baked_Op_120': 'gate_29_baked_pulse_120',
                'baked_Op_121': 'gate_29_baked_pulse_121',
                'baked_Op_122': 'gate_29_baked_pulse_122',
                'baked_Op_123': 'gate_29_baked_pulse_123',
                'baked_Op_124': 'gate_29_baked_pulse_124',
                'baked_Op_125': 'gate_29_baked_pulse_125',
                'baked_Op_126': 'gate_29_baked_pulse_126',
                'baked_Op_127': 'gate_29_baked_pulse_127',
                'baked_Op_128': 'gate_29_baked_pulse_128',
                'baked_Op_129': 'gate_29_baked_pulse_129',
                'baked_Op_130': 'gate_29_baked_pulse_130',
                'baked_Op_131': 'gate_29_baked_pulse_131',
                'baked_Op_132': 'gate_29_baked_pulse_132',
                'baked_Op_133': 'gate_29_baked_pulse_133',
                'baked_Op_134': 'gate_29_baked_pulse_134',
                'baked_Op_135': 'gate_29_baked_pulse_135',
                'baked_Op_136': 'gate_29_baked_pulse_136',
                'baked_Op_137': 'gate_29_baked_pulse_137',
                'baked_Op_138': 'gate_29_baked_pulse_138',
                'baked_Op_139': 'gate_29_baked_pulse_139',
                'baked_Op_140': 'gate_29_baked_pulse_140',
                'baked_Op_141': 'gate_29_baked_pulse_141',
                'baked_Op_142': 'gate_29_baked_pulse_142',
                'baked_Op_143': 'gate_29_baked_pulse_143',
                'baked_Op_144': 'gate_29_baked_pulse_144',
                'baked_Op_145': 'gate_29_baked_pulse_145',
                'baked_Op_146': 'gate_29_baked_pulse_146',
                'baked_Op_147': 'gate_29_baked_pulse_147',
                'baked_Op_148': 'gate_29_baked_pulse_148',
                'baked_Op_149': 'gate_29_baked_pulse_149',
                'baked_Op_150': 'gate_29_baked_pulse_150',
                'baked_Op_151': 'gate_29_baked_pulse_151',
                'baked_Op_152': 'gate_29_baked_pulse_152',
                'baked_Op_153': 'gate_29_baked_pulse_153',
                'baked_Op_154': 'gate_29_baked_pulse_154',
                'baked_Op_155': 'gate_29_baked_pulse_155',
                'baked_Op_156': 'gate_29_baked_pulse_156',
                'baked_Op_157': 'gate_29_baked_pulse_157',
                'baked_Op_158': 'gate_29_baked_pulse_158',
                'baked_Op_159': 'gate_29_baked_pulse_159',
                'baked_Op_160': 'gate_29_baked_pulse_160',
                'baked_Op_161': 'gate_29_baked_pulse_161',
                'baked_Op_162': 'gate_29_baked_pulse_162',
                'baked_Op_163': 'gate_29_baked_pulse_163',
                'baked_Op_164': 'gate_29_baked_pulse_164',
                'baked_Op_165': 'gate_29_baked_pulse_165',
                'baked_Op_166': 'gate_29_baked_pulse_166',
                'baked_Op_167': 'gate_29_baked_pulse_167',
                'baked_Op_168': 'gate_29_baked_pulse_168',
                'baked_Op_169': 'gate_29_baked_pulse_169',
                'baked_Op_170': 'gate_29_baked_pulse_170',
                'baked_Op_171': 'gate_29_baked_pulse_171',
                'baked_Op_172': 'gate_29_baked_pulse_172',
                'baked_Op_173': 'gate_29_baked_pulse_173',
                'baked_Op_174': 'gate_29_baked_pulse_174',
                'baked_Op_175': 'gate_29_baked_pulse_175',
                'baked_Op_176': 'gate_29_baked_pulse_176',
                'baked_Op_177': 'gate_29_baked_pulse_177',
                'baked_Op_178': 'gate_29_baked_pulse_178',
                'baked_Op_179': 'gate_29_baked_pulse_179',
                'baked_Op_180': 'gate_29_baked_pulse_180',
                'baked_Op_181': 'gate_29_baked_pulse_181',
                'baked_Op_182': 'gate_29_baked_pulse_182',
                'baked_Op_183': 'gate_29_baked_pulse_183',
                'baked_Op_184': 'gate_29_baked_pulse_184',
                'baked_Op_185': 'gate_29_baked_pulse_185',
                'baked_Op_186': 'gate_29_baked_pulse_186',
                'baked_Op_187': 'gate_29_baked_pulse_187',
                'baked_Op_188': 'gate_29_baked_pulse_188',
                'baked_Op_189': 'gate_29_baked_pulse_189',
                'baked_Op_190': 'gate_29_baked_pulse_190',
                'baked_Op_191': 'gate_29_baked_pulse_191',
                'baked_Op_192': 'gate_29_baked_pulse_192',
                'baked_Op_193': 'gate_29_baked_pulse_193',
                'baked_Op_194': 'gate_29_baked_pulse_194',
                'baked_Op_195': 'gate_29_baked_pulse_195',
                'baked_Op_196': 'gate_29_baked_pulse_196',
                'baked_Op_197': 'gate_29_baked_pulse_197',
                'baked_Op_198': 'gate_29_baked_pulse_198',
                'baked_Op_199': 'gate_29_baked_pulse_199',
                'baked_Op_200': 'gate_29_baked_pulse_200',
                'baked_Op_201': 'gate_29_baked_pulse_201',
                'baked_Op_202': 'gate_29_baked_pulse_202',
                'baked_Op_203': 'gate_29_baked_pulse_203',
                'baked_Op_204': 'gate_29_baked_pulse_204',
                'baked_Op_205': 'gate_29_baked_pulse_205',
                'baked_Op_206': 'gate_29_baked_pulse_206',
                'baked_Op_207': 'gate_29_baked_pulse_207',
                'baked_Op_208': 'gate_29_baked_pulse_208',
                'baked_Op_209': 'gate_29_baked_pulse_209',
                'baked_Op_210': 'gate_29_baked_pulse_210',
                'baked_Op_211': 'gate_29_baked_pulse_211',
                'baked_Op_212': 'gate_29_baked_pulse_212',
                'baked_Op_213': 'gate_29_baked_pulse_213',
                'baked_Op_214': 'gate_29_baked_pulse_214',
                'baked_Op_215': 'gate_29_baked_pulse_215',
                'baked_Op_216': 'gate_29_baked_pulse_216',
                'baked_Op_217': 'gate_29_baked_pulse_217',
                'baked_Op_218': 'gate_29_baked_pulse_218',
                'baked_Op_219': 'gate_29_baked_pulse_219',
                'baked_Op_220': 'gate_29_baked_pulse_220',
                'baked_Op_221': 'gate_29_baked_pulse_221',
                'baked_Op_222': 'gate_29_baked_pulse_222',
                'baked_Op_223': 'gate_29_baked_pulse_223',
                'baked_Op_224': 'gate_29_baked_pulse_224',
                'baked_Op_225': 'gate_29_baked_pulse_225',
                'baked_Op_226': 'gate_29_baked_pulse_226',
                'baked_Op_227': 'gate_29_baked_pulse_227',
                'baked_Op_228': 'gate_29_baked_pulse_228',
                'baked_Op_229': 'gate_29_baked_pulse_229',
                'baked_Op_230': 'gate_29_baked_pulse_230',
                'baked_Op_231': 'gate_29_baked_pulse_231',
                'baked_Op_232': 'gate_29_baked_pulse_232',
                'baked_Op_233': 'gate_29_baked_pulse_233',
                'baked_Op_234': 'gate_29_baked_pulse_234',
                'baked_Op_235': 'gate_29_baked_pulse_235',
                'baked_Op_236': 'gate_29_baked_pulse_236',
                'baked_Op_237': 'gate_29_baked_pulse_237',
                'baked_Op_238': 'gate_29_baked_pulse_238',
                'baked_Op_239': 'gate_29_baked_pulse_239',
                'baked_Op_240': 'gate_29_baked_pulse_240',
                'baked_Op_241': 'gate_29_baked_pulse_241',
                'baked_Op_242': 'gate_29_baked_pulse_242',
                'baked_Op_243': 'gate_29_baked_pulse_243',
                'baked_Op_244': 'gate_29_baked_pulse_244',
                'baked_Op_245': 'gate_29_baked_pulse_245',
                'baked_Op_246': 'gate_29_baked_pulse_246',
                'baked_Op_247': 'gate_29_baked_pulse_247',
                'baked_Op_248': 'gate_29_baked_pulse_248',
                'baked_Op_249': 'gate_29_baked_pulse_249',
                'baked_Op_250': 'gate_29_baked_pulse_250',
                'baked_Op_251': 'gate_29_baked_pulse_251',
                'baked_Op_252': 'gate_29_baked_pulse_252',
                'baked_Op_253': 'gate_29_baked_pulse_253',
                'baked_Op_254': 'gate_29_baked_pulse_254',
                'baked_Op_255': 'gate_29_baked_pulse_255',
                'baked_Op_256': 'gate_29_baked_pulse_256',
                'baked_Op_257': 'gate_29_baked_pulse_257',
                'baked_Op_258': 'gate_29_baked_pulse_258',
                'baked_Op_259': 'gate_29_baked_pulse_259',
                'baked_Op_260': 'gate_29_baked_pulse_260',
                'baked_Op_261': 'gate_29_baked_pulse_261',
                'baked_Op_262': 'gate_29_baked_pulse_262',
                'baked_Op_263': 'gate_29_baked_pulse_263',
                'baked_Op_264': 'gate_29_baked_pulse_264',
                'baked_Op_265': 'gate_29_baked_pulse_265',
                'baked_Op_266': 'gate_29_baked_pulse_266',
                'baked_Op_267': 'gate_29_baked_pulse_267',
                'baked_Op_268': 'gate_29_baked_pulse_268',
                'baked_Op_269': 'gate_29_baked_pulse_269',
                'baked_Op_270': 'gate_29_baked_pulse_270',
                'baked_Op_271': 'gate_29_baked_pulse_271',
                'baked_Op_272': 'gate_29_baked_pulse_272',
                'baked_Op_273': 'gate_29_baked_pulse_273',
                'baked_Op_274': 'gate_29_baked_pulse_274',
                'baked_Op_275': 'gate_29_baked_pulse_275',
                'baked_Op_276': 'gate_29_baked_pulse_276',
                'baked_Op_277': 'gate_29_baked_pulse_277',
                'baked_Op_278': 'gate_29_baked_pulse_278',
                'baked_Op_279': 'gate_29_baked_pulse_279',
                'baked_Op_280': 'gate_29_baked_pulse_280',
                'baked_Op_281': 'gate_29_baked_pulse_281',
                'baked_Op_282': 'gate_29_baked_pulse_282',
                'baked_Op_283': 'gate_29_baked_pulse_283',
                'baked_Op_284': 'gate_29_baked_pulse_284',
                'baked_Op_285': 'gate_29_baked_pulse_285',
                'baked_Op_286': 'gate_29_baked_pulse_286',
                'baked_Op_287': 'gate_29_baked_pulse_287',
                'baked_Op_288': 'gate_29_baked_pulse_288',
                'baked_Op_289': 'gate_29_baked_pulse_289',
                'baked_Op_290': 'gate_29_baked_pulse_290',
                'baked_Op_291': 'gate_29_baked_pulse_291',
                'baked_Op_292': 'gate_29_baked_pulse_292',
                'baked_Op_293': 'gate_29_baked_pulse_293',
                'baked_Op_294': 'gate_29_baked_pulse_294',
                'baked_Op_295': 'gate_29_baked_pulse_295',
                'baked_Op_296': 'gate_29_baked_pulse_296',
                'baked_Op_297': 'gate_29_baked_pulse_297',
                'baked_Op_298': 'gate_29_baked_pulse_298',
                'baked_Op_299': 'gate_29_baked_pulse_299',
                'baked_Op_300': 'gate_29_baked_pulse_300',
                'baked_Op_301': 'gate_29_baked_pulse_301',
                'baked_Op_302': 'gate_29_baked_pulse_302',
                'baked_Op_303': 'gate_29_baked_pulse_303',
                'baked_Op_304': 'gate_29_baked_pulse_304',
                'baked_Op_305': 'gate_29_baked_pulse_305',
                'baked_Op_306': 'gate_29_baked_pulse_306',
                'baked_Op_307': 'gate_29_baked_pulse_307',
                'baked_Op_308': 'gate_29_baked_pulse_308',
                'baked_Op_309': 'gate_29_baked_pulse_309',
                'baked_Op_310': 'gate_29_baked_pulse_310',
                'baked_Op_311': 'gate_29_baked_pulse_311',
                'baked_Op_312': 'gate_29_baked_pulse_312',
                'baked_Op_313': 'gate_29_baked_pulse_313',
                'baked_Op_314': 'gate_29_baked_pulse_314',
                'baked_Op_315': 'gate_29_baked_pulse_315',
                'baked_Op_316': 'gate_29_baked_pulse_316',
                'baked_Op_317': 'gate_29_baked_pulse_317',
                'baked_Op_318': 'gate_29_baked_pulse_318',
                'baked_Op_319': 'gate_29_baked_pulse_319',
                'baked_Op_320': 'gate_29_baked_pulse_320',
                'baked_Op_321': 'gate_29_baked_pulse_321',
                'baked_Op_322': 'gate_29_baked_pulse_322',
                'baked_Op_323': 'gate_29_baked_pulse_323',
                'baked_Op_324': 'gate_29_baked_pulse_324',
                'baked_Op_325': 'gate_29_baked_pulse_325',
                'baked_Op_326': 'gate_29_baked_pulse_326',
                'baked_Op_327': 'gate_29_baked_pulse_327',
                'baked_Op_328': 'gate_29_baked_pulse_328',
                'baked_Op_329': 'gate_29_baked_pulse_329',
                'baked_Op_330': 'gate_29_baked_pulse_330',
                'baked_Op_331': 'gate_29_baked_pulse_331',
                'baked_Op_332': 'gate_29_baked_pulse_332',
                'baked_Op_333': 'gate_29_baked_pulse_333',
                'baked_Op_334': 'gate_29_baked_pulse_334',
                'baked_Op_335': 'gate_29_baked_pulse_335',
                'baked_Op_336': 'gate_29_baked_pulse_336',
                'baked_Op_337': 'gate_29_baked_pulse_337',
                'baked_Op_338': 'gate_29_baked_pulse_338',
                'baked_Op_339': 'gate_29_baked_pulse_339',
                'baked_Op_340': 'gate_29_baked_pulse_340',
                'baked_Op_341': 'gate_29_baked_pulse_341',
                'baked_Op_342': 'gate_29_baked_pulse_342',
                'baked_Op_343': 'gate_29_baked_pulse_343',
                'baked_Op_344': 'gate_29_baked_pulse_344',
                'baked_Op_345': 'gate_29_baked_pulse_345',
                'baked_Op_346': 'gate_29_baked_pulse_346',
                'baked_Op_347': 'gate_29_baked_pulse_347',
                'baked_Op_348': 'gate_29_baked_pulse_348',
                'baked_Op_349': 'gate_29_baked_pulse_349',
                'baked_Op_350': 'gate_29_baked_pulse_350',
                'baked_Op_351': 'gate_29_baked_pulse_351',
                'baked_Op_352': 'gate_29_baked_pulse_352',
                'baked_Op_353': 'gate_29_baked_pulse_353',
                'baked_Op_354': 'gate_29_baked_pulse_354',
                'baked_Op_355': 'gate_29_baked_pulse_355',
                'baked_Op_356': 'gate_29_baked_pulse_356',
                'baked_Op_357': 'gate_29_baked_pulse_357',
                'baked_Op_358': 'gate_29_baked_pulse_358',
                'baked_Op_359': 'gate_29_baked_pulse_359',
                'baked_Op_360': 'gate_29_baked_pulse_360',
                'baked_Op_361': 'gate_29_baked_pulse_361',
                'baked_Op_362': 'gate_29_baked_pulse_362',
                'baked_Op_363': 'gate_29_baked_pulse_363',
                'baked_Op_364': 'gate_29_baked_pulse_364',
                'baked_Op_365': 'gate_29_baked_pulse_365',
                'baked_Op_366': 'gate_29_baked_pulse_366',
                'baked_Op_367': 'gate_29_baked_pulse_367',
                'baked_Op_368': 'gate_29_baked_pulse_368',
                'baked_Op_369': 'gate_29_baked_pulse_369',
                'baked_Op_370': 'gate_29_baked_pulse_370',
                'baked_Op_371': 'gate_29_baked_pulse_371',
                'baked_Op_372': 'gate_29_baked_pulse_372',
                'baked_Op_373': 'gate_29_baked_pulse_373',
                'baked_Op_374': 'gate_29_baked_pulse_374',
                'baked_Op_375': 'gate_29_baked_pulse_375',
                'baked_Op_376': 'gate_29_baked_pulse_376',
                'baked_Op_377': 'gate_29_baked_pulse_377',
                'baked_Op_378': 'gate_29_baked_pulse_378',
                'baked_Op_379': 'gate_29_baked_pulse_379',
                'baked_Op_380': 'gate_29_baked_pulse_380',
                'baked_Op_381': 'gate_29_baked_pulse_381',
                'baked_Op_382': 'gate_29_baked_pulse_382',
                'baked_Op_383': 'gate_29_baked_pulse_383',
                'baked_Op_384': 'gate_29_baked_pulse_384',
                'baked_Op_385': 'gate_29_baked_pulse_385',
                'baked_Op_386': 'gate_29_baked_pulse_386',
                'baked_Op_387': 'gate_29_baked_pulse_387',
                'baked_Op_388': 'gate_29_baked_pulse_388',
                'baked_Op_389': 'gate_29_baked_pulse_389',
                'baked_Op_390': 'gate_29_baked_pulse_390',
                'baked_Op_391': 'gate_29_baked_pulse_391',
                'baked_Op_392': 'gate_29_baked_pulse_392',
                'baked_Op_393': 'gate_29_baked_pulse_393',
                'baked_Op_394': 'gate_29_baked_pulse_394',
                'baked_Op_395': 'gate_29_baked_pulse_395',
                'baked_Op_396': 'gate_29_baked_pulse_396',
                'baked_Op_397': 'gate_29_baked_pulse_397',
                'baked_Op_398': 'gate_29_baked_pulse_398',
                'baked_Op_399': 'gate_29_baked_pulse_399',
                'baked_Op_400': 'gate_29_baked_pulse_400',
                'baked_Op_401': 'gate_29_baked_pulse_401',
            },
        },
        'gate_36': {
            'singleInput': {
                'port': ('con1', 2),
            },
            'intermediate_frequency': 0.0,
            'hold_offset': {
                'duration': 24,
            },
            'operations': {
                'CW': 'CW',
                'baked_Op_0': 'gate_36_baked_pulse_0',
                'baked_Op_1': 'gate_36_baked_pulse_1',
                'baked_Op_2': 'gate_36_baked_pulse_2',
                'baked_Op_3': 'gate_36_baked_pulse_3',
                'baked_Op_4': 'gate_36_baked_pulse_4',
                'baked_Op_5': 'gate_36_baked_pulse_5',
                'baked_Op_6': 'gate_36_baked_pulse_6',
                'baked_Op_7': 'gate_36_baked_pulse_7',
                'baked_Op_8': 'gate_36_baked_pulse_8',
                'baked_Op_9': 'gate_36_baked_pulse_9',
                'baked_Op_10': 'gate_36_baked_pulse_10',
                'baked_Op_11': 'gate_36_baked_pulse_11',
                'baked_Op_12': 'gate_36_baked_pulse_12',
                'baked_Op_13': 'gate_36_baked_pulse_13',
                'baked_Op_14': 'gate_36_baked_pulse_14',
                'baked_Op_15': 'gate_36_baked_pulse_15',
                'baked_Op_16': 'gate_36_baked_pulse_16',
                'baked_Op_17': 'gate_36_baked_pulse_17',
                'baked_Op_18': 'gate_36_baked_pulse_18',
                'baked_Op_19': 'gate_36_baked_pulse_19',
                'baked_Op_20': 'gate_36_baked_pulse_20',
                'baked_Op_21': 'gate_36_baked_pulse_21',
                'baked_Op_22': 'gate_36_baked_pulse_22',
                'baked_Op_23': 'gate_36_baked_pulse_23',
                'baked_Op_24': 'gate_36_baked_pulse_24',
                'baked_Op_25': 'gate_36_baked_pulse_25',
                'baked_Op_26': 'gate_36_baked_pulse_26',
                'baked_Op_27': 'gate_36_baked_pulse_27',
                'baked_Op_28': 'gate_36_baked_pulse_28',
                'baked_Op_29': 'gate_36_baked_pulse_29',
                'baked_Op_30': 'gate_36_baked_pulse_30',
                'baked_Op_31': 'gate_36_baked_pulse_31',
                'baked_Op_32': 'gate_36_baked_pulse_32',
                'baked_Op_33': 'gate_36_baked_pulse_33',
                'baked_Op_34': 'gate_36_baked_pulse_34',
                'baked_Op_35': 'gate_36_baked_pulse_35',
                'baked_Op_36': 'gate_36_baked_pulse_36',
                'baked_Op_37': 'gate_36_baked_pulse_37',
                'baked_Op_38': 'gate_36_baked_pulse_38',
                'baked_Op_39': 'gate_36_baked_pulse_39',
                'baked_Op_40': 'gate_36_baked_pulse_40',
                'baked_Op_41': 'gate_36_baked_pulse_41',
                'baked_Op_42': 'gate_36_baked_pulse_42',
                'baked_Op_43': 'gate_36_baked_pulse_43',
                'baked_Op_44': 'gate_36_baked_pulse_44',
                'baked_Op_45': 'gate_36_baked_pulse_45',
                'baked_Op_46': 'gate_36_baked_pulse_46',
                'baked_Op_47': 'gate_36_baked_pulse_47',
                'baked_Op_48': 'gate_36_baked_pulse_48',
                'baked_Op_49': 'gate_36_baked_pulse_49',
                'baked_Op_50': 'gate_36_baked_pulse_50',
                'baked_Op_51': 'gate_36_baked_pulse_51',
                'baked_Op_52': 'gate_36_baked_pulse_52',
                'baked_Op_53': 'gate_36_baked_pulse_53',
                'baked_Op_54': 'gate_36_baked_pulse_54',
                'baked_Op_55': 'gate_36_baked_pulse_55',
                'baked_Op_56': 'gate_36_baked_pulse_56',
                'baked_Op_57': 'gate_36_baked_pulse_57',
                'baked_Op_58': 'gate_36_baked_pulse_58',
                'baked_Op_59': 'gate_36_baked_pulse_59',
                'baked_Op_60': 'gate_36_baked_pulse_60',
                'baked_Op_61': 'gate_36_baked_pulse_61',
                'baked_Op_62': 'gate_36_baked_pulse_62',
                'baked_Op_63': 'gate_36_baked_pulse_63',
                'baked_Op_64': 'gate_36_baked_pulse_64',
                'baked_Op_65': 'gate_36_baked_pulse_65',
                'baked_Op_66': 'gate_36_baked_pulse_66',
                'baked_Op_67': 'gate_36_baked_pulse_67',
                'baked_Op_68': 'gate_36_baked_pulse_68',
                'baked_Op_69': 'gate_36_baked_pulse_69',
                'baked_Op_70': 'gate_36_baked_pulse_70',
                'baked_Op_71': 'gate_36_baked_pulse_71',
                'baked_Op_72': 'gate_36_baked_pulse_72',
                'baked_Op_73': 'gate_36_baked_pulse_73',
                'baked_Op_74': 'gate_36_baked_pulse_74',
                'baked_Op_75': 'gate_36_baked_pulse_75',
                'baked_Op_76': 'gate_36_baked_pulse_76',
                'baked_Op_77': 'gate_36_baked_pulse_77',
                'baked_Op_78': 'gate_36_baked_pulse_78',
                'baked_Op_79': 'gate_36_baked_pulse_79',
                'baked_Op_80': 'gate_36_baked_pulse_80',
                'baked_Op_81': 'gate_36_baked_pulse_81',
                'baked_Op_82': 'gate_36_baked_pulse_82',
                'baked_Op_83': 'gate_36_baked_pulse_83',
                'baked_Op_84': 'gate_36_baked_pulse_84',
                'baked_Op_85': 'gate_36_baked_pulse_85',
                'baked_Op_86': 'gate_36_baked_pulse_86',
                'baked_Op_87': 'gate_36_baked_pulse_87',
                'baked_Op_88': 'gate_36_baked_pulse_88',
                'baked_Op_89': 'gate_36_baked_pulse_89',
                'baked_Op_90': 'gate_36_baked_pulse_90',
                'baked_Op_91': 'gate_36_baked_pulse_91',
                'baked_Op_92': 'gate_36_baked_pulse_92',
                'baked_Op_93': 'gate_36_baked_pulse_93',
                'baked_Op_94': 'gate_36_baked_pulse_94',
                'baked_Op_95': 'gate_36_baked_pulse_95',
                'baked_Op_96': 'gate_36_baked_pulse_96',
                'baked_Op_97': 'gate_36_baked_pulse_97',
                'baked_Op_98': 'gate_36_baked_pulse_98',
                'baked_Op_99': 'gate_36_baked_pulse_99',
                'baked_Op_100': 'gate_36_baked_pulse_100',
                'baked_Op_101': 'gate_36_baked_pulse_101',
                'baked_Op_102': 'gate_36_baked_pulse_102',
                'baked_Op_103': 'gate_36_baked_pulse_103',
                'baked_Op_104': 'gate_36_baked_pulse_104',
                'baked_Op_105': 'gate_36_baked_pulse_105',
                'baked_Op_106': 'gate_36_baked_pulse_106',
                'baked_Op_107': 'gate_36_baked_pulse_107',
                'baked_Op_108': 'gate_36_baked_pulse_108',
                'baked_Op_109': 'gate_36_baked_pulse_109',
                'baked_Op_110': 'gate_36_baked_pulse_110',
                'baked_Op_111': 'gate_36_baked_pulse_111',
                'baked_Op_112': 'gate_36_baked_pulse_112',
                'baked_Op_113': 'gate_36_baked_pulse_113',
                'baked_Op_114': 'gate_36_baked_pulse_114',
                'baked_Op_115': 'gate_36_baked_pulse_115',
                'baked_Op_116': 'gate_36_baked_pulse_116',
                'baked_Op_117': 'gate_36_baked_pulse_117',
                'baked_Op_118': 'gate_36_baked_pulse_118',
                'baked_Op_119': 'gate_36_baked_pulse_119',
                'baked_Op_120': 'gate_36_baked_pulse_120',
                'baked_Op_121': 'gate_36_baked_pulse_121',
                'baked_Op_122': 'gate_36_baked_pulse_122',
                'baked_Op_123': 'gate_36_baked_pulse_123',
                'baked_Op_124': 'gate_36_baked_pulse_124',
                'baked_Op_125': 'gate_36_baked_pulse_125',
                'baked_Op_126': 'gate_36_baked_pulse_126',
                'baked_Op_127': 'gate_36_baked_pulse_127',
                'baked_Op_128': 'gate_36_baked_pulse_128',
                'baked_Op_129': 'gate_36_baked_pulse_129',
                'baked_Op_130': 'gate_36_baked_pulse_130',
                'baked_Op_131': 'gate_36_baked_pulse_131',
                'baked_Op_132': 'gate_36_baked_pulse_132',
                'baked_Op_133': 'gate_36_baked_pulse_133',
                'baked_Op_134': 'gate_36_baked_pulse_134',
                'baked_Op_135': 'gate_36_baked_pulse_135',
                'baked_Op_136': 'gate_36_baked_pulse_136',
                'baked_Op_137': 'gate_36_baked_pulse_137',
                'baked_Op_138': 'gate_36_baked_pulse_138',
                'baked_Op_139': 'gate_36_baked_pulse_139',
                'baked_Op_140': 'gate_36_baked_pulse_140',
                'baked_Op_141': 'gate_36_baked_pulse_141',
                'baked_Op_142': 'gate_36_baked_pulse_142',
                'baked_Op_143': 'gate_36_baked_pulse_143',
                'baked_Op_144': 'gate_36_baked_pulse_144',
                'baked_Op_145': 'gate_36_baked_pulse_145',
                'baked_Op_146': 'gate_36_baked_pulse_146',
                'baked_Op_147': 'gate_36_baked_pulse_147',
                'baked_Op_148': 'gate_36_baked_pulse_148',
                'baked_Op_149': 'gate_36_baked_pulse_149',
                'baked_Op_150': 'gate_36_baked_pulse_150',
                'baked_Op_151': 'gate_36_baked_pulse_151',
                'baked_Op_152': 'gate_36_baked_pulse_152',
                'baked_Op_153': 'gate_36_baked_pulse_153',
                'baked_Op_154': 'gate_36_baked_pulse_154',
                'baked_Op_155': 'gate_36_baked_pulse_155',
                'baked_Op_156': 'gate_36_baked_pulse_156',
                'baked_Op_157': 'gate_36_baked_pulse_157',
                'baked_Op_158': 'gate_36_baked_pulse_158',
                'baked_Op_159': 'gate_36_baked_pulse_159',
                'baked_Op_160': 'gate_36_baked_pulse_160',
                'baked_Op_161': 'gate_36_baked_pulse_161',
                'baked_Op_162': 'gate_36_baked_pulse_162',
                'baked_Op_163': 'gate_36_baked_pulse_163',
                'baked_Op_164': 'gate_36_baked_pulse_164',
                'baked_Op_165': 'gate_36_baked_pulse_165',
                'baked_Op_166': 'gate_36_baked_pulse_166',
                'baked_Op_167': 'gate_36_baked_pulse_167',
                'baked_Op_168': 'gate_36_baked_pulse_168',
                'baked_Op_169': 'gate_36_baked_pulse_169',
                'baked_Op_170': 'gate_36_baked_pulse_170',
                'baked_Op_171': 'gate_36_baked_pulse_171',
                'baked_Op_172': 'gate_36_baked_pulse_172',
                'baked_Op_173': 'gate_36_baked_pulse_173',
                'baked_Op_174': 'gate_36_baked_pulse_174',
                'baked_Op_175': 'gate_36_baked_pulse_175',
                'baked_Op_176': 'gate_36_baked_pulse_176',
                'baked_Op_177': 'gate_36_baked_pulse_177',
                'baked_Op_178': 'gate_36_baked_pulse_178',
                'baked_Op_179': 'gate_36_baked_pulse_179',
                'baked_Op_180': 'gate_36_baked_pulse_180',
                'baked_Op_181': 'gate_36_baked_pulse_181',
                'baked_Op_182': 'gate_36_baked_pulse_182',
                'baked_Op_183': 'gate_36_baked_pulse_183',
                'baked_Op_184': 'gate_36_baked_pulse_184',
                'baked_Op_185': 'gate_36_baked_pulse_185',
                'baked_Op_186': 'gate_36_baked_pulse_186',
                'baked_Op_187': 'gate_36_baked_pulse_187',
                'baked_Op_188': 'gate_36_baked_pulse_188',
                'baked_Op_189': 'gate_36_baked_pulse_189',
                'baked_Op_190': 'gate_36_baked_pulse_190',
                'baked_Op_191': 'gate_36_baked_pulse_191',
                'baked_Op_192': 'gate_36_baked_pulse_192',
                'baked_Op_193': 'gate_36_baked_pulse_193',
                'baked_Op_194': 'gate_36_baked_pulse_194',
                'baked_Op_195': 'gate_36_baked_pulse_195',
                'baked_Op_196': 'gate_36_baked_pulse_196',
                'baked_Op_197': 'gate_36_baked_pulse_197',
                'baked_Op_198': 'gate_36_baked_pulse_198',
                'baked_Op_199': 'gate_36_baked_pulse_199',
                'baked_Op_200': 'gate_36_baked_pulse_200',
                'baked_Op_201': 'gate_36_baked_pulse_201',
                'baked_Op_202': 'gate_36_baked_pulse_202',
                'baked_Op_203': 'gate_36_baked_pulse_203',
                'baked_Op_204': 'gate_36_baked_pulse_204',
                'baked_Op_205': 'gate_36_baked_pulse_205',
                'baked_Op_206': 'gate_36_baked_pulse_206',
                'baked_Op_207': 'gate_36_baked_pulse_207',
                'baked_Op_208': 'gate_36_baked_pulse_208',
                'baked_Op_209': 'gate_36_baked_pulse_209',
                'baked_Op_210': 'gate_36_baked_pulse_210',
                'baked_Op_211': 'gate_36_baked_pulse_211',
                'baked_Op_212': 'gate_36_baked_pulse_212',
                'baked_Op_213': 'gate_36_baked_pulse_213',
                'baked_Op_214': 'gate_36_baked_pulse_214',
                'baked_Op_215': 'gate_36_baked_pulse_215',
                'baked_Op_216': 'gate_36_baked_pulse_216',
                'baked_Op_217': 'gate_36_baked_pulse_217',
                'baked_Op_218': 'gate_36_baked_pulse_218',
                'baked_Op_219': 'gate_36_baked_pulse_219',
                'baked_Op_220': 'gate_36_baked_pulse_220',
                'baked_Op_221': 'gate_36_baked_pulse_221',
                'baked_Op_222': 'gate_36_baked_pulse_222',
                'baked_Op_223': 'gate_36_baked_pulse_223',
                'baked_Op_224': 'gate_36_baked_pulse_224',
                'baked_Op_225': 'gate_36_baked_pulse_225',
                'baked_Op_226': 'gate_36_baked_pulse_226',
                'baked_Op_227': 'gate_36_baked_pulse_227',
                'baked_Op_228': 'gate_36_baked_pulse_228',
                'baked_Op_229': 'gate_36_baked_pulse_229',
                'baked_Op_230': 'gate_36_baked_pulse_230',
                'baked_Op_231': 'gate_36_baked_pulse_231',
                'baked_Op_232': 'gate_36_baked_pulse_232',
                'baked_Op_233': 'gate_36_baked_pulse_233',
                'baked_Op_234': 'gate_36_baked_pulse_234',
                'baked_Op_235': 'gate_36_baked_pulse_235',
                'baked_Op_236': 'gate_36_baked_pulse_236',
                'baked_Op_237': 'gate_36_baked_pulse_237',
                'baked_Op_238': 'gate_36_baked_pulse_238',
                'baked_Op_239': 'gate_36_baked_pulse_239',
                'baked_Op_240': 'gate_36_baked_pulse_240',
                'baked_Op_241': 'gate_36_baked_pulse_241',
                'baked_Op_242': 'gate_36_baked_pulse_242',
                'baked_Op_243': 'gate_36_baked_pulse_243',
                'baked_Op_244': 'gate_36_baked_pulse_244',
                'baked_Op_245': 'gate_36_baked_pulse_245',
                'baked_Op_246': 'gate_36_baked_pulse_246',
                'baked_Op_247': 'gate_36_baked_pulse_247',
                'baked_Op_248': 'gate_36_baked_pulse_248',
                'baked_Op_249': 'gate_36_baked_pulse_249',
                'baked_Op_250': 'gate_36_baked_pulse_250',
                'baked_Op_251': 'gate_36_baked_pulse_251',
                'baked_Op_252': 'gate_36_baked_pulse_252',
                'baked_Op_253': 'gate_36_baked_pulse_253',
                'baked_Op_254': 'gate_36_baked_pulse_254',
                'baked_Op_255': 'gate_36_baked_pulse_255',
                'baked_Op_256': 'gate_36_baked_pulse_256',
                'baked_Op_257': 'gate_36_baked_pulse_257',
                'baked_Op_258': 'gate_36_baked_pulse_258',
                'baked_Op_259': 'gate_36_baked_pulse_259',
                'baked_Op_260': 'gate_36_baked_pulse_260',
                'baked_Op_261': 'gate_36_baked_pulse_261',
                'baked_Op_262': 'gate_36_baked_pulse_262',
                'baked_Op_263': 'gate_36_baked_pulse_263',
                'baked_Op_264': 'gate_36_baked_pulse_264',
                'baked_Op_265': 'gate_36_baked_pulse_265',
                'baked_Op_266': 'gate_36_baked_pulse_266',
                'baked_Op_267': 'gate_36_baked_pulse_267',
                'baked_Op_268': 'gate_36_baked_pulse_268',
                'baked_Op_269': 'gate_36_baked_pulse_269',
                'baked_Op_270': 'gate_36_baked_pulse_270',
                'baked_Op_271': 'gate_36_baked_pulse_271',
                'baked_Op_272': 'gate_36_baked_pulse_272',
                'baked_Op_273': 'gate_36_baked_pulse_273',
                'baked_Op_274': 'gate_36_baked_pulse_274',
                'baked_Op_275': 'gate_36_baked_pulse_275',
                'baked_Op_276': 'gate_36_baked_pulse_276',
                'baked_Op_277': 'gate_36_baked_pulse_277',
                'baked_Op_278': 'gate_36_baked_pulse_278',
                'baked_Op_279': 'gate_36_baked_pulse_279',
                'baked_Op_280': 'gate_36_baked_pulse_280',
                'baked_Op_281': 'gate_36_baked_pulse_281',
                'baked_Op_282': 'gate_36_baked_pulse_282',
                'baked_Op_283': 'gate_36_baked_pulse_283',
                'baked_Op_284': 'gate_36_baked_pulse_284',
                'baked_Op_285': 'gate_36_baked_pulse_285',
                'baked_Op_286': 'gate_36_baked_pulse_286',
                'baked_Op_287': 'gate_36_baked_pulse_287',
                'baked_Op_288': 'gate_36_baked_pulse_288',
                'baked_Op_289': 'gate_36_baked_pulse_289',
                'baked_Op_290': 'gate_36_baked_pulse_290',
                'baked_Op_291': 'gate_36_baked_pulse_291',
                'baked_Op_292': 'gate_36_baked_pulse_292',
                'baked_Op_293': 'gate_36_baked_pulse_293',
                'baked_Op_294': 'gate_36_baked_pulse_294',
                'baked_Op_295': 'gate_36_baked_pulse_295',
                'baked_Op_296': 'gate_36_baked_pulse_296',
                'baked_Op_297': 'gate_36_baked_pulse_297',
                'baked_Op_298': 'gate_36_baked_pulse_298',
                'baked_Op_299': 'gate_36_baked_pulse_299',
                'baked_Op_300': 'gate_36_baked_pulse_300',
                'baked_Op_301': 'gate_36_baked_pulse_301',
                'baked_Op_302': 'gate_36_baked_pulse_302',
                'baked_Op_303': 'gate_36_baked_pulse_303',
                'baked_Op_304': 'gate_36_baked_pulse_304',
                'baked_Op_305': 'gate_36_baked_pulse_305',
                'baked_Op_306': 'gate_36_baked_pulse_306',
                'baked_Op_307': 'gate_36_baked_pulse_307',
                'baked_Op_308': 'gate_36_baked_pulse_308',
                'baked_Op_309': 'gate_36_baked_pulse_309',
                'baked_Op_310': 'gate_36_baked_pulse_310',
                'baked_Op_311': 'gate_36_baked_pulse_311',
                'baked_Op_312': 'gate_36_baked_pulse_312',
                'baked_Op_313': 'gate_36_baked_pulse_313',
                'baked_Op_314': 'gate_36_baked_pulse_314',
                'baked_Op_315': 'gate_36_baked_pulse_315',
                'baked_Op_316': 'gate_36_baked_pulse_316',
                'baked_Op_317': 'gate_36_baked_pulse_317',
                'baked_Op_318': 'gate_36_baked_pulse_318',
                'baked_Op_319': 'gate_36_baked_pulse_319',
                'baked_Op_320': 'gate_36_baked_pulse_320',
                'baked_Op_321': 'gate_36_baked_pulse_321',
                'baked_Op_322': 'gate_36_baked_pulse_322',
                'baked_Op_323': 'gate_36_baked_pulse_323',
                'baked_Op_324': 'gate_36_baked_pulse_324',
                'baked_Op_325': 'gate_36_baked_pulse_325',
                'baked_Op_326': 'gate_36_baked_pulse_326',
                'baked_Op_327': 'gate_36_baked_pulse_327',
                'baked_Op_328': 'gate_36_baked_pulse_328',
                'baked_Op_329': 'gate_36_baked_pulse_329',
                'baked_Op_330': 'gate_36_baked_pulse_330',
                'baked_Op_331': 'gate_36_baked_pulse_331',
                'baked_Op_332': 'gate_36_baked_pulse_332',
                'baked_Op_333': 'gate_36_baked_pulse_333',
                'baked_Op_334': 'gate_36_baked_pulse_334',
                'baked_Op_335': 'gate_36_baked_pulse_335',
                'baked_Op_336': 'gate_36_baked_pulse_336',
                'baked_Op_337': 'gate_36_baked_pulse_337',
                'baked_Op_338': 'gate_36_baked_pulse_338',
                'baked_Op_339': 'gate_36_baked_pulse_339',
                'baked_Op_340': 'gate_36_baked_pulse_340',
                'baked_Op_341': 'gate_36_baked_pulse_341',
                'baked_Op_342': 'gate_36_baked_pulse_342',
                'baked_Op_343': 'gate_36_baked_pulse_343',
                'baked_Op_344': 'gate_36_baked_pulse_344',
                'baked_Op_345': 'gate_36_baked_pulse_345',
                'baked_Op_346': 'gate_36_baked_pulse_346',
                'baked_Op_347': 'gate_36_baked_pulse_347',
                'baked_Op_348': 'gate_36_baked_pulse_348',
                'baked_Op_349': 'gate_36_baked_pulse_349',
                'baked_Op_350': 'gate_36_baked_pulse_350',
                'baked_Op_351': 'gate_36_baked_pulse_351',
                'baked_Op_352': 'gate_36_baked_pulse_352',
                'baked_Op_353': 'gate_36_baked_pulse_353',
                'baked_Op_354': 'gate_36_baked_pulse_354',
                'baked_Op_355': 'gate_36_baked_pulse_355',
                'baked_Op_356': 'gate_36_baked_pulse_356',
                'baked_Op_357': 'gate_36_baked_pulse_357',
                'baked_Op_358': 'gate_36_baked_pulse_358',
                'baked_Op_359': 'gate_36_baked_pulse_359',
                'baked_Op_360': 'gate_36_baked_pulse_360',
                'baked_Op_361': 'gate_36_baked_pulse_361',
                'baked_Op_362': 'gate_36_baked_pulse_362',
                'baked_Op_363': 'gate_36_baked_pulse_363',
                'baked_Op_364': 'gate_36_baked_pulse_364',
                'baked_Op_365': 'gate_36_baked_pulse_365',
                'baked_Op_366': 'gate_36_baked_pulse_366',
                'baked_Op_367': 'gate_36_baked_pulse_367',
                'baked_Op_368': 'gate_36_baked_pulse_368',
                'baked_Op_369': 'gate_36_baked_pulse_369',
                'baked_Op_370': 'gate_36_baked_pulse_370',
                'baked_Op_371': 'gate_36_baked_pulse_371',
                'baked_Op_372': 'gate_36_baked_pulse_372',
                'baked_Op_373': 'gate_36_baked_pulse_373',
                'baked_Op_374': 'gate_36_baked_pulse_374',
                'baked_Op_375': 'gate_36_baked_pulse_375',
                'baked_Op_376': 'gate_36_baked_pulse_376',
                'baked_Op_377': 'gate_36_baked_pulse_377',
                'baked_Op_378': 'gate_36_baked_pulse_378',
                'baked_Op_379': 'gate_36_baked_pulse_379',
                'baked_Op_380': 'gate_36_baked_pulse_380',
                'baked_Op_381': 'gate_36_baked_pulse_381',
                'baked_Op_382': 'gate_36_baked_pulse_382',
                'baked_Op_383': 'gate_36_baked_pulse_383',
                'baked_Op_384': 'gate_36_baked_pulse_384',
                'baked_Op_385': 'gate_36_baked_pulse_385',
                'baked_Op_386': 'gate_36_baked_pulse_386',
                'baked_Op_387': 'gate_36_baked_pulse_387',
                'baked_Op_388': 'gate_36_baked_pulse_388',
                'baked_Op_389': 'gate_36_baked_pulse_389',
                'baked_Op_390': 'gate_36_baked_pulse_390',
                'baked_Op_391': 'gate_36_baked_pulse_391',
                'baked_Op_392': 'gate_36_baked_pulse_392',
                'baked_Op_393': 'gate_36_baked_pulse_393',
                'baked_Op_394': 'gate_36_baked_pulse_394',
                'baked_Op_395': 'gate_36_baked_pulse_395',
                'baked_Op_396': 'gate_36_baked_pulse_396',
                'baked_Op_397': 'gate_36_baked_pulse_397',
                'baked_Op_398': 'gate_36_baked_pulse_398',
                'baked_Op_399': 'gate_36_baked_pulse_399',
                'baked_Op_400': 'gate_36_baked_pulse_400',
                'baked_Op_401': 'gate_36_baked_pulse_401',
            },
        },
        'bottom_right_DQD_readout': {
            'singleInput': {
                'port': ('con1', 1),
            },
            'intermediate_frequency': 158256000,
            'operations': {
                'readout_pulse_10us': 'readout_pulse_10us',
                'readout_pulse_3ms': 'readout_pulse_3ms',
                'readout_pulse_3us': 'readout_pulse_3us',
                'readout_pulse_50us': 'readout_pulse_50us',
                'readout_pulse_t2star': 'readout_pulse_t2star',
                'readout_pulse_t2star_full_demod': 'readout_pulse_t2star_full_demod',
            },
            'outputs': {
                'out1': ('con1', 2),
            },
            'time_of_flight': 500,
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
        'readout_pulse_10us': {
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
        'readout_pulse_3us': {
            'operation': 'measurement',
            'length': 3000,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'integration_weights': {
                'cos': 'cos_3us',
                'sin': 'sin_3us',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_50us': {
            'operation': 'measurement',
            'length': 100000,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'integration_weights': {
                'cos': 'cos_50',
                'sin': 'sin_50',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_3ms': {
            'operation': 'measurement',
            'length': 3000000,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'integration_weights': {
                'cos': 'cos_buffered',
                'sin': 'sin_buffered',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_t2star': {
            'operation': 'measurement',
            'length': 15048,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'integration_weights': {
                'cos': 'cos_t2star',
                'sin': 'sin_t2star',
            },
            'digital_marker': 'ON',
        },
        'readout_pulse_t2star_full_demod': {
            'operation': 'measurement',
            'length': 15048,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'integration_weights': {
                'cos': 'cos_t2star_full_demod',
                'sin': 'sin_t2star_full_demod',
            },
            'digital_marker': 'ON',
        },
        'gate_29_baked_pulse_0': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_0',
            },
        },
        'gate_36_baked_pulse_0': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_0',
            },
        },
        'gate_29_baked_pulse_1': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_1',
            },
        },
        'gate_36_baked_pulse_1': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_1',
            },
        },
        'gate_29_baked_pulse_2': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_2',
            },
        },
        'gate_36_baked_pulse_2': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_2',
            },
        },
        'gate_29_baked_pulse_3': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_3',
            },
        },
        'gate_36_baked_pulse_3': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_3',
            },
        },
        'gate_29_baked_pulse_4': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_4',
            },
        },
        'gate_36_baked_pulse_4': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_4',
            },
        },
        'gate_29_baked_pulse_5': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_5',
            },
        },
        'gate_36_baked_pulse_5': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_5',
            },
        },
        'gate_29_baked_pulse_6': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_6',
            },
        },
        'gate_36_baked_pulse_6': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_6',
            },
        },
        'gate_29_baked_pulse_7': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_7',
            },
        },
        'gate_36_baked_pulse_7': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_7',
            },
        },
        'gate_29_baked_pulse_8': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_8',
            },
        },
        'gate_36_baked_pulse_8': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_8',
            },
        },
        'gate_29_baked_pulse_9': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_9',
            },
        },
        'gate_36_baked_pulse_9': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_9',
            },
        },
        'gate_29_baked_pulse_10': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_10',
            },
        },
        'gate_36_baked_pulse_10': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_10',
            },
        },
        'gate_29_baked_pulse_11': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_11',
            },
        },
        'gate_36_baked_pulse_11': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_11',
            },
        },
        'gate_29_baked_pulse_12': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_12',
            },
        },
        'gate_36_baked_pulse_12': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_12',
            },
        },
        'gate_29_baked_pulse_13': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_13',
            },
        },
        'gate_36_baked_pulse_13': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_13',
            },
        },
        'gate_29_baked_pulse_14': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_14',
            },
        },
        'gate_36_baked_pulse_14': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_14',
            },
        },
        'gate_29_baked_pulse_15': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_15',
            },
        },
        'gate_36_baked_pulse_15': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_15',
            },
        },
        'gate_29_baked_pulse_16': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_16',
            },
        },
        'gate_36_baked_pulse_16': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_16',
            },
        },
        'gate_29_baked_pulse_17': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_17',
            },
        },
        'gate_36_baked_pulse_17': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_17',
            },
        },
        'gate_29_baked_pulse_18': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_18',
            },
        },
        'gate_36_baked_pulse_18': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_18',
            },
        },
        'gate_29_baked_pulse_19': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_19',
            },
        },
        'gate_36_baked_pulse_19': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_19',
            },
        },
        'gate_29_baked_pulse_20': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_20',
            },
        },
        'gate_36_baked_pulse_20': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_20',
            },
        },
        'gate_29_baked_pulse_21': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_21',
            },
        },
        'gate_36_baked_pulse_21': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_21',
            },
        },
        'gate_29_baked_pulse_22': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_22',
            },
        },
        'gate_36_baked_pulse_22': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_22',
            },
        },
        'gate_29_baked_pulse_23': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_23',
            },
        },
        'gate_36_baked_pulse_23': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_23',
            },
        },
        'gate_29_baked_pulse_24': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_24',
            },
        },
        'gate_36_baked_pulse_24': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_24',
            },
        },
        'gate_29_baked_pulse_25': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_25',
            },
        },
        'gate_36_baked_pulse_25': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_25',
            },
        },
        'gate_29_baked_pulse_26': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_26',
            },
        },
        'gate_36_baked_pulse_26': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_26',
            },
        },
        'gate_29_baked_pulse_27': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_27',
            },
        },
        'gate_36_baked_pulse_27': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_27',
            },
        },
        'gate_29_baked_pulse_28': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_28',
            },
        },
        'gate_36_baked_pulse_28': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_28',
            },
        },
        'gate_29_baked_pulse_29': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_29',
            },
        },
        'gate_36_baked_pulse_29': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_29',
            },
        },
        'gate_29_baked_pulse_30': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_30',
            },
        },
        'gate_36_baked_pulse_30': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_30',
            },
        },
        'gate_29_baked_pulse_31': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_31',
            },
        },
        'gate_36_baked_pulse_31': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_31',
            },
        },
        'gate_29_baked_pulse_32': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_32',
            },
        },
        'gate_36_baked_pulse_32': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_32',
            },
        },
        'gate_29_baked_pulse_33': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_33',
            },
        },
        'gate_36_baked_pulse_33': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_33',
            },
        },
        'gate_29_baked_pulse_34': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_34',
            },
        },
        'gate_36_baked_pulse_34': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_34',
            },
        },
        'gate_29_baked_pulse_35': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_35',
            },
        },
        'gate_36_baked_pulse_35': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_35',
            },
        },
        'gate_29_baked_pulse_36': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_36',
            },
        },
        'gate_36_baked_pulse_36': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_36',
            },
        },
        'gate_29_baked_pulse_37': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_37',
            },
        },
        'gate_36_baked_pulse_37': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_37',
            },
        },
        'gate_29_baked_pulse_38': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_38',
            },
        },
        'gate_36_baked_pulse_38': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_38',
            },
        },
        'gate_29_baked_pulse_39': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_39',
            },
        },
        'gate_36_baked_pulse_39': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_39',
            },
        },
        'gate_29_baked_pulse_40': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_40',
            },
        },
        'gate_36_baked_pulse_40': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_40',
            },
        },
        'gate_29_baked_pulse_41': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_41',
            },
        },
        'gate_36_baked_pulse_41': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_41',
            },
        },
        'gate_29_baked_pulse_42': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_42',
            },
        },
        'gate_36_baked_pulse_42': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_42',
            },
        },
        'gate_29_baked_pulse_43': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_43',
            },
        },
        'gate_36_baked_pulse_43': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_43',
            },
        },
        'gate_29_baked_pulse_44': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_44',
            },
        },
        'gate_36_baked_pulse_44': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_44',
            },
        },
        'gate_29_baked_pulse_45': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_45',
            },
        },
        'gate_36_baked_pulse_45': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_45',
            },
        },
        'gate_29_baked_pulse_46': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_46',
            },
        },
        'gate_36_baked_pulse_46': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_46',
            },
        },
        'gate_29_baked_pulse_47': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_47',
            },
        },
        'gate_36_baked_pulse_47': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_47',
            },
        },
        'gate_29_baked_pulse_48': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_48',
            },
        },
        'gate_36_baked_pulse_48': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_48',
            },
        },
        'gate_29_baked_pulse_49': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_49',
            },
        },
        'gate_36_baked_pulse_49': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_49',
            },
        },
        'gate_29_baked_pulse_50': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_50',
            },
        },
        'gate_36_baked_pulse_50': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_50',
            },
        },
        'gate_29_baked_pulse_51': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_51',
            },
        },
        'gate_36_baked_pulse_51': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_51',
            },
        },
        'gate_29_baked_pulse_52': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_52',
            },
        },
        'gate_36_baked_pulse_52': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_52',
            },
        },
        'gate_29_baked_pulse_53': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_53',
            },
        },
        'gate_36_baked_pulse_53': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_53',
            },
        },
        'gate_29_baked_pulse_54': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_54',
            },
        },
        'gate_36_baked_pulse_54': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_54',
            },
        },
        'gate_29_baked_pulse_55': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_55',
            },
        },
        'gate_36_baked_pulse_55': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_55',
            },
        },
        'gate_29_baked_pulse_56': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_56',
            },
        },
        'gate_36_baked_pulse_56': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_56',
            },
        },
        'gate_29_baked_pulse_57': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_57',
            },
        },
        'gate_36_baked_pulse_57': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_57',
            },
        },
        'gate_29_baked_pulse_58': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_58',
            },
        },
        'gate_36_baked_pulse_58': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_58',
            },
        },
        'gate_29_baked_pulse_59': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_59',
            },
        },
        'gate_36_baked_pulse_59': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_59',
            },
        },
        'gate_29_baked_pulse_60': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_60',
            },
        },
        'gate_36_baked_pulse_60': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_60',
            },
        },
        'gate_29_baked_pulse_61': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_61',
            },
        },
        'gate_36_baked_pulse_61': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_61',
            },
        },
        'gate_29_baked_pulse_62': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_62',
            },
        },
        'gate_36_baked_pulse_62': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_62',
            },
        },
        'gate_29_baked_pulse_63': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_63',
            },
        },
        'gate_36_baked_pulse_63': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_63',
            },
        },
        'gate_29_baked_pulse_64': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_64',
            },
        },
        'gate_36_baked_pulse_64': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_64',
            },
        },
        'gate_29_baked_pulse_65': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_65',
            },
        },
        'gate_36_baked_pulse_65': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_65',
            },
        },
        'gate_29_baked_pulse_66': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_66',
            },
        },
        'gate_36_baked_pulse_66': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_66',
            },
        },
        'gate_29_baked_pulse_67': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_67',
            },
        },
        'gate_36_baked_pulse_67': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_67',
            },
        },
        'gate_29_baked_pulse_68': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_68',
            },
        },
        'gate_36_baked_pulse_68': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_68',
            },
        },
        'gate_29_baked_pulse_69': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_69',
            },
        },
        'gate_36_baked_pulse_69': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_69',
            },
        },
        'gate_29_baked_pulse_70': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_70',
            },
        },
        'gate_36_baked_pulse_70': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_70',
            },
        },
        'gate_29_baked_pulse_71': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_71',
            },
        },
        'gate_36_baked_pulse_71': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_71',
            },
        },
        'gate_29_baked_pulse_72': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_72',
            },
        },
        'gate_36_baked_pulse_72': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_72',
            },
        },
        'gate_29_baked_pulse_73': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_73',
            },
        },
        'gate_36_baked_pulse_73': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_73',
            },
        },
        'gate_29_baked_pulse_74': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_74',
            },
        },
        'gate_36_baked_pulse_74': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_74',
            },
        },
        'gate_29_baked_pulse_75': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_75',
            },
        },
        'gate_36_baked_pulse_75': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_75',
            },
        },
        'gate_29_baked_pulse_76': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_76',
            },
        },
        'gate_36_baked_pulse_76': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_76',
            },
        },
        'gate_29_baked_pulse_77': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_77',
            },
        },
        'gate_36_baked_pulse_77': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_77',
            },
        },
        'gate_29_baked_pulse_78': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_78',
            },
        },
        'gate_36_baked_pulse_78': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_78',
            },
        },
        'gate_29_baked_pulse_79': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_79',
            },
        },
        'gate_36_baked_pulse_79': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_79',
            },
        },
        'gate_29_baked_pulse_80': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_80',
            },
        },
        'gate_36_baked_pulse_80': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_80',
            },
        },
        'gate_29_baked_pulse_81': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_81',
            },
        },
        'gate_36_baked_pulse_81': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_81',
            },
        },
        'gate_29_baked_pulse_82': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_82',
            },
        },
        'gate_36_baked_pulse_82': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_82',
            },
        },
        'gate_29_baked_pulse_83': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_83',
            },
        },
        'gate_36_baked_pulse_83': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_83',
            },
        },
        'gate_29_baked_pulse_84': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_84',
            },
        },
        'gate_36_baked_pulse_84': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_84',
            },
        },
        'gate_29_baked_pulse_85': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_85',
            },
        },
        'gate_36_baked_pulse_85': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_85',
            },
        },
        'gate_29_baked_pulse_86': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_86',
            },
        },
        'gate_36_baked_pulse_86': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_86',
            },
        },
        'gate_29_baked_pulse_87': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_87',
            },
        },
        'gate_36_baked_pulse_87': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_87',
            },
        },
        'gate_29_baked_pulse_88': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_88',
            },
        },
        'gate_36_baked_pulse_88': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_88',
            },
        },
        'gate_29_baked_pulse_89': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_89',
            },
        },
        'gate_36_baked_pulse_89': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_89',
            },
        },
        'gate_29_baked_pulse_90': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_90',
            },
        },
        'gate_36_baked_pulse_90': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_90',
            },
        },
        'gate_29_baked_pulse_91': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_91',
            },
        },
        'gate_36_baked_pulse_91': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_91',
            },
        },
        'gate_29_baked_pulse_92': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_92',
            },
        },
        'gate_36_baked_pulse_92': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_92',
            },
        },
        'gate_29_baked_pulse_93': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_93',
            },
        },
        'gate_36_baked_pulse_93': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_93',
            },
        },
        'gate_29_baked_pulse_94': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_94',
            },
        },
        'gate_36_baked_pulse_94': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_94',
            },
        },
        'gate_29_baked_pulse_95': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_95',
            },
        },
        'gate_36_baked_pulse_95': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_95',
            },
        },
        'gate_29_baked_pulse_96': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_96',
            },
        },
        'gate_36_baked_pulse_96': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_96',
            },
        },
        'gate_29_baked_pulse_97': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_97',
            },
        },
        'gate_36_baked_pulse_97': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_97',
            },
        },
        'gate_29_baked_pulse_98': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_98',
            },
        },
        'gate_36_baked_pulse_98': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_98',
            },
        },
        'gate_29_baked_pulse_99': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_99',
            },
        },
        'gate_36_baked_pulse_99': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_99',
            },
        },
        'gate_29_baked_pulse_100': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_100',
            },
        },
        'gate_36_baked_pulse_100': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_100',
            },
        },
        'gate_29_baked_pulse_101': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_101',
            },
        },
        'gate_36_baked_pulse_101': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_101',
            },
        },
        'gate_29_baked_pulse_102': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_102',
            },
        },
        'gate_36_baked_pulse_102': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_102',
            },
        },
        'gate_29_baked_pulse_103': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_103',
            },
        },
        'gate_36_baked_pulse_103': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_103',
            },
        },
        'gate_29_baked_pulse_104': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_104',
            },
        },
        'gate_36_baked_pulse_104': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_104',
            },
        },
        'gate_29_baked_pulse_105': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_105',
            },
        },
        'gate_36_baked_pulse_105': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_105',
            },
        },
        'gate_29_baked_pulse_106': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_106',
            },
        },
        'gate_36_baked_pulse_106': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_106',
            },
        },
        'gate_29_baked_pulse_107': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_107',
            },
        },
        'gate_36_baked_pulse_107': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_107',
            },
        },
        'gate_29_baked_pulse_108': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_108',
            },
        },
        'gate_36_baked_pulse_108': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_108',
            },
        },
        'gate_29_baked_pulse_109': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_109',
            },
        },
        'gate_36_baked_pulse_109': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_109',
            },
        },
        'gate_29_baked_pulse_110': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_110',
            },
        },
        'gate_36_baked_pulse_110': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_110',
            },
        },
        'gate_29_baked_pulse_111': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_111',
            },
        },
        'gate_36_baked_pulse_111': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_111',
            },
        },
        'gate_29_baked_pulse_112': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_112',
            },
        },
        'gate_36_baked_pulse_112': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_112',
            },
        },
        'gate_29_baked_pulse_113': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_113',
            },
        },
        'gate_36_baked_pulse_113': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_113',
            },
        },
        'gate_29_baked_pulse_114': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_114',
            },
        },
        'gate_36_baked_pulse_114': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_114',
            },
        },
        'gate_29_baked_pulse_115': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_115',
            },
        },
        'gate_36_baked_pulse_115': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_115',
            },
        },
        'gate_29_baked_pulse_116': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_116',
            },
        },
        'gate_36_baked_pulse_116': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_116',
            },
        },
        'gate_29_baked_pulse_117': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_117',
            },
        },
        'gate_36_baked_pulse_117': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_117',
            },
        },
        'gate_29_baked_pulse_118': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_118',
            },
        },
        'gate_36_baked_pulse_118': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_118',
            },
        },
        'gate_29_baked_pulse_119': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_119',
            },
        },
        'gate_36_baked_pulse_119': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_119',
            },
        },
        'gate_29_baked_pulse_120': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_120',
            },
        },
        'gate_36_baked_pulse_120': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_120',
            },
        },
        'gate_29_baked_pulse_121': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_121',
            },
        },
        'gate_36_baked_pulse_121': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_121',
            },
        },
        'gate_29_baked_pulse_122': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_122',
            },
        },
        'gate_36_baked_pulse_122': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_122',
            },
        },
        'gate_29_baked_pulse_123': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_123',
            },
        },
        'gate_36_baked_pulse_123': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_123',
            },
        },
        'gate_29_baked_pulse_124': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_124',
            },
        },
        'gate_36_baked_pulse_124': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_124',
            },
        },
        'gate_29_baked_pulse_125': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_125',
            },
        },
        'gate_36_baked_pulse_125': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_125',
            },
        },
        'gate_29_baked_pulse_126': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_126',
            },
        },
        'gate_36_baked_pulse_126': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_126',
            },
        },
        'gate_29_baked_pulse_127': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_127',
            },
        },
        'gate_36_baked_pulse_127': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_127',
            },
        },
        'gate_29_baked_pulse_128': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_128',
            },
        },
        'gate_36_baked_pulse_128': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_128',
            },
        },
        'gate_29_baked_pulse_129': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_129',
            },
        },
        'gate_36_baked_pulse_129': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_129',
            },
        },
        'gate_29_baked_pulse_130': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_130',
            },
        },
        'gate_36_baked_pulse_130': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_130',
            },
        },
        'gate_29_baked_pulse_131': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_131',
            },
        },
        'gate_36_baked_pulse_131': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_131',
            },
        },
        'gate_29_baked_pulse_132': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_132',
            },
        },
        'gate_36_baked_pulse_132': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_132',
            },
        },
        'gate_29_baked_pulse_133': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_133',
            },
        },
        'gate_36_baked_pulse_133': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_133',
            },
        },
        'gate_29_baked_pulse_134': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_134',
            },
        },
        'gate_36_baked_pulse_134': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_134',
            },
        },
        'gate_29_baked_pulse_135': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_135',
            },
        },
        'gate_36_baked_pulse_135': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_135',
            },
        },
        'gate_29_baked_pulse_136': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_136',
            },
        },
        'gate_36_baked_pulse_136': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_136',
            },
        },
        'gate_29_baked_pulse_137': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_137',
            },
        },
        'gate_36_baked_pulse_137': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_137',
            },
        },
        'gate_29_baked_pulse_138': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_138',
            },
        },
        'gate_36_baked_pulse_138': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_138',
            },
        },
        'gate_29_baked_pulse_139': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_139',
            },
        },
        'gate_36_baked_pulse_139': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_139',
            },
        },
        'gate_29_baked_pulse_140': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_140',
            },
        },
        'gate_36_baked_pulse_140': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_140',
            },
        },
        'gate_29_baked_pulse_141': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_141',
            },
        },
        'gate_36_baked_pulse_141': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_141',
            },
        },
        'gate_29_baked_pulse_142': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_142',
            },
        },
        'gate_36_baked_pulse_142': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_142',
            },
        },
        'gate_29_baked_pulse_143': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_143',
            },
        },
        'gate_36_baked_pulse_143': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_143',
            },
        },
        'gate_29_baked_pulse_144': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_144',
            },
        },
        'gate_36_baked_pulse_144': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_144',
            },
        },
        'gate_29_baked_pulse_145': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_145',
            },
        },
        'gate_36_baked_pulse_145': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_145',
            },
        },
        'gate_29_baked_pulse_146': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_146',
            },
        },
        'gate_36_baked_pulse_146': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_146',
            },
        },
        'gate_29_baked_pulse_147': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_147',
            },
        },
        'gate_36_baked_pulse_147': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_147',
            },
        },
        'gate_29_baked_pulse_148': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_148',
            },
        },
        'gate_36_baked_pulse_148': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_148',
            },
        },
        'gate_29_baked_pulse_149': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_149',
            },
        },
        'gate_36_baked_pulse_149': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_149',
            },
        },
        'gate_29_baked_pulse_150': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_150',
            },
        },
        'gate_36_baked_pulse_150': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_150',
            },
        },
        'gate_29_baked_pulse_151': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_151',
            },
        },
        'gate_36_baked_pulse_151': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_151',
            },
        },
        'gate_29_baked_pulse_152': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_152',
            },
        },
        'gate_36_baked_pulse_152': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_152',
            },
        },
        'gate_29_baked_pulse_153': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_153',
            },
        },
        'gate_36_baked_pulse_153': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_153',
            },
        },
        'gate_29_baked_pulse_154': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_154',
            },
        },
        'gate_36_baked_pulse_154': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_154',
            },
        },
        'gate_29_baked_pulse_155': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_155',
            },
        },
        'gate_36_baked_pulse_155': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_155',
            },
        },
        'gate_29_baked_pulse_156': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_156',
            },
        },
        'gate_36_baked_pulse_156': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_156',
            },
        },
        'gate_29_baked_pulse_157': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_157',
            },
        },
        'gate_36_baked_pulse_157': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_157',
            },
        },
        'gate_29_baked_pulse_158': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_158',
            },
        },
        'gate_36_baked_pulse_158': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_158',
            },
        },
        'gate_29_baked_pulse_159': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_159',
            },
        },
        'gate_36_baked_pulse_159': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_159',
            },
        },
        'gate_29_baked_pulse_160': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_160',
            },
        },
        'gate_36_baked_pulse_160': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_160',
            },
        },
        'gate_29_baked_pulse_161': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_161',
            },
        },
        'gate_36_baked_pulse_161': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_161',
            },
        },
        'gate_29_baked_pulse_162': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_162',
            },
        },
        'gate_36_baked_pulse_162': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_162',
            },
        },
        'gate_29_baked_pulse_163': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_163',
            },
        },
        'gate_36_baked_pulse_163': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_163',
            },
        },
        'gate_29_baked_pulse_164': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_164',
            },
        },
        'gate_36_baked_pulse_164': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_164',
            },
        },
        'gate_29_baked_pulse_165': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_165',
            },
        },
        'gate_36_baked_pulse_165': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_165',
            },
        },
        'gate_29_baked_pulse_166': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_166',
            },
        },
        'gate_36_baked_pulse_166': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_166',
            },
        },
        'gate_29_baked_pulse_167': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_167',
            },
        },
        'gate_36_baked_pulse_167': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_167',
            },
        },
        'gate_29_baked_pulse_168': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_168',
            },
        },
        'gate_36_baked_pulse_168': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_168',
            },
        },
        'gate_29_baked_pulse_169': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_169',
            },
        },
        'gate_36_baked_pulse_169': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_169',
            },
        },
        'gate_29_baked_pulse_170': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_170',
            },
        },
        'gate_36_baked_pulse_170': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_170',
            },
        },
        'gate_29_baked_pulse_171': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_171',
            },
        },
        'gate_36_baked_pulse_171': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_171',
            },
        },
        'gate_29_baked_pulse_172': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_172',
            },
        },
        'gate_36_baked_pulse_172': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_172',
            },
        },
        'gate_29_baked_pulse_173': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_173',
            },
        },
        'gate_36_baked_pulse_173': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_173',
            },
        },
        'gate_29_baked_pulse_174': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_174',
            },
        },
        'gate_36_baked_pulse_174': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_174',
            },
        },
        'gate_29_baked_pulse_175': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_175',
            },
        },
        'gate_36_baked_pulse_175': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_175',
            },
        },
        'gate_29_baked_pulse_176': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_176',
            },
        },
        'gate_36_baked_pulse_176': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_176',
            },
        },
        'gate_29_baked_pulse_177': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_177',
            },
        },
        'gate_36_baked_pulse_177': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_177',
            },
        },
        'gate_29_baked_pulse_178': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_178',
            },
        },
        'gate_36_baked_pulse_178': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_178',
            },
        },
        'gate_29_baked_pulse_179': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_179',
            },
        },
        'gate_36_baked_pulse_179': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_179',
            },
        },
        'gate_29_baked_pulse_180': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_180',
            },
        },
        'gate_36_baked_pulse_180': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_180',
            },
        },
        'gate_29_baked_pulse_181': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_181',
            },
        },
        'gate_36_baked_pulse_181': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_181',
            },
        },
        'gate_29_baked_pulse_182': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_182',
            },
        },
        'gate_36_baked_pulse_182': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_182',
            },
        },
        'gate_29_baked_pulse_183': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_183',
            },
        },
        'gate_36_baked_pulse_183': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_183',
            },
        },
        'gate_29_baked_pulse_184': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_184',
            },
        },
        'gate_36_baked_pulse_184': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_184',
            },
        },
        'gate_29_baked_pulse_185': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_185',
            },
        },
        'gate_36_baked_pulse_185': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_185',
            },
        },
        'gate_29_baked_pulse_186': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_186',
            },
        },
        'gate_36_baked_pulse_186': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_186',
            },
        },
        'gate_29_baked_pulse_187': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_187',
            },
        },
        'gate_36_baked_pulse_187': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_187',
            },
        },
        'gate_29_baked_pulse_188': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_188',
            },
        },
        'gate_36_baked_pulse_188': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_188',
            },
        },
        'gate_29_baked_pulse_189': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_189',
            },
        },
        'gate_36_baked_pulse_189': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_189',
            },
        },
        'gate_29_baked_pulse_190': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_190',
            },
        },
        'gate_36_baked_pulse_190': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_190',
            },
        },
        'gate_29_baked_pulse_191': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_191',
            },
        },
        'gate_36_baked_pulse_191': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_191',
            },
        },
        'gate_29_baked_pulse_192': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_192',
            },
        },
        'gate_36_baked_pulse_192': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_192',
            },
        },
        'gate_29_baked_pulse_193': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_193',
            },
        },
        'gate_36_baked_pulse_193': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_193',
            },
        },
        'gate_29_baked_pulse_194': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_194',
            },
        },
        'gate_36_baked_pulse_194': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_194',
            },
        },
        'gate_29_baked_pulse_195': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_195',
            },
        },
        'gate_36_baked_pulse_195': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_195',
            },
        },
        'gate_29_baked_pulse_196': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_196',
            },
        },
        'gate_36_baked_pulse_196': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_196',
            },
        },
        'gate_29_baked_pulse_197': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_197',
            },
        },
        'gate_36_baked_pulse_197': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_197',
            },
        },
        'gate_29_baked_pulse_198': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_198',
            },
        },
        'gate_36_baked_pulse_198': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_198',
            },
        },
        'gate_29_baked_pulse_199': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_199',
            },
        },
        'gate_36_baked_pulse_199': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_199',
            },
        },
        'gate_29_baked_pulse_200': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_200',
            },
        },
        'gate_36_baked_pulse_200': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_200',
            },
        },
        'gate_29_baked_pulse_201': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_201',
            },
        },
        'gate_36_baked_pulse_201': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_201',
            },
        },
        'gate_29_baked_pulse_202': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_202',
            },
        },
        'gate_36_baked_pulse_202': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_202',
            },
        },
        'gate_29_baked_pulse_203': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_203',
            },
        },
        'gate_36_baked_pulse_203': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_203',
            },
        },
        'gate_29_baked_pulse_204': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_204',
            },
        },
        'gate_36_baked_pulse_204': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_204',
            },
        },
        'gate_29_baked_pulse_205': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_205',
            },
        },
        'gate_36_baked_pulse_205': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_205',
            },
        },
        'gate_29_baked_pulse_206': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_206',
            },
        },
        'gate_36_baked_pulse_206': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_206',
            },
        },
        'gate_29_baked_pulse_207': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_207',
            },
        },
        'gate_36_baked_pulse_207': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_207',
            },
        },
        'gate_29_baked_pulse_208': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_208',
            },
        },
        'gate_36_baked_pulse_208': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_208',
            },
        },
        'gate_29_baked_pulse_209': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_209',
            },
        },
        'gate_36_baked_pulse_209': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_209',
            },
        },
        'gate_29_baked_pulse_210': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_210',
            },
        },
        'gate_36_baked_pulse_210': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_210',
            },
        },
        'gate_29_baked_pulse_211': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_211',
            },
        },
        'gate_36_baked_pulse_211': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_211',
            },
        },
        'gate_29_baked_pulse_212': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_212',
            },
        },
        'gate_36_baked_pulse_212': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_212',
            },
        },
        'gate_29_baked_pulse_213': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_213',
            },
        },
        'gate_36_baked_pulse_213': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_213',
            },
        },
        'gate_29_baked_pulse_214': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_214',
            },
        },
        'gate_36_baked_pulse_214': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_214',
            },
        },
        'gate_29_baked_pulse_215': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_215',
            },
        },
        'gate_36_baked_pulse_215': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_215',
            },
        },
        'gate_29_baked_pulse_216': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_216',
            },
        },
        'gate_36_baked_pulse_216': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_216',
            },
        },
        'gate_29_baked_pulse_217': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_217',
            },
        },
        'gate_36_baked_pulse_217': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_217',
            },
        },
        'gate_29_baked_pulse_218': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_218',
            },
        },
        'gate_36_baked_pulse_218': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_218',
            },
        },
        'gate_29_baked_pulse_219': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_219',
            },
        },
        'gate_36_baked_pulse_219': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_219',
            },
        },
        'gate_29_baked_pulse_220': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_220',
            },
        },
        'gate_36_baked_pulse_220': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_220',
            },
        },
        'gate_29_baked_pulse_221': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_221',
            },
        },
        'gate_36_baked_pulse_221': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_221',
            },
        },
        'gate_29_baked_pulse_222': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_222',
            },
        },
        'gate_36_baked_pulse_222': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_222',
            },
        },
        'gate_29_baked_pulse_223': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_223',
            },
        },
        'gate_36_baked_pulse_223': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_223',
            },
        },
        'gate_29_baked_pulse_224': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_224',
            },
        },
        'gate_36_baked_pulse_224': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_224',
            },
        },
        'gate_29_baked_pulse_225': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_225',
            },
        },
        'gate_36_baked_pulse_225': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_225',
            },
        },
        'gate_29_baked_pulse_226': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_226',
            },
        },
        'gate_36_baked_pulse_226': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_226',
            },
        },
        'gate_29_baked_pulse_227': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_227',
            },
        },
        'gate_36_baked_pulse_227': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_227',
            },
        },
        'gate_29_baked_pulse_228': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_228',
            },
        },
        'gate_36_baked_pulse_228': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_228',
            },
        },
        'gate_29_baked_pulse_229': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_229',
            },
        },
        'gate_36_baked_pulse_229': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_229',
            },
        },
        'gate_29_baked_pulse_230': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_230',
            },
        },
        'gate_36_baked_pulse_230': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_230',
            },
        },
        'gate_29_baked_pulse_231': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_231',
            },
        },
        'gate_36_baked_pulse_231': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_231',
            },
        },
        'gate_29_baked_pulse_232': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_232',
            },
        },
        'gate_36_baked_pulse_232': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_232',
            },
        },
        'gate_29_baked_pulse_233': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_233',
            },
        },
        'gate_36_baked_pulse_233': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_233',
            },
        },
        'gate_29_baked_pulse_234': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_234',
            },
        },
        'gate_36_baked_pulse_234': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_234',
            },
        },
        'gate_29_baked_pulse_235': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_235',
            },
        },
        'gate_36_baked_pulse_235': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_235',
            },
        },
        'gate_29_baked_pulse_236': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_236',
            },
        },
        'gate_36_baked_pulse_236': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_236',
            },
        },
        'gate_29_baked_pulse_237': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_237',
            },
        },
        'gate_36_baked_pulse_237': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_237',
            },
        },
        'gate_29_baked_pulse_238': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_238',
            },
        },
        'gate_36_baked_pulse_238': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_238',
            },
        },
        'gate_29_baked_pulse_239': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_239',
            },
        },
        'gate_36_baked_pulse_239': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_239',
            },
        },
        'gate_29_baked_pulse_240': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_240',
            },
        },
        'gate_36_baked_pulse_240': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_240',
            },
        },
        'gate_29_baked_pulse_241': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_241',
            },
        },
        'gate_36_baked_pulse_241': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_241',
            },
        },
        'gate_29_baked_pulse_242': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_242',
            },
        },
        'gate_36_baked_pulse_242': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_242',
            },
        },
        'gate_29_baked_pulse_243': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_243',
            },
        },
        'gate_36_baked_pulse_243': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_243',
            },
        },
        'gate_29_baked_pulse_244': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_244',
            },
        },
        'gate_36_baked_pulse_244': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_244',
            },
        },
        'gate_29_baked_pulse_245': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_245',
            },
        },
        'gate_36_baked_pulse_245': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_245',
            },
        },
        'gate_29_baked_pulse_246': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_246',
            },
        },
        'gate_36_baked_pulse_246': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_246',
            },
        },
        'gate_29_baked_pulse_247': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_247',
            },
        },
        'gate_36_baked_pulse_247': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_247',
            },
        },
        'gate_29_baked_pulse_248': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_248',
            },
        },
        'gate_36_baked_pulse_248': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_248',
            },
        },
        'gate_29_baked_pulse_249': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_249',
            },
        },
        'gate_36_baked_pulse_249': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_249',
            },
        },
        'gate_29_baked_pulse_250': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_250',
            },
        },
        'gate_36_baked_pulse_250': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_250',
            },
        },
        'gate_29_baked_pulse_251': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_251',
            },
        },
        'gate_36_baked_pulse_251': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_251',
            },
        },
        'gate_29_baked_pulse_252': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_252',
            },
        },
        'gate_36_baked_pulse_252': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_252',
            },
        },
        'gate_29_baked_pulse_253': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_253',
            },
        },
        'gate_36_baked_pulse_253': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_253',
            },
        },
        'gate_29_baked_pulse_254': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_254',
            },
        },
        'gate_36_baked_pulse_254': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_254',
            },
        },
        'gate_29_baked_pulse_255': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_255',
            },
        },
        'gate_36_baked_pulse_255': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_255',
            },
        },
        'gate_29_baked_pulse_256': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_256',
            },
        },
        'gate_36_baked_pulse_256': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_256',
            },
        },
        'gate_29_baked_pulse_257': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_257',
            },
        },
        'gate_36_baked_pulse_257': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_257',
            },
        },
        'gate_29_baked_pulse_258': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_258',
            },
        },
        'gate_36_baked_pulse_258': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_258',
            },
        },
        'gate_29_baked_pulse_259': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_259',
            },
        },
        'gate_36_baked_pulse_259': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_259',
            },
        },
        'gate_29_baked_pulse_260': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_260',
            },
        },
        'gate_36_baked_pulse_260': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_260',
            },
        },
        'gate_29_baked_pulse_261': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_261',
            },
        },
        'gate_36_baked_pulse_261': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_261',
            },
        },
        'gate_29_baked_pulse_262': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_262',
            },
        },
        'gate_36_baked_pulse_262': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_262',
            },
        },
        'gate_29_baked_pulse_263': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_263',
            },
        },
        'gate_36_baked_pulse_263': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_263',
            },
        },
        'gate_29_baked_pulse_264': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_264',
            },
        },
        'gate_36_baked_pulse_264': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_264',
            },
        },
        'gate_29_baked_pulse_265': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_265',
            },
        },
        'gate_36_baked_pulse_265': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_265',
            },
        },
        'gate_29_baked_pulse_266': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_266',
            },
        },
        'gate_36_baked_pulse_266': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_266',
            },
        },
        'gate_29_baked_pulse_267': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_267',
            },
        },
        'gate_36_baked_pulse_267': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_267',
            },
        },
        'gate_29_baked_pulse_268': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_268',
            },
        },
        'gate_36_baked_pulse_268': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_268',
            },
        },
        'gate_29_baked_pulse_269': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_269',
            },
        },
        'gate_36_baked_pulse_269': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_269',
            },
        },
        'gate_29_baked_pulse_270': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_270',
            },
        },
        'gate_36_baked_pulse_270': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_270',
            },
        },
        'gate_29_baked_pulse_271': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_271',
            },
        },
        'gate_36_baked_pulse_271': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_271',
            },
        },
        'gate_29_baked_pulse_272': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_272',
            },
        },
        'gate_36_baked_pulse_272': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_272',
            },
        },
        'gate_29_baked_pulse_273': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_273',
            },
        },
        'gate_36_baked_pulse_273': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_273',
            },
        },
        'gate_29_baked_pulse_274': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_274',
            },
        },
        'gate_36_baked_pulse_274': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_274',
            },
        },
        'gate_29_baked_pulse_275': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_275',
            },
        },
        'gate_36_baked_pulse_275': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_275',
            },
        },
        'gate_29_baked_pulse_276': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_276',
            },
        },
        'gate_36_baked_pulse_276': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_276',
            },
        },
        'gate_29_baked_pulse_277': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_277',
            },
        },
        'gate_36_baked_pulse_277': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_277',
            },
        },
        'gate_29_baked_pulse_278': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_278',
            },
        },
        'gate_36_baked_pulse_278': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_278',
            },
        },
        'gate_29_baked_pulse_279': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_279',
            },
        },
        'gate_36_baked_pulse_279': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_279',
            },
        },
        'gate_29_baked_pulse_280': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_280',
            },
        },
        'gate_36_baked_pulse_280': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_280',
            },
        },
        'gate_29_baked_pulse_281': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_281',
            },
        },
        'gate_36_baked_pulse_281': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_281',
            },
        },
        'gate_29_baked_pulse_282': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_282',
            },
        },
        'gate_36_baked_pulse_282': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_282',
            },
        },
        'gate_29_baked_pulse_283': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_283',
            },
        },
        'gate_36_baked_pulse_283': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_283',
            },
        },
        'gate_29_baked_pulse_284': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_284',
            },
        },
        'gate_36_baked_pulse_284': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_284',
            },
        },
        'gate_29_baked_pulse_285': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_285',
            },
        },
        'gate_36_baked_pulse_285': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_285',
            },
        },
        'gate_29_baked_pulse_286': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_286',
            },
        },
        'gate_36_baked_pulse_286': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_286',
            },
        },
        'gate_29_baked_pulse_287': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_287',
            },
        },
        'gate_36_baked_pulse_287': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_287',
            },
        },
        'gate_29_baked_pulse_288': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_288',
            },
        },
        'gate_36_baked_pulse_288': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_288',
            },
        },
        'gate_29_baked_pulse_289': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_289',
            },
        },
        'gate_36_baked_pulse_289': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_289',
            },
        },
        'gate_29_baked_pulse_290': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_290',
            },
        },
        'gate_36_baked_pulse_290': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_290',
            },
        },
        'gate_29_baked_pulse_291': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_291',
            },
        },
        'gate_36_baked_pulse_291': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_291',
            },
        },
        'gate_29_baked_pulse_292': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_292',
            },
        },
        'gate_36_baked_pulse_292': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_292',
            },
        },
        'gate_29_baked_pulse_293': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_293',
            },
        },
        'gate_36_baked_pulse_293': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_293',
            },
        },
        'gate_29_baked_pulse_294': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_294',
            },
        },
        'gate_36_baked_pulse_294': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_294',
            },
        },
        'gate_29_baked_pulse_295': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_295',
            },
        },
        'gate_36_baked_pulse_295': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_295',
            },
        },
        'gate_29_baked_pulse_296': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_296',
            },
        },
        'gate_36_baked_pulse_296': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_296',
            },
        },
        'gate_29_baked_pulse_297': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_297',
            },
        },
        'gate_36_baked_pulse_297': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_297',
            },
        },
        'gate_29_baked_pulse_298': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_298',
            },
        },
        'gate_36_baked_pulse_298': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_298',
            },
        },
        'gate_29_baked_pulse_299': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_299',
            },
        },
        'gate_36_baked_pulse_299': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_299',
            },
        },
        'gate_29_baked_pulse_300': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_300',
            },
        },
        'gate_36_baked_pulse_300': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_300',
            },
        },
        'gate_29_baked_pulse_301': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_301',
            },
        },
        'gate_36_baked_pulse_301': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_301',
            },
        },
        'gate_29_baked_pulse_302': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_302',
            },
        },
        'gate_36_baked_pulse_302': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_302',
            },
        },
        'gate_29_baked_pulse_303': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_303',
            },
        },
        'gate_36_baked_pulse_303': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_303',
            },
        },
        'gate_29_baked_pulse_304': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_304',
            },
        },
        'gate_36_baked_pulse_304': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_304',
            },
        },
        'gate_29_baked_pulse_305': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_305',
            },
        },
        'gate_36_baked_pulse_305': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_305',
            },
        },
        'gate_29_baked_pulse_306': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_306',
            },
        },
        'gate_36_baked_pulse_306': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_306',
            },
        },
        'gate_29_baked_pulse_307': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_307',
            },
        },
        'gate_36_baked_pulse_307': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_307',
            },
        },
        'gate_29_baked_pulse_308': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_308',
            },
        },
        'gate_36_baked_pulse_308': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_308',
            },
        },
        'gate_29_baked_pulse_309': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_309',
            },
        },
        'gate_36_baked_pulse_309': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_309',
            },
        },
        'gate_29_baked_pulse_310': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_310',
            },
        },
        'gate_36_baked_pulse_310': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_310',
            },
        },
        'gate_29_baked_pulse_311': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_311',
            },
        },
        'gate_36_baked_pulse_311': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_311',
            },
        },
        'gate_29_baked_pulse_312': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_312',
            },
        },
        'gate_36_baked_pulse_312': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_312',
            },
        },
        'gate_29_baked_pulse_313': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_313',
            },
        },
        'gate_36_baked_pulse_313': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_313',
            },
        },
        'gate_29_baked_pulse_314': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_314',
            },
        },
        'gate_36_baked_pulse_314': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_314',
            },
        },
        'gate_29_baked_pulse_315': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_315',
            },
        },
        'gate_36_baked_pulse_315': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_315',
            },
        },
        'gate_29_baked_pulse_316': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_316',
            },
        },
        'gate_36_baked_pulse_316': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_316',
            },
        },
        'gate_29_baked_pulse_317': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_317',
            },
        },
        'gate_36_baked_pulse_317': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_317',
            },
        },
        'gate_29_baked_pulse_318': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_318',
            },
        },
        'gate_36_baked_pulse_318': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_318',
            },
        },
        'gate_29_baked_pulse_319': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_319',
            },
        },
        'gate_36_baked_pulse_319': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_319',
            },
        },
        'gate_29_baked_pulse_320': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_320',
            },
        },
        'gate_36_baked_pulse_320': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_320',
            },
        },
        'gate_29_baked_pulse_321': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_321',
            },
        },
        'gate_36_baked_pulse_321': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_321',
            },
        },
        'gate_29_baked_pulse_322': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_322',
            },
        },
        'gate_36_baked_pulse_322': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_322',
            },
        },
        'gate_29_baked_pulse_323': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_323',
            },
        },
        'gate_36_baked_pulse_323': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_323',
            },
        },
        'gate_29_baked_pulse_324': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_324',
            },
        },
        'gate_36_baked_pulse_324': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_324',
            },
        },
        'gate_29_baked_pulse_325': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_325',
            },
        },
        'gate_36_baked_pulse_325': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_325',
            },
        },
        'gate_29_baked_pulse_326': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_326',
            },
        },
        'gate_36_baked_pulse_326': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_326',
            },
        },
        'gate_29_baked_pulse_327': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_327',
            },
        },
        'gate_36_baked_pulse_327': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_327',
            },
        },
        'gate_29_baked_pulse_328': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_328',
            },
        },
        'gate_36_baked_pulse_328': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_328',
            },
        },
        'gate_29_baked_pulse_329': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_329',
            },
        },
        'gate_36_baked_pulse_329': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_329',
            },
        },
        'gate_29_baked_pulse_330': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_330',
            },
        },
        'gate_36_baked_pulse_330': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_330',
            },
        },
        'gate_29_baked_pulse_331': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_331',
            },
        },
        'gate_36_baked_pulse_331': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_331',
            },
        },
        'gate_29_baked_pulse_332': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_332',
            },
        },
        'gate_36_baked_pulse_332': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_332',
            },
        },
        'gate_29_baked_pulse_333': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_333',
            },
        },
        'gate_36_baked_pulse_333': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_333',
            },
        },
        'gate_29_baked_pulse_334': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_334',
            },
        },
        'gate_36_baked_pulse_334': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_334',
            },
        },
        'gate_29_baked_pulse_335': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_335',
            },
        },
        'gate_36_baked_pulse_335': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_335',
            },
        },
        'gate_29_baked_pulse_336': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_336',
            },
        },
        'gate_36_baked_pulse_336': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_336',
            },
        },
        'gate_29_baked_pulse_337': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_337',
            },
        },
        'gate_36_baked_pulse_337': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_337',
            },
        },
        'gate_29_baked_pulse_338': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_338',
            },
        },
        'gate_36_baked_pulse_338': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_338',
            },
        },
        'gate_29_baked_pulse_339': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_339',
            },
        },
        'gate_36_baked_pulse_339': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_339',
            },
        },
        'gate_29_baked_pulse_340': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_340',
            },
        },
        'gate_36_baked_pulse_340': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_340',
            },
        },
        'gate_29_baked_pulse_341': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_341',
            },
        },
        'gate_36_baked_pulse_341': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_341',
            },
        },
        'gate_29_baked_pulse_342': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_342',
            },
        },
        'gate_36_baked_pulse_342': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_342',
            },
        },
        'gate_29_baked_pulse_343': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_343',
            },
        },
        'gate_36_baked_pulse_343': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_343',
            },
        },
        'gate_29_baked_pulse_344': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_344',
            },
        },
        'gate_36_baked_pulse_344': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_344',
            },
        },
        'gate_29_baked_pulse_345': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_345',
            },
        },
        'gate_36_baked_pulse_345': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_345',
            },
        },
        'gate_29_baked_pulse_346': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_346',
            },
        },
        'gate_36_baked_pulse_346': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_346',
            },
        },
        'gate_29_baked_pulse_347': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_347',
            },
        },
        'gate_36_baked_pulse_347': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_347',
            },
        },
        'gate_29_baked_pulse_348': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_348',
            },
        },
        'gate_36_baked_pulse_348': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_348',
            },
        },
        'gate_29_baked_pulse_349': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_349',
            },
        },
        'gate_36_baked_pulse_349': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_349',
            },
        },
        'gate_29_baked_pulse_350': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_350',
            },
        },
        'gate_36_baked_pulse_350': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_350',
            },
        },
        'gate_29_baked_pulse_351': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_351',
            },
        },
        'gate_36_baked_pulse_351': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_351',
            },
        },
        'gate_29_baked_pulse_352': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_352',
            },
        },
        'gate_36_baked_pulse_352': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_352',
            },
        },
        'gate_29_baked_pulse_353': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_353',
            },
        },
        'gate_36_baked_pulse_353': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_353',
            },
        },
        'gate_29_baked_pulse_354': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_354',
            },
        },
        'gate_36_baked_pulse_354': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_354',
            },
        },
        'gate_29_baked_pulse_355': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_355',
            },
        },
        'gate_36_baked_pulse_355': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_355',
            },
        },
        'gate_29_baked_pulse_356': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_356',
            },
        },
        'gate_36_baked_pulse_356': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_356',
            },
        },
        'gate_29_baked_pulse_357': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_357',
            },
        },
        'gate_36_baked_pulse_357': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_357',
            },
        },
        'gate_29_baked_pulse_358': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_358',
            },
        },
        'gate_36_baked_pulse_358': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_358',
            },
        },
        'gate_29_baked_pulse_359': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_359',
            },
        },
        'gate_36_baked_pulse_359': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_359',
            },
        },
        'gate_29_baked_pulse_360': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_360',
            },
        },
        'gate_36_baked_pulse_360': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_360',
            },
        },
        'gate_29_baked_pulse_361': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_361',
            },
        },
        'gate_36_baked_pulse_361': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_361',
            },
        },
        'gate_29_baked_pulse_362': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_362',
            },
        },
        'gate_36_baked_pulse_362': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_362',
            },
        },
        'gate_29_baked_pulse_363': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_363',
            },
        },
        'gate_36_baked_pulse_363': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_363',
            },
        },
        'gate_29_baked_pulse_364': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_364',
            },
        },
        'gate_36_baked_pulse_364': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_364',
            },
        },
        'gate_29_baked_pulse_365': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_365',
            },
        },
        'gate_36_baked_pulse_365': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_365',
            },
        },
        'gate_29_baked_pulse_366': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_366',
            },
        },
        'gate_36_baked_pulse_366': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_366',
            },
        },
        'gate_29_baked_pulse_367': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_367',
            },
        },
        'gate_36_baked_pulse_367': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_367',
            },
        },
        'gate_29_baked_pulse_368': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_368',
            },
        },
        'gate_36_baked_pulse_368': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_368',
            },
        },
        'gate_29_baked_pulse_369': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_369',
            },
        },
        'gate_36_baked_pulse_369': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_369',
            },
        },
        'gate_29_baked_pulse_370': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_370',
            },
        },
        'gate_36_baked_pulse_370': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_370',
            },
        },
        'gate_29_baked_pulse_371': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_371',
            },
        },
        'gate_36_baked_pulse_371': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_371',
            },
        },
        'gate_29_baked_pulse_372': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_372',
            },
        },
        'gate_36_baked_pulse_372': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_372',
            },
        },
        'gate_29_baked_pulse_373': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_373',
            },
        },
        'gate_36_baked_pulse_373': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_373',
            },
        },
        'gate_29_baked_pulse_374': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_374',
            },
        },
        'gate_36_baked_pulse_374': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_374',
            },
        },
        'gate_29_baked_pulse_375': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_375',
            },
        },
        'gate_36_baked_pulse_375': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_375',
            },
        },
        'gate_29_baked_pulse_376': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_376',
            },
        },
        'gate_36_baked_pulse_376': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_376',
            },
        },
        'gate_29_baked_pulse_377': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_377',
            },
        },
        'gate_36_baked_pulse_377': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_377',
            },
        },
        'gate_29_baked_pulse_378': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_378',
            },
        },
        'gate_36_baked_pulse_378': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_378',
            },
        },
        'gate_29_baked_pulse_379': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_379',
            },
        },
        'gate_36_baked_pulse_379': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_379',
            },
        },
        'gate_29_baked_pulse_380': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_380',
            },
        },
        'gate_36_baked_pulse_380': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_380',
            },
        },
        'gate_29_baked_pulse_381': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_381',
            },
        },
        'gate_36_baked_pulse_381': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_381',
            },
        },
        'gate_29_baked_pulse_382': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_382',
            },
        },
        'gate_36_baked_pulse_382': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_382',
            },
        },
        'gate_29_baked_pulse_383': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_383',
            },
        },
        'gate_36_baked_pulse_383': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_383',
            },
        },
        'gate_29_baked_pulse_384': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_384',
            },
        },
        'gate_36_baked_pulse_384': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_384',
            },
        },
        'gate_29_baked_pulse_385': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_385',
            },
        },
        'gate_36_baked_pulse_385': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_385',
            },
        },
        'gate_29_baked_pulse_386': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_386',
            },
        },
        'gate_36_baked_pulse_386': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_386',
            },
        },
        'gate_29_baked_pulse_387': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_387',
            },
        },
        'gate_36_baked_pulse_387': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_387',
            },
        },
        'gate_29_baked_pulse_388': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_388',
            },
        },
        'gate_36_baked_pulse_388': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_388',
            },
        },
        'gate_29_baked_pulse_389': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_389',
            },
        },
        'gate_36_baked_pulse_389': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_389',
            },
        },
        'gate_29_baked_pulse_390': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_390',
            },
        },
        'gate_36_baked_pulse_390': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_390',
            },
        },
        'gate_29_baked_pulse_391': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_391',
            },
        },
        'gate_36_baked_pulse_391': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_391',
            },
        },
        'gate_29_baked_pulse_392': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_392',
            },
        },
        'gate_36_baked_pulse_392': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_392',
            },
        },
        'gate_29_baked_pulse_393': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_393',
            },
        },
        'gate_36_baked_pulse_393': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_393',
            },
        },
        'gate_29_baked_pulse_394': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_394',
            },
        },
        'gate_36_baked_pulse_394': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_394',
            },
        },
        'gate_29_baked_pulse_395': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_395',
            },
        },
        'gate_36_baked_pulse_395': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_395',
            },
        },
        'gate_29_baked_pulse_396': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_396',
            },
        },
        'gate_36_baked_pulse_396': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_396',
            },
        },
        'gate_29_baked_pulse_397': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_397',
            },
        },
        'gate_36_baked_pulse_397': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_397',
            },
        },
        'gate_29_baked_pulse_398': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_398',
            },
        },
        'gate_36_baked_pulse_398': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_398',
            },
        },
        'gate_29_baked_pulse_399': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_399',
            },
        },
        'gate_36_baked_pulse_399': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_399',
            },
        },
        'gate_29_baked_pulse_400': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_400',
            },
        },
        'gate_36_baked_pulse_400': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_400',
            },
        },
        'gate_29_baked_pulse_401': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_401',
            },
        },
        'gate_36_baked_pulse_401': {
            'operation': 'control',
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_401',
            },
        },
    },
    'waveforms': {
        'const_wf': {
            'type': 'constant',
            'sample': 0.25,
        },
        'zero_wf': {
            'type': 'constant',
            'sample': 0.0,
        },
        'readout_wf_0_2': {
            'type': 'constant',
            'sample': 0.2,
        },
        'gate_29_baked_wf_0': {
            'type': 'arbitrary',
            'samples': [0.0] * 204,
            'is_overridable': False,
        },
        'gate_36_baked_wf_0': {
            'type': 'arbitrary',
            'samples': [0.0] * 204,
            'is_overridable': False,
        },
        'gate_29_baked_wf_1': {
            'type': 'arbitrary',
            'samples': [0.0] * 203 + [-0.2081559],
            'is_overridable': False,
        },
        'gate_36_baked_wf_1': {
            'type': 'arbitrary',
            'samples': [0.0] * 203 + [0.254468348],
            'is_overridable': False,
        },
        'gate_29_baked_wf_2': {
            'type': 'arbitrary',
            'samples': [0.0] * 202 + [-0.2081559] * 2,
            'is_overridable': False,
        },
        'gate_36_baked_wf_2': {
            'type': 'arbitrary',
            'samples': [0.0] * 202 + [0.254468348] * 2,
            'is_overridable': False,
        },
        'gate_29_baked_wf_3': {
            'type': 'arbitrary',
            'samples': [0.0] * 201 + [-0.2081559] * 3,
            'is_overridable': False,
        },
        'gate_36_baked_wf_3': {
            'type': 'arbitrary',
            'samples': [0.0] * 201 + [0.254468348] * 3,
            'is_overridable': False,
        },
        'gate_29_baked_wf_4': {
            'type': 'arbitrary',
            'samples': [0.0] * 200 + [-0.2081559] * 4,
            'is_overridable': False,
        },
        'gate_36_baked_wf_4': {
            'type': 'arbitrary',
            'samples': [0.0] * 200 + [0.254468348] * 4,
            'is_overridable': False,
        },
        'gate_29_baked_wf_5': {
            'type': 'arbitrary',
            'samples': [0.0] * 199 + [-0.2081559] * 5,
            'is_overridable': False,
        },
        'gate_36_baked_wf_5': {
            'type': 'arbitrary',
            'samples': [0.0] * 199 + [0.254468348] * 5,
            'is_overridable': False,
        },
        'gate_29_baked_wf_6': {
            'type': 'arbitrary',
            'samples': [0.0] * 198 + [-0.2081559] * 6,
            'is_overridable': False,
        },
        'gate_36_baked_wf_6': {
            'type': 'arbitrary',
            'samples': [0.0] * 198 + [0.254468348] * 6,
            'is_overridable': False,
        },
        'gate_29_baked_wf_7': {
            'type': 'arbitrary',
            'samples': [0.0] * 197 + [-0.2081559] * 7,
            'is_overridable': False,
        },
        'gate_36_baked_wf_7': {
            'type': 'arbitrary',
            'samples': [0.0] * 197 + [0.254468348] * 7,
            'is_overridable': False,
        },
        'gate_29_baked_wf_8': {
            'type': 'arbitrary',
            'samples': [0.0] * 196 + [-0.2081559] * 8,
            'is_overridable': False,
        },
        'gate_36_baked_wf_8': {
            'type': 'arbitrary',
            'samples': [0.0] * 196 + [0.254468348] * 8,
            'is_overridable': False,
        },
        'gate_29_baked_wf_9': {
            'type': 'arbitrary',
            'samples': [0.0] * 195 + [-0.2081559] * 9,
            'is_overridable': False,
        },
        'gate_36_baked_wf_9': {
            'type': 'arbitrary',
            'samples': [0.0] * 195 + [0.254468348] * 9,
            'is_overridable': False,
        },
        'gate_29_baked_wf_10': {
            'type': 'arbitrary',
            'samples': [0.0] * 194 + [-0.2081559] * 10,
            'is_overridable': False,
        },
        'gate_36_baked_wf_10': {
            'type': 'arbitrary',
            'samples': [0.0] * 194 + [0.254468348] * 10,
            'is_overridable': False,
        },
        'gate_29_baked_wf_11': {
            'type': 'arbitrary',
            'samples': [0.0] * 193 + [-0.2081559] * 11,
            'is_overridable': False,
        },
        'gate_36_baked_wf_11': {
            'type': 'arbitrary',
            'samples': [0.0] * 193 + [0.254468348] * 11,
            'is_overridable': False,
        },
        'gate_29_baked_wf_12': {
            'type': 'arbitrary',
            'samples': [0.0] * 192 + [-0.2081559] * 12,
            'is_overridable': False,
        },
        'gate_36_baked_wf_12': {
            'type': 'arbitrary',
            'samples': [0.0] * 192 + [0.254468348] * 12,
            'is_overridable': False,
        },
        'gate_29_baked_wf_13': {
            'type': 'arbitrary',
            'samples': [0.0] * 191 + [-0.2081559] * 13,
            'is_overridable': False,
        },
        'gate_36_baked_wf_13': {
            'type': 'arbitrary',
            'samples': [0.0] * 191 + [0.254468348] * 13,
            'is_overridable': False,
        },
        'gate_29_baked_wf_14': {
            'type': 'arbitrary',
            'samples': [0.0] * 190 + [-0.2081559] * 14,
            'is_overridable': False,
        },
        'gate_36_baked_wf_14': {
            'type': 'arbitrary',
            'samples': [0.0] * 190 + [0.254468348] * 14,
            'is_overridable': False,
        },
        'gate_29_baked_wf_15': {
            'type': 'arbitrary',
            'samples': [0.0] * 189 + [-0.2081559] * 15,
            'is_overridable': False,
        },
        'gate_36_baked_wf_15': {
            'type': 'arbitrary',
            'samples': [0.0] * 189 + [0.254468348] * 15,
            'is_overridable': False,
        },
        'gate_29_baked_wf_16': {
            'type': 'arbitrary',
            'samples': [0.0] * 188 + [-0.2081559] * 16,
            'is_overridable': False,
        },
        'gate_36_baked_wf_16': {
            'type': 'arbitrary',
            'samples': [0.0] * 188 + [0.254468348] * 16,
            'is_overridable': False,
        },
        'gate_29_baked_wf_17': {
            'type': 'arbitrary',
            'samples': [0.0] * 187 + [-0.2081559] * 17,
            'is_overridable': False,
        },
        'gate_36_baked_wf_17': {
            'type': 'arbitrary',
            'samples': [0.0] * 187 + [0.254468348] * 17,
            'is_overridable': False,
        },
        'gate_29_baked_wf_18': {
            'type': 'arbitrary',
            'samples': [0.0] * 186 + [-0.2081559] * 18,
            'is_overridable': False,
        },
        'gate_36_baked_wf_18': {
            'type': 'arbitrary',
            'samples': [0.0] * 186 + [0.254468348] * 18,
            'is_overridable': False,
        },
        'gate_29_baked_wf_19': {
            'type': 'arbitrary',
            'samples': [0.0] * 185 + [-0.2081559] * 19,
            'is_overridable': False,
        },
        'gate_36_baked_wf_19': {
            'type': 'arbitrary',
            'samples': [0.0] * 185 + [0.254468348] * 19,
            'is_overridable': False,
        },
        'gate_29_baked_wf_20': {
            'type': 'arbitrary',
            'samples': [0.0] * 184 + [-0.2081559] * 20,
            'is_overridable': False,
        },
        'gate_36_baked_wf_20': {
            'type': 'arbitrary',
            'samples': [0.0] * 184 + [0.254468348] * 20,
            'is_overridable': False,
        },
        'gate_29_baked_wf_21': {
            'type': 'arbitrary',
            'samples': [0.0] * 183 + [-0.2081559] * 21,
            'is_overridable': False,
        },
        'gate_36_baked_wf_21': {
            'type': 'arbitrary',
            'samples': [0.0] * 183 + [0.254468348] * 21,
            'is_overridable': False,
        },
        'gate_29_baked_wf_22': {
            'type': 'arbitrary',
            'samples': [0.0] * 182 + [-0.2081559] * 22,
            'is_overridable': False,
        },
        'gate_36_baked_wf_22': {
            'type': 'arbitrary',
            'samples': [0.0] * 182 + [0.254468348] * 22,
            'is_overridable': False,
        },
        'gate_29_baked_wf_23': {
            'type': 'arbitrary',
            'samples': [0.0] * 181 + [-0.2081559] * 23,
            'is_overridable': False,
        },
        'gate_36_baked_wf_23': {
            'type': 'arbitrary',
            'samples': [0.0] * 181 + [0.254468348] * 23,
            'is_overridable': False,
        },
        'gate_29_baked_wf_24': {
            'type': 'arbitrary',
            'samples': [0.0] * 180 + [-0.2081559] * 24,
            'is_overridable': False,
        },
        'gate_36_baked_wf_24': {
            'type': 'arbitrary',
            'samples': [0.0] * 180 + [0.254468348] * 24,
            'is_overridable': False,
        },
        'gate_29_baked_wf_25': {
            'type': 'arbitrary',
            'samples': [0.0] * 179 + [-0.2081559] * 25,
            'is_overridable': False,
        },
        'gate_36_baked_wf_25': {
            'type': 'arbitrary',
            'samples': [0.0] * 179 + [0.254468348] * 25,
            'is_overridable': False,
        },
        'gate_29_baked_wf_26': {
            'type': 'arbitrary',
            'samples': [0.0] * 178 + [-0.2081559] * 26,
            'is_overridable': False,
        },
        'gate_36_baked_wf_26': {
            'type': 'arbitrary',
            'samples': [0.0] * 178 + [0.254468348] * 26,
            'is_overridable': False,
        },
        'gate_29_baked_wf_27': {
            'type': 'arbitrary',
            'samples': [0.0] * 177 + [-0.2081559] * 27,
            'is_overridable': False,
        },
        'gate_36_baked_wf_27': {
            'type': 'arbitrary',
            'samples': [0.0] * 177 + [0.254468348] * 27,
            'is_overridable': False,
        },
        'gate_29_baked_wf_28': {
            'type': 'arbitrary',
            'samples': [0.0] * 176 + [-0.2081559] * 28,
            'is_overridable': False,
        },
        'gate_36_baked_wf_28': {
            'type': 'arbitrary',
            'samples': [0.0] * 176 + [0.254468348] * 28,
            'is_overridable': False,
        },
        'gate_29_baked_wf_29': {
            'type': 'arbitrary',
            'samples': [0.0] * 175 + [-0.2081559] * 29,
            'is_overridable': False,
        },
        'gate_36_baked_wf_29': {
            'type': 'arbitrary',
            'samples': [0.0] * 175 + [0.254468348] * 29,
            'is_overridable': False,
        },
        'gate_29_baked_wf_30': {
            'type': 'arbitrary',
            'samples': [0.0] * 174 + [-0.2081559] * 30,
            'is_overridable': False,
        },
        'gate_36_baked_wf_30': {
            'type': 'arbitrary',
            'samples': [0.0] * 174 + [0.254468348] * 30,
            'is_overridable': False,
        },
        'gate_29_baked_wf_31': {
            'type': 'arbitrary',
            'samples': [0.0] * 173 + [-0.2081559] * 31,
            'is_overridable': False,
        },
        'gate_36_baked_wf_31': {
            'type': 'arbitrary',
            'samples': [0.0] * 173 + [0.254468348] * 31,
            'is_overridable': False,
        },
        'gate_29_baked_wf_32': {
            'type': 'arbitrary',
            'samples': [0.0] * 172 + [-0.2081559] * 32,
            'is_overridable': False,
        },
        'gate_36_baked_wf_32': {
            'type': 'arbitrary',
            'samples': [0.0] * 172 + [0.254468348] * 32,
            'is_overridable': False,
        },
        'gate_29_baked_wf_33': {
            'type': 'arbitrary',
            'samples': [0.0] * 171 + [-0.2081559] * 33,
            'is_overridable': False,
        },
        'gate_36_baked_wf_33': {
            'type': 'arbitrary',
            'samples': [0.0] * 171 + [0.254468348] * 33,
            'is_overridable': False,
        },
        'gate_29_baked_wf_34': {
            'type': 'arbitrary',
            'samples': [0.0] * 170 + [-0.2081559] * 34,
            'is_overridable': False,
        },
        'gate_36_baked_wf_34': {
            'type': 'arbitrary',
            'samples': [0.0] * 170 + [0.254468348] * 34,
            'is_overridable': False,
        },
        'gate_29_baked_wf_35': {
            'type': 'arbitrary',
            'samples': [0.0] * 169 + [-0.2081559] * 35,
            'is_overridable': False,
        },
        'gate_36_baked_wf_35': {
            'type': 'arbitrary',
            'samples': [0.0] * 169 + [0.254468348] * 35,
            'is_overridable': False,
        },
        'gate_29_baked_wf_36': {
            'type': 'arbitrary',
            'samples': [0.0] * 168 + [-0.2081559] * 36,
            'is_overridable': False,
        },
        'gate_36_baked_wf_36': {
            'type': 'arbitrary',
            'samples': [0.0] * 168 + [0.254468348] * 36,
            'is_overridable': False,
        },
        'gate_29_baked_wf_37': {
            'type': 'arbitrary',
            'samples': [0.0] * 167 + [-0.2081559] * 37,
            'is_overridable': False,
        },
        'gate_36_baked_wf_37': {
            'type': 'arbitrary',
            'samples': [0.0] * 167 + [0.254468348] * 37,
            'is_overridable': False,
        },
        'gate_29_baked_wf_38': {
            'type': 'arbitrary',
            'samples': [0.0] * 166 + [-0.2081559] * 38,
            'is_overridable': False,
        },
        'gate_36_baked_wf_38': {
            'type': 'arbitrary',
            'samples': [0.0] * 166 + [0.254468348] * 38,
            'is_overridable': False,
        },
        'gate_29_baked_wf_39': {
            'type': 'arbitrary',
            'samples': [0.0] * 165 + [-0.2081559] * 39,
            'is_overridable': False,
        },
        'gate_36_baked_wf_39': {
            'type': 'arbitrary',
            'samples': [0.0] * 165 + [0.254468348] * 39,
            'is_overridable': False,
        },
        'gate_29_baked_wf_40': {
            'type': 'arbitrary',
            'samples': [0.0] * 164 + [-0.2081559] * 40,
            'is_overridable': False,
        },
        'gate_36_baked_wf_40': {
            'type': 'arbitrary',
            'samples': [0.0] * 164 + [0.254468348] * 40,
            'is_overridable': False,
        },
        'gate_29_baked_wf_41': {
            'type': 'arbitrary',
            'samples': [0.0] * 163 + [-0.2081559] * 41,
            'is_overridable': False,
        },
        'gate_36_baked_wf_41': {
            'type': 'arbitrary',
            'samples': [0.0] * 163 + [0.254468348] * 41,
            'is_overridable': False,
        },
        'gate_29_baked_wf_42': {
            'type': 'arbitrary',
            'samples': [0.0] * 162 + [-0.2081559] * 42,
            'is_overridable': False,
        },
        'gate_36_baked_wf_42': {
            'type': 'arbitrary',
            'samples': [0.0] * 162 + [0.254468348] * 42,
            'is_overridable': False,
        },
        'gate_29_baked_wf_43': {
            'type': 'arbitrary',
            'samples': [0.0] * 161 + [-0.2081559] * 43,
            'is_overridable': False,
        },
        'gate_36_baked_wf_43': {
            'type': 'arbitrary',
            'samples': [0.0] * 161 + [0.254468348] * 43,
            'is_overridable': False,
        },
        'gate_29_baked_wf_44': {
            'type': 'arbitrary',
            'samples': [0.0] * 160 + [-0.2081559] * 44,
            'is_overridable': False,
        },
        'gate_36_baked_wf_44': {
            'type': 'arbitrary',
            'samples': [0.0] * 160 + [0.254468348] * 44,
            'is_overridable': False,
        },
        'gate_29_baked_wf_45': {
            'type': 'arbitrary',
            'samples': [0.0] * 159 + [-0.2081559] * 45,
            'is_overridable': False,
        },
        'gate_36_baked_wf_45': {
            'type': 'arbitrary',
            'samples': [0.0] * 159 + [0.254468348] * 45,
            'is_overridable': False,
        },
        'gate_29_baked_wf_46': {
            'type': 'arbitrary',
            'samples': [0.0] * 158 + [-0.2081559] * 46,
            'is_overridable': False,
        },
        'gate_36_baked_wf_46': {
            'type': 'arbitrary',
            'samples': [0.0] * 158 + [0.254468348] * 46,
            'is_overridable': False,
        },
        'gate_29_baked_wf_47': {
            'type': 'arbitrary',
            'samples': [0.0] * 157 + [-0.2081559] * 47,
            'is_overridable': False,
        },
        'gate_36_baked_wf_47': {
            'type': 'arbitrary',
            'samples': [0.0] * 157 + [0.254468348] * 47,
            'is_overridable': False,
        },
        'gate_29_baked_wf_48': {
            'type': 'arbitrary',
            'samples': [0.0] * 156 + [-0.2081559] * 48,
            'is_overridable': False,
        },
        'gate_36_baked_wf_48': {
            'type': 'arbitrary',
            'samples': [0.0] * 156 + [0.254468348] * 48,
            'is_overridable': False,
        },
        'gate_29_baked_wf_49': {
            'type': 'arbitrary',
            'samples': [0.0] * 155 + [-0.2081559] * 49,
            'is_overridable': False,
        },
        'gate_36_baked_wf_49': {
            'type': 'arbitrary',
            'samples': [0.0] * 155 + [0.254468348] * 49,
            'is_overridable': False,
        },
        'gate_29_baked_wf_50': {
            'type': 'arbitrary',
            'samples': [0.0] * 154 + [-0.2081559] * 50,
            'is_overridable': False,
        },
        'gate_36_baked_wf_50': {
            'type': 'arbitrary',
            'samples': [0.0] * 154 + [0.254468348] * 50,
            'is_overridable': False,
        },
        'gate_29_baked_wf_51': {
            'type': 'arbitrary',
            'samples': [0.0] * 153 + [-0.2081559] * 51,
            'is_overridable': False,
        },
        'gate_36_baked_wf_51': {
            'type': 'arbitrary',
            'samples': [0.0] * 153 + [0.254468348] * 51,
            'is_overridable': False,
        },
        'gate_29_baked_wf_52': {
            'type': 'arbitrary',
            'samples': [0.0] * 152 + [-0.2081559] * 52,
            'is_overridable': False,
        },
        'gate_36_baked_wf_52': {
            'type': 'arbitrary',
            'samples': [0.0] * 152 + [0.254468348] * 52,
            'is_overridable': False,
        },
        'gate_29_baked_wf_53': {
            'type': 'arbitrary',
            'samples': [0.0] * 151 + [-0.2081559] * 53,
            'is_overridable': False,
        },
        'gate_36_baked_wf_53': {
            'type': 'arbitrary',
            'samples': [0.0] * 151 + [0.254468348] * 53,
            'is_overridable': False,
        },
        'gate_29_baked_wf_54': {
            'type': 'arbitrary',
            'samples': [0.0] * 150 + [-0.2081559] * 54,
            'is_overridable': False,
        },
        'gate_36_baked_wf_54': {
            'type': 'arbitrary',
            'samples': [0.0] * 150 + [0.254468348] * 54,
            'is_overridable': False,
        },
        'gate_29_baked_wf_55': {
            'type': 'arbitrary',
            'samples': [0.0] * 149 + [-0.2081559] * 55,
            'is_overridable': False,
        },
        'gate_36_baked_wf_55': {
            'type': 'arbitrary',
            'samples': [0.0] * 149 + [0.254468348] * 55,
            'is_overridable': False,
        },
        'gate_29_baked_wf_56': {
            'type': 'arbitrary',
            'samples': [0.0] * 148 + [-0.2081559] * 56,
            'is_overridable': False,
        },
        'gate_36_baked_wf_56': {
            'type': 'arbitrary',
            'samples': [0.0] * 148 + [0.254468348] * 56,
            'is_overridable': False,
        },
        'gate_29_baked_wf_57': {
            'type': 'arbitrary',
            'samples': [0.0] * 147 + [-0.2081559] * 57,
            'is_overridable': False,
        },
        'gate_36_baked_wf_57': {
            'type': 'arbitrary',
            'samples': [0.0] * 147 + [0.254468348] * 57,
            'is_overridable': False,
        },
        'gate_29_baked_wf_58': {
            'type': 'arbitrary',
            'samples': [0.0] * 146 + [-0.2081559] * 58,
            'is_overridable': False,
        },
        'gate_36_baked_wf_58': {
            'type': 'arbitrary',
            'samples': [0.0] * 146 + [0.254468348] * 58,
            'is_overridable': False,
        },
        'gate_29_baked_wf_59': {
            'type': 'arbitrary',
            'samples': [0.0] * 145 + [-0.2081559] * 59,
            'is_overridable': False,
        },
        'gate_36_baked_wf_59': {
            'type': 'arbitrary',
            'samples': [0.0] * 145 + [0.254468348] * 59,
            'is_overridable': False,
        },
        'gate_29_baked_wf_60': {
            'type': 'arbitrary',
            'samples': [0.0] * 144 + [-0.2081559] * 60,
            'is_overridable': False,
        },
        'gate_36_baked_wf_60': {
            'type': 'arbitrary',
            'samples': [0.0] * 144 + [0.254468348] * 60,
            'is_overridable': False,
        },
        'gate_29_baked_wf_61': {
            'type': 'arbitrary',
            'samples': [0.0] * 143 + [-0.2081559] * 61,
            'is_overridable': False,
        },
        'gate_36_baked_wf_61': {
            'type': 'arbitrary',
            'samples': [0.0] * 143 + [0.254468348] * 61,
            'is_overridable': False,
        },
        'gate_29_baked_wf_62': {
            'type': 'arbitrary',
            'samples': [0.0] * 142 + [-0.2081559] * 62,
            'is_overridable': False,
        },
        'gate_36_baked_wf_62': {
            'type': 'arbitrary',
            'samples': [0.0] * 142 + [0.254468348] * 62,
            'is_overridable': False,
        },
        'gate_29_baked_wf_63': {
            'type': 'arbitrary',
            'samples': [0.0] * 141 + [-0.2081559] * 63,
            'is_overridable': False,
        },
        'gate_36_baked_wf_63': {
            'type': 'arbitrary',
            'samples': [0.0] * 141 + [0.254468348] * 63,
            'is_overridable': False,
        },
        'gate_29_baked_wf_64': {
            'type': 'arbitrary',
            'samples': [0.0] * 140 + [-0.2081559] * 64,
            'is_overridable': False,
        },
        'gate_36_baked_wf_64': {
            'type': 'arbitrary',
            'samples': [0.0] * 140 + [0.254468348] * 64,
            'is_overridable': False,
        },
        'gate_29_baked_wf_65': {
            'type': 'arbitrary',
            'samples': [0.0] * 139 + [-0.2081559] * 65,
            'is_overridable': False,
        },
        'gate_36_baked_wf_65': {
            'type': 'arbitrary',
            'samples': [0.0] * 139 + [0.254468348] * 65,
            'is_overridable': False,
        },
        'gate_29_baked_wf_66': {
            'type': 'arbitrary',
            'samples': [0.0] * 138 + [-0.2081559] * 66,
            'is_overridable': False,
        },
        'gate_36_baked_wf_66': {
            'type': 'arbitrary',
            'samples': [0.0] * 138 + [0.254468348] * 66,
            'is_overridable': False,
        },
        'gate_29_baked_wf_67': {
            'type': 'arbitrary',
            'samples': [0.0] * 137 + [-0.2081559] * 67,
            'is_overridable': False,
        },
        'gate_36_baked_wf_67': {
            'type': 'arbitrary',
            'samples': [0.0] * 137 + [0.254468348] * 67,
            'is_overridable': False,
        },
        'gate_29_baked_wf_68': {
            'type': 'arbitrary',
            'samples': [0.0] * 136 + [-0.2081559] * 68,
            'is_overridable': False,
        },
        'gate_36_baked_wf_68': {
            'type': 'arbitrary',
            'samples': [0.0] * 136 + [0.254468348] * 68,
            'is_overridable': False,
        },
        'gate_29_baked_wf_69': {
            'type': 'arbitrary',
            'samples': [0.0] * 135 + [-0.2081559] * 69,
            'is_overridable': False,
        },
        'gate_36_baked_wf_69': {
            'type': 'arbitrary',
            'samples': [0.0] * 135 + [0.254468348] * 69,
            'is_overridable': False,
        },
        'gate_29_baked_wf_70': {
            'type': 'arbitrary',
            'samples': [0.0] * 134 + [-0.2081559] * 70,
            'is_overridable': False,
        },
        'gate_36_baked_wf_70': {
            'type': 'arbitrary',
            'samples': [0.0] * 134 + [0.254468348] * 70,
            'is_overridable': False,
        },
        'gate_29_baked_wf_71': {
            'type': 'arbitrary',
            'samples': [0.0] * 133 + [-0.2081559] * 71,
            'is_overridable': False,
        },
        'gate_36_baked_wf_71': {
            'type': 'arbitrary',
            'samples': [0.0] * 133 + [0.254468348] * 71,
            'is_overridable': False,
        },
        'gate_29_baked_wf_72': {
            'type': 'arbitrary',
            'samples': [0.0] * 132 + [-0.2081559] * 72,
            'is_overridable': False,
        },
        'gate_36_baked_wf_72': {
            'type': 'arbitrary',
            'samples': [0.0] * 132 + [0.254468348] * 72,
            'is_overridable': False,
        },
        'gate_29_baked_wf_73': {
            'type': 'arbitrary',
            'samples': [0.0] * 131 + [-0.2081559] * 73,
            'is_overridable': False,
        },
        'gate_36_baked_wf_73': {
            'type': 'arbitrary',
            'samples': [0.0] * 131 + [0.254468348] * 73,
            'is_overridable': False,
        },
        'gate_29_baked_wf_74': {
            'type': 'arbitrary',
            'samples': [0.0] * 130 + [-0.2081559] * 74,
            'is_overridable': False,
        },
        'gate_36_baked_wf_74': {
            'type': 'arbitrary',
            'samples': [0.0] * 130 + [0.254468348] * 74,
            'is_overridable': False,
        },
        'gate_29_baked_wf_75': {
            'type': 'arbitrary',
            'samples': [0.0] * 129 + [-0.2081559] * 75,
            'is_overridable': False,
        },
        'gate_36_baked_wf_75': {
            'type': 'arbitrary',
            'samples': [0.0] * 129 + [0.254468348] * 75,
            'is_overridable': False,
        },
        'gate_29_baked_wf_76': {
            'type': 'arbitrary',
            'samples': [0.0] * 128 + [-0.2081559] * 76,
            'is_overridable': False,
        },
        'gate_36_baked_wf_76': {
            'type': 'arbitrary',
            'samples': [0.0] * 128 + [0.254468348] * 76,
            'is_overridable': False,
        },
        'gate_29_baked_wf_77': {
            'type': 'arbitrary',
            'samples': [0.0] * 127 + [-0.2081559] * 77,
            'is_overridable': False,
        },
        'gate_36_baked_wf_77': {
            'type': 'arbitrary',
            'samples': [0.0] * 127 + [0.254468348] * 77,
            'is_overridable': False,
        },
        'gate_29_baked_wf_78': {
            'type': 'arbitrary',
            'samples': [0.0] * 126 + [-0.2081559] * 78,
            'is_overridable': False,
        },
        'gate_36_baked_wf_78': {
            'type': 'arbitrary',
            'samples': [0.0] * 126 + [0.254468348] * 78,
            'is_overridable': False,
        },
        'gate_29_baked_wf_79': {
            'type': 'arbitrary',
            'samples': [0.0] * 125 + [-0.2081559] * 79,
            'is_overridable': False,
        },
        'gate_36_baked_wf_79': {
            'type': 'arbitrary',
            'samples': [0.0] * 125 + [0.254468348] * 79,
            'is_overridable': False,
        },
        'gate_29_baked_wf_80': {
            'type': 'arbitrary',
            'samples': [0.0] * 124 + [-0.2081559] * 80,
            'is_overridable': False,
        },
        'gate_36_baked_wf_80': {
            'type': 'arbitrary',
            'samples': [0.0] * 124 + [0.254468348] * 80,
            'is_overridable': False,
        },
        'gate_29_baked_wf_81': {
            'type': 'arbitrary',
            'samples': [0.0] * 123 + [-0.2081559] * 81,
            'is_overridable': False,
        },
        'gate_36_baked_wf_81': {
            'type': 'arbitrary',
            'samples': [0.0] * 123 + [0.254468348] * 81,
            'is_overridable': False,
        },
        'gate_29_baked_wf_82': {
            'type': 'arbitrary',
            'samples': [0.0] * 122 + [-0.2081559] * 82,
            'is_overridable': False,
        },
        'gate_36_baked_wf_82': {
            'type': 'arbitrary',
            'samples': [0.0] * 122 + [0.254468348] * 82,
            'is_overridable': False,
        },
        'gate_29_baked_wf_83': {
            'type': 'arbitrary',
            'samples': [0.0] * 121 + [-0.2081559] * 83,
            'is_overridable': False,
        },
        'gate_36_baked_wf_83': {
            'type': 'arbitrary',
            'samples': [0.0] * 121 + [0.254468348] * 83,
            'is_overridable': False,
        },
        'gate_29_baked_wf_84': {
            'type': 'arbitrary',
            'samples': [0.0] * 120 + [-0.2081559] * 84,
            'is_overridable': False,
        },
        'gate_36_baked_wf_84': {
            'type': 'arbitrary',
            'samples': [0.0] * 120 + [0.254468348] * 84,
            'is_overridable': False,
        },
        'gate_29_baked_wf_85': {
            'type': 'arbitrary',
            'samples': [0.0] * 119 + [-0.2081559] * 85,
            'is_overridable': False,
        },
        'gate_36_baked_wf_85': {
            'type': 'arbitrary',
            'samples': [0.0] * 119 + [0.254468348] * 85,
            'is_overridable': False,
        },
        'gate_29_baked_wf_86': {
            'type': 'arbitrary',
            'samples': [0.0] * 118 + [-0.2081559] * 86,
            'is_overridable': False,
        },
        'gate_36_baked_wf_86': {
            'type': 'arbitrary',
            'samples': [0.0] * 118 + [0.254468348] * 86,
            'is_overridable': False,
        },
        'gate_29_baked_wf_87': {
            'type': 'arbitrary',
            'samples': [0.0] * 117 + [-0.2081559] * 87,
            'is_overridable': False,
        },
        'gate_36_baked_wf_87': {
            'type': 'arbitrary',
            'samples': [0.0] * 117 + [0.254468348] * 87,
            'is_overridable': False,
        },
        'gate_29_baked_wf_88': {
            'type': 'arbitrary',
            'samples': [0.0] * 116 + [-0.2081559] * 88,
            'is_overridable': False,
        },
        'gate_36_baked_wf_88': {
            'type': 'arbitrary',
            'samples': [0.0] * 116 + [0.254468348] * 88,
            'is_overridable': False,
        },
        'gate_29_baked_wf_89': {
            'type': 'arbitrary',
            'samples': [0.0] * 115 + [-0.2081559] * 89,
            'is_overridable': False,
        },
        'gate_36_baked_wf_89': {
            'type': 'arbitrary',
            'samples': [0.0] * 115 + [0.254468348] * 89,
            'is_overridable': False,
        },
        'gate_29_baked_wf_90': {
            'type': 'arbitrary',
            'samples': [0.0] * 114 + [-0.2081559] * 90,
            'is_overridable': False,
        },
        'gate_36_baked_wf_90': {
            'type': 'arbitrary',
            'samples': [0.0] * 114 + [0.254468348] * 90,
            'is_overridable': False,
        },
        'gate_29_baked_wf_91': {
            'type': 'arbitrary',
            'samples': [0.0] * 113 + [-0.2081559] * 91,
            'is_overridable': False,
        },
        'gate_36_baked_wf_91': {
            'type': 'arbitrary',
            'samples': [0.0] * 113 + [0.254468348] * 91,
            'is_overridable': False,
        },
        'gate_29_baked_wf_92': {
            'type': 'arbitrary',
            'samples': [0.0] * 112 + [-0.2081559] * 92,
            'is_overridable': False,
        },
        'gate_36_baked_wf_92': {
            'type': 'arbitrary',
            'samples': [0.0] * 112 + [0.254468348] * 92,
            'is_overridable': False,
        },
        'gate_29_baked_wf_93': {
            'type': 'arbitrary',
            'samples': [0.0] * 111 + [-0.2081559] * 93,
            'is_overridable': False,
        },
        'gate_36_baked_wf_93': {
            'type': 'arbitrary',
            'samples': [0.0] * 111 + [0.254468348] * 93,
            'is_overridable': False,
        },
        'gate_29_baked_wf_94': {
            'type': 'arbitrary',
            'samples': [0.0] * 110 + [-0.2081559] * 94,
            'is_overridable': False,
        },
        'gate_36_baked_wf_94': {
            'type': 'arbitrary',
            'samples': [0.0] * 110 + [0.254468348] * 94,
            'is_overridable': False,
        },
        'gate_29_baked_wf_95': {
            'type': 'arbitrary',
            'samples': [0.0] * 109 + [-0.2081559] * 95,
            'is_overridable': False,
        },
        'gate_36_baked_wf_95': {
            'type': 'arbitrary',
            'samples': [0.0] * 109 + [0.254468348] * 95,
            'is_overridable': False,
        },
        'gate_29_baked_wf_96': {
            'type': 'arbitrary',
            'samples': [0.0] * 108 + [-0.2081559] * 96,
            'is_overridable': False,
        },
        'gate_36_baked_wf_96': {
            'type': 'arbitrary',
            'samples': [0.0] * 108 + [0.254468348] * 96,
            'is_overridable': False,
        },
        'gate_29_baked_wf_97': {
            'type': 'arbitrary',
            'samples': [0.0] * 107 + [-0.2081559] * 97,
            'is_overridable': False,
        },
        'gate_36_baked_wf_97': {
            'type': 'arbitrary',
            'samples': [0.0] * 107 + [0.254468348] * 97,
            'is_overridable': False,
        },
        'gate_29_baked_wf_98': {
            'type': 'arbitrary',
            'samples': [0.0] * 106 + [-0.2081559] * 98,
            'is_overridable': False,
        },
        'gate_36_baked_wf_98': {
            'type': 'arbitrary',
            'samples': [0.0] * 106 + [0.254468348] * 98,
            'is_overridable': False,
        },
        'gate_29_baked_wf_99': {
            'type': 'arbitrary',
            'samples': [0.0] * 105 + [-0.2081559] * 99,
            'is_overridable': False,
        },
        'gate_36_baked_wf_99': {
            'type': 'arbitrary',
            'samples': [0.0] * 105 + [0.254468348] * 99,
            'is_overridable': False,
        },
        'gate_29_baked_wf_100': {
            'type': 'arbitrary',
            'samples': [0.0] * 104 + [-0.2081559] * 100,
            'is_overridable': False,
        },
        'gate_36_baked_wf_100': {
            'type': 'arbitrary',
            'samples': [0.0] * 104 + [0.254468348] * 100,
            'is_overridable': False,
        },
        'gate_29_baked_wf_101': {
            'type': 'arbitrary',
            'samples': [0.0] * 103 + [-0.2081559] * 101,
            'is_overridable': False,
        },
        'gate_36_baked_wf_101': {
            'type': 'arbitrary',
            'samples': [0.0] * 103 + [0.254468348] * 101,
            'is_overridable': False,
        },
        'gate_29_baked_wf_102': {
            'type': 'arbitrary',
            'samples': [0.0] * 102 + [-0.2081559] * 102,
            'is_overridable': False,
        },
        'gate_36_baked_wf_102': {
            'type': 'arbitrary',
            'samples': [0.0] * 102 + [0.254468348] * 102,
            'is_overridable': False,
        },
        'gate_29_baked_wf_103': {
            'type': 'arbitrary',
            'samples': [0.0] * 101 + [-0.2081559] * 103,
            'is_overridable': False,
        },
        'gate_36_baked_wf_103': {
            'type': 'arbitrary',
            'samples': [0.0] * 101 + [0.254468348] * 103,
            'is_overridable': False,
        },
        'gate_29_baked_wf_104': {
            'type': 'arbitrary',
            'samples': [0.0] * 100 + [-0.2081559] * 104,
            'is_overridable': False,
        },
        'gate_36_baked_wf_104': {
            'type': 'arbitrary',
            'samples': [0.0] * 100 + [0.254468348] * 104,
            'is_overridable': False,
        },
        'gate_29_baked_wf_105': {
            'type': 'arbitrary',
            'samples': [0.0] * 99 + [-0.2081559] * 105,
            'is_overridable': False,
        },
        'gate_36_baked_wf_105': {
            'type': 'arbitrary',
            'samples': [0.0] * 99 + [0.254468348] * 105,
            'is_overridable': False,
        },
        'gate_29_baked_wf_106': {
            'type': 'arbitrary',
            'samples': [0.0] * 98 + [-0.2081559] * 106,
            'is_overridable': False,
        },
        'gate_36_baked_wf_106': {
            'type': 'arbitrary',
            'samples': [0.0] * 98 + [0.254468348] * 106,
            'is_overridable': False,
        },
        'gate_29_baked_wf_107': {
            'type': 'arbitrary',
            'samples': [0.0] * 97 + [-0.2081559] * 107,
            'is_overridable': False,
        },
        'gate_36_baked_wf_107': {
            'type': 'arbitrary',
            'samples': [0.0] * 97 + [0.254468348] * 107,
            'is_overridable': False,
        },
        'gate_29_baked_wf_108': {
            'type': 'arbitrary',
            'samples': [0.0] * 96 + [-0.2081559] * 108,
            'is_overridable': False,
        },
        'gate_36_baked_wf_108': {
            'type': 'arbitrary',
            'samples': [0.0] * 96 + [0.254468348] * 108,
            'is_overridable': False,
        },
        'gate_29_baked_wf_109': {
            'type': 'arbitrary',
            'samples': [0.0] * 95 + [-0.2081559] * 109,
            'is_overridable': False,
        },
        'gate_36_baked_wf_109': {
            'type': 'arbitrary',
            'samples': [0.0] * 95 + [0.254468348] * 109,
            'is_overridable': False,
        },
        'gate_29_baked_wf_110': {
            'type': 'arbitrary',
            'samples': [0.0] * 94 + [-0.2081559] * 110,
            'is_overridable': False,
        },
        'gate_36_baked_wf_110': {
            'type': 'arbitrary',
            'samples': [0.0] * 94 + [0.254468348] * 110,
            'is_overridable': False,
        },
        'gate_29_baked_wf_111': {
            'type': 'arbitrary',
            'samples': [0.0] * 93 + [-0.2081559] * 111,
            'is_overridable': False,
        },
        'gate_36_baked_wf_111': {
            'type': 'arbitrary',
            'samples': [0.0] * 93 + [0.254468348] * 111,
            'is_overridable': False,
        },
        'gate_29_baked_wf_112': {
            'type': 'arbitrary',
            'samples': [0.0] * 92 + [-0.2081559] * 112,
            'is_overridable': False,
        },
        'gate_36_baked_wf_112': {
            'type': 'arbitrary',
            'samples': [0.0] * 92 + [0.254468348] * 112,
            'is_overridable': False,
        },
        'gate_29_baked_wf_113': {
            'type': 'arbitrary',
            'samples': [0.0] * 91 + [-0.2081559] * 113,
            'is_overridable': False,
        },
        'gate_36_baked_wf_113': {
            'type': 'arbitrary',
            'samples': [0.0] * 91 + [0.254468348] * 113,
            'is_overridable': False,
        },
        'gate_29_baked_wf_114': {
            'type': 'arbitrary',
            'samples': [0.0] * 90 + [-0.2081559] * 114,
            'is_overridable': False,
        },
        'gate_36_baked_wf_114': {
            'type': 'arbitrary',
            'samples': [0.0] * 90 + [0.254468348] * 114,
            'is_overridable': False,
        },
        'gate_29_baked_wf_115': {
            'type': 'arbitrary',
            'samples': [0.0] * 89 + [-0.2081559] * 115,
            'is_overridable': False,
        },
        'gate_36_baked_wf_115': {
            'type': 'arbitrary',
            'samples': [0.0] * 89 + [0.254468348] * 115,
            'is_overridable': False,
        },
        'gate_29_baked_wf_116': {
            'type': 'arbitrary',
            'samples': [0.0] * 88 + [-0.2081559] * 116,
            'is_overridable': False,
        },
        'gate_36_baked_wf_116': {
            'type': 'arbitrary',
            'samples': [0.0] * 88 + [0.254468348] * 116,
            'is_overridable': False,
        },
        'gate_29_baked_wf_117': {
            'type': 'arbitrary',
            'samples': [0.0] * 87 + [-0.2081559] * 117,
            'is_overridable': False,
        },
        'gate_36_baked_wf_117': {
            'type': 'arbitrary',
            'samples': [0.0] * 87 + [0.254468348] * 117,
            'is_overridable': False,
        },
        'gate_29_baked_wf_118': {
            'type': 'arbitrary',
            'samples': [0.0] * 86 + [-0.2081559] * 118,
            'is_overridable': False,
        },
        'gate_36_baked_wf_118': {
            'type': 'arbitrary',
            'samples': [0.0] * 86 + [0.254468348] * 118,
            'is_overridable': False,
        },
        'gate_29_baked_wf_119': {
            'type': 'arbitrary',
            'samples': [0.0] * 85 + [-0.2081559] * 119,
            'is_overridable': False,
        },
        'gate_36_baked_wf_119': {
            'type': 'arbitrary',
            'samples': [0.0] * 85 + [0.254468348] * 119,
            'is_overridable': False,
        },
        'gate_29_baked_wf_120': {
            'type': 'arbitrary',
            'samples': [0.0] * 84 + [-0.2081559] * 120,
            'is_overridable': False,
        },
        'gate_36_baked_wf_120': {
            'type': 'arbitrary',
            'samples': [0.0] * 84 + [0.254468348] * 120,
            'is_overridable': False,
        },
        'gate_29_baked_wf_121': {
            'type': 'arbitrary',
            'samples': [0.0] * 83 + [-0.2081559] * 121,
            'is_overridable': False,
        },
        'gate_36_baked_wf_121': {
            'type': 'arbitrary',
            'samples': [0.0] * 83 + [0.254468348] * 121,
            'is_overridable': False,
        },
        'gate_29_baked_wf_122': {
            'type': 'arbitrary',
            'samples': [0.0] * 82 + [-0.2081559] * 122,
            'is_overridable': False,
        },
        'gate_36_baked_wf_122': {
            'type': 'arbitrary',
            'samples': [0.0] * 82 + [0.254468348] * 122,
            'is_overridable': False,
        },
        'gate_29_baked_wf_123': {
            'type': 'arbitrary',
            'samples': [0.0] * 81 + [-0.2081559] * 123,
            'is_overridable': False,
        },
        'gate_36_baked_wf_123': {
            'type': 'arbitrary',
            'samples': [0.0] * 81 + [0.254468348] * 123,
            'is_overridable': False,
        },
        'gate_29_baked_wf_124': {
            'type': 'arbitrary',
            'samples': [0.0] * 80 + [-0.2081559] * 124,
            'is_overridable': False,
        },
        'gate_36_baked_wf_124': {
            'type': 'arbitrary',
            'samples': [0.0] * 80 + [0.254468348] * 124,
            'is_overridable': False,
        },
        'gate_29_baked_wf_125': {
            'type': 'arbitrary',
            'samples': [0.0] * 79 + [-0.2081559] * 125,
            'is_overridable': False,
        },
        'gate_36_baked_wf_125': {
            'type': 'arbitrary',
            'samples': [0.0] * 79 + [0.254468348] * 125,
            'is_overridable': False,
        },
        'gate_29_baked_wf_126': {
            'type': 'arbitrary',
            'samples': [0.0] * 78 + [-0.2081559] * 126,
            'is_overridable': False,
        },
        'gate_36_baked_wf_126': {
            'type': 'arbitrary',
            'samples': [0.0] * 78 + [0.254468348] * 126,
            'is_overridable': False,
        },
        'gate_29_baked_wf_127': {
            'type': 'arbitrary',
            'samples': [0.0] * 77 + [-0.2081559] * 127,
            'is_overridable': False,
        },
        'gate_36_baked_wf_127': {
            'type': 'arbitrary',
            'samples': [0.0] * 77 + [0.254468348] * 127,
            'is_overridable': False,
        },
        'gate_29_baked_wf_128': {
            'type': 'arbitrary',
            'samples': [0.0] * 76 + [-0.2081559] * 128,
            'is_overridable': False,
        },
        'gate_36_baked_wf_128': {
            'type': 'arbitrary',
            'samples': [0.0] * 76 + [0.254468348] * 128,
            'is_overridable': False,
        },
        'gate_29_baked_wf_129': {
            'type': 'arbitrary',
            'samples': [0.0] * 75 + [-0.2081559] * 129,
            'is_overridable': False,
        },
        'gate_36_baked_wf_129': {
            'type': 'arbitrary',
            'samples': [0.0] * 75 + [0.254468348] * 129,
            'is_overridable': False,
        },
        'gate_29_baked_wf_130': {
            'type': 'arbitrary',
            'samples': [0.0] * 74 + [-0.2081559] * 130,
            'is_overridable': False,
        },
        'gate_36_baked_wf_130': {
            'type': 'arbitrary',
            'samples': [0.0] * 74 + [0.254468348] * 130,
            'is_overridable': False,
        },
        'gate_29_baked_wf_131': {
            'type': 'arbitrary',
            'samples': [0.0] * 73 + [-0.2081559] * 131,
            'is_overridable': False,
        },
        'gate_36_baked_wf_131': {
            'type': 'arbitrary',
            'samples': [0.0] * 73 + [0.254468348] * 131,
            'is_overridable': False,
        },
        'gate_29_baked_wf_132': {
            'type': 'arbitrary',
            'samples': [0.0] * 72 + [-0.2081559] * 132,
            'is_overridable': False,
        },
        'gate_36_baked_wf_132': {
            'type': 'arbitrary',
            'samples': [0.0] * 72 + [0.254468348] * 132,
            'is_overridable': False,
        },
        'gate_29_baked_wf_133': {
            'type': 'arbitrary',
            'samples': [0.0] * 71 + [-0.2081559] * 133,
            'is_overridable': False,
        },
        'gate_36_baked_wf_133': {
            'type': 'arbitrary',
            'samples': [0.0] * 71 + [0.254468348] * 133,
            'is_overridable': False,
        },
        'gate_29_baked_wf_134': {
            'type': 'arbitrary',
            'samples': [0.0] * 70 + [-0.2081559] * 134,
            'is_overridable': False,
        },
        'gate_36_baked_wf_134': {
            'type': 'arbitrary',
            'samples': [0.0] * 70 + [0.254468348] * 134,
            'is_overridable': False,
        },
        'gate_29_baked_wf_135': {
            'type': 'arbitrary',
            'samples': [0.0] * 69 + [-0.2081559] * 135,
            'is_overridable': False,
        },
        'gate_36_baked_wf_135': {
            'type': 'arbitrary',
            'samples': [0.0] * 69 + [0.254468348] * 135,
            'is_overridable': False,
        },
        'gate_29_baked_wf_136': {
            'type': 'arbitrary',
            'samples': [0.0] * 68 + [-0.2081559] * 136,
            'is_overridable': False,
        },
        'gate_36_baked_wf_136': {
            'type': 'arbitrary',
            'samples': [0.0] * 68 + [0.254468348] * 136,
            'is_overridable': False,
        },
        'gate_29_baked_wf_137': {
            'type': 'arbitrary',
            'samples': [0.0] * 67 + [-0.2081559] * 137,
            'is_overridable': False,
        },
        'gate_36_baked_wf_137': {
            'type': 'arbitrary',
            'samples': [0.0] * 67 + [0.254468348] * 137,
            'is_overridable': False,
        },
        'gate_29_baked_wf_138': {
            'type': 'arbitrary',
            'samples': [0.0] * 66 + [-0.2081559] * 138,
            'is_overridable': False,
        },
        'gate_36_baked_wf_138': {
            'type': 'arbitrary',
            'samples': [0.0] * 66 + [0.254468348] * 138,
            'is_overridable': False,
        },
        'gate_29_baked_wf_139': {
            'type': 'arbitrary',
            'samples': [0.0] * 65 + [-0.2081559] * 139,
            'is_overridable': False,
        },
        'gate_36_baked_wf_139': {
            'type': 'arbitrary',
            'samples': [0.0] * 65 + [0.254468348] * 139,
            'is_overridable': False,
        },
        'gate_29_baked_wf_140': {
            'type': 'arbitrary',
            'samples': [0.0] * 64 + [-0.2081559] * 140,
            'is_overridable': False,
        },
        'gate_36_baked_wf_140': {
            'type': 'arbitrary',
            'samples': [0.0] * 64 + [0.254468348] * 140,
            'is_overridable': False,
        },
        'gate_29_baked_wf_141': {
            'type': 'arbitrary',
            'samples': [0.0] * 63 + [-0.2081559] * 141,
            'is_overridable': False,
        },
        'gate_36_baked_wf_141': {
            'type': 'arbitrary',
            'samples': [0.0] * 63 + [0.254468348] * 141,
            'is_overridable': False,
        },
        'gate_29_baked_wf_142': {
            'type': 'arbitrary',
            'samples': [0.0] * 62 + [-0.2081559] * 142,
            'is_overridable': False,
        },
        'gate_36_baked_wf_142': {
            'type': 'arbitrary',
            'samples': [0.0] * 62 + [0.254468348] * 142,
            'is_overridable': False,
        },
        'gate_29_baked_wf_143': {
            'type': 'arbitrary',
            'samples': [0.0] * 61 + [-0.2081559] * 143,
            'is_overridable': False,
        },
        'gate_36_baked_wf_143': {
            'type': 'arbitrary',
            'samples': [0.0] * 61 + [0.254468348] * 143,
            'is_overridable': False,
        },
        'gate_29_baked_wf_144': {
            'type': 'arbitrary',
            'samples': [0.0] * 60 + [-0.2081559] * 144,
            'is_overridable': False,
        },
        'gate_36_baked_wf_144': {
            'type': 'arbitrary',
            'samples': [0.0] * 60 + [0.254468348] * 144,
            'is_overridable': False,
        },
        'gate_29_baked_wf_145': {
            'type': 'arbitrary',
            'samples': [0.0] * 59 + [-0.2081559] * 145,
            'is_overridable': False,
        },
        'gate_36_baked_wf_145': {
            'type': 'arbitrary',
            'samples': [0.0] * 59 + [0.254468348] * 145,
            'is_overridable': False,
        },
        'gate_29_baked_wf_146': {
            'type': 'arbitrary',
            'samples': [0.0] * 58 + [-0.2081559] * 146,
            'is_overridable': False,
        },
        'gate_36_baked_wf_146': {
            'type': 'arbitrary',
            'samples': [0.0] * 58 + [0.254468348] * 146,
            'is_overridable': False,
        },
        'gate_29_baked_wf_147': {
            'type': 'arbitrary',
            'samples': [0.0] * 57 + [-0.2081559] * 147,
            'is_overridable': False,
        },
        'gate_36_baked_wf_147': {
            'type': 'arbitrary',
            'samples': [0.0] * 57 + [0.254468348] * 147,
            'is_overridable': False,
        },
        'gate_29_baked_wf_148': {
            'type': 'arbitrary',
            'samples': [0.0] * 56 + [-0.2081559] * 148,
            'is_overridable': False,
        },
        'gate_36_baked_wf_148': {
            'type': 'arbitrary',
            'samples': [0.0] * 56 + [0.254468348] * 148,
            'is_overridable': False,
        },
        'gate_29_baked_wf_149': {
            'type': 'arbitrary',
            'samples': [0.0] * 55 + [-0.2081559] * 149,
            'is_overridable': False,
        },
        'gate_36_baked_wf_149': {
            'type': 'arbitrary',
            'samples': [0.0] * 55 + [0.254468348] * 149,
            'is_overridable': False,
        },
        'gate_29_baked_wf_150': {
            'type': 'arbitrary',
            'samples': [0.0] * 54 + [-0.2081559] * 150,
            'is_overridable': False,
        },
        'gate_36_baked_wf_150': {
            'type': 'arbitrary',
            'samples': [0.0] * 54 + [0.254468348] * 150,
            'is_overridable': False,
        },
        'gate_29_baked_wf_151': {
            'type': 'arbitrary',
            'samples': [0.0] * 53 + [-0.2081559] * 151,
            'is_overridable': False,
        },
        'gate_36_baked_wf_151': {
            'type': 'arbitrary',
            'samples': [0.0] * 53 + [0.254468348] * 151,
            'is_overridable': False,
        },
        'gate_29_baked_wf_152': {
            'type': 'arbitrary',
            'samples': [0.0] * 52 + [-0.2081559] * 152,
            'is_overridable': False,
        },
        'gate_36_baked_wf_152': {
            'type': 'arbitrary',
            'samples': [0.0] * 52 + [0.254468348] * 152,
            'is_overridable': False,
        },
        'gate_29_baked_wf_153': {
            'type': 'arbitrary',
            'samples': [0.0] * 51 + [-0.2081559] * 153,
            'is_overridable': False,
        },
        'gate_36_baked_wf_153': {
            'type': 'arbitrary',
            'samples': [0.0] * 51 + [0.254468348] * 153,
            'is_overridable': False,
        },
        'gate_29_baked_wf_154': {
            'type': 'arbitrary',
            'samples': [0.0] * 50 + [-0.2081559] * 154,
            'is_overridable': False,
        },
        'gate_36_baked_wf_154': {
            'type': 'arbitrary',
            'samples': [0.0] * 50 + [0.254468348] * 154,
            'is_overridable': False,
        },
        'gate_29_baked_wf_155': {
            'type': 'arbitrary',
            'samples': [0.0] * 49 + [-0.2081559] * 155,
            'is_overridable': False,
        },
        'gate_36_baked_wf_155': {
            'type': 'arbitrary',
            'samples': [0.0] * 49 + [0.254468348] * 155,
            'is_overridable': False,
        },
        'gate_29_baked_wf_156': {
            'type': 'arbitrary',
            'samples': [0.0] * 48 + [-0.2081559] * 156,
            'is_overridable': False,
        },
        'gate_36_baked_wf_156': {
            'type': 'arbitrary',
            'samples': [0.0] * 48 + [0.254468348] * 156,
            'is_overridable': False,
        },
        'gate_29_baked_wf_157': {
            'type': 'arbitrary',
            'samples': [0.0] * 47 + [-0.2081559] * 157,
            'is_overridable': False,
        },
        'gate_36_baked_wf_157': {
            'type': 'arbitrary',
            'samples': [0.0] * 47 + [0.254468348] * 157,
            'is_overridable': False,
        },
        'gate_29_baked_wf_158': {
            'type': 'arbitrary',
            'samples': [0.0] * 46 + [-0.2081559] * 158,
            'is_overridable': False,
        },
        'gate_36_baked_wf_158': {
            'type': 'arbitrary',
            'samples': [0.0] * 46 + [0.254468348] * 158,
            'is_overridable': False,
        },
        'gate_29_baked_wf_159': {
            'type': 'arbitrary',
            'samples': [0.0] * 45 + [-0.2081559] * 159,
            'is_overridable': False,
        },
        'gate_36_baked_wf_159': {
            'type': 'arbitrary',
            'samples': [0.0] * 45 + [0.254468348] * 159,
            'is_overridable': False,
        },
        'gate_29_baked_wf_160': {
            'type': 'arbitrary',
            'samples': [0.0] * 44 + [-0.2081559] * 160,
            'is_overridable': False,
        },
        'gate_36_baked_wf_160': {
            'type': 'arbitrary',
            'samples': [0.0] * 44 + [0.254468348] * 160,
            'is_overridable': False,
        },
        'gate_29_baked_wf_161': {
            'type': 'arbitrary',
            'samples': [0.0] * 43 + [-0.2081559] * 161,
            'is_overridable': False,
        },
        'gate_36_baked_wf_161': {
            'type': 'arbitrary',
            'samples': [0.0] * 43 + [0.254468348] * 161,
            'is_overridable': False,
        },
        'gate_29_baked_wf_162': {
            'type': 'arbitrary',
            'samples': [0.0] * 42 + [-0.2081559] * 162,
            'is_overridable': False,
        },
        'gate_36_baked_wf_162': {
            'type': 'arbitrary',
            'samples': [0.0] * 42 + [0.254468348] * 162,
            'is_overridable': False,
        },
        'gate_29_baked_wf_163': {
            'type': 'arbitrary',
            'samples': [0.0] * 41 + [-0.2081559] * 163,
            'is_overridable': False,
        },
        'gate_36_baked_wf_163': {
            'type': 'arbitrary',
            'samples': [0.0] * 41 + [0.254468348] * 163,
            'is_overridable': False,
        },
        'gate_29_baked_wf_164': {
            'type': 'arbitrary',
            'samples': [0.0] * 40 + [-0.2081559] * 164,
            'is_overridable': False,
        },
        'gate_36_baked_wf_164': {
            'type': 'arbitrary',
            'samples': [0.0] * 40 + [0.254468348] * 164,
            'is_overridable': False,
        },
        'gate_29_baked_wf_165': {
            'type': 'arbitrary',
            'samples': [0.0] * 39 + [-0.2081559] * 165,
            'is_overridable': False,
        },
        'gate_36_baked_wf_165': {
            'type': 'arbitrary',
            'samples': [0.0] * 39 + [0.254468348] * 165,
            'is_overridable': False,
        },
        'gate_29_baked_wf_166': {
            'type': 'arbitrary',
            'samples': [0.0] * 38 + [-0.2081559] * 166,
            'is_overridable': False,
        },
        'gate_36_baked_wf_166': {
            'type': 'arbitrary',
            'samples': [0.0] * 38 + [0.254468348] * 166,
            'is_overridable': False,
        },
        'gate_29_baked_wf_167': {
            'type': 'arbitrary',
            'samples': [0.0] * 37 + [-0.2081559] * 167,
            'is_overridable': False,
        },
        'gate_36_baked_wf_167': {
            'type': 'arbitrary',
            'samples': [0.0] * 37 + [0.254468348] * 167,
            'is_overridable': False,
        },
        'gate_29_baked_wf_168': {
            'type': 'arbitrary',
            'samples': [0.0] * 36 + [-0.2081559] * 168,
            'is_overridable': False,
        },
        'gate_36_baked_wf_168': {
            'type': 'arbitrary',
            'samples': [0.0] * 36 + [0.254468348] * 168,
            'is_overridable': False,
        },
        'gate_29_baked_wf_169': {
            'type': 'arbitrary',
            'samples': [0.0] * 35 + [-0.2081559] * 169,
            'is_overridable': False,
        },
        'gate_36_baked_wf_169': {
            'type': 'arbitrary',
            'samples': [0.0] * 35 + [0.254468348] * 169,
            'is_overridable': False,
        },
        'gate_29_baked_wf_170': {
            'type': 'arbitrary',
            'samples': [0.0] * 34 + [-0.2081559] * 170,
            'is_overridable': False,
        },
        'gate_36_baked_wf_170': {
            'type': 'arbitrary',
            'samples': [0.0] * 34 + [0.254468348] * 170,
            'is_overridable': False,
        },
        'gate_29_baked_wf_171': {
            'type': 'arbitrary',
            'samples': [0.0] * 33 + [-0.2081559] * 171,
            'is_overridable': False,
        },
        'gate_36_baked_wf_171': {
            'type': 'arbitrary',
            'samples': [0.0] * 33 + [0.254468348] * 171,
            'is_overridable': False,
        },
        'gate_29_baked_wf_172': {
            'type': 'arbitrary',
            'samples': [0.0] * 32 + [-0.2081559] * 172,
            'is_overridable': False,
        },
        'gate_36_baked_wf_172': {
            'type': 'arbitrary',
            'samples': [0.0] * 32 + [0.254468348] * 172,
            'is_overridable': False,
        },
        'gate_29_baked_wf_173': {
            'type': 'arbitrary',
            'samples': [0.0] * 31 + [-0.2081559] * 173,
            'is_overridable': False,
        },
        'gate_36_baked_wf_173': {
            'type': 'arbitrary',
            'samples': [0.0] * 31 + [0.254468348] * 173,
            'is_overridable': False,
        },
        'gate_29_baked_wf_174': {
            'type': 'arbitrary',
            'samples': [0.0] * 30 + [-0.2081559] * 174,
            'is_overridable': False,
        },
        'gate_36_baked_wf_174': {
            'type': 'arbitrary',
            'samples': [0.0] * 30 + [0.254468348] * 174,
            'is_overridable': False,
        },
        'gate_29_baked_wf_175': {
            'type': 'arbitrary',
            'samples': [0.0] * 29 + [-0.2081559] * 175,
            'is_overridable': False,
        },
        'gate_36_baked_wf_175': {
            'type': 'arbitrary',
            'samples': [0.0] * 29 + [0.254468348] * 175,
            'is_overridable': False,
        },
        'gate_29_baked_wf_176': {
            'type': 'arbitrary',
            'samples': [0.0] * 28 + [-0.2081559] * 176,
            'is_overridable': False,
        },
        'gate_36_baked_wf_176': {
            'type': 'arbitrary',
            'samples': [0.0] * 28 + [0.254468348] * 176,
            'is_overridable': False,
        },
        'gate_29_baked_wf_177': {
            'type': 'arbitrary',
            'samples': [0.0] * 27 + [-0.2081559] * 177,
            'is_overridable': False,
        },
        'gate_36_baked_wf_177': {
            'type': 'arbitrary',
            'samples': [0.0] * 27 + [0.254468348] * 177,
            'is_overridable': False,
        },
        'gate_29_baked_wf_178': {
            'type': 'arbitrary',
            'samples': [0.0] * 26 + [-0.2081559] * 178,
            'is_overridable': False,
        },
        'gate_36_baked_wf_178': {
            'type': 'arbitrary',
            'samples': [0.0] * 26 + [0.254468348] * 178,
            'is_overridable': False,
        },
        'gate_29_baked_wf_179': {
            'type': 'arbitrary',
            'samples': [0.0] * 25 + [-0.2081559] * 179,
            'is_overridable': False,
        },
        'gate_36_baked_wf_179': {
            'type': 'arbitrary',
            'samples': [0.0] * 25 + [0.254468348] * 179,
            'is_overridable': False,
        },
        'gate_29_baked_wf_180': {
            'type': 'arbitrary',
            'samples': [0.0] * 24 + [-0.2081559] * 180,
            'is_overridable': False,
        },
        'gate_36_baked_wf_180': {
            'type': 'arbitrary',
            'samples': [0.0] * 24 + [0.254468348] * 180,
            'is_overridable': False,
        },
        'gate_29_baked_wf_181': {
            'type': 'arbitrary',
            'samples': [0.0] * 23 + [-0.2081559] * 181,
            'is_overridable': False,
        },
        'gate_36_baked_wf_181': {
            'type': 'arbitrary',
            'samples': [0.0] * 23 + [0.254468348] * 181,
            'is_overridable': False,
        },
        'gate_29_baked_wf_182': {
            'type': 'arbitrary',
            'samples': [0.0] * 22 + [-0.2081559] * 182,
            'is_overridable': False,
        },
        'gate_36_baked_wf_182': {
            'type': 'arbitrary',
            'samples': [0.0] * 22 + [0.254468348] * 182,
            'is_overridable': False,
        },
        'gate_29_baked_wf_183': {
            'type': 'arbitrary',
            'samples': [0.0] * 21 + [-0.2081559] * 183,
            'is_overridable': False,
        },
        'gate_36_baked_wf_183': {
            'type': 'arbitrary',
            'samples': [0.0] * 21 + [0.254468348] * 183,
            'is_overridable': False,
        },
        'gate_29_baked_wf_184': {
            'type': 'arbitrary',
            'samples': [0.0] * 20 + [-0.2081559] * 184,
            'is_overridable': False,
        },
        'gate_36_baked_wf_184': {
            'type': 'arbitrary',
            'samples': [0.0] * 20 + [0.254468348] * 184,
            'is_overridable': False,
        },
        'gate_29_baked_wf_185': {
            'type': 'arbitrary',
            'samples': [0.0] * 19 + [-0.2081559] * 185,
            'is_overridable': False,
        },
        'gate_36_baked_wf_185': {
            'type': 'arbitrary',
            'samples': [0.0] * 19 + [0.254468348] * 185,
            'is_overridable': False,
        },
        'gate_29_baked_wf_186': {
            'type': 'arbitrary',
            'samples': [0.0] * 18 + [-0.2081559] * 186,
            'is_overridable': False,
        },
        'gate_36_baked_wf_186': {
            'type': 'arbitrary',
            'samples': [0.0] * 18 + [0.254468348] * 186,
            'is_overridable': False,
        },
        'gate_29_baked_wf_187': {
            'type': 'arbitrary',
            'samples': [0.0] * 17 + [-0.2081559] * 187,
            'is_overridable': False,
        },
        'gate_36_baked_wf_187': {
            'type': 'arbitrary',
            'samples': [0.0] * 17 + [0.254468348] * 187,
            'is_overridable': False,
        },
        'gate_29_baked_wf_188': {
            'type': 'arbitrary',
            'samples': [0.0] * 16 + [-0.2081559] * 188,
            'is_overridable': False,
        },
        'gate_36_baked_wf_188': {
            'type': 'arbitrary',
            'samples': [0.0] * 16 + [0.254468348] * 188,
            'is_overridable': False,
        },
        'gate_29_baked_wf_189': {
            'type': 'arbitrary',
            'samples': [0.0] * 15 + [-0.2081559] * 189,
            'is_overridable': False,
        },
        'gate_36_baked_wf_189': {
            'type': 'arbitrary',
            'samples': [0.0] * 15 + [0.254468348] * 189,
            'is_overridable': False,
        },
        'gate_29_baked_wf_190': {
            'type': 'arbitrary',
            'samples': [0.0] * 14 + [-0.2081559] * 190,
            'is_overridable': False,
        },
        'gate_36_baked_wf_190': {
            'type': 'arbitrary',
            'samples': [0.0] * 14 + [0.254468348] * 190,
            'is_overridable': False,
        },
        'gate_29_baked_wf_191': {
            'type': 'arbitrary',
            'samples': [0.0] * 13 + [-0.2081559] * 191,
            'is_overridable': False,
        },
        'gate_36_baked_wf_191': {
            'type': 'arbitrary',
            'samples': [0.0] * 13 + [0.254468348] * 191,
            'is_overridable': False,
        },
        'gate_29_baked_wf_192': {
            'type': 'arbitrary',
            'samples': [0.0] * 12 + [-0.2081559] * 192,
            'is_overridable': False,
        },
        'gate_36_baked_wf_192': {
            'type': 'arbitrary',
            'samples': [0.0] * 12 + [0.254468348] * 192,
            'is_overridable': False,
        },
        'gate_29_baked_wf_193': {
            'type': 'arbitrary',
            'samples': [0.0] * 11 + [-0.2081559] * 193,
            'is_overridable': False,
        },
        'gate_36_baked_wf_193': {
            'type': 'arbitrary',
            'samples': [0.0] * 11 + [0.254468348] * 193,
            'is_overridable': False,
        },
        'gate_29_baked_wf_194': {
            'type': 'arbitrary',
            'samples': [0.0] * 10 + [-0.2081559] * 194,
            'is_overridable': False,
        },
        'gate_36_baked_wf_194': {
            'type': 'arbitrary',
            'samples': [0.0] * 10 + [0.254468348] * 194,
            'is_overridable': False,
        },
        'gate_29_baked_wf_195': {
            'type': 'arbitrary',
            'samples': [0.0] * 9 + [-0.2081559] * 195,
            'is_overridable': False,
        },
        'gate_36_baked_wf_195': {
            'type': 'arbitrary',
            'samples': [0.0] * 9 + [0.254468348] * 195,
            'is_overridable': False,
        },
        'gate_29_baked_wf_196': {
            'type': 'arbitrary',
            'samples': [0.0] * 8 + [-0.2081559] * 196,
            'is_overridable': False,
        },
        'gate_36_baked_wf_196': {
            'type': 'arbitrary',
            'samples': [0.0] * 8 + [0.254468348] * 196,
            'is_overridable': False,
        },
        'gate_29_baked_wf_197': {
            'type': 'arbitrary',
            'samples': [0.0] * 7 + [-0.2081559] * 197,
            'is_overridable': False,
        },
        'gate_36_baked_wf_197': {
            'type': 'arbitrary',
            'samples': [0.0] * 7 + [0.254468348] * 197,
            'is_overridable': False,
        },
        'gate_29_baked_wf_198': {
            'type': 'arbitrary',
            'samples': [0.0] * 6 + [-0.2081559] * 198,
            'is_overridable': False,
        },
        'gate_36_baked_wf_198': {
            'type': 'arbitrary',
            'samples': [0.0] * 6 + [0.254468348] * 198,
            'is_overridable': False,
        },
        'gate_29_baked_wf_199': {
            'type': 'arbitrary',
            'samples': [0.0] * 5 + [-0.2081559] * 199,
            'is_overridable': False,
        },
        'gate_36_baked_wf_199': {
            'type': 'arbitrary',
            'samples': [0.0] * 5 + [0.254468348] * 199,
            'is_overridable': False,
        },
        'gate_29_baked_wf_200': {
            'type': 'arbitrary',
            'samples': [0.0] * 4 + [-0.2081559] * 200,
            'is_overridable': False,
        },
        'gate_36_baked_wf_200': {
            'type': 'arbitrary',
            'samples': [0.0] * 4 + [0.254468348] * 200,
            'is_overridable': False,
        },
        'gate_29_baked_wf_201': {
            'type': 'arbitrary',
            'samples': [0.0] * 204,
            'is_overridable': False,
        },
        'gate_36_baked_wf_201': {
            'type': 'arbitrary',
            'samples': [0.0] * 204,
            'is_overridable': False,
        },
        'gate_29_baked_wf_202': {
            'type': 'arbitrary',
            'samples': [0.0] * 203 + [-0.2081559],
            'is_overridable': False,
        },
        'gate_36_baked_wf_202': {
            'type': 'arbitrary',
            'samples': [0.0] * 203 + [0.254468348],
            'is_overridable': False,
        },
        'gate_29_baked_wf_203': {
            'type': 'arbitrary',
            'samples': [0.0] * 202 + [-0.2081559] * 2,
            'is_overridable': False,
        },
        'gate_36_baked_wf_203': {
            'type': 'arbitrary',
            'samples': [0.0] * 202 + [0.254468348] * 2,
            'is_overridable': False,
        },
        'gate_29_baked_wf_204': {
            'type': 'arbitrary',
            'samples': [0.0] * 201 + [-0.2081559] * 3,
            'is_overridable': False,
        },
        'gate_36_baked_wf_204': {
            'type': 'arbitrary',
            'samples': [0.0] * 201 + [0.254468348] * 3,
            'is_overridable': False,
        },
        'gate_29_baked_wf_205': {
            'type': 'arbitrary',
            'samples': [0.0] * 200 + [-0.2081559] * 4,
            'is_overridable': False,
        },
        'gate_36_baked_wf_205': {
            'type': 'arbitrary',
            'samples': [0.0] * 200 + [0.254468348] * 4,
            'is_overridable': False,
        },
        'gate_29_baked_wf_206': {
            'type': 'arbitrary',
            'samples': [0.0] * 199 + [-0.2081559] * 5,
            'is_overridable': False,
        },
        'gate_36_baked_wf_206': {
            'type': 'arbitrary',
            'samples': [0.0] * 199 + [0.254468348] * 5,
            'is_overridable': False,
        },
        'gate_29_baked_wf_207': {
            'type': 'arbitrary',
            'samples': [0.0] * 198 + [-0.2081559] * 6,
            'is_overridable': False,
        },
        'gate_36_baked_wf_207': {
            'type': 'arbitrary',
            'samples': [0.0] * 198 + [0.254468348] * 6,
            'is_overridable': False,
        },
        'gate_29_baked_wf_208': {
            'type': 'arbitrary',
            'samples': [0.0] * 197 + [-0.2081559] * 7,
            'is_overridable': False,
        },
        'gate_36_baked_wf_208': {
            'type': 'arbitrary',
            'samples': [0.0] * 197 + [0.254468348] * 7,
            'is_overridable': False,
        },
        'gate_29_baked_wf_209': {
            'type': 'arbitrary',
            'samples': [0.0] * 196 + [-0.2081559] * 8,
            'is_overridable': False,
        },
        'gate_36_baked_wf_209': {
            'type': 'arbitrary',
            'samples': [0.0] * 196 + [0.254468348] * 8,
            'is_overridable': False,
        },
        'gate_29_baked_wf_210': {
            'type': 'arbitrary',
            'samples': [0.0] * 195 + [-0.2081559] * 9,
            'is_overridable': False,
        },
        'gate_36_baked_wf_210': {
            'type': 'arbitrary',
            'samples': [0.0] * 195 + [0.254468348] * 9,
            'is_overridable': False,
        },
        'gate_29_baked_wf_211': {
            'type': 'arbitrary',
            'samples': [0.0] * 194 + [-0.2081559] * 10,
            'is_overridable': False,
        },
        'gate_36_baked_wf_211': {
            'type': 'arbitrary',
            'samples': [0.0] * 194 + [0.254468348] * 10,
            'is_overridable': False,
        },
        'gate_29_baked_wf_212': {
            'type': 'arbitrary',
            'samples': [0.0] * 193 + [-0.2081559] * 11,
            'is_overridable': False,
        },
        'gate_36_baked_wf_212': {
            'type': 'arbitrary',
            'samples': [0.0] * 193 + [0.254468348] * 11,
            'is_overridable': False,
        },
        'gate_29_baked_wf_213': {
            'type': 'arbitrary',
            'samples': [0.0] * 192 + [-0.2081559] * 12,
            'is_overridable': False,
        },
        'gate_36_baked_wf_213': {
            'type': 'arbitrary',
            'samples': [0.0] * 192 + [0.254468348] * 12,
            'is_overridable': False,
        },
        'gate_29_baked_wf_214': {
            'type': 'arbitrary',
            'samples': [0.0] * 191 + [-0.2081559] * 13,
            'is_overridable': False,
        },
        'gate_36_baked_wf_214': {
            'type': 'arbitrary',
            'samples': [0.0] * 191 + [0.254468348] * 13,
            'is_overridable': False,
        },
        'gate_29_baked_wf_215': {
            'type': 'arbitrary',
            'samples': [0.0] * 190 + [-0.2081559] * 14,
            'is_overridable': False,
        },
        'gate_36_baked_wf_215': {
            'type': 'arbitrary',
            'samples': [0.0] * 190 + [0.254468348] * 14,
            'is_overridable': False,
        },
        'gate_29_baked_wf_216': {
            'type': 'arbitrary',
            'samples': [0.0] * 189 + [-0.2081559] * 15,
            'is_overridable': False,
        },
        'gate_36_baked_wf_216': {
            'type': 'arbitrary',
            'samples': [0.0] * 189 + [0.254468348] * 15,
            'is_overridable': False,
        },
        'gate_29_baked_wf_217': {
            'type': 'arbitrary',
            'samples': [0.0] * 188 + [-0.2081559] * 16,
            'is_overridable': False,
        },
        'gate_36_baked_wf_217': {
            'type': 'arbitrary',
            'samples': [0.0] * 188 + [0.254468348] * 16,
            'is_overridable': False,
        },
        'gate_29_baked_wf_218': {
            'type': 'arbitrary',
            'samples': [0.0] * 187 + [-0.2081559] * 17,
            'is_overridable': False,
        },
        'gate_36_baked_wf_218': {
            'type': 'arbitrary',
            'samples': [0.0] * 187 + [0.254468348] * 17,
            'is_overridable': False,
        },
        'gate_29_baked_wf_219': {
            'type': 'arbitrary',
            'samples': [0.0] * 186 + [-0.2081559] * 18,
            'is_overridable': False,
        },
        'gate_36_baked_wf_219': {
            'type': 'arbitrary',
            'samples': [0.0] * 186 + [0.254468348] * 18,
            'is_overridable': False,
        },
        'gate_29_baked_wf_220': {
            'type': 'arbitrary',
            'samples': [0.0] * 185 + [-0.2081559] * 19,
            'is_overridable': False,
        },
        'gate_36_baked_wf_220': {
            'type': 'arbitrary',
            'samples': [0.0] * 185 + [0.254468348] * 19,
            'is_overridable': False,
        },
        'gate_29_baked_wf_221': {
            'type': 'arbitrary',
            'samples': [0.0] * 184 + [-0.2081559] * 20,
            'is_overridable': False,
        },
        'gate_36_baked_wf_221': {
            'type': 'arbitrary',
            'samples': [0.0] * 184 + [0.254468348] * 20,
            'is_overridable': False,
        },
        'gate_29_baked_wf_222': {
            'type': 'arbitrary',
            'samples': [0.0] * 183 + [-0.2081559] * 21,
            'is_overridable': False,
        },
        'gate_36_baked_wf_222': {
            'type': 'arbitrary',
            'samples': [0.0] * 183 + [0.254468348] * 21,
            'is_overridable': False,
        },
        'gate_29_baked_wf_223': {
            'type': 'arbitrary',
            'samples': [0.0] * 182 + [-0.2081559] * 22,
            'is_overridable': False,
        },
        'gate_36_baked_wf_223': {
            'type': 'arbitrary',
            'samples': [0.0] * 182 + [0.254468348] * 22,
            'is_overridable': False,
        },
        'gate_29_baked_wf_224': {
            'type': 'arbitrary',
            'samples': [0.0] * 181 + [-0.2081559] * 23,
            'is_overridable': False,
        },
        'gate_36_baked_wf_224': {
            'type': 'arbitrary',
            'samples': [0.0] * 181 + [0.254468348] * 23,
            'is_overridable': False,
        },
        'gate_29_baked_wf_225': {
            'type': 'arbitrary',
            'samples': [0.0] * 180 + [-0.2081559] * 24,
            'is_overridable': False,
        },
        'gate_36_baked_wf_225': {
            'type': 'arbitrary',
            'samples': [0.0] * 180 + [0.254468348] * 24,
            'is_overridable': False,
        },
        'gate_29_baked_wf_226': {
            'type': 'arbitrary',
            'samples': [0.0] * 179 + [-0.2081559] * 25,
            'is_overridable': False,
        },
        'gate_36_baked_wf_226': {
            'type': 'arbitrary',
            'samples': [0.0] * 179 + [0.254468348] * 25,
            'is_overridable': False,
        },
        'gate_29_baked_wf_227': {
            'type': 'arbitrary',
            'samples': [0.0] * 178 + [-0.2081559] * 26,
            'is_overridable': False,
        },
        'gate_36_baked_wf_227': {
            'type': 'arbitrary',
            'samples': [0.0] * 178 + [0.254468348] * 26,
            'is_overridable': False,
        },
        'gate_29_baked_wf_228': {
            'type': 'arbitrary',
            'samples': [0.0] * 177 + [-0.2081559] * 27,
            'is_overridable': False,
        },
        'gate_36_baked_wf_228': {
            'type': 'arbitrary',
            'samples': [0.0] * 177 + [0.254468348] * 27,
            'is_overridable': False,
        },
        'gate_29_baked_wf_229': {
            'type': 'arbitrary',
            'samples': [0.0] * 176 + [-0.2081559] * 28,
            'is_overridable': False,
        },
        'gate_36_baked_wf_229': {
            'type': 'arbitrary',
            'samples': [0.0] * 176 + [0.254468348] * 28,
            'is_overridable': False,
        },
        'gate_29_baked_wf_230': {
            'type': 'arbitrary',
            'samples': [0.0] * 175 + [-0.2081559] * 29,
            'is_overridable': False,
        },
        'gate_36_baked_wf_230': {
            'type': 'arbitrary',
            'samples': [0.0] * 175 + [0.254468348] * 29,
            'is_overridable': False,
        },
        'gate_29_baked_wf_231': {
            'type': 'arbitrary',
            'samples': [0.0] * 174 + [-0.2081559] * 30,
            'is_overridable': False,
        },
        'gate_36_baked_wf_231': {
            'type': 'arbitrary',
            'samples': [0.0] * 174 + [0.254468348] * 30,
            'is_overridable': False,
        },
        'gate_29_baked_wf_232': {
            'type': 'arbitrary',
            'samples': [0.0] * 173 + [-0.2081559] * 31,
            'is_overridable': False,
        },
        'gate_36_baked_wf_232': {
            'type': 'arbitrary',
            'samples': [0.0] * 173 + [0.254468348] * 31,
            'is_overridable': False,
        },
        'gate_29_baked_wf_233': {
            'type': 'arbitrary',
            'samples': [0.0] * 172 + [-0.2081559] * 32,
            'is_overridable': False,
        },
        'gate_36_baked_wf_233': {
            'type': 'arbitrary',
            'samples': [0.0] * 172 + [0.254468348] * 32,
            'is_overridable': False,
        },
        'gate_29_baked_wf_234': {
            'type': 'arbitrary',
            'samples': [0.0] * 171 + [-0.2081559] * 33,
            'is_overridable': False,
        },
        'gate_36_baked_wf_234': {
            'type': 'arbitrary',
            'samples': [0.0] * 171 + [0.254468348] * 33,
            'is_overridable': False,
        },
        'gate_29_baked_wf_235': {
            'type': 'arbitrary',
            'samples': [0.0] * 170 + [-0.2081559] * 34,
            'is_overridable': False,
        },
        'gate_36_baked_wf_235': {
            'type': 'arbitrary',
            'samples': [0.0] * 170 + [0.254468348] * 34,
            'is_overridable': False,
        },
        'gate_29_baked_wf_236': {
            'type': 'arbitrary',
            'samples': [0.0] * 169 + [-0.2081559] * 35,
            'is_overridable': False,
        },
        'gate_36_baked_wf_236': {
            'type': 'arbitrary',
            'samples': [0.0] * 169 + [0.254468348] * 35,
            'is_overridable': False,
        },
        'gate_29_baked_wf_237': {
            'type': 'arbitrary',
            'samples': [0.0] * 168 + [-0.2081559] * 36,
            'is_overridable': False,
        },
        'gate_36_baked_wf_237': {
            'type': 'arbitrary',
            'samples': [0.0] * 168 + [0.254468348] * 36,
            'is_overridable': False,
        },
        'gate_29_baked_wf_238': {
            'type': 'arbitrary',
            'samples': [0.0] * 167 + [-0.2081559] * 37,
            'is_overridable': False,
        },
        'gate_36_baked_wf_238': {
            'type': 'arbitrary',
            'samples': [0.0] * 167 + [0.254468348] * 37,
            'is_overridable': False,
        },
        'gate_29_baked_wf_239': {
            'type': 'arbitrary',
            'samples': [0.0] * 166 + [-0.2081559] * 38,
            'is_overridable': False,
        },
        'gate_36_baked_wf_239': {
            'type': 'arbitrary',
            'samples': [0.0] * 166 + [0.254468348] * 38,
            'is_overridable': False,
        },
        'gate_29_baked_wf_240': {
            'type': 'arbitrary',
            'samples': [0.0] * 165 + [-0.2081559] * 39,
            'is_overridable': False,
        },
        'gate_36_baked_wf_240': {
            'type': 'arbitrary',
            'samples': [0.0] * 165 + [0.254468348] * 39,
            'is_overridable': False,
        },
        'gate_29_baked_wf_241': {
            'type': 'arbitrary',
            'samples': [0.0] * 164 + [-0.2081559] * 40,
            'is_overridable': False,
        },
        'gate_36_baked_wf_241': {
            'type': 'arbitrary',
            'samples': [0.0] * 164 + [0.254468348] * 40,
            'is_overridable': False,
        },
        'gate_29_baked_wf_242': {
            'type': 'arbitrary',
            'samples': [0.0] * 163 + [-0.2081559] * 41,
            'is_overridable': False,
        },
        'gate_36_baked_wf_242': {
            'type': 'arbitrary',
            'samples': [0.0] * 163 + [0.254468348] * 41,
            'is_overridable': False,
        },
        'gate_29_baked_wf_243': {
            'type': 'arbitrary',
            'samples': [0.0] * 162 + [-0.2081559] * 42,
            'is_overridable': False,
        },
        'gate_36_baked_wf_243': {
            'type': 'arbitrary',
            'samples': [0.0] * 162 + [0.254468348] * 42,
            'is_overridable': False,
        },
        'gate_29_baked_wf_244': {
            'type': 'arbitrary',
            'samples': [0.0] * 161 + [-0.2081559] * 43,
            'is_overridable': False,
        },
        'gate_36_baked_wf_244': {
            'type': 'arbitrary',
            'samples': [0.0] * 161 + [0.254468348] * 43,
            'is_overridable': False,
        },
        'gate_29_baked_wf_245': {
            'type': 'arbitrary',
            'samples': [0.0] * 160 + [-0.2081559] * 44,
            'is_overridable': False,
        },
        'gate_36_baked_wf_245': {
            'type': 'arbitrary',
            'samples': [0.0] * 160 + [0.254468348] * 44,
            'is_overridable': False,
        },
        'gate_29_baked_wf_246': {
            'type': 'arbitrary',
            'samples': [0.0] * 159 + [-0.2081559] * 45,
            'is_overridable': False,
        },
        'gate_36_baked_wf_246': {
            'type': 'arbitrary',
            'samples': [0.0] * 159 + [0.254468348] * 45,
            'is_overridable': False,
        },
        'gate_29_baked_wf_247': {
            'type': 'arbitrary',
            'samples': [0.0] * 158 + [-0.2081559] * 46,
            'is_overridable': False,
        },
        'gate_36_baked_wf_247': {
            'type': 'arbitrary',
            'samples': [0.0] * 158 + [0.254468348] * 46,
            'is_overridable': False,
        },
        'gate_29_baked_wf_248': {
            'type': 'arbitrary',
            'samples': [0.0] * 157 + [-0.2081559] * 47,
            'is_overridable': False,
        },
        'gate_36_baked_wf_248': {
            'type': 'arbitrary',
            'samples': [0.0] * 157 + [0.254468348] * 47,
            'is_overridable': False,
        },
        'gate_29_baked_wf_249': {
            'type': 'arbitrary',
            'samples': [0.0] * 156 + [-0.2081559] * 48,
            'is_overridable': False,
        },
        'gate_36_baked_wf_249': {
            'type': 'arbitrary',
            'samples': [0.0] * 156 + [0.254468348] * 48,
            'is_overridable': False,
        },
        'gate_29_baked_wf_250': {
            'type': 'arbitrary',
            'samples': [0.0] * 155 + [-0.2081559] * 49,
            'is_overridable': False,
        },
        'gate_36_baked_wf_250': {
            'type': 'arbitrary',
            'samples': [0.0] * 155 + [0.254468348] * 49,
            'is_overridable': False,
        },
        'gate_29_baked_wf_251': {
            'type': 'arbitrary',
            'samples': [0.0] * 154 + [-0.2081559] * 50,
            'is_overridable': False,
        },
        'gate_36_baked_wf_251': {
            'type': 'arbitrary',
            'samples': [0.0] * 154 + [0.254468348] * 50,
            'is_overridable': False,
        },
        'gate_29_baked_wf_252': {
            'type': 'arbitrary',
            'samples': [0.0] * 153 + [-0.2081559] * 51,
            'is_overridable': False,
        },
        'gate_36_baked_wf_252': {
            'type': 'arbitrary',
            'samples': [0.0] * 153 + [0.254468348] * 51,
            'is_overridable': False,
        },
        'gate_29_baked_wf_253': {
            'type': 'arbitrary',
            'samples': [0.0] * 152 + [-0.2081559] * 52,
            'is_overridable': False,
        },
        'gate_36_baked_wf_253': {
            'type': 'arbitrary',
            'samples': [0.0] * 152 + [0.254468348] * 52,
            'is_overridable': False,
        },
        'gate_29_baked_wf_254': {
            'type': 'arbitrary',
            'samples': [0.0] * 151 + [-0.2081559] * 53,
            'is_overridable': False,
        },
        'gate_36_baked_wf_254': {
            'type': 'arbitrary',
            'samples': [0.0] * 151 + [0.254468348] * 53,
            'is_overridable': False,
        },
        'gate_29_baked_wf_255': {
            'type': 'arbitrary',
            'samples': [0.0] * 150 + [-0.2081559] * 54,
            'is_overridable': False,
        },
        'gate_36_baked_wf_255': {
            'type': 'arbitrary',
            'samples': [0.0] * 150 + [0.254468348] * 54,
            'is_overridable': False,
        },
        'gate_29_baked_wf_256': {
            'type': 'arbitrary',
            'samples': [0.0] * 149 + [-0.2081559] * 55,
            'is_overridable': False,
        },
        'gate_36_baked_wf_256': {
            'type': 'arbitrary',
            'samples': [0.0] * 149 + [0.254468348] * 55,
            'is_overridable': False,
        },
        'gate_29_baked_wf_257': {
            'type': 'arbitrary',
            'samples': [0.0] * 148 + [-0.2081559] * 56,
            'is_overridable': False,
        },
        'gate_36_baked_wf_257': {
            'type': 'arbitrary',
            'samples': [0.0] * 148 + [0.254468348] * 56,
            'is_overridable': False,
        },
        'gate_29_baked_wf_258': {
            'type': 'arbitrary',
            'samples': [0.0] * 147 + [-0.2081559] * 57,
            'is_overridable': False,
        },
        'gate_36_baked_wf_258': {
            'type': 'arbitrary',
            'samples': [0.0] * 147 + [0.254468348] * 57,
            'is_overridable': False,
        },
        'gate_29_baked_wf_259': {
            'type': 'arbitrary',
            'samples': [0.0] * 146 + [-0.2081559] * 58,
            'is_overridable': False,
        },
        'gate_36_baked_wf_259': {
            'type': 'arbitrary',
            'samples': [0.0] * 146 + [0.254468348] * 58,
            'is_overridable': False,
        },
        'gate_29_baked_wf_260': {
            'type': 'arbitrary',
            'samples': [0.0] * 145 + [-0.2081559] * 59,
            'is_overridable': False,
        },
        'gate_36_baked_wf_260': {
            'type': 'arbitrary',
            'samples': [0.0] * 145 + [0.254468348] * 59,
            'is_overridable': False,
        },
        'gate_29_baked_wf_261': {
            'type': 'arbitrary',
            'samples': [0.0] * 144 + [-0.2081559] * 60,
            'is_overridable': False,
        },
        'gate_36_baked_wf_261': {
            'type': 'arbitrary',
            'samples': [0.0] * 144 + [0.254468348] * 60,
            'is_overridable': False,
        },
        'gate_29_baked_wf_262': {
            'type': 'arbitrary',
            'samples': [0.0] * 143 + [-0.2081559] * 61,
            'is_overridable': False,
        },
        'gate_36_baked_wf_262': {
            'type': 'arbitrary',
            'samples': [0.0] * 143 + [0.254468348] * 61,
            'is_overridable': False,
        },
        'gate_29_baked_wf_263': {
            'type': 'arbitrary',
            'samples': [0.0] * 142 + [-0.2081559] * 62,
            'is_overridable': False,
        },
        'gate_36_baked_wf_263': {
            'type': 'arbitrary',
            'samples': [0.0] * 142 + [0.254468348] * 62,
            'is_overridable': False,
        },
        'gate_29_baked_wf_264': {
            'type': 'arbitrary',
            'samples': [0.0] * 141 + [-0.2081559] * 63,
            'is_overridable': False,
        },
        'gate_36_baked_wf_264': {
            'type': 'arbitrary',
            'samples': [0.0] * 141 + [0.254468348] * 63,
            'is_overridable': False,
        },
        'gate_29_baked_wf_265': {
            'type': 'arbitrary',
            'samples': [0.0] * 140 + [-0.2081559] * 64,
            'is_overridable': False,
        },
        'gate_36_baked_wf_265': {
            'type': 'arbitrary',
            'samples': [0.0] * 140 + [0.254468348] * 64,
            'is_overridable': False,
        },
        'gate_29_baked_wf_266': {
            'type': 'arbitrary',
            'samples': [0.0] * 139 + [-0.2081559] * 65,
            'is_overridable': False,
        },
        'gate_36_baked_wf_266': {
            'type': 'arbitrary',
            'samples': [0.0] * 139 + [0.254468348] * 65,
            'is_overridable': False,
        },
        'gate_29_baked_wf_267': {
            'type': 'arbitrary',
            'samples': [0.0] * 138 + [-0.2081559] * 66,
            'is_overridable': False,
        },
        'gate_36_baked_wf_267': {
            'type': 'arbitrary',
            'samples': [0.0] * 138 + [0.254468348] * 66,
            'is_overridable': False,
        },
        'gate_29_baked_wf_268': {
            'type': 'arbitrary',
            'samples': [0.0] * 137 + [-0.2081559] * 67,
            'is_overridable': False,
        },
        'gate_36_baked_wf_268': {
            'type': 'arbitrary',
            'samples': [0.0] * 137 + [0.254468348] * 67,
            'is_overridable': False,
        },
        'gate_29_baked_wf_269': {
            'type': 'arbitrary',
            'samples': [0.0] * 136 + [-0.2081559] * 68,
            'is_overridable': False,
        },
        'gate_36_baked_wf_269': {
            'type': 'arbitrary',
            'samples': [0.0] * 136 + [0.254468348] * 68,
            'is_overridable': False,
        },
        'gate_29_baked_wf_270': {
            'type': 'arbitrary',
            'samples': [0.0] * 135 + [-0.2081559] * 69,
            'is_overridable': False,
        },
        'gate_36_baked_wf_270': {
            'type': 'arbitrary',
            'samples': [0.0] * 135 + [0.254468348] * 69,
            'is_overridable': False,
        },
        'gate_29_baked_wf_271': {
            'type': 'arbitrary',
            'samples': [0.0] * 134 + [-0.2081559] * 70,
            'is_overridable': False,
        },
        'gate_36_baked_wf_271': {
            'type': 'arbitrary',
            'samples': [0.0] * 134 + [0.254468348] * 70,
            'is_overridable': False,
        },
        'gate_29_baked_wf_272': {
            'type': 'arbitrary',
            'samples': [0.0] * 133 + [-0.2081559] * 71,
            'is_overridable': False,
        },
        'gate_36_baked_wf_272': {
            'type': 'arbitrary',
            'samples': [0.0] * 133 + [0.254468348] * 71,
            'is_overridable': False,
        },
        'gate_29_baked_wf_273': {
            'type': 'arbitrary',
            'samples': [0.0] * 132 + [-0.2081559] * 72,
            'is_overridable': False,
        },
        'gate_36_baked_wf_273': {
            'type': 'arbitrary',
            'samples': [0.0] * 132 + [0.254468348] * 72,
            'is_overridable': False,
        },
        'gate_29_baked_wf_274': {
            'type': 'arbitrary',
            'samples': [0.0] * 131 + [-0.2081559] * 73,
            'is_overridable': False,
        },
        'gate_36_baked_wf_274': {
            'type': 'arbitrary',
            'samples': [0.0] * 131 + [0.254468348] * 73,
            'is_overridable': False,
        },
        'gate_29_baked_wf_275': {
            'type': 'arbitrary',
            'samples': [0.0] * 130 + [-0.2081559] * 74,
            'is_overridable': False,
        },
        'gate_36_baked_wf_275': {
            'type': 'arbitrary',
            'samples': [0.0] * 130 + [0.254468348] * 74,
            'is_overridable': False,
        },
        'gate_29_baked_wf_276': {
            'type': 'arbitrary',
            'samples': [0.0] * 129 + [-0.2081559] * 75,
            'is_overridable': False,
        },
        'gate_36_baked_wf_276': {
            'type': 'arbitrary',
            'samples': [0.0] * 129 + [0.254468348] * 75,
            'is_overridable': False,
        },
        'gate_29_baked_wf_277': {
            'type': 'arbitrary',
            'samples': [0.0] * 128 + [-0.2081559] * 76,
            'is_overridable': False,
        },
        'gate_36_baked_wf_277': {
            'type': 'arbitrary',
            'samples': [0.0] * 128 + [0.254468348] * 76,
            'is_overridable': False,
        },
        'gate_29_baked_wf_278': {
            'type': 'arbitrary',
            'samples': [0.0] * 127 + [-0.2081559] * 77,
            'is_overridable': False,
        },
        'gate_36_baked_wf_278': {
            'type': 'arbitrary',
            'samples': [0.0] * 127 + [0.254468348] * 77,
            'is_overridable': False,
        },
        'gate_29_baked_wf_279': {
            'type': 'arbitrary',
            'samples': [0.0] * 126 + [-0.2081559] * 78,
            'is_overridable': False,
        },
        'gate_36_baked_wf_279': {
            'type': 'arbitrary',
            'samples': [0.0] * 126 + [0.254468348] * 78,
            'is_overridable': False,
        },
        'gate_29_baked_wf_280': {
            'type': 'arbitrary',
            'samples': [0.0] * 125 + [-0.2081559] * 79,
            'is_overridable': False,
        },
        'gate_36_baked_wf_280': {
            'type': 'arbitrary',
            'samples': [0.0] * 125 + [0.254468348] * 79,
            'is_overridable': False,
        },
        'gate_29_baked_wf_281': {
            'type': 'arbitrary',
            'samples': [0.0] * 124 + [-0.2081559] * 80,
            'is_overridable': False,
        },
        'gate_36_baked_wf_281': {
            'type': 'arbitrary',
            'samples': [0.0] * 124 + [0.254468348] * 80,
            'is_overridable': False,
        },
        'gate_29_baked_wf_282': {
            'type': 'arbitrary',
            'samples': [0.0] * 123 + [-0.2081559] * 81,
            'is_overridable': False,
        },
        'gate_36_baked_wf_282': {
            'type': 'arbitrary',
            'samples': [0.0] * 123 + [0.254468348] * 81,
            'is_overridable': False,
        },
        'gate_29_baked_wf_283': {
            'type': 'arbitrary',
            'samples': [0.0] * 122 + [-0.2081559] * 82,
            'is_overridable': False,
        },
        'gate_36_baked_wf_283': {
            'type': 'arbitrary',
            'samples': [0.0] * 122 + [0.254468348] * 82,
            'is_overridable': False,
        },
        'gate_29_baked_wf_284': {
            'type': 'arbitrary',
            'samples': [0.0] * 121 + [-0.2081559] * 83,
            'is_overridable': False,
        },
        'gate_36_baked_wf_284': {
            'type': 'arbitrary',
            'samples': [0.0] * 121 + [0.254468348] * 83,
            'is_overridable': False,
        },
        'gate_29_baked_wf_285': {
            'type': 'arbitrary',
            'samples': [0.0] * 120 + [-0.2081559] * 84,
            'is_overridable': False,
        },
        'gate_36_baked_wf_285': {
            'type': 'arbitrary',
            'samples': [0.0] * 120 + [0.254468348] * 84,
            'is_overridable': False,
        },
        'gate_29_baked_wf_286': {
            'type': 'arbitrary',
            'samples': [0.0] * 119 + [-0.2081559] * 85,
            'is_overridable': False,
        },
        'gate_36_baked_wf_286': {
            'type': 'arbitrary',
            'samples': [0.0] * 119 + [0.254468348] * 85,
            'is_overridable': False,
        },
        'gate_29_baked_wf_287': {
            'type': 'arbitrary',
            'samples': [0.0] * 118 + [-0.2081559] * 86,
            'is_overridable': False,
        },
        'gate_36_baked_wf_287': {
            'type': 'arbitrary',
            'samples': [0.0] * 118 + [0.254468348] * 86,
            'is_overridable': False,
        },
        'gate_29_baked_wf_288': {
            'type': 'arbitrary',
            'samples': [0.0] * 117 + [-0.2081559] * 87,
            'is_overridable': False,
        },
        'gate_36_baked_wf_288': {
            'type': 'arbitrary',
            'samples': [0.0] * 117 + [0.254468348] * 87,
            'is_overridable': False,
        },
        'gate_29_baked_wf_289': {
            'type': 'arbitrary',
            'samples': [0.0] * 116 + [-0.2081559] * 88,
            'is_overridable': False,
        },
        'gate_36_baked_wf_289': {
            'type': 'arbitrary',
            'samples': [0.0] * 116 + [0.254468348] * 88,
            'is_overridable': False,
        },
        'gate_29_baked_wf_290': {
            'type': 'arbitrary',
            'samples': [0.0] * 115 + [-0.2081559] * 89,
            'is_overridable': False,
        },
        'gate_36_baked_wf_290': {
            'type': 'arbitrary',
            'samples': [0.0] * 115 + [0.254468348] * 89,
            'is_overridable': False,
        },
        'gate_29_baked_wf_291': {
            'type': 'arbitrary',
            'samples': [0.0] * 114 + [-0.2081559] * 90,
            'is_overridable': False,
        },
        'gate_36_baked_wf_291': {
            'type': 'arbitrary',
            'samples': [0.0] * 114 + [0.254468348] * 90,
            'is_overridable': False,
        },
        'gate_29_baked_wf_292': {
            'type': 'arbitrary',
            'samples': [0.0] * 113 + [-0.2081559] * 91,
            'is_overridable': False,
        },
        'gate_36_baked_wf_292': {
            'type': 'arbitrary',
            'samples': [0.0] * 113 + [0.254468348] * 91,
            'is_overridable': False,
        },
        'gate_29_baked_wf_293': {
            'type': 'arbitrary',
            'samples': [0.0] * 112 + [-0.2081559] * 92,
            'is_overridable': False,
        },
        'gate_36_baked_wf_293': {
            'type': 'arbitrary',
            'samples': [0.0] * 112 + [0.254468348] * 92,
            'is_overridable': False,
        },
        'gate_29_baked_wf_294': {
            'type': 'arbitrary',
            'samples': [0.0] * 111 + [-0.2081559] * 93,
            'is_overridable': False,
        },
        'gate_36_baked_wf_294': {
            'type': 'arbitrary',
            'samples': [0.0] * 111 + [0.254468348] * 93,
            'is_overridable': False,
        },
        'gate_29_baked_wf_295': {
            'type': 'arbitrary',
            'samples': [0.0] * 110 + [-0.2081559] * 94,
            'is_overridable': False,
        },
        'gate_36_baked_wf_295': {
            'type': 'arbitrary',
            'samples': [0.0] * 110 + [0.254468348] * 94,
            'is_overridable': False,
        },
        'gate_29_baked_wf_296': {
            'type': 'arbitrary',
            'samples': [0.0] * 109 + [-0.2081559] * 95,
            'is_overridable': False,
        },
        'gate_36_baked_wf_296': {
            'type': 'arbitrary',
            'samples': [0.0] * 109 + [0.254468348] * 95,
            'is_overridable': False,
        },
        'gate_29_baked_wf_297': {
            'type': 'arbitrary',
            'samples': [0.0] * 108 + [-0.2081559] * 96,
            'is_overridable': False,
        },
        'gate_36_baked_wf_297': {
            'type': 'arbitrary',
            'samples': [0.0] * 108 + [0.254468348] * 96,
            'is_overridable': False,
        },
        'gate_29_baked_wf_298': {
            'type': 'arbitrary',
            'samples': [0.0] * 107 + [-0.2081559] * 97,
            'is_overridable': False,
        },
        'gate_36_baked_wf_298': {
            'type': 'arbitrary',
            'samples': [0.0] * 107 + [0.254468348] * 97,
            'is_overridable': False,
        },
        'gate_29_baked_wf_299': {
            'type': 'arbitrary',
            'samples': [0.0] * 106 + [-0.2081559] * 98,
            'is_overridable': False,
        },
        'gate_36_baked_wf_299': {
            'type': 'arbitrary',
            'samples': [0.0] * 106 + [0.254468348] * 98,
            'is_overridable': False,
        },
        'gate_29_baked_wf_300': {
            'type': 'arbitrary',
            'samples': [0.0] * 105 + [-0.2081559] * 99,
            'is_overridable': False,
        },
        'gate_36_baked_wf_300': {
            'type': 'arbitrary',
            'samples': [0.0] * 105 + [0.254468348] * 99,
            'is_overridable': False,
        },
        'gate_29_baked_wf_301': {
            'type': 'arbitrary',
            'samples': [0.0] * 104 + [-0.2081559] * 100,
            'is_overridable': False,
        },
        'gate_36_baked_wf_301': {
            'type': 'arbitrary',
            'samples': [0.0] * 104 + [0.254468348] * 100,
            'is_overridable': False,
        },
        'gate_29_baked_wf_302': {
            'type': 'arbitrary',
            'samples': [0.0] * 103 + [-0.2081559] * 101,
            'is_overridable': False,
        },
        'gate_36_baked_wf_302': {
            'type': 'arbitrary',
            'samples': [0.0] * 103 + [0.254468348] * 101,
            'is_overridable': False,
        },
        'gate_29_baked_wf_303': {
            'type': 'arbitrary',
            'samples': [0.0] * 102 + [-0.2081559] * 102,
            'is_overridable': False,
        },
        'gate_36_baked_wf_303': {
            'type': 'arbitrary',
            'samples': [0.0] * 102 + [0.254468348] * 102,
            'is_overridable': False,
        },
        'gate_29_baked_wf_304': {
            'type': 'arbitrary',
            'samples': [0.0] * 101 + [-0.2081559] * 103,
            'is_overridable': False,
        },
        'gate_36_baked_wf_304': {
            'type': 'arbitrary',
            'samples': [0.0] * 101 + [0.254468348] * 103,
            'is_overridable': False,
        },
        'gate_29_baked_wf_305': {
            'type': 'arbitrary',
            'samples': [0.0] * 100 + [-0.2081559] * 104,
            'is_overridable': False,
        },
        'gate_36_baked_wf_305': {
            'type': 'arbitrary',
            'samples': [0.0] * 100 + [0.254468348] * 104,
            'is_overridable': False,
        },
        'gate_29_baked_wf_306': {
            'type': 'arbitrary',
            'samples': [0.0] * 99 + [-0.2081559] * 105,
            'is_overridable': False,
        },
        'gate_36_baked_wf_306': {
            'type': 'arbitrary',
            'samples': [0.0] * 99 + [0.254468348] * 105,
            'is_overridable': False,
        },
        'gate_29_baked_wf_307': {
            'type': 'arbitrary',
            'samples': [0.0] * 98 + [-0.2081559] * 106,
            'is_overridable': False,
        },
        'gate_36_baked_wf_307': {
            'type': 'arbitrary',
            'samples': [0.0] * 98 + [0.254468348] * 106,
            'is_overridable': False,
        },
        'gate_29_baked_wf_308': {
            'type': 'arbitrary',
            'samples': [0.0] * 97 + [-0.2081559] * 107,
            'is_overridable': False,
        },
        'gate_36_baked_wf_308': {
            'type': 'arbitrary',
            'samples': [0.0] * 97 + [0.254468348] * 107,
            'is_overridable': False,
        },
        'gate_29_baked_wf_309': {
            'type': 'arbitrary',
            'samples': [0.0] * 96 + [-0.2081559] * 108,
            'is_overridable': False,
        },
        'gate_36_baked_wf_309': {
            'type': 'arbitrary',
            'samples': [0.0] * 96 + [0.254468348] * 108,
            'is_overridable': False,
        },
        'gate_29_baked_wf_310': {
            'type': 'arbitrary',
            'samples': [0.0] * 95 + [-0.2081559] * 109,
            'is_overridable': False,
        },
        'gate_36_baked_wf_310': {
            'type': 'arbitrary',
            'samples': [0.0] * 95 + [0.254468348] * 109,
            'is_overridable': False,
        },
        'gate_29_baked_wf_311': {
            'type': 'arbitrary',
            'samples': [0.0] * 94 + [-0.2081559] * 110,
            'is_overridable': False,
        },
        'gate_36_baked_wf_311': {
            'type': 'arbitrary',
            'samples': [0.0] * 94 + [0.254468348] * 110,
            'is_overridable': False,
        },
        'gate_29_baked_wf_312': {
            'type': 'arbitrary',
            'samples': [0.0] * 93 + [-0.2081559] * 111,
            'is_overridable': False,
        },
        'gate_36_baked_wf_312': {
            'type': 'arbitrary',
            'samples': [0.0] * 93 + [0.254468348] * 111,
            'is_overridable': False,
        },
        'gate_29_baked_wf_313': {
            'type': 'arbitrary',
            'samples': [0.0] * 92 + [-0.2081559] * 112,
            'is_overridable': False,
        },
        'gate_36_baked_wf_313': {
            'type': 'arbitrary',
            'samples': [0.0] * 92 + [0.254468348] * 112,
            'is_overridable': False,
        },
        'gate_29_baked_wf_314': {
            'type': 'arbitrary',
            'samples': [0.0] * 91 + [-0.2081559] * 113,
            'is_overridable': False,
        },
        'gate_36_baked_wf_314': {
            'type': 'arbitrary',
            'samples': [0.0] * 91 + [0.254468348] * 113,
            'is_overridable': False,
        },
        'gate_29_baked_wf_315': {
            'type': 'arbitrary',
            'samples': [0.0] * 90 + [-0.2081559] * 114,
            'is_overridable': False,
        },
        'gate_36_baked_wf_315': {
            'type': 'arbitrary',
            'samples': [0.0] * 90 + [0.254468348] * 114,
            'is_overridable': False,
        },
        'gate_29_baked_wf_316': {
            'type': 'arbitrary',
            'samples': [0.0] * 89 + [-0.2081559] * 115,
            'is_overridable': False,
        },
        'gate_36_baked_wf_316': {
            'type': 'arbitrary',
            'samples': [0.0] * 89 + [0.254468348] * 115,
            'is_overridable': False,
        },
        'gate_29_baked_wf_317': {
            'type': 'arbitrary',
            'samples': [0.0] * 88 + [-0.2081559] * 116,
            'is_overridable': False,
        },
        'gate_36_baked_wf_317': {
            'type': 'arbitrary',
            'samples': [0.0] * 88 + [0.254468348] * 116,
            'is_overridable': False,
        },
        'gate_29_baked_wf_318': {
            'type': 'arbitrary',
            'samples': [0.0] * 87 + [-0.2081559] * 117,
            'is_overridable': False,
        },
        'gate_36_baked_wf_318': {
            'type': 'arbitrary',
            'samples': [0.0] * 87 + [0.254468348] * 117,
            'is_overridable': False,
        },
        'gate_29_baked_wf_319': {
            'type': 'arbitrary',
            'samples': [0.0] * 86 + [-0.2081559] * 118,
            'is_overridable': False,
        },
        'gate_36_baked_wf_319': {
            'type': 'arbitrary',
            'samples': [0.0] * 86 + [0.254468348] * 118,
            'is_overridable': False,
        },
        'gate_29_baked_wf_320': {
            'type': 'arbitrary',
            'samples': [0.0] * 85 + [-0.2081559] * 119,
            'is_overridable': False,
        },
        'gate_36_baked_wf_320': {
            'type': 'arbitrary',
            'samples': [0.0] * 85 + [0.254468348] * 119,
            'is_overridable': False,
        },
        'gate_29_baked_wf_321': {
            'type': 'arbitrary',
            'samples': [0.0] * 84 + [-0.2081559] * 120,
            'is_overridable': False,
        },
        'gate_36_baked_wf_321': {
            'type': 'arbitrary',
            'samples': [0.0] * 84 + [0.254468348] * 120,
            'is_overridable': False,
        },
        'gate_29_baked_wf_322': {
            'type': 'arbitrary',
            'samples': [0.0] * 83 + [-0.2081559] * 121,
            'is_overridable': False,
        },
        'gate_36_baked_wf_322': {
            'type': 'arbitrary',
            'samples': [0.0] * 83 + [0.254468348] * 121,
            'is_overridable': False,
        },
        'gate_29_baked_wf_323': {
            'type': 'arbitrary',
            'samples': [0.0] * 82 + [-0.2081559] * 122,
            'is_overridable': False,
        },
        'gate_36_baked_wf_323': {
            'type': 'arbitrary',
            'samples': [0.0] * 82 + [0.254468348] * 122,
            'is_overridable': False,
        },
        'gate_29_baked_wf_324': {
            'type': 'arbitrary',
            'samples': [0.0] * 81 + [-0.2081559] * 123,
            'is_overridable': False,
        },
        'gate_36_baked_wf_324': {
            'type': 'arbitrary',
            'samples': [0.0] * 81 + [0.254468348] * 123,
            'is_overridable': False,
        },
        'gate_29_baked_wf_325': {
            'type': 'arbitrary',
            'samples': [0.0] * 80 + [-0.2081559] * 124,
            'is_overridable': False,
        },
        'gate_36_baked_wf_325': {
            'type': 'arbitrary',
            'samples': [0.0] * 80 + [0.254468348] * 124,
            'is_overridable': False,
        },
        'gate_29_baked_wf_326': {
            'type': 'arbitrary',
            'samples': [0.0] * 79 + [-0.2081559] * 125,
            'is_overridable': False,
        },
        'gate_36_baked_wf_326': {
            'type': 'arbitrary',
            'samples': [0.0] * 79 + [0.254468348] * 125,
            'is_overridable': False,
        },
        'gate_29_baked_wf_327': {
            'type': 'arbitrary',
            'samples': [0.0] * 78 + [-0.2081559] * 126,
            'is_overridable': False,
        },
        'gate_36_baked_wf_327': {
            'type': 'arbitrary',
            'samples': [0.0] * 78 + [0.254468348] * 126,
            'is_overridable': False,
        },
        'gate_29_baked_wf_328': {
            'type': 'arbitrary',
            'samples': [0.0] * 77 + [-0.2081559] * 127,
            'is_overridable': False,
        },
        'gate_36_baked_wf_328': {
            'type': 'arbitrary',
            'samples': [0.0] * 77 + [0.254468348] * 127,
            'is_overridable': False,
        },
        'gate_29_baked_wf_329': {
            'type': 'arbitrary',
            'samples': [0.0] * 76 + [-0.2081559] * 128,
            'is_overridable': False,
        },
        'gate_36_baked_wf_329': {
            'type': 'arbitrary',
            'samples': [0.0] * 76 + [0.254468348] * 128,
            'is_overridable': False,
        },
        'gate_29_baked_wf_330': {
            'type': 'arbitrary',
            'samples': [0.0] * 75 + [-0.2081559] * 129,
            'is_overridable': False,
        },
        'gate_36_baked_wf_330': {
            'type': 'arbitrary',
            'samples': [0.0] * 75 + [0.254468348] * 129,
            'is_overridable': False,
        },
        'gate_29_baked_wf_331': {
            'type': 'arbitrary',
            'samples': [0.0] * 74 + [-0.2081559] * 130,
            'is_overridable': False,
        },
        'gate_36_baked_wf_331': {
            'type': 'arbitrary',
            'samples': [0.0] * 74 + [0.254468348] * 130,
            'is_overridable': False,
        },
        'gate_29_baked_wf_332': {
            'type': 'arbitrary',
            'samples': [0.0] * 73 + [-0.2081559] * 131,
            'is_overridable': False,
        },
        'gate_36_baked_wf_332': {
            'type': 'arbitrary',
            'samples': [0.0] * 73 + [0.254468348] * 131,
            'is_overridable': False,
        },
        'gate_29_baked_wf_333': {
            'type': 'arbitrary',
            'samples': [0.0] * 72 + [-0.2081559] * 132,
            'is_overridable': False,
        },
        'gate_36_baked_wf_333': {
            'type': 'arbitrary',
            'samples': [0.0] * 72 + [0.254468348] * 132,
            'is_overridable': False,
        },
        'gate_29_baked_wf_334': {
            'type': 'arbitrary',
            'samples': [0.0] * 71 + [-0.2081559] * 133,
            'is_overridable': False,
        },
        'gate_36_baked_wf_334': {
            'type': 'arbitrary',
            'samples': [0.0] * 71 + [0.254468348] * 133,
            'is_overridable': False,
        },
        'gate_29_baked_wf_335': {
            'type': 'arbitrary',
            'samples': [0.0] * 70 + [-0.2081559] * 134,
            'is_overridable': False,
        },
        'gate_36_baked_wf_335': {
            'type': 'arbitrary',
            'samples': [0.0] * 70 + [0.254468348] * 134,
            'is_overridable': False,
        },
        'gate_29_baked_wf_336': {
            'type': 'arbitrary',
            'samples': [0.0] * 69 + [-0.2081559] * 135,
            'is_overridable': False,
        },
        'gate_36_baked_wf_336': {
            'type': 'arbitrary',
            'samples': [0.0] * 69 + [0.254468348] * 135,
            'is_overridable': False,
        },
        'gate_29_baked_wf_337': {
            'type': 'arbitrary',
            'samples': [0.0] * 68 + [-0.2081559] * 136,
            'is_overridable': False,
        },
        'gate_36_baked_wf_337': {
            'type': 'arbitrary',
            'samples': [0.0] * 68 + [0.254468348] * 136,
            'is_overridable': False,
        },
        'gate_29_baked_wf_338': {
            'type': 'arbitrary',
            'samples': [0.0] * 67 + [-0.2081559] * 137,
            'is_overridable': False,
        },
        'gate_36_baked_wf_338': {
            'type': 'arbitrary',
            'samples': [0.0] * 67 + [0.254468348] * 137,
            'is_overridable': False,
        },
        'gate_29_baked_wf_339': {
            'type': 'arbitrary',
            'samples': [0.0] * 66 + [-0.2081559] * 138,
            'is_overridable': False,
        },
        'gate_36_baked_wf_339': {
            'type': 'arbitrary',
            'samples': [0.0] * 66 + [0.254468348] * 138,
            'is_overridable': False,
        },
        'gate_29_baked_wf_340': {
            'type': 'arbitrary',
            'samples': [0.0] * 65 + [-0.2081559] * 139,
            'is_overridable': False,
        },
        'gate_36_baked_wf_340': {
            'type': 'arbitrary',
            'samples': [0.0] * 65 + [0.254468348] * 139,
            'is_overridable': False,
        },
        'gate_29_baked_wf_341': {
            'type': 'arbitrary',
            'samples': [0.0] * 64 + [-0.2081559] * 140,
            'is_overridable': False,
        },
        'gate_36_baked_wf_341': {
            'type': 'arbitrary',
            'samples': [0.0] * 64 + [0.254468348] * 140,
            'is_overridable': False,
        },
        'gate_29_baked_wf_342': {
            'type': 'arbitrary',
            'samples': [0.0] * 63 + [-0.2081559] * 141,
            'is_overridable': False,
        },
        'gate_36_baked_wf_342': {
            'type': 'arbitrary',
            'samples': [0.0] * 63 + [0.254468348] * 141,
            'is_overridable': False,
        },
        'gate_29_baked_wf_343': {
            'type': 'arbitrary',
            'samples': [0.0] * 62 + [-0.2081559] * 142,
            'is_overridable': False,
        },
        'gate_36_baked_wf_343': {
            'type': 'arbitrary',
            'samples': [0.0] * 62 + [0.254468348] * 142,
            'is_overridable': False,
        },
        'gate_29_baked_wf_344': {
            'type': 'arbitrary',
            'samples': [0.0] * 61 + [-0.2081559] * 143,
            'is_overridable': False,
        },
        'gate_36_baked_wf_344': {
            'type': 'arbitrary',
            'samples': [0.0] * 61 + [0.254468348] * 143,
            'is_overridable': False,
        },
        'gate_29_baked_wf_345': {
            'type': 'arbitrary',
            'samples': [0.0] * 60 + [-0.2081559] * 144,
            'is_overridable': False,
        },
        'gate_36_baked_wf_345': {
            'type': 'arbitrary',
            'samples': [0.0] * 60 + [0.254468348] * 144,
            'is_overridable': False,
        },
        'gate_29_baked_wf_346': {
            'type': 'arbitrary',
            'samples': [0.0] * 59 + [-0.2081559] * 145,
            'is_overridable': False,
        },
        'gate_36_baked_wf_346': {
            'type': 'arbitrary',
            'samples': [0.0] * 59 + [0.254468348] * 145,
            'is_overridable': False,
        },
        'gate_29_baked_wf_347': {
            'type': 'arbitrary',
            'samples': [0.0] * 58 + [-0.2081559] * 146,
            'is_overridable': False,
        },
        'gate_36_baked_wf_347': {
            'type': 'arbitrary',
            'samples': [0.0] * 58 + [0.254468348] * 146,
            'is_overridable': False,
        },
        'gate_29_baked_wf_348': {
            'type': 'arbitrary',
            'samples': [0.0] * 57 + [-0.2081559] * 147,
            'is_overridable': False,
        },
        'gate_36_baked_wf_348': {
            'type': 'arbitrary',
            'samples': [0.0] * 57 + [0.254468348] * 147,
            'is_overridable': False,
        },
        'gate_29_baked_wf_349': {
            'type': 'arbitrary',
            'samples': [0.0] * 56 + [-0.2081559] * 148,
            'is_overridable': False,
        },
        'gate_36_baked_wf_349': {
            'type': 'arbitrary',
            'samples': [0.0] * 56 + [0.254468348] * 148,
            'is_overridable': False,
        },
        'gate_29_baked_wf_350': {
            'type': 'arbitrary',
            'samples': [0.0] * 55 + [-0.2081559] * 149,
            'is_overridable': False,
        },
        'gate_36_baked_wf_350': {
            'type': 'arbitrary',
            'samples': [0.0] * 55 + [0.254468348] * 149,
            'is_overridable': False,
        },
        'gate_29_baked_wf_351': {
            'type': 'arbitrary',
            'samples': [0.0] * 54 + [-0.2081559] * 150,
            'is_overridable': False,
        },
        'gate_36_baked_wf_351': {
            'type': 'arbitrary',
            'samples': [0.0] * 54 + [0.254468348] * 150,
            'is_overridable': False,
        },
        'gate_29_baked_wf_352': {
            'type': 'arbitrary',
            'samples': [0.0] * 53 + [-0.2081559] * 151,
            'is_overridable': False,
        },
        'gate_36_baked_wf_352': {
            'type': 'arbitrary',
            'samples': [0.0] * 53 + [0.254468348] * 151,
            'is_overridable': False,
        },
        'gate_29_baked_wf_353': {
            'type': 'arbitrary',
            'samples': [0.0] * 52 + [-0.2081559] * 152,
            'is_overridable': False,
        },
        'gate_36_baked_wf_353': {
            'type': 'arbitrary',
            'samples': [0.0] * 52 + [0.254468348] * 152,
            'is_overridable': False,
        },
        'gate_29_baked_wf_354': {
            'type': 'arbitrary',
            'samples': [0.0] * 51 + [-0.2081559] * 153,
            'is_overridable': False,
        },
        'gate_36_baked_wf_354': {
            'type': 'arbitrary',
            'samples': [0.0] * 51 + [0.254468348] * 153,
            'is_overridable': False,
        },
        'gate_29_baked_wf_355': {
            'type': 'arbitrary',
            'samples': [0.0] * 50 + [-0.2081559] * 154,
            'is_overridable': False,
        },
        'gate_36_baked_wf_355': {
            'type': 'arbitrary',
            'samples': [0.0] * 50 + [0.254468348] * 154,
            'is_overridable': False,
        },
        'gate_29_baked_wf_356': {
            'type': 'arbitrary',
            'samples': [0.0] * 49 + [-0.2081559] * 155,
            'is_overridable': False,
        },
        'gate_36_baked_wf_356': {
            'type': 'arbitrary',
            'samples': [0.0] * 49 + [0.254468348] * 155,
            'is_overridable': False,
        },
        'gate_29_baked_wf_357': {
            'type': 'arbitrary',
            'samples': [0.0] * 48 + [-0.2081559] * 156,
            'is_overridable': False,
        },
        'gate_36_baked_wf_357': {
            'type': 'arbitrary',
            'samples': [0.0] * 48 + [0.254468348] * 156,
            'is_overridable': False,
        },
        'gate_29_baked_wf_358': {
            'type': 'arbitrary',
            'samples': [0.0] * 47 + [-0.2081559] * 157,
            'is_overridable': False,
        },
        'gate_36_baked_wf_358': {
            'type': 'arbitrary',
            'samples': [0.0] * 47 + [0.254468348] * 157,
            'is_overridable': False,
        },
        'gate_29_baked_wf_359': {
            'type': 'arbitrary',
            'samples': [0.0] * 46 + [-0.2081559] * 158,
            'is_overridable': False,
        },
        'gate_36_baked_wf_359': {
            'type': 'arbitrary',
            'samples': [0.0] * 46 + [0.254468348] * 158,
            'is_overridable': False,
        },
        'gate_29_baked_wf_360': {
            'type': 'arbitrary',
            'samples': [0.0] * 45 + [-0.2081559] * 159,
            'is_overridable': False,
        },
        'gate_36_baked_wf_360': {
            'type': 'arbitrary',
            'samples': [0.0] * 45 + [0.254468348] * 159,
            'is_overridable': False,
        },
        'gate_29_baked_wf_361': {
            'type': 'arbitrary',
            'samples': [0.0] * 44 + [-0.2081559] * 160,
            'is_overridable': False,
        },
        'gate_36_baked_wf_361': {
            'type': 'arbitrary',
            'samples': [0.0] * 44 + [0.254468348] * 160,
            'is_overridable': False,
        },
        'gate_29_baked_wf_362': {
            'type': 'arbitrary',
            'samples': [0.0] * 43 + [-0.2081559] * 161,
            'is_overridable': False,
        },
        'gate_36_baked_wf_362': {
            'type': 'arbitrary',
            'samples': [0.0] * 43 + [0.254468348] * 161,
            'is_overridable': False,
        },
        'gate_29_baked_wf_363': {
            'type': 'arbitrary',
            'samples': [0.0] * 42 + [-0.2081559] * 162,
            'is_overridable': False,
        },
        'gate_36_baked_wf_363': {
            'type': 'arbitrary',
            'samples': [0.0] * 42 + [0.254468348] * 162,
            'is_overridable': False,
        },
        'gate_29_baked_wf_364': {
            'type': 'arbitrary',
            'samples': [0.0] * 41 + [-0.2081559] * 163,
            'is_overridable': False,
        },
        'gate_36_baked_wf_364': {
            'type': 'arbitrary',
            'samples': [0.0] * 41 + [0.254468348] * 163,
            'is_overridable': False,
        },
        'gate_29_baked_wf_365': {
            'type': 'arbitrary',
            'samples': [0.0] * 40 + [-0.2081559] * 164,
            'is_overridable': False,
        },
        'gate_36_baked_wf_365': {
            'type': 'arbitrary',
            'samples': [0.0] * 40 + [0.254468348] * 164,
            'is_overridable': False,
        },
        'gate_29_baked_wf_366': {
            'type': 'arbitrary',
            'samples': [0.0] * 39 + [-0.2081559] * 165,
            'is_overridable': False,
        },
        'gate_36_baked_wf_366': {
            'type': 'arbitrary',
            'samples': [0.0] * 39 + [0.254468348] * 165,
            'is_overridable': False,
        },
        'gate_29_baked_wf_367': {
            'type': 'arbitrary',
            'samples': [0.0] * 38 + [-0.2081559] * 166,
            'is_overridable': False,
        },
        'gate_36_baked_wf_367': {
            'type': 'arbitrary',
            'samples': [0.0] * 38 + [0.254468348] * 166,
            'is_overridable': False,
        },
        'gate_29_baked_wf_368': {
            'type': 'arbitrary',
            'samples': [0.0] * 37 + [-0.2081559] * 167,
            'is_overridable': False,
        },
        'gate_36_baked_wf_368': {
            'type': 'arbitrary',
            'samples': [0.0] * 37 + [0.254468348] * 167,
            'is_overridable': False,
        },
        'gate_29_baked_wf_369': {
            'type': 'arbitrary',
            'samples': [0.0] * 36 + [-0.2081559] * 168,
            'is_overridable': False,
        },
        'gate_36_baked_wf_369': {
            'type': 'arbitrary',
            'samples': [0.0] * 36 + [0.254468348] * 168,
            'is_overridable': False,
        },
        'gate_29_baked_wf_370': {
            'type': 'arbitrary',
            'samples': [0.0] * 35 + [-0.2081559] * 169,
            'is_overridable': False,
        },
        'gate_36_baked_wf_370': {
            'type': 'arbitrary',
            'samples': [0.0] * 35 + [0.254468348] * 169,
            'is_overridable': False,
        },
        'gate_29_baked_wf_371': {
            'type': 'arbitrary',
            'samples': [0.0] * 34 + [-0.2081559] * 170,
            'is_overridable': False,
        },
        'gate_36_baked_wf_371': {
            'type': 'arbitrary',
            'samples': [0.0] * 34 + [0.254468348] * 170,
            'is_overridable': False,
        },
        'gate_29_baked_wf_372': {
            'type': 'arbitrary',
            'samples': [0.0] * 33 + [-0.2081559] * 171,
            'is_overridable': False,
        },
        'gate_36_baked_wf_372': {
            'type': 'arbitrary',
            'samples': [0.0] * 33 + [0.254468348] * 171,
            'is_overridable': False,
        },
        'gate_29_baked_wf_373': {
            'type': 'arbitrary',
            'samples': [0.0] * 32 + [-0.2081559] * 172,
            'is_overridable': False,
        },
        'gate_36_baked_wf_373': {
            'type': 'arbitrary',
            'samples': [0.0] * 32 + [0.254468348] * 172,
            'is_overridable': False,
        },
        'gate_29_baked_wf_374': {
            'type': 'arbitrary',
            'samples': [0.0] * 31 + [-0.2081559] * 173,
            'is_overridable': False,
        },
        'gate_36_baked_wf_374': {
            'type': 'arbitrary',
            'samples': [0.0] * 31 + [0.254468348] * 173,
            'is_overridable': False,
        },
        'gate_29_baked_wf_375': {
            'type': 'arbitrary',
            'samples': [0.0] * 30 + [-0.2081559] * 174,
            'is_overridable': False,
        },
        'gate_36_baked_wf_375': {
            'type': 'arbitrary',
            'samples': [0.0] * 30 + [0.254468348] * 174,
            'is_overridable': False,
        },
        'gate_29_baked_wf_376': {
            'type': 'arbitrary',
            'samples': [0.0] * 29 + [-0.2081559] * 175,
            'is_overridable': False,
        },
        'gate_36_baked_wf_376': {
            'type': 'arbitrary',
            'samples': [0.0] * 29 + [0.254468348] * 175,
            'is_overridable': False,
        },
        'gate_29_baked_wf_377': {
            'type': 'arbitrary',
            'samples': [0.0] * 28 + [-0.2081559] * 176,
            'is_overridable': False,
        },
        'gate_36_baked_wf_377': {
            'type': 'arbitrary',
            'samples': [0.0] * 28 + [0.254468348] * 176,
            'is_overridable': False,
        },
        'gate_29_baked_wf_378': {
            'type': 'arbitrary',
            'samples': [0.0] * 27 + [-0.2081559] * 177,
            'is_overridable': False,
        },
        'gate_36_baked_wf_378': {
            'type': 'arbitrary',
            'samples': [0.0] * 27 + [0.254468348] * 177,
            'is_overridable': False,
        },
        'gate_29_baked_wf_379': {
            'type': 'arbitrary',
            'samples': [0.0] * 26 + [-0.2081559] * 178,
            'is_overridable': False,
        },
        'gate_36_baked_wf_379': {
            'type': 'arbitrary',
            'samples': [0.0] * 26 + [0.254468348] * 178,
            'is_overridable': False,
        },
        'gate_29_baked_wf_380': {
            'type': 'arbitrary',
            'samples': [0.0] * 25 + [-0.2081559] * 179,
            'is_overridable': False,
        },
        'gate_36_baked_wf_380': {
            'type': 'arbitrary',
            'samples': [0.0] * 25 + [0.254468348] * 179,
            'is_overridable': False,
        },
        'gate_29_baked_wf_381': {
            'type': 'arbitrary',
            'samples': [0.0] * 24 + [-0.2081559] * 180,
            'is_overridable': False,
        },
        'gate_36_baked_wf_381': {
            'type': 'arbitrary',
            'samples': [0.0] * 24 + [0.254468348] * 180,
            'is_overridable': False,
        },
        'gate_29_baked_wf_382': {
            'type': 'arbitrary',
            'samples': [0.0] * 23 + [-0.2081559] * 181,
            'is_overridable': False,
        },
        'gate_36_baked_wf_382': {
            'type': 'arbitrary',
            'samples': [0.0] * 23 + [0.254468348] * 181,
            'is_overridable': False,
        },
        'gate_29_baked_wf_383': {
            'type': 'arbitrary',
            'samples': [0.0] * 22 + [-0.2081559] * 182,
            'is_overridable': False,
        },
        'gate_36_baked_wf_383': {
            'type': 'arbitrary',
            'samples': [0.0] * 22 + [0.254468348] * 182,
            'is_overridable': False,
        },
        'gate_29_baked_wf_384': {
            'type': 'arbitrary',
            'samples': [0.0] * 21 + [-0.2081559] * 183,
            'is_overridable': False,
        },
        'gate_36_baked_wf_384': {
            'type': 'arbitrary',
            'samples': [0.0] * 21 + [0.254468348] * 183,
            'is_overridable': False,
        },
        'gate_29_baked_wf_385': {
            'type': 'arbitrary',
            'samples': [0.0] * 20 + [-0.2081559] * 184,
            'is_overridable': False,
        },
        'gate_36_baked_wf_385': {
            'type': 'arbitrary',
            'samples': [0.0] * 20 + [0.254468348] * 184,
            'is_overridable': False,
        },
        'gate_29_baked_wf_386': {
            'type': 'arbitrary',
            'samples': [0.0] * 19 + [-0.2081559] * 185,
            'is_overridable': False,
        },
        'gate_36_baked_wf_386': {
            'type': 'arbitrary',
            'samples': [0.0] * 19 + [0.254468348] * 185,
            'is_overridable': False,
        },
        'gate_29_baked_wf_387': {
            'type': 'arbitrary',
            'samples': [0.0] * 18 + [-0.2081559] * 186,
            'is_overridable': False,
        },
        'gate_36_baked_wf_387': {
            'type': 'arbitrary',
            'samples': [0.0] * 18 + [0.254468348] * 186,
            'is_overridable': False,
        },
        'gate_29_baked_wf_388': {
            'type': 'arbitrary',
            'samples': [0.0] * 17 + [-0.2081559] * 187,
            'is_overridable': False,
        },
        'gate_36_baked_wf_388': {
            'type': 'arbitrary',
            'samples': [0.0] * 17 + [0.254468348] * 187,
            'is_overridable': False,
        },
        'gate_29_baked_wf_389': {
            'type': 'arbitrary',
            'samples': [0.0] * 16 + [-0.2081559] * 188,
            'is_overridable': False,
        },
        'gate_36_baked_wf_389': {
            'type': 'arbitrary',
            'samples': [0.0] * 16 + [0.254468348] * 188,
            'is_overridable': False,
        },
        'gate_29_baked_wf_390': {
            'type': 'arbitrary',
            'samples': [0.0] * 15 + [-0.2081559] * 189,
            'is_overridable': False,
        },
        'gate_36_baked_wf_390': {
            'type': 'arbitrary',
            'samples': [0.0] * 15 + [0.254468348] * 189,
            'is_overridable': False,
        },
        'gate_29_baked_wf_391': {
            'type': 'arbitrary',
            'samples': [0.0] * 14 + [-0.2081559] * 190,
            'is_overridable': False,
        },
        'gate_36_baked_wf_391': {
            'type': 'arbitrary',
            'samples': [0.0] * 14 + [0.254468348] * 190,
            'is_overridable': False,
        },
        'gate_29_baked_wf_392': {
            'type': 'arbitrary',
            'samples': [0.0] * 13 + [-0.2081559] * 191,
            'is_overridable': False,
        },
        'gate_36_baked_wf_392': {
            'type': 'arbitrary',
            'samples': [0.0] * 13 + [0.254468348] * 191,
            'is_overridable': False,
        },
        'gate_29_baked_wf_393': {
            'type': 'arbitrary',
            'samples': [0.0] * 12 + [-0.2081559] * 192,
            'is_overridable': False,
        },
        'gate_36_baked_wf_393': {
            'type': 'arbitrary',
            'samples': [0.0] * 12 + [0.254468348] * 192,
            'is_overridable': False,
        },
        'gate_29_baked_wf_394': {
            'type': 'arbitrary',
            'samples': [0.0] * 11 + [-0.2081559] * 193,
            'is_overridable': False,
        },
        'gate_36_baked_wf_394': {
            'type': 'arbitrary',
            'samples': [0.0] * 11 + [0.254468348] * 193,
            'is_overridable': False,
        },
        'gate_29_baked_wf_395': {
            'type': 'arbitrary',
            'samples': [0.0] * 10 + [-0.2081559] * 194,
            'is_overridable': False,
        },
        'gate_36_baked_wf_395': {
            'type': 'arbitrary',
            'samples': [0.0] * 10 + [0.254468348] * 194,
            'is_overridable': False,
        },
        'gate_29_baked_wf_396': {
            'type': 'arbitrary',
            'samples': [0.0] * 9 + [-0.2081559] * 195,
            'is_overridable': False,
        },
        'gate_36_baked_wf_396': {
            'type': 'arbitrary',
            'samples': [0.0] * 9 + [0.254468348] * 195,
            'is_overridable': False,
        },
        'gate_29_baked_wf_397': {
            'type': 'arbitrary',
            'samples': [0.0] * 8 + [-0.2081559] * 196,
            'is_overridable': False,
        },
        'gate_36_baked_wf_397': {
            'type': 'arbitrary',
            'samples': [0.0] * 8 + [0.254468348] * 196,
            'is_overridable': False,
        },
        'gate_29_baked_wf_398': {
            'type': 'arbitrary',
            'samples': [0.0] * 7 + [-0.2081559] * 197,
            'is_overridable': False,
        },
        'gate_36_baked_wf_398': {
            'type': 'arbitrary',
            'samples': [0.0] * 7 + [0.254468348] * 197,
            'is_overridable': False,
        },
        'gate_29_baked_wf_399': {
            'type': 'arbitrary',
            'samples': [0.0] * 6 + [-0.2081559] * 198,
            'is_overridable': False,
        },
        'gate_36_baked_wf_399': {
            'type': 'arbitrary',
            'samples': [0.0] * 6 + [0.254468348] * 198,
            'is_overridable': False,
        },
        'gate_29_baked_wf_400': {
            'type': 'arbitrary',
            'samples': [0.0] * 5 + [-0.2081559] * 199,
            'is_overridable': False,
        },
        'gate_36_baked_wf_400': {
            'type': 'arbitrary',
            'samples': [0.0] * 5 + [0.254468348] * 199,
            'is_overridable': False,
        },
        'gate_29_baked_wf_401': {
            'type': 'arbitrary',
            'samples': [0.0] * 4 + [-0.2081559] * 200,
            'is_overridable': False,
        },
        'gate_36_baked_wf_401': {
            'type': 'arbitrary',
            'samples': [0.0] * 4 + [0.254468348] * 200,
            'is_overridable': False,
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
        'cos_50': {
            'cosine': [(1.0, 100000)],
            'sine': [(0.0, 100000)],
        },
        'sin_50': {
            'cosine': [(0.0, 100000)],
            'sine': [(1.0, 100000)],
        },
        'cos_3us': {
            'cosine': [(1.0, 3000)],
            'sine': [(0.0, 3000)],
        },
        'sin_3us': {
            'cosine': [(0.0, 3000)],
            'sine': [(1.0, 3000)],
        },
        'cos_buffered': {
            'cosine': [(1.0, 3000000)],
            'sine': [(0.0, 3000000)],
        },
        'sin_buffered': {
            'cosine': [(0.0, 3000000)],
            'sine': [(1.0, 3000000)],
        },
        'cos_t2star': {
            'cosine': [(1.0, 15048)],
            'sine': [(0.0, 15048)],
        },
        'sin_t2star': {
            'cosine': [(0.0, 15048)],
            'sine': [(1.0, 15048)],
        },
        'cos_t2star_full_demod': {
            'cosine': [(0.005050505050505051, 15048)],
            'sine': [(0.0, 15048)],
        },
        'sin_t2star_full_demod': {
            'cosine': [(0.0, 15048)],
            'sine': [(0.005050505050505051, 15048)],
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
                    'delay': 0,
                    'shareable': False,
                    'filter': {
                        'feedforward': [],
                        'feedback': [],
                    },
                },
                '3': {
                    'offset': -0.0072,
                    'delay': 0,
                    'shareable': False,
                    'filter': {
                        'feedforward': [],
                        'feedback': [],
                    },
                },
                '2': {
                    'offset': -0.0072,
                    'delay': 0,
                    'shareable': False,
                    'filter': {
                        'feedforward': [],
                        'feedback': [],
                    },
                },
            },
            'analog_inputs': {
                '2': {
                    'offset': 0.0,
                    'gain_db': 0,
                    'shareable': False,
                },
            },
            'digital_outputs': {
                '2': {
                    'shareable': False,
                },
            },
        },
    },
    'oscillators': {},
    'elements': {
        'gate_29': {
            'digitalInputs': {},
            'digitalOutputs': {},
            'intermediate_frequency': 0,
            'operations': {
                'CW': 'CW',
                'baked_Op_0': 'gate_29_baked_pulse_0',
                'baked_Op_1': 'gate_29_baked_pulse_1',
                'baked_Op_2': 'gate_29_baked_pulse_2',
                'baked_Op_3': 'gate_29_baked_pulse_3',
                'baked_Op_4': 'gate_29_baked_pulse_4',
                'baked_Op_5': 'gate_29_baked_pulse_5',
                'baked_Op_6': 'gate_29_baked_pulse_6',
                'baked_Op_7': 'gate_29_baked_pulse_7',
                'baked_Op_8': 'gate_29_baked_pulse_8',
                'baked_Op_9': 'gate_29_baked_pulse_9',
                'baked_Op_10': 'gate_29_baked_pulse_10',
                'baked_Op_11': 'gate_29_baked_pulse_11',
                'baked_Op_12': 'gate_29_baked_pulse_12',
                'baked_Op_13': 'gate_29_baked_pulse_13',
                'baked_Op_14': 'gate_29_baked_pulse_14',
                'baked_Op_15': 'gate_29_baked_pulse_15',
                'baked_Op_16': 'gate_29_baked_pulse_16',
                'baked_Op_17': 'gate_29_baked_pulse_17',
                'baked_Op_18': 'gate_29_baked_pulse_18',
                'baked_Op_19': 'gate_29_baked_pulse_19',
                'baked_Op_20': 'gate_29_baked_pulse_20',
                'baked_Op_21': 'gate_29_baked_pulse_21',
                'baked_Op_22': 'gate_29_baked_pulse_22',
                'baked_Op_23': 'gate_29_baked_pulse_23',
                'baked_Op_24': 'gate_29_baked_pulse_24',
                'baked_Op_25': 'gate_29_baked_pulse_25',
                'baked_Op_26': 'gate_29_baked_pulse_26',
                'baked_Op_27': 'gate_29_baked_pulse_27',
                'baked_Op_28': 'gate_29_baked_pulse_28',
                'baked_Op_29': 'gate_29_baked_pulse_29',
                'baked_Op_30': 'gate_29_baked_pulse_30',
                'baked_Op_31': 'gate_29_baked_pulse_31',
                'baked_Op_32': 'gate_29_baked_pulse_32',
                'baked_Op_33': 'gate_29_baked_pulse_33',
                'baked_Op_34': 'gate_29_baked_pulse_34',
                'baked_Op_35': 'gate_29_baked_pulse_35',
                'baked_Op_36': 'gate_29_baked_pulse_36',
                'baked_Op_37': 'gate_29_baked_pulse_37',
                'baked_Op_38': 'gate_29_baked_pulse_38',
                'baked_Op_39': 'gate_29_baked_pulse_39',
                'baked_Op_40': 'gate_29_baked_pulse_40',
                'baked_Op_41': 'gate_29_baked_pulse_41',
                'baked_Op_42': 'gate_29_baked_pulse_42',
                'baked_Op_43': 'gate_29_baked_pulse_43',
                'baked_Op_44': 'gate_29_baked_pulse_44',
                'baked_Op_45': 'gate_29_baked_pulse_45',
                'baked_Op_46': 'gate_29_baked_pulse_46',
                'baked_Op_47': 'gate_29_baked_pulse_47',
                'baked_Op_48': 'gate_29_baked_pulse_48',
                'baked_Op_49': 'gate_29_baked_pulse_49',
                'baked_Op_50': 'gate_29_baked_pulse_50',
                'baked_Op_51': 'gate_29_baked_pulse_51',
                'baked_Op_52': 'gate_29_baked_pulse_52',
                'baked_Op_53': 'gate_29_baked_pulse_53',
                'baked_Op_54': 'gate_29_baked_pulse_54',
                'baked_Op_55': 'gate_29_baked_pulse_55',
                'baked_Op_56': 'gate_29_baked_pulse_56',
                'baked_Op_57': 'gate_29_baked_pulse_57',
                'baked_Op_58': 'gate_29_baked_pulse_58',
                'baked_Op_59': 'gate_29_baked_pulse_59',
                'baked_Op_60': 'gate_29_baked_pulse_60',
                'baked_Op_61': 'gate_29_baked_pulse_61',
                'baked_Op_62': 'gate_29_baked_pulse_62',
                'baked_Op_63': 'gate_29_baked_pulse_63',
                'baked_Op_64': 'gate_29_baked_pulse_64',
                'baked_Op_65': 'gate_29_baked_pulse_65',
                'baked_Op_66': 'gate_29_baked_pulse_66',
                'baked_Op_67': 'gate_29_baked_pulse_67',
                'baked_Op_68': 'gate_29_baked_pulse_68',
                'baked_Op_69': 'gate_29_baked_pulse_69',
                'baked_Op_70': 'gate_29_baked_pulse_70',
                'baked_Op_71': 'gate_29_baked_pulse_71',
                'baked_Op_72': 'gate_29_baked_pulse_72',
                'baked_Op_73': 'gate_29_baked_pulse_73',
                'baked_Op_74': 'gate_29_baked_pulse_74',
                'baked_Op_75': 'gate_29_baked_pulse_75',
                'baked_Op_76': 'gate_29_baked_pulse_76',
                'baked_Op_77': 'gate_29_baked_pulse_77',
                'baked_Op_78': 'gate_29_baked_pulse_78',
                'baked_Op_79': 'gate_29_baked_pulse_79',
                'baked_Op_80': 'gate_29_baked_pulse_80',
                'baked_Op_81': 'gate_29_baked_pulse_81',
                'baked_Op_82': 'gate_29_baked_pulse_82',
                'baked_Op_83': 'gate_29_baked_pulse_83',
                'baked_Op_84': 'gate_29_baked_pulse_84',
                'baked_Op_85': 'gate_29_baked_pulse_85',
                'baked_Op_86': 'gate_29_baked_pulse_86',
                'baked_Op_87': 'gate_29_baked_pulse_87',
                'baked_Op_88': 'gate_29_baked_pulse_88',
                'baked_Op_89': 'gate_29_baked_pulse_89',
                'baked_Op_90': 'gate_29_baked_pulse_90',
                'baked_Op_91': 'gate_29_baked_pulse_91',
                'baked_Op_92': 'gate_29_baked_pulse_92',
                'baked_Op_93': 'gate_29_baked_pulse_93',
                'baked_Op_94': 'gate_29_baked_pulse_94',
                'baked_Op_95': 'gate_29_baked_pulse_95',
                'baked_Op_96': 'gate_29_baked_pulse_96',
                'baked_Op_97': 'gate_29_baked_pulse_97',
                'baked_Op_98': 'gate_29_baked_pulse_98',
                'baked_Op_99': 'gate_29_baked_pulse_99',
                'baked_Op_100': 'gate_29_baked_pulse_100',
                'baked_Op_101': 'gate_29_baked_pulse_101',
                'baked_Op_102': 'gate_29_baked_pulse_102',
                'baked_Op_103': 'gate_29_baked_pulse_103',
                'baked_Op_104': 'gate_29_baked_pulse_104',
                'baked_Op_105': 'gate_29_baked_pulse_105',
                'baked_Op_106': 'gate_29_baked_pulse_106',
                'baked_Op_107': 'gate_29_baked_pulse_107',
                'baked_Op_108': 'gate_29_baked_pulse_108',
                'baked_Op_109': 'gate_29_baked_pulse_109',
                'baked_Op_110': 'gate_29_baked_pulse_110',
                'baked_Op_111': 'gate_29_baked_pulse_111',
                'baked_Op_112': 'gate_29_baked_pulse_112',
                'baked_Op_113': 'gate_29_baked_pulse_113',
                'baked_Op_114': 'gate_29_baked_pulse_114',
                'baked_Op_115': 'gate_29_baked_pulse_115',
                'baked_Op_116': 'gate_29_baked_pulse_116',
                'baked_Op_117': 'gate_29_baked_pulse_117',
                'baked_Op_118': 'gate_29_baked_pulse_118',
                'baked_Op_119': 'gate_29_baked_pulse_119',
                'baked_Op_120': 'gate_29_baked_pulse_120',
                'baked_Op_121': 'gate_29_baked_pulse_121',
                'baked_Op_122': 'gate_29_baked_pulse_122',
                'baked_Op_123': 'gate_29_baked_pulse_123',
                'baked_Op_124': 'gate_29_baked_pulse_124',
                'baked_Op_125': 'gate_29_baked_pulse_125',
                'baked_Op_126': 'gate_29_baked_pulse_126',
                'baked_Op_127': 'gate_29_baked_pulse_127',
                'baked_Op_128': 'gate_29_baked_pulse_128',
                'baked_Op_129': 'gate_29_baked_pulse_129',
                'baked_Op_130': 'gate_29_baked_pulse_130',
                'baked_Op_131': 'gate_29_baked_pulse_131',
                'baked_Op_132': 'gate_29_baked_pulse_132',
                'baked_Op_133': 'gate_29_baked_pulse_133',
                'baked_Op_134': 'gate_29_baked_pulse_134',
                'baked_Op_135': 'gate_29_baked_pulse_135',
                'baked_Op_136': 'gate_29_baked_pulse_136',
                'baked_Op_137': 'gate_29_baked_pulse_137',
                'baked_Op_138': 'gate_29_baked_pulse_138',
                'baked_Op_139': 'gate_29_baked_pulse_139',
                'baked_Op_140': 'gate_29_baked_pulse_140',
                'baked_Op_141': 'gate_29_baked_pulse_141',
                'baked_Op_142': 'gate_29_baked_pulse_142',
                'baked_Op_143': 'gate_29_baked_pulse_143',
                'baked_Op_144': 'gate_29_baked_pulse_144',
                'baked_Op_145': 'gate_29_baked_pulse_145',
                'baked_Op_146': 'gate_29_baked_pulse_146',
                'baked_Op_147': 'gate_29_baked_pulse_147',
                'baked_Op_148': 'gate_29_baked_pulse_148',
                'baked_Op_149': 'gate_29_baked_pulse_149',
                'baked_Op_150': 'gate_29_baked_pulse_150',
                'baked_Op_151': 'gate_29_baked_pulse_151',
                'baked_Op_152': 'gate_29_baked_pulse_152',
                'baked_Op_153': 'gate_29_baked_pulse_153',
                'baked_Op_154': 'gate_29_baked_pulse_154',
                'baked_Op_155': 'gate_29_baked_pulse_155',
                'baked_Op_156': 'gate_29_baked_pulse_156',
                'baked_Op_157': 'gate_29_baked_pulse_157',
                'baked_Op_158': 'gate_29_baked_pulse_158',
                'baked_Op_159': 'gate_29_baked_pulse_159',
                'baked_Op_160': 'gate_29_baked_pulse_160',
                'baked_Op_161': 'gate_29_baked_pulse_161',
                'baked_Op_162': 'gate_29_baked_pulse_162',
                'baked_Op_163': 'gate_29_baked_pulse_163',
                'baked_Op_164': 'gate_29_baked_pulse_164',
                'baked_Op_165': 'gate_29_baked_pulse_165',
                'baked_Op_166': 'gate_29_baked_pulse_166',
                'baked_Op_167': 'gate_29_baked_pulse_167',
                'baked_Op_168': 'gate_29_baked_pulse_168',
                'baked_Op_169': 'gate_29_baked_pulse_169',
                'baked_Op_170': 'gate_29_baked_pulse_170',
                'baked_Op_171': 'gate_29_baked_pulse_171',
                'baked_Op_172': 'gate_29_baked_pulse_172',
                'baked_Op_173': 'gate_29_baked_pulse_173',
                'baked_Op_174': 'gate_29_baked_pulse_174',
                'baked_Op_175': 'gate_29_baked_pulse_175',
                'baked_Op_176': 'gate_29_baked_pulse_176',
                'baked_Op_177': 'gate_29_baked_pulse_177',
                'baked_Op_178': 'gate_29_baked_pulse_178',
                'baked_Op_179': 'gate_29_baked_pulse_179',
                'baked_Op_180': 'gate_29_baked_pulse_180',
                'baked_Op_181': 'gate_29_baked_pulse_181',
                'baked_Op_182': 'gate_29_baked_pulse_182',
                'baked_Op_183': 'gate_29_baked_pulse_183',
                'baked_Op_184': 'gate_29_baked_pulse_184',
                'baked_Op_185': 'gate_29_baked_pulse_185',
                'baked_Op_186': 'gate_29_baked_pulse_186',
                'baked_Op_187': 'gate_29_baked_pulse_187',
                'baked_Op_188': 'gate_29_baked_pulse_188',
                'baked_Op_189': 'gate_29_baked_pulse_189',
                'baked_Op_190': 'gate_29_baked_pulse_190',
                'baked_Op_191': 'gate_29_baked_pulse_191',
                'baked_Op_192': 'gate_29_baked_pulse_192',
                'baked_Op_193': 'gate_29_baked_pulse_193',
                'baked_Op_194': 'gate_29_baked_pulse_194',
                'baked_Op_195': 'gate_29_baked_pulse_195',
                'baked_Op_196': 'gate_29_baked_pulse_196',
                'baked_Op_197': 'gate_29_baked_pulse_197',
                'baked_Op_198': 'gate_29_baked_pulse_198',
                'baked_Op_199': 'gate_29_baked_pulse_199',
                'baked_Op_200': 'gate_29_baked_pulse_200',
                'baked_Op_201': 'gate_29_baked_pulse_201',
                'baked_Op_202': 'gate_29_baked_pulse_202',
                'baked_Op_203': 'gate_29_baked_pulse_203',
                'baked_Op_204': 'gate_29_baked_pulse_204',
                'baked_Op_205': 'gate_29_baked_pulse_205',
                'baked_Op_206': 'gate_29_baked_pulse_206',
                'baked_Op_207': 'gate_29_baked_pulse_207',
                'baked_Op_208': 'gate_29_baked_pulse_208',
                'baked_Op_209': 'gate_29_baked_pulse_209',
                'baked_Op_210': 'gate_29_baked_pulse_210',
                'baked_Op_211': 'gate_29_baked_pulse_211',
                'baked_Op_212': 'gate_29_baked_pulse_212',
                'baked_Op_213': 'gate_29_baked_pulse_213',
                'baked_Op_214': 'gate_29_baked_pulse_214',
                'baked_Op_215': 'gate_29_baked_pulse_215',
                'baked_Op_216': 'gate_29_baked_pulse_216',
                'baked_Op_217': 'gate_29_baked_pulse_217',
                'baked_Op_218': 'gate_29_baked_pulse_218',
                'baked_Op_219': 'gate_29_baked_pulse_219',
                'baked_Op_220': 'gate_29_baked_pulse_220',
                'baked_Op_221': 'gate_29_baked_pulse_221',
                'baked_Op_222': 'gate_29_baked_pulse_222',
                'baked_Op_223': 'gate_29_baked_pulse_223',
                'baked_Op_224': 'gate_29_baked_pulse_224',
                'baked_Op_225': 'gate_29_baked_pulse_225',
                'baked_Op_226': 'gate_29_baked_pulse_226',
                'baked_Op_227': 'gate_29_baked_pulse_227',
                'baked_Op_228': 'gate_29_baked_pulse_228',
                'baked_Op_229': 'gate_29_baked_pulse_229',
                'baked_Op_230': 'gate_29_baked_pulse_230',
                'baked_Op_231': 'gate_29_baked_pulse_231',
                'baked_Op_232': 'gate_29_baked_pulse_232',
                'baked_Op_233': 'gate_29_baked_pulse_233',
                'baked_Op_234': 'gate_29_baked_pulse_234',
                'baked_Op_235': 'gate_29_baked_pulse_235',
                'baked_Op_236': 'gate_29_baked_pulse_236',
                'baked_Op_237': 'gate_29_baked_pulse_237',
                'baked_Op_238': 'gate_29_baked_pulse_238',
                'baked_Op_239': 'gate_29_baked_pulse_239',
                'baked_Op_240': 'gate_29_baked_pulse_240',
                'baked_Op_241': 'gate_29_baked_pulse_241',
                'baked_Op_242': 'gate_29_baked_pulse_242',
                'baked_Op_243': 'gate_29_baked_pulse_243',
                'baked_Op_244': 'gate_29_baked_pulse_244',
                'baked_Op_245': 'gate_29_baked_pulse_245',
                'baked_Op_246': 'gate_29_baked_pulse_246',
                'baked_Op_247': 'gate_29_baked_pulse_247',
                'baked_Op_248': 'gate_29_baked_pulse_248',
                'baked_Op_249': 'gate_29_baked_pulse_249',
                'baked_Op_250': 'gate_29_baked_pulse_250',
                'baked_Op_251': 'gate_29_baked_pulse_251',
                'baked_Op_252': 'gate_29_baked_pulse_252',
                'baked_Op_253': 'gate_29_baked_pulse_253',
                'baked_Op_254': 'gate_29_baked_pulse_254',
                'baked_Op_255': 'gate_29_baked_pulse_255',
                'baked_Op_256': 'gate_29_baked_pulse_256',
                'baked_Op_257': 'gate_29_baked_pulse_257',
                'baked_Op_258': 'gate_29_baked_pulse_258',
                'baked_Op_259': 'gate_29_baked_pulse_259',
                'baked_Op_260': 'gate_29_baked_pulse_260',
                'baked_Op_261': 'gate_29_baked_pulse_261',
                'baked_Op_262': 'gate_29_baked_pulse_262',
                'baked_Op_263': 'gate_29_baked_pulse_263',
                'baked_Op_264': 'gate_29_baked_pulse_264',
                'baked_Op_265': 'gate_29_baked_pulse_265',
                'baked_Op_266': 'gate_29_baked_pulse_266',
                'baked_Op_267': 'gate_29_baked_pulse_267',
                'baked_Op_268': 'gate_29_baked_pulse_268',
                'baked_Op_269': 'gate_29_baked_pulse_269',
                'baked_Op_270': 'gate_29_baked_pulse_270',
                'baked_Op_271': 'gate_29_baked_pulse_271',
                'baked_Op_272': 'gate_29_baked_pulse_272',
                'baked_Op_273': 'gate_29_baked_pulse_273',
                'baked_Op_274': 'gate_29_baked_pulse_274',
                'baked_Op_275': 'gate_29_baked_pulse_275',
                'baked_Op_276': 'gate_29_baked_pulse_276',
                'baked_Op_277': 'gate_29_baked_pulse_277',
                'baked_Op_278': 'gate_29_baked_pulse_278',
                'baked_Op_279': 'gate_29_baked_pulse_279',
                'baked_Op_280': 'gate_29_baked_pulse_280',
                'baked_Op_281': 'gate_29_baked_pulse_281',
                'baked_Op_282': 'gate_29_baked_pulse_282',
                'baked_Op_283': 'gate_29_baked_pulse_283',
                'baked_Op_284': 'gate_29_baked_pulse_284',
                'baked_Op_285': 'gate_29_baked_pulse_285',
                'baked_Op_286': 'gate_29_baked_pulse_286',
                'baked_Op_287': 'gate_29_baked_pulse_287',
                'baked_Op_288': 'gate_29_baked_pulse_288',
                'baked_Op_289': 'gate_29_baked_pulse_289',
                'baked_Op_290': 'gate_29_baked_pulse_290',
                'baked_Op_291': 'gate_29_baked_pulse_291',
                'baked_Op_292': 'gate_29_baked_pulse_292',
                'baked_Op_293': 'gate_29_baked_pulse_293',
                'baked_Op_294': 'gate_29_baked_pulse_294',
                'baked_Op_295': 'gate_29_baked_pulse_295',
                'baked_Op_296': 'gate_29_baked_pulse_296',
                'baked_Op_297': 'gate_29_baked_pulse_297',
                'baked_Op_298': 'gate_29_baked_pulse_298',
                'baked_Op_299': 'gate_29_baked_pulse_299',
                'baked_Op_300': 'gate_29_baked_pulse_300',
                'baked_Op_301': 'gate_29_baked_pulse_301',
                'baked_Op_302': 'gate_29_baked_pulse_302',
                'baked_Op_303': 'gate_29_baked_pulse_303',
                'baked_Op_304': 'gate_29_baked_pulse_304',
                'baked_Op_305': 'gate_29_baked_pulse_305',
                'baked_Op_306': 'gate_29_baked_pulse_306',
                'baked_Op_307': 'gate_29_baked_pulse_307',
                'baked_Op_308': 'gate_29_baked_pulse_308',
                'baked_Op_309': 'gate_29_baked_pulse_309',
                'baked_Op_310': 'gate_29_baked_pulse_310',
                'baked_Op_311': 'gate_29_baked_pulse_311',
                'baked_Op_312': 'gate_29_baked_pulse_312',
                'baked_Op_313': 'gate_29_baked_pulse_313',
                'baked_Op_314': 'gate_29_baked_pulse_314',
                'baked_Op_315': 'gate_29_baked_pulse_315',
                'baked_Op_316': 'gate_29_baked_pulse_316',
                'baked_Op_317': 'gate_29_baked_pulse_317',
                'baked_Op_318': 'gate_29_baked_pulse_318',
                'baked_Op_319': 'gate_29_baked_pulse_319',
                'baked_Op_320': 'gate_29_baked_pulse_320',
                'baked_Op_321': 'gate_29_baked_pulse_321',
                'baked_Op_322': 'gate_29_baked_pulse_322',
                'baked_Op_323': 'gate_29_baked_pulse_323',
                'baked_Op_324': 'gate_29_baked_pulse_324',
                'baked_Op_325': 'gate_29_baked_pulse_325',
                'baked_Op_326': 'gate_29_baked_pulse_326',
                'baked_Op_327': 'gate_29_baked_pulse_327',
                'baked_Op_328': 'gate_29_baked_pulse_328',
                'baked_Op_329': 'gate_29_baked_pulse_329',
                'baked_Op_330': 'gate_29_baked_pulse_330',
                'baked_Op_331': 'gate_29_baked_pulse_331',
                'baked_Op_332': 'gate_29_baked_pulse_332',
                'baked_Op_333': 'gate_29_baked_pulse_333',
                'baked_Op_334': 'gate_29_baked_pulse_334',
                'baked_Op_335': 'gate_29_baked_pulse_335',
                'baked_Op_336': 'gate_29_baked_pulse_336',
                'baked_Op_337': 'gate_29_baked_pulse_337',
                'baked_Op_338': 'gate_29_baked_pulse_338',
                'baked_Op_339': 'gate_29_baked_pulse_339',
                'baked_Op_340': 'gate_29_baked_pulse_340',
                'baked_Op_341': 'gate_29_baked_pulse_341',
                'baked_Op_342': 'gate_29_baked_pulse_342',
                'baked_Op_343': 'gate_29_baked_pulse_343',
                'baked_Op_344': 'gate_29_baked_pulse_344',
                'baked_Op_345': 'gate_29_baked_pulse_345',
                'baked_Op_346': 'gate_29_baked_pulse_346',
                'baked_Op_347': 'gate_29_baked_pulse_347',
                'baked_Op_348': 'gate_29_baked_pulse_348',
                'baked_Op_349': 'gate_29_baked_pulse_349',
                'baked_Op_350': 'gate_29_baked_pulse_350',
                'baked_Op_351': 'gate_29_baked_pulse_351',
                'baked_Op_352': 'gate_29_baked_pulse_352',
                'baked_Op_353': 'gate_29_baked_pulse_353',
                'baked_Op_354': 'gate_29_baked_pulse_354',
                'baked_Op_355': 'gate_29_baked_pulse_355',
                'baked_Op_356': 'gate_29_baked_pulse_356',
                'baked_Op_357': 'gate_29_baked_pulse_357',
                'baked_Op_358': 'gate_29_baked_pulse_358',
                'baked_Op_359': 'gate_29_baked_pulse_359',
                'baked_Op_360': 'gate_29_baked_pulse_360',
                'baked_Op_361': 'gate_29_baked_pulse_361',
                'baked_Op_362': 'gate_29_baked_pulse_362',
                'baked_Op_363': 'gate_29_baked_pulse_363',
                'baked_Op_364': 'gate_29_baked_pulse_364',
                'baked_Op_365': 'gate_29_baked_pulse_365',
                'baked_Op_366': 'gate_29_baked_pulse_366',
                'baked_Op_367': 'gate_29_baked_pulse_367',
                'baked_Op_368': 'gate_29_baked_pulse_368',
                'baked_Op_369': 'gate_29_baked_pulse_369',
                'baked_Op_370': 'gate_29_baked_pulse_370',
                'baked_Op_371': 'gate_29_baked_pulse_371',
                'baked_Op_372': 'gate_29_baked_pulse_372',
                'baked_Op_373': 'gate_29_baked_pulse_373',
                'baked_Op_374': 'gate_29_baked_pulse_374',
                'baked_Op_375': 'gate_29_baked_pulse_375',
                'baked_Op_376': 'gate_29_baked_pulse_376',
                'baked_Op_377': 'gate_29_baked_pulse_377',
                'baked_Op_378': 'gate_29_baked_pulse_378',
                'baked_Op_379': 'gate_29_baked_pulse_379',
                'baked_Op_380': 'gate_29_baked_pulse_380',
                'baked_Op_381': 'gate_29_baked_pulse_381',
                'baked_Op_382': 'gate_29_baked_pulse_382',
                'baked_Op_383': 'gate_29_baked_pulse_383',
                'baked_Op_384': 'gate_29_baked_pulse_384',
                'baked_Op_385': 'gate_29_baked_pulse_385',
                'baked_Op_386': 'gate_29_baked_pulse_386',
                'baked_Op_387': 'gate_29_baked_pulse_387',
                'baked_Op_388': 'gate_29_baked_pulse_388',
                'baked_Op_389': 'gate_29_baked_pulse_389',
                'baked_Op_390': 'gate_29_baked_pulse_390',
                'baked_Op_391': 'gate_29_baked_pulse_391',
                'baked_Op_392': 'gate_29_baked_pulse_392',
                'baked_Op_393': 'gate_29_baked_pulse_393',
                'baked_Op_394': 'gate_29_baked_pulse_394',
                'baked_Op_395': 'gate_29_baked_pulse_395',
                'baked_Op_396': 'gate_29_baked_pulse_396',
                'baked_Op_397': 'gate_29_baked_pulse_397',
                'baked_Op_398': 'gate_29_baked_pulse_398',
                'baked_Op_399': 'gate_29_baked_pulse_399',
                'baked_Op_400': 'gate_29_baked_pulse_400',
                'baked_Op_401': 'gate_29_baked_pulse_401',
            },
            'singleInput': {
                'port': ('con1', 3),
            },
            'hold_offset': {
                'duration': 24,
            },
        },
        'gate_36': {
            'digitalInputs': {},
            'digitalOutputs': {},
            'intermediate_frequency': 0,
            'operations': {
                'CW': 'CW',
                'baked_Op_0': 'gate_36_baked_pulse_0',
                'baked_Op_1': 'gate_36_baked_pulse_1',
                'baked_Op_2': 'gate_36_baked_pulse_2',
                'baked_Op_3': 'gate_36_baked_pulse_3',
                'baked_Op_4': 'gate_36_baked_pulse_4',
                'baked_Op_5': 'gate_36_baked_pulse_5',
                'baked_Op_6': 'gate_36_baked_pulse_6',
                'baked_Op_7': 'gate_36_baked_pulse_7',
                'baked_Op_8': 'gate_36_baked_pulse_8',
                'baked_Op_9': 'gate_36_baked_pulse_9',
                'baked_Op_10': 'gate_36_baked_pulse_10',
                'baked_Op_11': 'gate_36_baked_pulse_11',
                'baked_Op_12': 'gate_36_baked_pulse_12',
                'baked_Op_13': 'gate_36_baked_pulse_13',
                'baked_Op_14': 'gate_36_baked_pulse_14',
                'baked_Op_15': 'gate_36_baked_pulse_15',
                'baked_Op_16': 'gate_36_baked_pulse_16',
                'baked_Op_17': 'gate_36_baked_pulse_17',
                'baked_Op_18': 'gate_36_baked_pulse_18',
                'baked_Op_19': 'gate_36_baked_pulse_19',
                'baked_Op_20': 'gate_36_baked_pulse_20',
                'baked_Op_21': 'gate_36_baked_pulse_21',
                'baked_Op_22': 'gate_36_baked_pulse_22',
                'baked_Op_23': 'gate_36_baked_pulse_23',
                'baked_Op_24': 'gate_36_baked_pulse_24',
                'baked_Op_25': 'gate_36_baked_pulse_25',
                'baked_Op_26': 'gate_36_baked_pulse_26',
                'baked_Op_27': 'gate_36_baked_pulse_27',
                'baked_Op_28': 'gate_36_baked_pulse_28',
                'baked_Op_29': 'gate_36_baked_pulse_29',
                'baked_Op_30': 'gate_36_baked_pulse_30',
                'baked_Op_31': 'gate_36_baked_pulse_31',
                'baked_Op_32': 'gate_36_baked_pulse_32',
                'baked_Op_33': 'gate_36_baked_pulse_33',
                'baked_Op_34': 'gate_36_baked_pulse_34',
                'baked_Op_35': 'gate_36_baked_pulse_35',
                'baked_Op_36': 'gate_36_baked_pulse_36',
                'baked_Op_37': 'gate_36_baked_pulse_37',
                'baked_Op_38': 'gate_36_baked_pulse_38',
                'baked_Op_39': 'gate_36_baked_pulse_39',
                'baked_Op_40': 'gate_36_baked_pulse_40',
                'baked_Op_41': 'gate_36_baked_pulse_41',
                'baked_Op_42': 'gate_36_baked_pulse_42',
                'baked_Op_43': 'gate_36_baked_pulse_43',
                'baked_Op_44': 'gate_36_baked_pulse_44',
                'baked_Op_45': 'gate_36_baked_pulse_45',
                'baked_Op_46': 'gate_36_baked_pulse_46',
                'baked_Op_47': 'gate_36_baked_pulse_47',
                'baked_Op_48': 'gate_36_baked_pulse_48',
                'baked_Op_49': 'gate_36_baked_pulse_49',
                'baked_Op_50': 'gate_36_baked_pulse_50',
                'baked_Op_51': 'gate_36_baked_pulse_51',
                'baked_Op_52': 'gate_36_baked_pulse_52',
                'baked_Op_53': 'gate_36_baked_pulse_53',
                'baked_Op_54': 'gate_36_baked_pulse_54',
                'baked_Op_55': 'gate_36_baked_pulse_55',
                'baked_Op_56': 'gate_36_baked_pulse_56',
                'baked_Op_57': 'gate_36_baked_pulse_57',
                'baked_Op_58': 'gate_36_baked_pulse_58',
                'baked_Op_59': 'gate_36_baked_pulse_59',
                'baked_Op_60': 'gate_36_baked_pulse_60',
                'baked_Op_61': 'gate_36_baked_pulse_61',
                'baked_Op_62': 'gate_36_baked_pulse_62',
                'baked_Op_63': 'gate_36_baked_pulse_63',
                'baked_Op_64': 'gate_36_baked_pulse_64',
                'baked_Op_65': 'gate_36_baked_pulse_65',
                'baked_Op_66': 'gate_36_baked_pulse_66',
                'baked_Op_67': 'gate_36_baked_pulse_67',
                'baked_Op_68': 'gate_36_baked_pulse_68',
                'baked_Op_69': 'gate_36_baked_pulse_69',
                'baked_Op_70': 'gate_36_baked_pulse_70',
                'baked_Op_71': 'gate_36_baked_pulse_71',
                'baked_Op_72': 'gate_36_baked_pulse_72',
                'baked_Op_73': 'gate_36_baked_pulse_73',
                'baked_Op_74': 'gate_36_baked_pulse_74',
                'baked_Op_75': 'gate_36_baked_pulse_75',
                'baked_Op_76': 'gate_36_baked_pulse_76',
                'baked_Op_77': 'gate_36_baked_pulse_77',
                'baked_Op_78': 'gate_36_baked_pulse_78',
                'baked_Op_79': 'gate_36_baked_pulse_79',
                'baked_Op_80': 'gate_36_baked_pulse_80',
                'baked_Op_81': 'gate_36_baked_pulse_81',
                'baked_Op_82': 'gate_36_baked_pulse_82',
                'baked_Op_83': 'gate_36_baked_pulse_83',
                'baked_Op_84': 'gate_36_baked_pulse_84',
                'baked_Op_85': 'gate_36_baked_pulse_85',
                'baked_Op_86': 'gate_36_baked_pulse_86',
                'baked_Op_87': 'gate_36_baked_pulse_87',
                'baked_Op_88': 'gate_36_baked_pulse_88',
                'baked_Op_89': 'gate_36_baked_pulse_89',
                'baked_Op_90': 'gate_36_baked_pulse_90',
                'baked_Op_91': 'gate_36_baked_pulse_91',
                'baked_Op_92': 'gate_36_baked_pulse_92',
                'baked_Op_93': 'gate_36_baked_pulse_93',
                'baked_Op_94': 'gate_36_baked_pulse_94',
                'baked_Op_95': 'gate_36_baked_pulse_95',
                'baked_Op_96': 'gate_36_baked_pulse_96',
                'baked_Op_97': 'gate_36_baked_pulse_97',
                'baked_Op_98': 'gate_36_baked_pulse_98',
                'baked_Op_99': 'gate_36_baked_pulse_99',
                'baked_Op_100': 'gate_36_baked_pulse_100',
                'baked_Op_101': 'gate_36_baked_pulse_101',
                'baked_Op_102': 'gate_36_baked_pulse_102',
                'baked_Op_103': 'gate_36_baked_pulse_103',
                'baked_Op_104': 'gate_36_baked_pulse_104',
                'baked_Op_105': 'gate_36_baked_pulse_105',
                'baked_Op_106': 'gate_36_baked_pulse_106',
                'baked_Op_107': 'gate_36_baked_pulse_107',
                'baked_Op_108': 'gate_36_baked_pulse_108',
                'baked_Op_109': 'gate_36_baked_pulse_109',
                'baked_Op_110': 'gate_36_baked_pulse_110',
                'baked_Op_111': 'gate_36_baked_pulse_111',
                'baked_Op_112': 'gate_36_baked_pulse_112',
                'baked_Op_113': 'gate_36_baked_pulse_113',
                'baked_Op_114': 'gate_36_baked_pulse_114',
                'baked_Op_115': 'gate_36_baked_pulse_115',
                'baked_Op_116': 'gate_36_baked_pulse_116',
                'baked_Op_117': 'gate_36_baked_pulse_117',
                'baked_Op_118': 'gate_36_baked_pulse_118',
                'baked_Op_119': 'gate_36_baked_pulse_119',
                'baked_Op_120': 'gate_36_baked_pulse_120',
                'baked_Op_121': 'gate_36_baked_pulse_121',
                'baked_Op_122': 'gate_36_baked_pulse_122',
                'baked_Op_123': 'gate_36_baked_pulse_123',
                'baked_Op_124': 'gate_36_baked_pulse_124',
                'baked_Op_125': 'gate_36_baked_pulse_125',
                'baked_Op_126': 'gate_36_baked_pulse_126',
                'baked_Op_127': 'gate_36_baked_pulse_127',
                'baked_Op_128': 'gate_36_baked_pulse_128',
                'baked_Op_129': 'gate_36_baked_pulse_129',
                'baked_Op_130': 'gate_36_baked_pulse_130',
                'baked_Op_131': 'gate_36_baked_pulse_131',
                'baked_Op_132': 'gate_36_baked_pulse_132',
                'baked_Op_133': 'gate_36_baked_pulse_133',
                'baked_Op_134': 'gate_36_baked_pulse_134',
                'baked_Op_135': 'gate_36_baked_pulse_135',
                'baked_Op_136': 'gate_36_baked_pulse_136',
                'baked_Op_137': 'gate_36_baked_pulse_137',
                'baked_Op_138': 'gate_36_baked_pulse_138',
                'baked_Op_139': 'gate_36_baked_pulse_139',
                'baked_Op_140': 'gate_36_baked_pulse_140',
                'baked_Op_141': 'gate_36_baked_pulse_141',
                'baked_Op_142': 'gate_36_baked_pulse_142',
                'baked_Op_143': 'gate_36_baked_pulse_143',
                'baked_Op_144': 'gate_36_baked_pulse_144',
                'baked_Op_145': 'gate_36_baked_pulse_145',
                'baked_Op_146': 'gate_36_baked_pulse_146',
                'baked_Op_147': 'gate_36_baked_pulse_147',
                'baked_Op_148': 'gate_36_baked_pulse_148',
                'baked_Op_149': 'gate_36_baked_pulse_149',
                'baked_Op_150': 'gate_36_baked_pulse_150',
                'baked_Op_151': 'gate_36_baked_pulse_151',
                'baked_Op_152': 'gate_36_baked_pulse_152',
                'baked_Op_153': 'gate_36_baked_pulse_153',
                'baked_Op_154': 'gate_36_baked_pulse_154',
                'baked_Op_155': 'gate_36_baked_pulse_155',
                'baked_Op_156': 'gate_36_baked_pulse_156',
                'baked_Op_157': 'gate_36_baked_pulse_157',
                'baked_Op_158': 'gate_36_baked_pulse_158',
                'baked_Op_159': 'gate_36_baked_pulse_159',
                'baked_Op_160': 'gate_36_baked_pulse_160',
                'baked_Op_161': 'gate_36_baked_pulse_161',
                'baked_Op_162': 'gate_36_baked_pulse_162',
                'baked_Op_163': 'gate_36_baked_pulse_163',
                'baked_Op_164': 'gate_36_baked_pulse_164',
                'baked_Op_165': 'gate_36_baked_pulse_165',
                'baked_Op_166': 'gate_36_baked_pulse_166',
                'baked_Op_167': 'gate_36_baked_pulse_167',
                'baked_Op_168': 'gate_36_baked_pulse_168',
                'baked_Op_169': 'gate_36_baked_pulse_169',
                'baked_Op_170': 'gate_36_baked_pulse_170',
                'baked_Op_171': 'gate_36_baked_pulse_171',
                'baked_Op_172': 'gate_36_baked_pulse_172',
                'baked_Op_173': 'gate_36_baked_pulse_173',
                'baked_Op_174': 'gate_36_baked_pulse_174',
                'baked_Op_175': 'gate_36_baked_pulse_175',
                'baked_Op_176': 'gate_36_baked_pulse_176',
                'baked_Op_177': 'gate_36_baked_pulse_177',
                'baked_Op_178': 'gate_36_baked_pulse_178',
                'baked_Op_179': 'gate_36_baked_pulse_179',
                'baked_Op_180': 'gate_36_baked_pulse_180',
                'baked_Op_181': 'gate_36_baked_pulse_181',
                'baked_Op_182': 'gate_36_baked_pulse_182',
                'baked_Op_183': 'gate_36_baked_pulse_183',
                'baked_Op_184': 'gate_36_baked_pulse_184',
                'baked_Op_185': 'gate_36_baked_pulse_185',
                'baked_Op_186': 'gate_36_baked_pulse_186',
                'baked_Op_187': 'gate_36_baked_pulse_187',
                'baked_Op_188': 'gate_36_baked_pulse_188',
                'baked_Op_189': 'gate_36_baked_pulse_189',
                'baked_Op_190': 'gate_36_baked_pulse_190',
                'baked_Op_191': 'gate_36_baked_pulse_191',
                'baked_Op_192': 'gate_36_baked_pulse_192',
                'baked_Op_193': 'gate_36_baked_pulse_193',
                'baked_Op_194': 'gate_36_baked_pulse_194',
                'baked_Op_195': 'gate_36_baked_pulse_195',
                'baked_Op_196': 'gate_36_baked_pulse_196',
                'baked_Op_197': 'gate_36_baked_pulse_197',
                'baked_Op_198': 'gate_36_baked_pulse_198',
                'baked_Op_199': 'gate_36_baked_pulse_199',
                'baked_Op_200': 'gate_36_baked_pulse_200',
                'baked_Op_201': 'gate_36_baked_pulse_201',
                'baked_Op_202': 'gate_36_baked_pulse_202',
                'baked_Op_203': 'gate_36_baked_pulse_203',
                'baked_Op_204': 'gate_36_baked_pulse_204',
                'baked_Op_205': 'gate_36_baked_pulse_205',
                'baked_Op_206': 'gate_36_baked_pulse_206',
                'baked_Op_207': 'gate_36_baked_pulse_207',
                'baked_Op_208': 'gate_36_baked_pulse_208',
                'baked_Op_209': 'gate_36_baked_pulse_209',
                'baked_Op_210': 'gate_36_baked_pulse_210',
                'baked_Op_211': 'gate_36_baked_pulse_211',
                'baked_Op_212': 'gate_36_baked_pulse_212',
                'baked_Op_213': 'gate_36_baked_pulse_213',
                'baked_Op_214': 'gate_36_baked_pulse_214',
                'baked_Op_215': 'gate_36_baked_pulse_215',
                'baked_Op_216': 'gate_36_baked_pulse_216',
                'baked_Op_217': 'gate_36_baked_pulse_217',
                'baked_Op_218': 'gate_36_baked_pulse_218',
                'baked_Op_219': 'gate_36_baked_pulse_219',
                'baked_Op_220': 'gate_36_baked_pulse_220',
                'baked_Op_221': 'gate_36_baked_pulse_221',
                'baked_Op_222': 'gate_36_baked_pulse_222',
                'baked_Op_223': 'gate_36_baked_pulse_223',
                'baked_Op_224': 'gate_36_baked_pulse_224',
                'baked_Op_225': 'gate_36_baked_pulse_225',
                'baked_Op_226': 'gate_36_baked_pulse_226',
                'baked_Op_227': 'gate_36_baked_pulse_227',
                'baked_Op_228': 'gate_36_baked_pulse_228',
                'baked_Op_229': 'gate_36_baked_pulse_229',
                'baked_Op_230': 'gate_36_baked_pulse_230',
                'baked_Op_231': 'gate_36_baked_pulse_231',
                'baked_Op_232': 'gate_36_baked_pulse_232',
                'baked_Op_233': 'gate_36_baked_pulse_233',
                'baked_Op_234': 'gate_36_baked_pulse_234',
                'baked_Op_235': 'gate_36_baked_pulse_235',
                'baked_Op_236': 'gate_36_baked_pulse_236',
                'baked_Op_237': 'gate_36_baked_pulse_237',
                'baked_Op_238': 'gate_36_baked_pulse_238',
                'baked_Op_239': 'gate_36_baked_pulse_239',
                'baked_Op_240': 'gate_36_baked_pulse_240',
                'baked_Op_241': 'gate_36_baked_pulse_241',
                'baked_Op_242': 'gate_36_baked_pulse_242',
                'baked_Op_243': 'gate_36_baked_pulse_243',
                'baked_Op_244': 'gate_36_baked_pulse_244',
                'baked_Op_245': 'gate_36_baked_pulse_245',
                'baked_Op_246': 'gate_36_baked_pulse_246',
                'baked_Op_247': 'gate_36_baked_pulse_247',
                'baked_Op_248': 'gate_36_baked_pulse_248',
                'baked_Op_249': 'gate_36_baked_pulse_249',
                'baked_Op_250': 'gate_36_baked_pulse_250',
                'baked_Op_251': 'gate_36_baked_pulse_251',
                'baked_Op_252': 'gate_36_baked_pulse_252',
                'baked_Op_253': 'gate_36_baked_pulse_253',
                'baked_Op_254': 'gate_36_baked_pulse_254',
                'baked_Op_255': 'gate_36_baked_pulse_255',
                'baked_Op_256': 'gate_36_baked_pulse_256',
                'baked_Op_257': 'gate_36_baked_pulse_257',
                'baked_Op_258': 'gate_36_baked_pulse_258',
                'baked_Op_259': 'gate_36_baked_pulse_259',
                'baked_Op_260': 'gate_36_baked_pulse_260',
                'baked_Op_261': 'gate_36_baked_pulse_261',
                'baked_Op_262': 'gate_36_baked_pulse_262',
                'baked_Op_263': 'gate_36_baked_pulse_263',
                'baked_Op_264': 'gate_36_baked_pulse_264',
                'baked_Op_265': 'gate_36_baked_pulse_265',
                'baked_Op_266': 'gate_36_baked_pulse_266',
                'baked_Op_267': 'gate_36_baked_pulse_267',
                'baked_Op_268': 'gate_36_baked_pulse_268',
                'baked_Op_269': 'gate_36_baked_pulse_269',
                'baked_Op_270': 'gate_36_baked_pulse_270',
                'baked_Op_271': 'gate_36_baked_pulse_271',
                'baked_Op_272': 'gate_36_baked_pulse_272',
                'baked_Op_273': 'gate_36_baked_pulse_273',
                'baked_Op_274': 'gate_36_baked_pulse_274',
                'baked_Op_275': 'gate_36_baked_pulse_275',
                'baked_Op_276': 'gate_36_baked_pulse_276',
                'baked_Op_277': 'gate_36_baked_pulse_277',
                'baked_Op_278': 'gate_36_baked_pulse_278',
                'baked_Op_279': 'gate_36_baked_pulse_279',
                'baked_Op_280': 'gate_36_baked_pulse_280',
                'baked_Op_281': 'gate_36_baked_pulse_281',
                'baked_Op_282': 'gate_36_baked_pulse_282',
                'baked_Op_283': 'gate_36_baked_pulse_283',
                'baked_Op_284': 'gate_36_baked_pulse_284',
                'baked_Op_285': 'gate_36_baked_pulse_285',
                'baked_Op_286': 'gate_36_baked_pulse_286',
                'baked_Op_287': 'gate_36_baked_pulse_287',
                'baked_Op_288': 'gate_36_baked_pulse_288',
                'baked_Op_289': 'gate_36_baked_pulse_289',
                'baked_Op_290': 'gate_36_baked_pulse_290',
                'baked_Op_291': 'gate_36_baked_pulse_291',
                'baked_Op_292': 'gate_36_baked_pulse_292',
                'baked_Op_293': 'gate_36_baked_pulse_293',
                'baked_Op_294': 'gate_36_baked_pulse_294',
                'baked_Op_295': 'gate_36_baked_pulse_295',
                'baked_Op_296': 'gate_36_baked_pulse_296',
                'baked_Op_297': 'gate_36_baked_pulse_297',
                'baked_Op_298': 'gate_36_baked_pulse_298',
                'baked_Op_299': 'gate_36_baked_pulse_299',
                'baked_Op_300': 'gate_36_baked_pulse_300',
                'baked_Op_301': 'gate_36_baked_pulse_301',
                'baked_Op_302': 'gate_36_baked_pulse_302',
                'baked_Op_303': 'gate_36_baked_pulse_303',
                'baked_Op_304': 'gate_36_baked_pulse_304',
                'baked_Op_305': 'gate_36_baked_pulse_305',
                'baked_Op_306': 'gate_36_baked_pulse_306',
                'baked_Op_307': 'gate_36_baked_pulse_307',
                'baked_Op_308': 'gate_36_baked_pulse_308',
                'baked_Op_309': 'gate_36_baked_pulse_309',
                'baked_Op_310': 'gate_36_baked_pulse_310',
                'baked_Op_311': 'gate_36_baked_pulse_311',
                'baked_Op_312': 'gate_36_baked_pulse_312',
                'baked_Op_313': 'gate_36_baked_pulse_313',
                'baked_Op_314': 'gate_36_baked_pulse_314',
                'baked_Op_315': 'gate_36_baked_pulse_315',
                'baked_Op_316': 'gate_36_baked_pulse_316',
                'baked_Op_317': 'gate_36_baked_pulse_317',
                'baked_Op_318': 'gate_36_baked_pulse_318',
                'baked_Op_319': 'gate_36_baked_pulse_319',
                'baked_Op_320': 'gate_36_baked_pulse_320',
                'baked_Op_321': 'gate_36_baked_pulse_321',
                'baked_Op_322': 'gate_36_baked_pulse_322',
                'baked_Op_323': 'gate_36_baked_pulse_323',
                'baked_Op_324': 'gate_36_baked_pulse_324',
                'baked_Op_325': 'gate_36_baked_pulse_325',
                'baked_Op_326': 'gate_36_baked_pulse_326',
                'baked_Op_327': 'gate_36_baked_pulse_327',
                'baked_Op_328': 'gate_36_baked_pulse_328',
                'baked_Op_329': 'gate_36_baked_pulse_329',
                'baked_Op_330': 'gate_36_baked_pulse_330',
                'baked_Op_331': 'gate_36_baked_pulse_331',
                'baked_Op_332': 'gate_36_baked_pulse_332',
                'baked_Op_333': 'gate_36_baked_pulse_333',
                'baked_Op_334': 'gate_36_baked_pulse_334',
                'baked_Op_335': 'gate_36_baked_pulse_335',
                'baked_Op_336': 'gate_36_baked_pulse_336',
                'baked_Op_337': 'gate_36_baked_pulse_337',
                'baked_Op_338': 'gate_36_baked_pulse_338',
                'baked_Op_339': 'gate_36_baked_pulse_339',
                'baked_Op_340': 'gate_36_baked_pulse_340',
                'baked_Op_341': 'gate_36_baked_pulse_341',
                'baked_Op_342': 'gate_36_baked_pulse_342',
                'baked_Op_343': 'gate_36_baked_pulse_343',
                'baked_Op_344': 'gate_36_baked_pulse_344',
                'baked_Op_345': 'gate_36_baked_pulse_345',
                'baked_Op_346': 'gate_36_baked_pulse_346',
                'baked_Op_347': 'gate_36_baked_pulse_347',
                'baked_Op_348': 'gate_36_baked_pulse_348',
                'baked_Op_349': 'gate_36_baked_pulse_349',
                'baked_Op_350': 'gate_36_baked_pulse_350',
                'baked_Op_351': 'gate_36_baked_pulse_351',
                'baked_Op_352': 'gate_36_baked_pulse_352',
                'baked_Op_353': 'gate_36_baked_pulse_353',
                'baked_Op_354': 'gate_36_baked_pulse_354',
                'baked_Op_355': 'gate_36_baked_pulse_355',
                'baked_Op_356': 'gate_36_baked_pulse_356',
                'baked_Op_357': 'gate_36_baked_pulse_357',
                'baked_Op_358': 'gate_36_baked_pulse_358',
                'baked_Op_359': 'gate_36_baked_pulse_359',
                'baked_Op_360': 'gate_36_baked_pulse_360',
                'baked_Op_361': 'gate_36_baked_pulse_361',
                'baked_Op_362': 'gate_36_baked_pulse_362',
                'baked_Op_363': 'gate_36_baked_pulse_363',
                'baked_Op_364': 'gate_36_baked_pulse_364',
                'baked_Op_365': 'gate_36_baked_pulse_365',
                'baked_Op_366': 'gate_36_baked_pulse_366',
                'baked_Op_367': 'gate_36_baked_pulse_367',
                'baked_Op_368': 'gate_36_baked_pulse_368',
                'baked_Op_369': 'gate_36_baked_pulse_369',
                'baked_Op_370': 'gate_36_baked_pulse_370',
                'baked_Op_371': 'gate_36_baked_pulse_371',
                'baked_Op_372': 'gate_36_baked_pulse_372',
                'baked_Op_373': 'gate_36_baked_pulse_373',
                'baked_Op_374': 'gate_36_baked_pulse_374',
                'baked_Op_375': 'gate_36_baked_pulse_375',
                'baked_Op_376': 'gate_36_baked_pulse_376',
                'baked_Op_377': 'gate_36_baked_pulse_377',
                'baked_Op_378': 'gate_36_baked_pulse_378',
                'baked_Op_379': 'gate_36_baked_pulse_379',
                'baked_Op_380': 'gate_36_baked_pulse_380',
                'baked_Op_381': 'gate_36_baked_pulse_381',
                'baked_Op_382': 'gate_36_baked_pulse_382',
                'baked_Op_383': 'gate_36_baked_pulse_383',
                'baked_Op_384': 'gate_36_baked_pulse_384',
                'baked_Op_385': 'gate_36_baked_pulse_385',
                'baked_Op_386': 'gate_36_baked_pulse_386',
                'baked_Op_387': 'gate_36_baked_pulse_387',
                'baked_Op_388': 'gate_36_baked_pulse_388',
                'baked_Op_389': 'gate_36_baked_pulse_389',
                'baked_Op_390': 'gate_36_baked_pulse_390',
                'baked_Op_391': 'gate_36_baked_pulse_391',
                'baked_Op_392': 'gate_36_baked_pulse_392',
                'baked_Op_393': 'gate_36_baked_pulse_393',
                'baked_Op_394': 'gate_36_baked_pulse_394',
                'baked_Op_395': 'gate_36_baked_pulse_395',
                'baked_Op_396': 'gate_36_baked_pulse_396',
                'baked_Op_397': 'gate_36_baked_pulse_397',
                'baked_Op_398': 'gate_36_baked_pulse_398',
                'baked_Op_399': 'gate_36_baked_pulse_399',
                'baked_Op_400': 'gate_36_baked_pulse_400',
                'baked_Op_401': 'gate_36_baked_pulse_401',
            },
            'singleInput': {
                'port': ('con1', 2),
            },
            'hold_offset': {
                'duration': 24,
            },
        },
        'bottom_right_DQD_readout': {
            'digitalInputs': {},
            'digitalOutputs': {},
            'outputs': {
                'out1': ('con1', 2),
            },
            'time_of_flight': 500,
            'smearing': 0,
            'intermediate_frequency': 158256000,
            'operations': {
                'readout_pulse_10us': 'readout_pulse_10us',
                'readout_pulse_3ms': 'readout_pulse_3ms',
                'readout_pulse_3us': 'readout_pulse_3us',
                'readout_pulse_50us': 'readout_pulse_50us',
                'readout_pulse_t2star': 'readout_pulse_t2star',
                'readout_pulse_t2star_full_demod': 'readout_pulse_t2star_full_demod',
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
        'readout_pulse_10us': {
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
        'readout_pulse_3us': {
            'length': 3000,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos_3us',
                'sin': 'sin_3us',
            },
            'operation': 'measurement',
        },
        'readout_pulse_50us': {
            'length': 100000,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos_50',
                'sin': 'sin_50',
            },
            'operation': 'measurement',
        },
        'readout_pulse_3ms': {
            'length': 3000000,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos_buffered',
                'sin': 'sin_buffered',
            },
            'operation': 'measurement',
        },
        'readout_pulse_t2star': {
            'length': 15048,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos_t2star',
                'sin': 'sin_t2star',
            },
            'operation': 'measurement',
        },
        'readout_pulse_t2star_full_demod': {
            'length': 15048,
            'waveforms': {
                'single': 'readout_wf_0_2',
            },
            'digital_marker': 'ON',
            'integration_weights': {
                'cos': 'cos_t2star_full_demod',
                'sin': 'sin_t2star_full_demod',
            },
            'operation': 'measurement',
        },
        'gate_29_baked_pulse_0': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_0',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_0': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_0',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_1': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_1',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_1': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_1',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_2': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_2',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_2': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_2',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_3': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_3',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_3': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_3',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_4': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_4',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_4': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_4',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_5': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_5',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_5': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_5',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_6': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_6',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_6': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_6',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_7': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_7',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_7': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_7',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_8': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_8',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_8': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_8',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_9': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_9',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_9': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_9',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_10': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_10',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_10': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_10',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_11': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_11',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_11': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_11',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_12': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_12',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_12': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_12',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_13': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_13',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_13': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_13',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_14': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_14',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_14': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_14',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_15': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_15',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_15': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_15',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_16': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_16',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_16': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_16',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_17': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_17',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_17': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_17',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_18': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_18',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_18': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_18',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_19': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_19',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_19': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_19',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_20': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_20',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_20': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_20',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_21': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_21',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_21': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_21',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_22': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_22',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_22': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_22',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_23': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_23',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_23': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_23',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_24': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_24',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_24': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_24',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_25': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_25',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_25': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_25',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_26': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_26',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_26': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_26',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_27': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_27',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_27': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_27',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_28': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_28',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_28': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_28',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_29': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_29',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_29': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_29',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_30': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_30',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_30': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_30',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_31': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_31',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_31': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_31',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_32': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_32',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_32': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_32',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_33': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_33',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_33': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_33',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_34': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_34',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_34': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_34',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_35': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_35',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_35': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_35',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_36': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_36',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_36': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_36',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_37': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_37',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_37': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_37',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_38': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_38',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_38': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_38',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_39': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_39',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_39': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_39',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_40': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_40',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_40': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_40',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_41': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_41',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_41': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_41',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_42': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_42',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_42': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_42',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_43': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_43',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_43': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_43',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_44': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_44',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_44': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_44',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_45': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_45',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_45': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_45',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_46': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_46',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_46': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_46',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_47': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_47',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_47': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_47',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_48': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_48',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_48': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_48',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_49': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_49',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_49': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_49',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_50': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_50',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_50': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_50',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_51': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_51',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_51': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_51',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_52': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_52',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_52': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_52',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_53': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_53',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_53': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_53',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_54': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_54',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_54': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_54',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_55': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_55',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_55': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_55',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_56': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_56',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_56': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_56',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_57': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_57',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_57': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_57',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_58': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_58',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_58': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_58',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_59': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_59',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_59': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_59',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_60': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_60',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_60': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_60',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_61': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_61',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_61': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_61',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_62': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_62',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_62': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_62',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_63': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_63',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_63': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_63',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_64': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_64',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_64': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_64',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_65': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_65',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_65': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_65',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_66': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_66',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_66': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_66',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_67': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_67',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_67': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_67',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_68': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_68',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_68': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_68',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_69': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_69',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_69': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_69',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_70': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_70',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_70': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_70',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_71': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_71',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_71': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_71',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_72': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_72',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_72': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_72',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_73': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_73',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_73': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_73',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_74': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_74',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_74': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_74',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_75': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_75',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_75': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_75',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_76': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_76',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_76': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_76',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_77': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_77',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_77': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_77',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_78': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_78',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_78': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_78',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_79': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_79',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_79': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_79',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_80': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_80',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_80': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_80',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_81': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_81',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_81': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_81',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_82': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_82',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_82': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_82',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_83': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_83',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_83': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_83',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_84': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_84',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_84': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_84',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_85': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_85',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_85': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_85',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_86': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_86',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_86': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_86',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_87': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_87',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_87': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_87',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_88': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_88',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_88': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_88',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_89': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_89',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_89': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_89',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_90': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_90',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_90': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_90',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_91': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_91',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_91': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_91',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_92': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_92',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_92': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_92',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_93': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_93',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_93': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_93',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_94': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_94',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_94': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_94',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_95': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_95',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_95': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_95',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_96': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_96',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_96': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_96',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_97': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_97',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_97': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_97',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_98': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_98',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_98': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_98',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_99': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_99',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_99': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_99',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_100': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_100',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_100': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_100',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_101': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_101',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_101': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_101',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_102': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_102',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_102': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_102',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_103': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_103',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_103': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_103',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_104': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_104',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_104': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_104',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_105': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_105',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_105': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_105',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_106': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_106',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_106': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_106',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_107': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_107',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_107': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_107',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_108': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_108',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_108': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_108',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_109': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_109',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_109': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_109',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_110': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_110',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_110': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_110',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_111': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_111',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_111': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_111',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_112': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_112',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_112': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_112',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_113': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_113',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_113': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_113',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_114': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_114',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_114': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_114',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_115': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_115',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_115': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_115',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_116': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_116',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_116': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_116',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_117': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_117',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_117': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_117',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_118': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_118',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_118': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_118',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_119': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_119',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_119': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_119',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_120': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_120',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_120': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_120',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_121': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_121',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_121': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_121',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_122': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_122',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_122': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_122',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_123': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_123',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_123': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_123',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_124': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_124',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_124': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_124',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_125': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_125',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_125': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_125',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_126': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_126',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_126': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_126',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_127': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_127',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_127': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_127',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_128': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_128',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_128': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_128',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_129': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_129',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_129': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_129',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_130': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_130',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_130': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_130',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_131': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_131',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_131': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_131',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_132': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_132',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_132': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_132',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_133': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_133',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_133': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_133',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_134': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_134',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_134': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_134',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_135': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_135',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_135': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_135',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_136': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_136',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_136': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_136',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_137': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_137',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_137': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_137',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_138': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_138',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_138': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_138',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_139': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_139',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_139': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_139',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_140': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_140',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_140': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_140',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_141': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_141',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_141': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_141',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_142': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_142',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_142': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_142',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_143': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_143',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_143': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_143',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_144': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_144',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_144': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_144',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_145': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_145',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_145': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_145',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_146': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_146',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_146': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_146',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_147': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_147',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_147': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_147',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_148': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_148',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_148': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_148',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_149': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_149',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_149': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_149',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_150': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_150',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_150': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_150',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_151': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_151',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_151': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_151',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_152': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_152',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_152': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_152',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_153': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_153',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_153': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_153',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_154': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_154',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_154': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_154',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_155': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_155',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_155': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_155',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_156': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_156',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_156': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_156',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_157': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_157',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_157': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_157',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_158': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_158',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_158': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_158',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_159': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_159',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_159': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_159',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_160': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_160',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_160': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_160',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_161': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_161',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_161': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_161',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_162': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_162',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_162': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_162',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_163': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_163',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_163': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_163',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_164': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_164',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_164': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_164',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_165': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_165',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_165': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_165',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_166': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_166',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_166': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_166',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_167': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_167',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_167': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_167',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_168': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_168',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_168': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_168',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_169': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_169',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_169': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_169',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_170': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_170',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_170': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_170',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_171': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_171',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_171': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_171',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_172': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_172',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_172': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_172',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_173': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_173',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_173': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_173',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_174': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_174',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_174': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_174',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_175': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_175',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_175': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_175',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_176': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_176',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_176': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_176',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_177': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_177',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_177': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_177',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_178': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_178',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_178': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_178',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_179': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_179',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_179': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_179',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_180': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_180',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_180': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_180',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_181': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_181',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_181': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_181',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_182': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_182',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_182': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_182',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_183': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_183',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_183': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_183',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_184': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_184',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_184': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_184',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_185': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_185',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_185': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_185',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_186': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_186',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_186': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_186',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_187': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_187',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_187': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_187',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_188': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_188',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_188': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_188',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_189': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_189',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_189': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_189',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_190': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_190',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_190': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_190',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_191': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_191',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_191': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_191',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_192': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_192',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_192': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_192',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_193': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_193',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_193': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_193',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_194': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_194',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_194': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_194',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_195': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_195',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_195': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_195',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_196': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_196',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_196': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_196',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_197': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_197',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_197': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_197',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_198': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_198',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_198': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_198',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_199': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_199',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_199': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_199',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_200': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_200',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_200': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_200',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_201': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_201',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_201': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_201',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_202': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_202',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_202': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_202',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_203': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_203',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_203': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_203',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_204': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_204',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_204': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_204',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_205': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_205',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_205': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_205',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_206': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_206',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_206': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_206',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_207': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_207',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_207': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_207',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_208': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_208',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_208': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_208',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_209': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_209',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_209': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_209',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_210': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_210',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_210': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_210',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_211': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_211',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_211': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_211',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_212': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_212',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_212': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_212',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_213': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_213',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_213': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_213',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_214': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_214',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_214': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_214',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_215': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_215',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_215': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_215',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_216': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_216',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_216': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_216',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_217': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_217',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_217': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_217',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_218': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_218',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_218': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_218',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_219': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_219',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_219': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_219',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_220': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_220',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_220': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_220',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_221': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_221',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_221': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_221',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_222': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_222',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_222': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_222',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_223': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_223',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_223': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_223',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_224': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_224',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_224': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_224',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_225': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_225',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_225': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_225',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_226': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_226',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_226': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_226',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_227': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_227',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_227': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_227',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_228': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_228',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_228': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_228',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_229': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_229',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_229': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_229',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_230': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_230',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_230': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_230',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_231': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_231',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_231': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_231',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_232': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_232',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_232': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_232',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_233': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_233',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_233': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_233',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_234': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_234',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_234': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_234',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_235': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_235',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_235': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_235',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_236': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_236',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_236': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_236',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_237': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_237',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_237': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_237',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_238': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_238',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_238': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_238',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_239': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_239',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_239': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_239',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_240': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_240',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_240': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_240',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_241': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_241',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_241': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_241',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_242': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_242',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_242': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_242',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_243': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_243',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_243': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_243',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_244': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_244',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_244': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_244',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_245': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_245',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_245': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_245',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_246': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_246',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_246': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_246',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_247': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_247',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_247': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_247',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_248': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_248',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_248': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_248',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_249': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_249',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_249': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_249',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_250': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_250',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_250': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_250',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_251': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_251',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_251': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_251',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_252': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_252',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_252': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_252',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_253': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_253',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_253': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_253',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_254': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_254',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_254': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_254',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_255': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_255',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_255': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_255',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_256': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_256',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_256': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_256',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_257': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_257',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_257': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_257',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_258': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_258',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_258': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_258',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_259': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_259',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_259': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_259',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_260': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_260',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_260': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_260',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_261': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_261',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_261': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_261',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_262': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_262',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_262': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_262',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_263': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_263',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_263': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_263',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_264': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_264',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_264': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_264',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_265': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_265',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_265': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_265',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_266': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_266',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_266': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_266',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_267': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_267',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_267': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_267',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_268': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_268',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_268': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_268',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_269': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_269',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_269': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_269',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_270': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_270',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_270': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_270',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_271': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_271',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_271': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_271',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_272': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_272',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_272': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_272',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_273': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_273',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_273': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_273',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_274': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_274',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_274': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_274',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_275': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_275',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_275': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_275',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_276': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_276',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_276': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_276',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_277': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_277',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_277': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_277',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_278': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_278',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_278': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_278',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_279': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_279',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_279': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_279',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_280': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_280',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_280': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_280',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_281': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_281',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_281': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_281',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_282': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_282',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_282': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_282',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_283': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_283',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_283': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_283',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_284': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_284',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_284': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_284',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_285': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_285',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_285': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_285',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_286': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_286',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_286': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_286',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_287': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_287',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_287': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_287',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_288': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_288',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_288': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_288',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_289': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_289',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_289': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_289',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_290': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_290',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_290': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_290',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_291': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_291',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_291': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_291',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_292': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_292',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_292': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_292',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_293': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_293',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_293': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_293',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_294': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_294',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_294': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_294',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_295': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_295',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_295': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_295',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_296': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_296',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_296': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_296',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_297': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_297',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_297': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_297',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_298': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_298',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_298': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_298',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_299': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_299',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_299': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_299',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_300': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_300',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_300': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_300',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_301': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_301',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_301': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_301',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_302': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_302',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_302': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_302',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_303': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_303',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_303': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_303',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_304': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_304',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_304': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_304',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_305': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_305',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_305': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_305',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_306': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_306',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_306': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_306',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_307': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_307',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_307': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_307',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_308': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_308',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_308': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_308',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_309': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_309',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_309': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_309',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_310': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_310',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_310': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_310',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_311': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_311',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_311': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_311',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_312': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_312',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_312': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_312',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_313': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_313',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_313': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_313',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_314': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_314',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_314': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_314',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_315': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_315',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_315': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_315',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_316': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_316',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_316': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_316',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_317': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_317',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_317': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_317',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_318': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_318',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_318': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_318',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_319': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_319',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_319': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_319',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_320': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_320',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_320': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_320',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_321': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_321',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_321': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_321',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_322': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_322',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_322': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_322',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_323': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_323',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_323': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_323',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_324': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_324',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_324': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_324',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_325': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_325',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_325': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_325',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_326': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_326',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_326': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_326',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_327': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_327',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_327': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_327',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_328': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_328',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_328': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_328',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_329': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_329',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_329': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_329',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_330': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_330',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_330': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_330',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_331': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_331',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_331': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_331',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_332': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_332',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_332': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_332',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_333': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_333',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_333': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_333',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_334': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_334',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_334': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_334',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_335': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_335',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_335': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_335',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_336': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_336',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_336': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_336',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_337': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_337',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_337': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_337',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_338': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_338',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_338': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_338',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_339': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_339',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_339': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_339',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_340': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_340',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_340': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_340',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_341': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_341',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_341': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_341',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_342': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_342',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_342': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_342',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_343': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_343',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_343': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_343',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_344': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_344',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_344': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_344',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_345': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_345',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_345': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_345',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_346': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_346',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_346': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_346',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_347': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_347',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_347': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_347',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_348': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_348',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_348': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_348',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_349': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_349',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_349': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_349',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_350': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_350',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_350': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_350',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_351': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_351',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_351': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_351',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_352': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_352',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_352': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_352',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_353': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_353',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_353': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_353',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_354': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_354',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_354': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_354',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_355': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_355',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_355': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_355',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_356': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_356',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_356': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_356',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_357': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_357',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_357': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_357',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_358': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_358',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_358': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_358',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_359': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_359',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_359': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_359',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_360': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_360',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_360': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_360',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_361': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_361',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_361': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_361',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_362': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_362',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_362': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_362',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_363': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_363',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_363': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_363',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_364': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_364',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_364': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_364',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_365': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_365',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_365': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_365',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_366': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_366',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_366': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_366',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_367': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_367',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_367': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_367',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_368': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_368',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_368': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_368',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_369': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_369',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_369': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_369',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_370': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_370',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_370': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_370',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_371': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_371',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_371': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_371',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_372': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_372',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_372': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_372',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_373': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_373',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_373': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_373',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_374': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_374',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_374': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_374',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_375': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_375',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_375': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_375',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_376': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_376',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_376': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_376',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_377': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_377',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_377': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_377',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_378': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_378',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_378': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_378',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_379': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_379',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_379': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_379',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_380': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_380',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_380': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_380',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_381': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_381',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_381': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_381',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_382': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_382',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_382': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_382',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_383': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_383',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_383': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_383',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_384': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_384',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_384': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_384',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_385': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_385',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_385': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_385',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_386': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_386',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_386': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_386',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_387': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_387',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_387': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_387',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_388': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_388',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_388': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_388',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_389': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_389',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_389': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_389',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_390': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_390',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_390': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_390',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_391': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_391',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_391': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_391',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_392': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_392',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_392': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_392',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_393': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_393',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_393': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_393',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_394': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_394',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_394': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_394',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_395': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_395',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_395': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_395',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_396': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_396',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_396': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_396',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_397': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_397',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_397': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_397',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_398': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_398',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_398': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_398',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_399': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_399',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_399': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_399',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_400': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_400',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_400': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_400',
            },
            'operation': 'control',
        },
        'gate_29_baked_pulse_401': {
            'length': 204,
            'waveforms': {
                'single': 'gate_29_baked_wf_401',
            },
            'operation': 'control',
        },
        'gate_36_baked_pulse_401': {
            'length': 204,
            'waveforms': {
                'single': 'gate_36_baked_wf_401',
            },
            'operation': 'control',
        },
    },
    'waveforms': {
        'const_wf': {
            'sample': 0.25,
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
        'gate_29_baked_wf_0': {
            'samples': [0.0] * 204,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_0': {
            'samples': [0.0] * 204,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_1': {
            'samples': [0.0] * 203 + [-0.2081559],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_1': {
            'samples': [0.0] * 203 + [0.254468348],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_2': {
            'samples': [0.0] * 202 + [-0.2081559] * 2,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_2': {
            'samples': [0.0] * 202 + [0.254468348] * 2,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_3': {
            'samples': [0.0] * 201 + [-0.2081559] * 3,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_3': {
            'samples': [0.0] * 201 + [0.254468348] * 3,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_4': {
            'samples': [0.0] * 200 + [-0.2081559] * 4,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_4': {
            'samples': [0.0] * 200 + [0.254468348] * 4,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_5': {
            'samples': [0.0] * 199 + [-0.2081559] * 5,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_5': {
            'samples': [0.0] * 199 + [0.254468348] * 5,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_6': {
            'samples': [0.0] * 198 + [-0.2081559] * 6,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_6': {
            'samples': [0.0] * 198 + [0.254468348] * 6,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_7': {
            'samples': [0.0] * 197 + [-0.2081559] * 7,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_7': {
            'samples': [0.0] * 197 + [0.254468348] * 7,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_8': {
            'samples': [0.0] * 196 + [-0.2081559] * 8,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_8': {
            'samples': [0.0] * 196 + [0.254468348] * 8,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_9': {
            'samples': [0.0] * 195 + [-0.2081559] * 9,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_9': {
            'samples': [0.0] * 195 + [0.254468348] * 9,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_10': {
            'samples': [0.0] * 194 + [-0.2081559] * 10,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_10': {
            'samples': [0.0] * 194 + [0.254468348] * 10,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_11': {
            'samples': [0.0] * 193 + [-0.2081559] * 11,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_11': {
            'samples': [0.0] * 193 + [0.254468348] * 11,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_12': {
            'samples': [0.0] * 192 + [-0.2081559] * 12,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_12': {
            'samples': [0.0] * 192 + [0.254468348] * 12,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_13': {
            'samples': [0.0] * 191 + [-0.2081559] * 13,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_13': {
            'samples': [0.0] * 191 + [0.254468348] * 13,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_14': {
            'samples': [0.0] * 190 + [-0.2081559] * 14,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_14': {
            'samples': [0.0] * 190 + [0.254468348] * 14,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_15': {
            'samples': [0.0] * 189 + [-0.2081559] * 15,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_15': {
            'samples': [0.0] * 189 + [0.254468348] * 15,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_16': {
            'samples': [0.0] * 188 + [-0.2081559] * 16,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_16': {
            'samples': [0.0] * 188 + [0.254468348] * 16,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_17': {
            'samples': [0.0] * 187 + [-0.2081559] * 17,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_17': {
            'samples': [0.0] * 187 + [0.254468348] * 17,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_18': {
            'samples': [0.0] * 186 + [-0.2081559] * 18,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_18': {
            'samples': [0.0] * 186 + [0.254468348] * 18,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_19': {
            'samples': [0.0] * 185 + [-0.2081559] * 19,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_19': {
            'samples': [0.0] * 185 + [0.254468348] * 19,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_20': {
            'samples': [0.0] * 184 + [-0.2081559] * 20,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_20': {
            'samples': [0.0] * 184 + [0.254468348] * 20,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_21': {
            'samples': [0.0] * 183 + [-0.2081559] * 21,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_21': {
            'samples': [0.0] * 183 + [0.254468348] * 21,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_22': {
            'samples': [0.0] * 182 + [-0.2081559] * 22,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_22': {
            'samples': [0.0] * 182 + [0.254468348] * 22,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_23': {
            'samples': [0.0] * 181 + [-0.2081559] * 23,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_23': {
            'samples': [0.0] * 181 + [0.254468348] * 23,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_24': {
            'samples': [0.0] * 180 + [-0.2081559] * 24,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_24': {
            'samples': [0.0] * 180 + [0.254468348] * 24,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_25': {
            'samples': [0.0] * 179 + [-0.2081559] * 25,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_25': {
            'samples': [0.0] * 179 + [0.254468348] * 25,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_26': {
            'samples': [0.0] * 178 + [-0.2081559] * 26,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_26': {
            'samples': [0.0] * 178 + [0.254468348] * 26,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_27': {
            'samples': [0.0] * 177 + [-0.2081559] * 27,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_27': {
            'samples': [0.0] * 177 + [0.254468348] * 27,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_28': {
            'samples': [0.0] * 176 + [-0.2081559] * 28,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_28': {
            'samples': [0.0] * 176 + [0.254468348] * 28,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_29': {
            'samples': [0.0] * 175 + [-0.2081559] * 29,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_29': {
            'samples': [0.0] * 175 + [0.254468348] * 29,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_30': {
            'samples': [0.0] * 174 + [-0.2081559] * 30,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_30': {
            'samples': [0.0] * 174 + [0.254468348] * 30,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_31': {
            'samples': [0.0] * 173 + [-0.2081559] * 31,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_31': {
            'samples': [0.0] * 173 + [0.254468348] * 31,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_32': {
            'samples': [0.0] * 172 + [-0.2081559] * 32,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_32': {
            'samples': [0.0] * 172 + [0.254468348] * 32,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_33': {
            'samples': [0.0] * 171 + [-0.2081559] * 33,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_33': {
            'samples': [0.0] * 171 + [0.254468348] * 33,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_34': {
            'samples': [0.0] * 170 + [-0.2081559] * 34,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_34': {
            'samples': [0.0] * 170 + [0.254468348] * 34,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_35': {
            'samples': [0.0] * 169 + [-0.2081559] * 35,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_35': {
            'samples': [0.0] * 169 + [0.254468348] * 35,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_36': {
            'samples': [0.0] * 168 + [-0.2081559] * 36,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_36': {
            'samples': [0.0] * 168 + [0.254468348] * 36,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_37': {
            'samples': [0.0] * 167 + [-0.2081559] * 37,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_37': {
            'samples': [0.0] * 167 + [0.254468348] * 37,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_38': {
            'samples': [0.0] * 166 + [-0.2081559] * 38,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_38': {
            'samples': [0.0] * 166 + [0.254468348] * 38,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_39': {
            'samples': [0.0] * 165 + [-0.2081559] * 39,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_39': {
            'samples': [0.0] * 165 + [0.254468348] * 39,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_40': {
            'samples': [0.0] * 164 + [-0.2081559] * 40,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_40': {
            'samples': [0.0] * 164 + [0.254468348] * 40,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_41': {
            'samples': [0.0] * 163 + [-0.2081559] * 41,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_41': {
            'samples': [0.0] * 163 + [0.254468348] * 41,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_42': {
            'samples': [0.0] * 162 + [-0.2081559] * 42,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_42': {
            'samples': [0.0] * 162 + [0.254468348] * 42,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_43': {
            'samples': [0.0] * 161 + [-0.2081559] * 43,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_43': {
            'samples': [0.0] * 161 + [0.254468348] * 43,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_44': {
            'samples': [0.0] * 160 + [-0.2081559] * 44,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_44': {
            'samples': [0.0] * 160 + [0.254468348] * 44,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_45': {
            'samples': [0.0] * 159 + [-0.2081559] * 45,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_45': {
            'samples': [0.0] * 159 + [0.254468348] * 45,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_46': {
            'samples': [0.0] * 158 + [-0.2081559] * 46,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_46': {
            'samples': [0.0] * 158 + [0.254468348] * 46,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_47': {
            'samples': [0.0] * 157 + [-0.2081559] * 47,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_47': {
            'samples': [0.0] * 157 + [0.254468348] * 47,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_48': {
            'samples': [0.0] * 156 + [-0.2081559] * 48,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_48': {
            'samples': [0.0] * 156 + [0.254468348] * 48,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_49': {
            'samples': [0.0] * 155 + [-0.2081559] * 49,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_49': {
            'samples': [0.0] * 155 + [0.254468348] * 49,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_50': {
            'samples': [0.0] * 154 + [-0.2081559] * 50,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_50': {
            'samples': [0.0] * 154 + [0.254468348] * 50,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_51': {
            'samples': [0.0] * 153 + [-0.2081559] * 51,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_51': {
            'samples': [0.0] * 153 + [0.254468348] * 51,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_52': {
            'samples': [0.0] * 152 + [-0.2081559] * 52,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_52': {
            'samples': [0.0] * 152 + [0.254468348] * 52,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_53': {
            'samples': [0.0] * 151 + [-0.2081559] * 53,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_53': {
            'samples': [0.0] * 151 + [0.254468348] * 53,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_54': {
            'samples': [0.0] * 150 + [-0.2081559] * 54,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_54': {
            'samples': [0.0] * 150 + [0.254468348] * 54,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_55': {
            'samples': [0.0] * 149 + [-0.2081559] * 55,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_55': {
            'samples': [0.0] * 149 + [0.254468348] * 55,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_56': {
            'samples': [0.0] * 148 + [-0.2081559] * 56,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_56': {
            'samples': [0.0] * 148 + [0.254468348] * 56,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_57': {
            'samples': [0.0] * 147 + [-0.2081559] * 57,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_57': {
            'samples': [0.0] * 147 + [0.254468348] * 57,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_58': {
            'samples': [0.0] * 146 + [-0.2081559] * 58,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_58': {
            'samples': [0.0] * 146 + [0.254468348] * 58,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_59': {
            'samples': [0.0] * 145 + [-0.2081559] * 59,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_59': {
            'samples': [0.0] * 145 + [0.254468348] * 59,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_60': {
            'samples': [0.0] * 144 + [-0.2081559] * 60,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_60': {
            'samples': [0.0] * 144 + [0.254468348] * 60,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_61': {
            'samples': [0.0] * 143 + [-0.2081559] * 61,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_61': {
            'samples': [0.0] * 143 + [0.254468348] * 61,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_62': {
            'samples': [0.0] * 142 + [-0.2081559] * 62,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_62': {
            'samples': [0.0] * 142 + [0.254468348] * 62,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_63': {
            'samples': [0.0] * 141 + [-0.2081559] * 63,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_63': {
            'samples': [0.0] * 141 + [0.254468348] * 63,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_64': {
            'samples': [0.0] * 140 + [-0.2081559] * 64,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_64': {
            'samples': [0.0] * 140 + [0.254468348] * 64,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_65': {
            'samples': [0.0] * 139 + [-0.2081559] * 65,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_65': {
            'samples': [0.0] * 139 + [0.254468348] * 65,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_66': {
            'samples': [0.0] * 138 + [-0.2081559] * 66,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_66': {
            'samples': [0.0] * 138 + [0.254468348] * 66,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_67': {
            'samples': [0.0] * 137 + [-0.2081559] * 67,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_67': {
            'samples': [0.0] * 137 + [0.254468348] * 67,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_68': {
            'samples': [0.0] * 136 + [-0.2081559] * 68,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_68': {
            'samples': [0.0] * 136 + [0.254468348] * 68,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_69': {
            'samples': [0.0] * 135 + [-0.2081559] * 69,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_69': {
            'samples': [0.0] * 135 + [0.254468348] * 69,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_70': {
            'samples': [0.0] * 134 + [-0.2081559] * 70,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_70': {
            'samples': [0.0] * 134 + [0.254468348] * 70,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_71': {
            'samples': [0.0] * 133 + [-0.2081559] * 71,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_71': {
            'samples': [0.0] * 133 + [0.254468348] * 71,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_72': {
            'samples': [0.0] * 132 + [-0.2081559] * 72,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_72': {
            'samples': [0.0] * 132 + [0.254468348] * 72,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_73': {
            'samples': [0.0] * 131 + [-0.2081559] * 73,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_73': {
            'samples': [0.0] * 131 + [0.254468348] * 73,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_74': {
            'samples': [0.0] * 130 + [-0.2081559] * 74,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_74': {
            'samples': [0.0] * 130 + [0.254468348] * 74,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_75': {
            'samples': [0.0] * 129 + [-0.2081559] * 75,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_75': {
            'samples': [0.0] * 129 + [0.254468348] * 75,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_76': {
            'samples': [0.0] * 128 + [-0.2081559] * 76,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_76': {
            'samples': [0.0] * 128 + [0.254468348] * 76,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_77': {
            'samples': [0.0] * 127 + [-0.2081559] * 77,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_77': {
            'samples': [0.0] * 127 + [0.254468348] * 77,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_78': {
            'samples': [0.0] * 126 + [-0.2081559] * 78,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_78': {
            'samples': [0.0] * 126 + [0.254468348] * 78,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_79': {
            'samples': [0.0] * 125 + [-0.2081559] * 79,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_79': {
            'samples': [0.0] * 125 + [0.254468348] * 79,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_80': {
            'samples': [0.0] * 124 + [-0.2081559] * 80,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_80': {
            'samples': [0.0] * 124 + [0.254468348] * 80,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_81': {
            'samples': [0.0] * 123 + [-0.2081559] * 81,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_81': {
            'samples': [0.0] * 123 + [0.254468348] * 81,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_82': {
            'samples': [0.0] * 122 + [-0.2081559] * 82,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_82': {
            'samples': [0.0] * 122 + [0.254468348] * 82,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_83': {
            'samples': [0.0] * 121 + [-0.2081559] * 83,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_83': {
            'samples': [0.0] * 121 + [0.254468348] * 83,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_84': {
            'samples': [0.0] * 120 + [-0.2081559] * 84,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_84': {
            'samples': [0.0] * 120 + [0.254468348] * 84,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_85': {
            'samples': [0.0] * 119 + [-0.2081559] * 85,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_85': {
            'samples': [0.0] * 119 + [0.254468348] * 85,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_86': {
            'samples': [0.0] * 118 + [-0.2081559] * 86,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_86': {
            'samples': [0.0] * 118 + [0.254468348] * 86,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_87': {
            'samples': [0.0] * 117 + [-0.2081559] * 87,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_87': {
            'samples': [0.0] * 117 + [0.254468348] * 87,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_88': {
            'samples': [0.0] * 116 + [-0.2081559] * 88,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_88': {
            'samples': [0.0] * 116 + [0.254468348] * 88,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_89': {
            'samples': [0.0] * 115 + [-0.2081559] * 89,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_89': {
            'samples': [0.0] * 115 + [0.254468348] * 89,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_90': {
            'samples': [0.0] * 114 + [-0.2081559] * 90,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_90': {
            'samples': [0.0] * 114 + [0.254468348] * 90,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_91': {
            'samples': [0.0] * 113 + [-0.2081559] * 91,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_91': {
            'samples': [0.0] * 113 + [0.254468348] * 91,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_92': {
            'samples': [0.0] * 112 + [-0.2081559] * 92,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_92': {
            'samples': [0.0] * 112 + [0.254468348] * 92,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_93': {
            'samples': [0.0] * 111 + [-0.2081559] * 93,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_93': {
            'samples': [0.0] * 111 + [0.254468348] * 93,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_94': {
            'samples': [0.0] * 110 + [-0.2081559] * 94,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_94': {
            'samples': [0.0] * 110 + [0.254468348] * 94,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_95': {
            'samples': [0.0] * 109 + [-0.2081559] * 95,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_95': {
            'samples': [0.0] * 109 + [0.254468348] * 95,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_96': {
            'samples': [0.0] * 108 + [-0.2081559] * 96,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_96': {
            'samples': [0.0] * 108 + [0.254468348] * 96,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_97': {
            'samples': [0.0] * 107 + [-0.2081559] * 97,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_97': {
            'samples': [0.0] * 107 + [0.254468348] * 97,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_98': {
            'samples': [0.0] * 106 + [-0.2081559] * 98,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_98': {
            'samples': [0.0] * 106 + [0.254468348] * 98,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_99': {
            'samples': [0.0] * 105 + [-0.2081559] * 99,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_99': {
            'samples': [0.0] * 105 + [0.254468348] * 99,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_100': {
            'samples': [0.0] * 104 + [-0.2081559] * 100,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_100': {
            'samples': [0.0] * 104 + [0.254468348] * 100,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_101': {
            'samples': [0.0] * 103 + [-0.2081559] * 101,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_101': {
            'samples': [0.0] * 103 + [0.254468348] * 101,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_102': {
            'samples': [0.0] * 102 + [-0.2081559] * 102,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_102': {
            'samples': [0.0] * 102 + [0.254468348] * 102,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_103': {
            'samples': [0.0] * 101 + [-0.2081559] * 103,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_103': {
            'samples': [0.0] * 101 + [0.254468348] * 103,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_104': {
            'samples': [0.0] * 100 + [-0.2081559] * 104,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_104': {
            'samples': [0.0] * 100 + [0.254468348] * 104,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_105': {
            'samples': [0.0] * 99 + [-0.2081559] * 105,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_105': {
            'samples': [0.0] * 99 + [0.254468348] * 105,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_106': {
            'samples': [0.0] * 98 + [-0.2081559] * 106,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_106': {
            'samples': [0.0] * 98 + [0.254468348] * 106,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_107': {
            'samples': [0.0] * 97 + [-0.2081559] * 107,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_107': {
            'samples': [0.0] * 97 + [0.254468348] * 107,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_108': {
            'samples': [0.0] * 96 + [-0.2081559] * 108,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_108': {
            'samples': [0.0] * 96 + [0.254468348] * 108,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_109': {
            'samples': [0.0] * 95 + [-0.2081559] * 109,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_109': {
            'samples': [0.0] * 95 + [0.254468348] * 109,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_110': {
            'samples': [0.0] * 94 + [-0.2081559] * 110,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_110': {
            'samples': [0.0] * 94 + [0.254468348] * 110,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_111': {
            'samples': [0.0] * 93 + [-0.2081559] * 111,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_111': {
            'samples': [0.0] * 93 + [0.254468348] * 111,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_112': {
            'samples': [0.0] * 92 + [-0.2081559] * 112,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_112': {
            'samples': [0.0] * 92 + [0.254468348] * 112,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_113': {
            'samples': [0.0] * 91 + [-0.2081559] * 113,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_113': {
            'samples': [0.0] * 91 + [0.254468348] * 113,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_114': {
            'samples': [0.0] * 90 + [-0.2081559] * 114,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_114': {
            'samples': [0.0] * 90 + [0.254468348] * 114,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_115': {
            'samples': [0.0] * 89 + [-0.2081559] * 115,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_115': {
            'samples': [0.0] * 89 + [0.254468348] * 115,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_116': {
            'samples': [0.0] * 88 + [-0.2081559] * 116,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_116': {
            'samples': [0.0] * 88 + [0.254468348] * 116,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_117': {
            'samples': [0.0] * 87 + [-0.2081559] * 117,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_117': {
            'samples': [0.0] * 87 + [0.254468348] * 117,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_118': {
            'samples': [0.0] * 86 + [-0.2081559] * 118,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_118': {
            'samples': [0.0] * 86 + [0.254468348] * 118,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_119': {
            'samples': [0.0] * 85 + [-0.2081559] * 119,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_119': {
            'samples': [0.0] * 85 + [0.254468348] * 119,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_120': {
            'samples': [0.0] * 84 + [-0.2081559] * 120,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_120': {
            'samples': [0.0] * 84 + [0.254468348] * 120,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_121': {
            'samples': [0.0] * 83 + [-0.2081559] * 121,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_121': {
            'samples': [0.0] * 83 + [0.254468348] * 121,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_122': {
            'samples': [0.0] * 82 + [-0.2081559] * 122,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_122': {
            'samples': [0.0] * 82 + [0.254468348] * 122,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_123': {
            'samples': [0.0] * 81 + [-0.2081559] * 123,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_123': {
            'samples': [0.0] * 81 + [0.254468348] * 123,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_124': {
            'samples': [0.0] * 80 + [-0.2081559] * 124,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_124': {
            'samples': [0.0] * 80 + [0.254468348] * 124,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_125': {
            'samples': [0.0] * 79 + [-0.2081559] * 125,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_125': {
            'samples': [0.0] * 79 + [0.254468348] * 125,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_126': {
            'samples': [0.0] * 78 + [-0.2081559] * 126,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_126': {
            'samples': [0.0] * 78 + [0.254468348] * 126,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_127': {
            'samples': [0.0] * 77 + [-0.2081559] * 127,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_127': {
            'samples': [0.0] * 77 + [0.254468348] * 127,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_128': {
            'samples': [0.0] * 76 + [-0.2081559] * 128,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_128': {
            'samples': [0.0] * 76 + [0.254468348] * 128,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_129': {
            'samples': [0.0] * 75 + [-0.2081559] * 129,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_129': {
            'samples': [0.0] * 75 + [0.254468348] * 129,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_130': {
            'samples': [0.0] * 74 + [-0.2081559] * 130,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_130': {
            'samples': [0.0] * 74 + [0.254468348] * 130,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_131': {
            'samples': [0.0] * 73 + [-0.2081559] * 131,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_131': {
            'samples': [0.0] * 73 + [0.254468348] * 131,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_132': {
            'samples': [0.0] * 72 + [-0.2081559] * 132,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_132': {
            'samples': [0.0] * 72 + [0.254468348] * 132,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_133': {
            'samples': [0.0] * 71 + [-0.2081559] * 133,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_133': {
            'samples': [0.0] * 71 + [0.254468348] * 133,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_134': {
            'samples': [0.0] * 70 + [-0.2081559] * 134,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_134': {
            'samples': [0.0] * 70 + [0.254468348] * 134,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_135': {
            'samples': [0.0] * 69 + [-0.2081559] * 135,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_135': {
            'samples': [0.0] * 69 + [0.254468348] * 135,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_136': {
            'samples': [0.0] * 68 + [-0.2081559] * 136,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_136': {
            'samples': [0.0] * 68 + [0.254468348] * 136,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_137': {
            'samples': [0.0] * 67 + [-0.2081559] * 137,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_137': {
            'samples': [0.0] * 67 + [0.254468348] * 137,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_138': {
            'samples': [0.0] * 66 + [-0.2081559] * 138,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_138': {
            'samples': [0.0] * 66 + [0.254468348] * 138,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_139': {
            'samples': [0.0] * 65 + [-0.2081559] * 139,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_139': {
            'samples': [0.0] * 65 + [0.254468348] * 139,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_140': {
            'samples': [0.0] * 64 + [-0.2081559] * 140,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_140': {
            'samples': [0.0] * 64 + [0.254468348] * 140,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_141': {
            'samples': [0.0] * 63 + [-0.2081559] * 141,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_141': {
            'samples': [0.0] * 63 + [0.254468348] * 141,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_142': {
            'samples': [0.0] * 62 + [-0.2081559] * 142,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_142': {
            'samples': [0.0] * 62 + [0.254468348] * 142,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_143': {
            'samples': [0.0] * 61 + [-0.2081559] * 143,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_143': {
            'samples': [0.0] * 61 + [0.254468348] * 143,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_144': {
            'samples': [0.0] * 60 + [-0.2081559] * 144,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_144': {
            'samples': [0.0] * 60 + [0.254468348] * 144,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_145': {
            'samples': [0.0] * 59 + [-0.2081559] * 145,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_145': {
            'samples': [0.0] * 59 + [0.254468348] * 145,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_146': {
            'samples': [0.0] * 58 + [-0.2081559] * 146,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_146': {
            'samples': [0.0] * 58 + [0.254468348] * 146,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_147': {
            'samples': [0.0] * 57 + [-0.2081559] * 147,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_147': {
            'samples': [0.0] * 57 + [0.254468348] * 147,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_148': {
            'samples': [0.0] * 56 + [-0.2081559] * 148,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_148': {
            'samples': [0.0] * 56 + [0.254468348] * 148,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_149': {
            'samples': [0.0] * 55 + [-0.2081559] * 149,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_149': {
            'samples': [0.0] * 55 + [0.254468348] * 149,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_150': {
            'samples': [0.0] * 54 + [-0.2081559] * 150,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_150': {
            'samples': [0.0] * 54 + [0.254468348] * 150,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_151': {
            'samples': [0.0] * 53 + [-0.2081559] * 151,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_151': {
            'samples': [0.0] * 53 + [0.254468348] * 151,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_152': {
            'samples': [0.0] * 52 + [-0.2081559] * 152,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_152': {
            'samples': [0.0] * 52 + [0.254468348] * 152,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_153': {
            'samples': [0.0] * 51 + [-0.2081559] * 153,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_153': {
            'samples': [0.0] * 51 + [0.254468348] * 153,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_154': {
            'samples': [0.0] * 50 + [-0.2081559] * 154,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_154': {
            'samples': [0.0] * 50 + [0.254468348] * 154,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_155': {
            'samples': [0.0] * 49 + [-0.2081559] * 155,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_155': {
            'samples': [0.0] * 49 + [0.254468348] * 155,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_156': {
            'samples': [0.0] * 48 + [-0.2081559] * 156,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_156': {
            'samples': [0.0] * 48 + [0.254468348] * 156,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_157': {
            'samples': [0.0] * 47 + [-0.2081559] * 157,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_157': {
            'samples': [0.0] * 47 + [0.254468348] * 157,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_158': {
            'samples': [0.0] * 46 + [-0.2081559] * 158,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_158': {
            'samples': [0.0] * 46 + [0.254468348] * 158,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_159': {
            'samples': [0.0] * 45 + [-0.2081559] * 159,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_159': {
            'samples': [0.0] * 45 + [0.254468348] * 159,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_160': {
            'samples': [0.0] * 44 + [-0.2081559] * 160,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_160': {
            'samples': [0.0] * 44 + [0.254468348] * 160,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_161': {
            'samples': [0.0] * 43 + [-0.2081559] * 161,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_161': {
            'samples': [0.0] * 43 + [0.254468348] * 161,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_162': {
            'samples': [0.0] * 42 + [-0.2081559] * 162,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_162': {
            'samples': [0.0] * 42 + [0.254468348] * 162,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_163': {
            'samples': [0.0] * 41 + [-0.2081559] * 163,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_163': {
            'samples': [0.0] * 41 + [0.254468348] * 163,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_164': {
            'samples': [0.0] * 40 + [-0.2081559] * 164,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_164': {
            'samples': [0.0] * 40 + [0.254468348] * 164,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_165': {
            'samples': [0.0] * 39 + [-0.2081559] * 165,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_165': {
            'samples': [0.0] * 39 + [0.254468348] * 165,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_166': {
            'samples': [0.0] * 38 + [-0.2081559] * 166,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_166': {
            'samples': [0.0] * 38 + [0.254468348] * 166,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_167': {
            'samples': [0.0] * 37 + [-0.2081559] * 167,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_167': {
            'samples': [0.0] * 37 + [0.254468348] * 167,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_168': {
            'samples': [0.0] * 36 + [-0.2081559] * 168,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_168': {
            'samples': [0.0] * 36 + [0.254468348] * 168,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_169': {
            'samples': [0.0] * 35 + [-0.2081559] * 169,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_169': {
            'samples': [0.0] * 35 + [0.254468348] * 169,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_170': {
            'samples': [0.0] * 34 + [-0.2081559] * 170,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_170': {
            'samples': [0.0] * 34 + [0.254468348] * 170,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_171': {
            'samples': [0.0] * 33 + [-0.2081559] * 171,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_171': {
            'samples': [0.0] * 33 + [0.254468348] * 171,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_172': {
            'samples': [0.0] * 32 + [-0.2081559] * 172,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_172': {
            'samples': [0.0] * 32 + [0.254468348] * 172,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_173': {
            'samples': [0.0] * 31 + [-0.2081559] * 173,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_173': {
            'samples': [0.0] * 31 + [0.254468348] * 173,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_174': {
            'samples': [0.0] * 30 + [-0.2081559] * 174,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_174': {
            'samples': [0.0] * 30 + [0.254468348] * 174,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_175': {
            'samples': [0.0] * 29 + [-0.2081559] * 175,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_175': {
            'samples': [0.0] * 29 + [0.254468348] * 175,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_176': {
            'samples': [0.0] * 28 + [-0.2081559] * 176,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_176': {
            'samples': [0.0] * 28 + [0.254468348] * 176,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_177': {
            'samples': [0.0] * 27 + [-0.2081559] * 177,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_177': {
            'samples': [0.0] * 27 + [0.254468348] * 177,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_178': {
            'samples': [0.0] * 26 + [-0.2081559] * 178,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_178': {
            'samples': [0.0] * 26 + [0.254468348] * 178,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_179': {
            'samples': [0.0] * 25 + [-0.2081559] * 179,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_179': {
            'samples': [0.0] * 25 + [0.254468348] * 179,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_180': {
            'samples': [0.0] * 24 + [-0.2081559] * 180,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_180': {
            'samples': [0.0] * 24 + [0.254468348] * 180,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_181': {
            'samples': [0.0] * 23 + [-0.2081559] * 181,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_181': {
            'samples': [0.0] * 23 + [0.254468348] * 181,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_182': {
            'samples': [0.0] * 22 + [-0.2081559] * 182,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_182': {
            'samples': [0.0] * 22 + [0.254468348] * 182,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_183': {
            'samples': [0.0] * 21 + [-0.2081559] * 183,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_183': {
            'samples': [0.0] * 21 + [0.254468348] * 183,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_184': {
            'samples': [0.0] * 20 + [-0.2081559] * 184,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_184': {
            'samples': [0.0] * 20 + [0.254468348] * 184,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_185': {
            'samples': [0.0] * 19 + [-0.2081559] * 185,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_185': {
            'samples': [0.0] * 19 + [0.254468348] * 185,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_186': {
            'samples': [0.0] * 18 + [-0.2081559] * 186,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_186': {
            'samples': [0.0] * 18 + [0.254468348] * 186,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_187': {
            'samples': [0.0] * 17 + [-0.2081559] * 187,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_187': {
            'samples': [0.0] * 17 + [0.254468348] * 187,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_188': {
            'samples': [0.0] * 16 + [-0.2081559] * 188,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_188': {
            'samples': [0.0] * 16 + [0.254468348] * 188,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_189': {
            'samples': [0.0] * 15 + [-0.2081559] * 189,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_189': {
            'samples': [0.0] * 15 + [0.254468348] * 189,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_190': {
            'samples': [0.0] * 14 + [-0.2081559] * 190,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_190': {
            'samples': [0.0] * 14 + [0.254468348] * 190,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_191': {
            'samples': [0.0] * 13 + [-0.2081559] * 191,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_191': {
            'samples': [0.0] * 13 + [0.254468348] * 191,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_192': {
            'samples': [0.0] * 12 + [-0.2081559] * 192,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_192': {
            'samples': [0.0] * 12 + [0.254468348] * 192,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_193': {
            'samples': [0.0] * 11 + [-0.2081559] * 193,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_193': {
            'samples': [0.0] * 11 + [0.254468348] * 193,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_194': {
            'samples': [0.0] * 10 + [-0.2081559] * 194,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_194': {
            'samples': [0.0] * 10 + [0.254468348] * 194,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_195': {
            'samples': [0.0] * 9 + [-0.2081559] * 195,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_195': {
            'samples': [0.0] * 9 + [0.254468348] * 195,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_196': {
            'samples': [0.0] * 8 + [-0.2081559] * 196,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_196': {
            'samples': [0.0] * 8 + [0.254468348] * 196,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_197': {
            'samples': [0.0] * 7 + [-0.2081559] * 197,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_197': {
            'samples': [0.0] * 7 + [0.254468348] * 197,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_198': {
            'samples': [0.0] * 6 + [-0.2081559] * 198,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_198': {
            'samples': [0.0] * 6 + [0.254468348] * 198,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_199': {
            'samples': [0.0] * 5 + [-0.2081559] * 199,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_199': {
            'samples': [0.0] * 5 + [0.254468348] * 199,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_200': {
            'samples': [0.0] * 4 + [-0.2081559] * 200,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_200': {
            'samples': [0.0] * 4 + [0.254468348] * 200,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_201': {
            'samples': [0.0] * 204,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_201': {
            'samples': [0.0] * 204,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_202': {
            'samples': [0.0] * 203 + [-0.2081559],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_202': {
            'samples': [0.0] * 203 + [0.254468348],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_203': {
            'samples': [0.0] * 202 + [-0.2081559] * 2,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_203': {
            'samples': [0.0] * 202 + [0.254468348] * 2,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_204': {
            'samples': [0.0] * 201 + [-0.2081559] * 3,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_204': {
            'samples': [0.0] * 201 + [0.254468348] * 3,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_205': {
            'samples': [0.0] * 200 + [-0.2081559] * 4,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_205': {
            'samples': [0.0] * 200 + [0.254468348] * 4,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_206': {
            'samples': [0.0] * 199 + [-0.2081559] * 5,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_206': {
            'samples': [0.0] * 199 + [0.254468348] * 5,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_207': {
            'samples': [0.0] * 198 + [-0.2081559] * 6,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_207': {
            'samples': [0.0] * 198 + [0.254468348] * 6,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_208': {
            'samples': [0.0] * 197 + [-0.2081559] * 7,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_208': {
            'samples': [0.0] * 197 + [0.254468348] * 7,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_209': {
            'samples': [0.0] * 196 + [-0.2081559] * 8,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_209': {
            'samples': [0.0] * 196 + [0.254468348] * 8,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_210': {
            'samples': [0.0] * 195 + [-0.2081559] * 9,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_210': {
            'samples': [0.0] * 195 + [0.254468348] * 9,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_211': {
            'samples': [0.0] * 194 + [-0.2081559] * 10,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_211': {
            'samples': [0.0] * 194 + [0.254468348] * 10,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_212': {
            'samples': [0.0] * 193 + [-0.2081559] * 11,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_212': {
            'samples': [0.0] * 193 + [0.254468348] * 11,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_213': {
            'samples': [0.0] * 192 + [-0.2081559] * 12,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_213': {
            'samples': [0.0] * 192 + [0.254468348] * 12,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_214': {
            'samples': [0.0] * 191 + [-0.2081559] * 13,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_214': {
            'samples': [0.0] * 191 + [0.254468348] * 13,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_215': {
            'samples': [0.0] * 190 + [-0.2081559] * 14,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_215': {
            'samples': [0.0] * 190 + [0.254468348] * 14,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_216': {
            'samples': [0.0] * 189 + [-0.2081559] * 15,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_216': {
            'samples': [0.0] * 189 + [0.254468348] * 15,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_217': {
            'samples': [0.0] * 188 + [-0.2081559] * 16,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_217': {
            'samples': [0.0] * 188 + [0.254468348] * 16,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_218': {
            'samples': [0.0] * 187 + [-0.2081559] * 17,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_218': {
            'samples': [0.0] * 187 + [0.254468348] * 17,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_219': {
            'samples': [0.0] * 186 + [-0.2081559] * 18,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_219': {
            'samples': [0.0] * 186 + [0.254468348] * 18,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_220': {
            'samples': [0.0] * 185 + [-0.2081559] * 19,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_220': {
            'samples': [0.0] * 185 + [0.254468348] * 19,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_221': {
            'samples': [0.0] * 184 + [-0.2081559] * 20,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_221': {
            'samples': [0.0] * 184 + [0.254468348] * 20,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_222': {
            'samples': [0.0] * 183 + [-0.2081559] * 21,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_222': {
            'samples': [0.0] * 183 + [0.254468348] * 21,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_223': {
            'samples': [0.0] * 182 + [-0.2081559] * 22,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_223': {
            'samples': [0.0] * 182 + [0.254468348] * 22,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_224': {
            'samples': [0.0] * 181 + [-0.2081559] * 23,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_224': {
            'samples': [0.0] * 181 + [0.254468348] * 23,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_225': {
            'samples': [0.0] * 180 + [-0.2081559] * 24,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_225': {
            'samples': [0.0] * 180 + [0.254468348] * 24,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_226': {
            'samples': [0.0] * 179 + [-0.2081559] * 25,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_226': {
            'samples': [0.0] * 179 + [0.254468348] * 25,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_227': {
            'samples': [0.0] * 178 + [-0.2081559] * 26,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_227': {
            'samples': [0.0] * 178 + [0.254468348] * 26,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_228': {
            'samples': [0.0] * 177 + [-0.2081559] * 27,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_228': {
            'samples': [0.0] * 177 + [0.254468348] * 27,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_229': {
            'samples': [0.0] * 176 + [-0.2081559] * 28,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_229': {
            'samples': [0.0] * 176 + [0.254468348] * 28,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_230': {
            'samples': [0.0] * 175 + [-0.2081559] * 29,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_230': {
            'samples': [0.0] * 175 + [0.254468348] * 29,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_231': {
            'samples': [0.0] * 174 + [-0.2081559] * 30,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_231': {
            'samples': [0.0] * 174 + [0.254468348] * 30,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_232': {
            'samples': [0.0] * 173 + [-0.2081559] * 31,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_232': {
            'samples': [0.0] * 173 + [0.254468348] * 31,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_233': {
            'samples': [0.0] * 172 + [-0.2081559] * 32,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_233': {
            'samples': [0.0] * 172 + [0.254468348] * 32,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_234': {
            'samples': [0.0] * 171 + [-0.2081559] * 33,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_234': {
            'samples': [0.0] * 171 + [0.254468348] * 33,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_235': {
            'samples': [0.0] * 170 + [-0.2081559] * 34,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_235': {
            'samples': [0.0] * 170 + [0.254468348] * 34,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_236': {
            'samples': [0.0] * 169 + [-0.2081559] * 35,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_236': {
            'samples': [0.0] * 169 + [0.254468348] * 35,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_237': {
            'samples': [0.0] * 168 + [-0.2081559] * 36,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_237': {
            'samples': [0.0] * 168 + [0.254468348] * 36,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_238': {
            'samples': [0.0] * 167 + [-0.2081559] * 37,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_238': {
            'samples': [0.0] * 167 + [0.254468348] * 37,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_239': {
            'samples': [0.0] * 166 + [-0.2081559] * 38,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_239': {
            'samples': [0.0] * 166 + [0.254468348] * 38,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_240': {
            'samples': [0.0] * 165 + [-0.2081559] * 39,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_240': {
            'samples': [0.0] * 165 + [0.254468348] * 39,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_241': {
            'samples': [0.0] * 164 + [-0.2081559] * 40,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_241': {
            'samples': [0.0] * 164 + [0.254468348] * 40,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_242': {
            'samples': [0.0] * 163 + [-0.2081559] * 41,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_242': {
            'samples': [0.0] * 163 + [0.254468348] * 41,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_243': {
            'samples': [0.0] * 162 + [-0.2081559] * 42,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_243': {
            'samples': [0.0] * 162 + [0.254468348] * 42,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_244': {
            'samples': [0.0] * 161 + [-0.2081559] * 43,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_244': {
            'samples': [0.0] * 161 + [0.254468348] * 43,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_245': {
            'samples': [0.0] * 160 + [-0.2081559] * 44,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_245': {
            'samples': [0.0] * 160 + [0.254468348] * 44,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_246': {
            'samples': [0.0] * 159 + [-0.2081559] * 45,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_246': {
            'samples': [0.0] * 159 + [0.254468348] * 45,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_247': {
            'samples': [0.0] * 158 + [-0.2081559] * 46,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_247': {
            'samples': [0.0] * 158 + [0.254468348] * 46,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_248': {
            'samples': [0.0] * 157 + [-0.2081559] * 47,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_248': {
            'samples': [0.0] * 157 + [0.254468348] * 47,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_249': {
            'samples': [0.0] * 156 + [-0.2081559] * 48,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_249': {
            'samples': [0.0] * 156 + [0.254468348] * 48,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_250': {
            'samples': [0.0] * 155 + [-0.2081559] * 49,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_250': {
            'samples': [0.0] * 155 + [0.254468348] * 49,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_251': {
            'samples': [0.0] * 154 + [-0.2081559] * 50,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_251': {
            'samples': [0.0] * 154 + [0.254468348] * 50,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_252': {
            'samples': [0.0] * 153 + [-0.2081559] * 51,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_252': {
            'samples': [0.0] * 153 + [0.254468348] * 51,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_253': {
            'samples': [0.0] * 152 + [-0.2081559] * 52,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_253': {
            'samples': [0.0] * 152 + [0.254468348] * 52,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_254': {
            'samples': [0.0] * 151 + [-0.2081559] * 53,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_254': {
            'samples': [0.0] * 151 + [0.254468348] * 53,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_255': {
            'samples': [0.0] * 150 + [-0.2081559] * 54,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_255': {
            'samples': [0.0] * 150 + [0.254468348] * 54,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_256': {
            'samples': [0.0] * 149 + [-0.2081559] * 55,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_256': {
            'samples': [0.0] * 149 + [0.254468348] * 55,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_257': {
            'samples': [0.0] * 148 + [-0.2081559] * 56,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_257': {
            'samples': [0.0] * 148 + [0.254468348] * 56,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_258': {
            'samples': [0.0] * 147 + [-0.2081559] * 57,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_258': {
            'samples': [0.0] * 147 + [0.254468348] * 57,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_259': {
            'samples': [0.0] * 146 + [-0.2081559] * 58,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_259': {
            'samples': [0.0] * 146 + [0.254468348] * 58,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_260': {
            'samples': [0.0] * 145 + [-0.2081559] * 59,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_260': {
            'samples': [0.0] * 145 + [0.254468348] * 59,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_261': {
            'samples': [0.0] * 144 + [-0.2081559] * 60,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_261': {
            'samples': [0.0] * 144 + [0.254468348] * 60,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_262': {
            'samples': [0.0] * 143 + [-0.2081559] * 61,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_262': {
            'samples': [0.0] * 143 + [0.254468348] * 61,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_263': {
            'samples': [0.0] * 142 + [-0.2081559] * 62,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_263': {
            'samples': [0.0] * 142 + [0.254468348] * 62,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_264': {
            'samples': [0.0] * 141 + [-0.2081559] * 63,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_264': {
            'samples': [0.0] * 141 + [0.254468348] * 63,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_265': {
            'samples': [0.0] * 140 + [-0.2081559] * 64,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_265': {
            'samples': [0.0] * 140 + [0.254468348] * 64,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_266': {
            'samples': [0.0] * 139 + [-0.2081559] * 65,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_266': {
            'samples': [0.0] * 139 + [0.254468348] * 65,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_267': {
            'samples': [0.0] * 138 + [-0.2081559] * 66,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_267': {
            'samples': [0.0] * 138 + [0.254468348] * 66,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_268': {
            'samples': [0.0] * 137 + [-0.2081559] * 67,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_268': {
            'samples': [0.0] * 137 + [0.254468348] * 67,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_269': {
            'samples': [0.0] * 136 + [-0.2081559] * 68,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_269': {
            'samples': [0.0] * 136 + [0.254468348] * 68,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_270': {
            'samples': [0.0] * 135 + [-0.2081559] * 69,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_270': {
            'samples': [0.0] * 135 + [0.254468348] * 69,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_271': {
            'samples': [0.0] * 134 + [-0.2081559] * 70,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_271': {
            'samples': [0.0] * 134 + [0.254468348] * 70,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_272': {
            'samples': [0.0] * 133 + [-0.2081559] * 71,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_272': {
            'samples': [0.0] * 133 + [0.254468348] * 71,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_273': {
            'samples': [0.0] * 132 + [-0.2081559] * 72,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_273': {
            'samples': [0.0] * 132 + [0.254468348] * 72,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_274': {
            'samples': [0.0] * 131 + [-0.2081559] * 73,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_274': {
            'samples': [0.0] * 131 + [0.254468348] * 73,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_275': {
            'samples': [0.0] * 130 + [-0.2081559] * 74,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_275': {
            'samples': [0.0] * 130 + [0.254468348] * 74,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_276': {
            'samples': [0.0] * 129 + [-0.2081559] * 75,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_276': {
            'samples': [0.0] * 129 + [0.254468348] * 75,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_277': {
            'samples': [0.0] * 128 + [-0.2081559] * 76,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_277': {
            'samples': [0.0] * 128 + [0.254468348] * 76,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_278': {
            'samples': [0.0] * 127 + [-0.2081559] * 77,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_278': {
            'samples': [0.0] * 127 + [0.254468348] * 77,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_279': {
            'samples': [0.0] * 126 + [-0.2081559] * 78,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_279': {
            'samples': [0.0] * 126 + [0.254468348] * 78,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_280': {
            'samples': [0.0] * 125 + [-0.2081559] * 79,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_280': {
            'samples': [0.0] * 125 + [0.254468348] * 79,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_281': {
            'samples': [0.0] * 124 + [-0.2081559] * 80,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_281': {
            'samples': [0.0] * 124 + [0.254468348] * 80,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_282': {
            'samples': [0.0] * 123 + [-0.2081559] * 81,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_282': {
            'samples': [0.0] * 123 + [0.254468348] * 81,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_283': {
            'samples': [0.0] * 122 + [-0.2081559] * 82,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_283': {
            'samples': [0.0] * 122 + [0.254468348] * 82,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_284': {
            'samples': [0.0] * 121 + [-0.2081559] * 83,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_284': {
            'samples': [0.0] * 121 + [0.254468348] * 83,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_285': {
            'samples': [0.0] * 120 + [-0.2081559] * 84,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_285': {
            'samples': [0.0] * 120 + [0.254468348] * 84,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_286': {
            'samples': [0.0] * 119 + [-0.2081559] * 85,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_286': {
            'samples': [0.0] * 119 + [0.254468348] * 85,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_287': {
            'samples': [0.0] * 118 + [-0.2081559] * 86,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_287': {
            'samples': [0.0] * 118 + [0.254468348] * 86,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_288': {
            'samples': [0.0] * 117 + [-0.2081559] * 87,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_288': {
            'samples': [0.0] * 117 + [0.254468348] * 87,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_289': {
            'samples': [0.0] * 116 + [-0.2081559] * 88,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_289': {
            'samples': [0.0] * 116 + [0.254468348] * 88,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_290': {
            'samples': [0.0] * 115 + [-0.2081559] * 89,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_290': {
            'samples': [0.0] * 115 + [0.254468348] * 89,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_291': {
            'samples': [0.0] * 114 + [-0.2081559] * 90,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_291': {
            'samples': [0.0] * 114 + [0.254468348] * 90,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_292': {
            'samples': [0.0] * 113 + [-0.2081559] * 91,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_292': {
            'samples': [0.0] * 113 + [0.254468348] * 91,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_293': {
            'samples': [0.0] * 112 + [-0.2081559] * 92,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_293': {
            'samples': [0.0] * 112 + [0.254468348] * 92,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_294': {
            'samples': [0.0] * 111 + [-0.2081559] * 93,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_294': {
            'samples': [0.0] * 111 + [0.254468348] * 93,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_295': {
            'samples': [0.0] * 110 + [-0.2081559] * 94,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_295': {
            'samples': [0.0] * 110 + [0.254468348] * 94,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_296': {
            'samples': [0.0] * 109 + [-0.2081559] * 95,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_296': {
            'samples': [0.0] * 109 + [0.254468348] * 95,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_297': {
            'samples': [0.0] * 108 + [-0.2081559] * 96,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_297': {
            'samples': [0.0] * 108 + [0.254468348] * 96,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_298': {
            'samples': [0.0] * 107 + [-0.2081559] * 97,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_298': {
            'samples': [0.0] * 107 + [0.254468348] * 97,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_299': {
            'samples': [0.0] * 106 + [-0.2081559] * 98,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_299': {
            'samples': [0.0] * 106 + [0.254468348] * 98,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_300': {
            'samples': [0.0] * 105 + [-0.2081559] * 99,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_300': {
            'samples': [0.0] * 105 + [0.254468348] * 99,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_301': {
            'samples': [0.0] * 104 + [-0.2081559] * 100,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_301': {
            'samples': [0.0] * 104 + [0.254468348] * 100,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_302': {
            'samples': [0.0] * 103 + [-0.2081559] * 101,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_302': {
            'samples': [0.0] * 103 + [0.254468348] * 101,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_303': {
            'samples': [0.0] * 102 + [-0.2081559] * 102,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_303': {
            'samples': [0.0] * 102 + [0.254468348] * 102,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_304': {
            'samples': [0.0] * 101 + [-0.2081559] * 103,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_304': {
            'samples': [0.0] * 101 + [0.254468348] * 103,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_305': {
            'samples': [0.0] * 100 + [-0.2081559] * 104,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_305': {
            'samples': [0.0] * 100 + [0.254468348] * 104,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_306': {
            'samples': [0.0] * 99 + [-0.2081559] * 105,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_306': {
            'samples': [0.0] * 99 + [0.254468348] * 105,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_307': {
            'samples': [0.0] * 98 + [-0.2081559] * 106,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_307': {
            'samples': [0.0] * 98 + [0.254468348] * 106,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_308': {
            'samples': [0.0] * 97 + [-0.2081559] * 107,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_308': {
            'samples': [0.0] * 97 + [0.254468348] * 107,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_309': {
            'samples': [0.0] * 96 + [-0.2081559] * 108,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_309': {
            'samples': [0.0] * 96 + [0.254468348] * 108,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_310': {
            'samples': [0.0] * 95 + [-0.2081559] * 109,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_310': {
            'samples': [0.0] * 95 + [0.254468348] * 109,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_311': {
            'samples': [0.0] * 94 + [-0.2081559] * 110,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_311': {
            'samples': [0.0] * 94 + [0.254468348] * 110,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_312': {
            'samples': [0.0] * 93 + [-0.2081559] * 111,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_312': {
            'samples': [0.0] * 93 + [0.254468348] * 111,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_313': {
            'samples': [0.0] * 92 + [-0.2081559] * 112,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_313': {
            'samples': [0.0] * 92 + [0.254468348] * 112,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_314': {
            'samples': [0.0] * 91 + [-0.2081559] * 113,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_314': {
            'samples': [0.0] * 91 + [0.254468348] * 113,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_315': {
            'samples': [0.0] * 90 + [-0.2081559] * 114,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_315': {
            'samples': [0.0] * 90 + [0.254468348] * 114,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_316': {
            'samples': [0.0] * 89 + [-0.2081559] * 115,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_316': {
            'samples': [0.0] * 89 + [0.254468348] * 115,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_317': {
            'samples': [0.0] * 88 + [-0.2081559] * 116,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_317': {
            'samples': [0.0] * 88 + [0.254468348] * 116,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_318': {
            'samples': [0.0] * 87 + [-0.2081559] * 117,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_318': {
            'samples': [0.0] * 87 + [0.254468348] * 117,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_319': {
            'samples': [0.0] * 86 + [-0.2081559] * 118,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_319': {
            'samples': [0.0] * 86 + [0.254468348] * 118,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_320': {
            'samples': [0.0] * 85 + [-0.2081559] * 119,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_320': {
            'samples': [0.0] * 85 + [0.254468348] * 119,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_321': {
            'samples': [0.0] * 84 + [-0.2081559] * 120,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_321': {
            'samples': [0.0] * 84 + [0.254468348] * 120,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_322': {
            'samples': [0.0] * 83 + [-0.2081559] * 121,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_322': {
            'samples': [0.0] * 83 + [0.254468348] * 121,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_323': {
            'samples': [0.0] * 82 + [-0.2081559] * 122,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_323': {
            'samples': [0.0] * 82 + [0.254468348] * 122,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_324': {
            'samples': [0.0] * 81 + [-0.2081559] * 123,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_324': {
            'samples': [0.0] * 81 + [0.254468348] * 123,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_325': {
            'samples': [0.0] * 80 + [-0.2081559] * 124,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_325': {
            'samples': [0.0] * 80 + [0.254468348] * 124,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_326': {
            'samples': [0.0] * 79 + [-0.2081559] * 125,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_326': {
            'samples': [0.0] * 79 + [0.254468348] * 125,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_327': {
            'samples': [0.0] * 78 + [-0.2081559] * 126,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_327': {
            'samples': [0.0] * 78 + [0.254468348] * 126,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_328': {
            'samples': [0.0] * 77 + [-0.2081559] * 127,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_328': {
            'samples': [0.0] * 77 + [0.254468348] * 127,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_329': {
            'samples': [0.0] * 76 + [-0.2081559] * 128,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_329': {
            'samples': [0.0] * 76 + [0.254468348] * 128,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_330': {
            'samples': [0.0] * 75 + [-0.2081559] * 129,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_330': {
            'samples': [0.0] * 75 + [0.254468348] * 129,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_331': {
            'samples': [0.0] * 74 + [-0.2081559] * 130,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_331': {
            'samples': [0.0] * 74 + [0.254468348] * 130,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_332': {
            'samples': [0.0] * 73 + [-0.2081559] * 131,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_332': {
            'samples': [0.0] * 73 + [0.254468348] * 131,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_333': {
            'samples': [0.0] * 72 + [-0.2081559] * 132,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_333': {
            'samples': [0.0] * 72 + [0.254468348] * 132,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_334': {
            'samples': [0.0] * 71 + [-0.2081559] * 133,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_334': {
            'samples': [0.0] * 71 + [0.254468348] * 133,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_335': {
            'samples': [0.0] * 70 + [-0.2081559] * 134,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_335': {
            'samples': [0.0] * 70 + [0.254468348] * 134,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_336': {
            'samples': [0.0] * 69 + [-0.2081559] * 135,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_336': {
            'samples': [0.0] * 69 + [0.254468348] * 135,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_337': {
            'samples': [0.0] * 68 + [-0.2081559] * 136,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_337': {
            'samples': [0.0] * 68 + [0.254468348] * 136,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_338': {
            'samples': [0.0] * 67 + [-0.2081559] * 137,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_338': {
            'samples': [0.0] * 67 + [0.254468348] * 137,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_339': {
            'samples': [0.0] * 66 + [-0.2081559] * 138,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_339': {
            'samples': [0.0] * 66 + [0.254468348] * 138,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_340': {
            'samples': [0.0] * 65 + [-0.2081559] * 139,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_340': {
            'samples': [0.0] * 65 + [0.254468348] * 139,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_341': {
            'samples': [0.0] * 64 + [-0.2081559] * 140,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_341': {
            'samples': [0.0] * 64 + [0.254468348] * 140,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_342': {
            'samples': [0.0] * 63 + [-0.2081559] * 141,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_342': {
            'samples': [0.0] * 63 + [0.254468348] * 141,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_343': {
            'samples': [0.0] * 62 + [-0.2081559] * 142,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_343': {
            'samples': [0.0] * 62 + [0.254468348] * 142,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_344': {
            'samples': [0.0] * 61 + [-0.2081559] * 143,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_344': {
            'samples': [0.0] * 61 + [0.254468348] * 143,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_345': {
            'samples': [0.0] * 60 + [-0.2081559] * 144,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_345': {
            'samples': [0.0] * 60 + [0.254468348] * 144,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_346': {
            'samples': [0.0] * 59 + [-0.2081559] * 145,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_346': {
            'samples': [0.0] * 59 + [0.254468348] * 145,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_347': {
            'samples': [0.0] * 58 + [-0.2081559] * 146,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_347': {
            'samples': [0.0] * 58 + [0.254468348] * 146,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_348': {
            'samples': [0.0] * 57 + [-0.2081559] * 147,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_348': {
            'samples': [0.0] * 57 + [0.254468348] * 147,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_349': {
            'samples': [0.0] * 56 + [-0.2081559] * 148,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_349': {
            'samples': [0.0] * 56 + [0.254468348] * 148,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_350': {
            'samples': [0.0] * 55 + [-0.2081559] * 149,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_350': {
            'samples': [0.0] * 55 + [0.254468348] * 149,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_351': {
            'samples': [0.0] * 54 + [-0.2081559] * 150,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_351': {
            'samples': [0.0] * 54 + [0.254468348] * 150,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_352': {
            'samples': [0.0] * 53 + [-0.2081559] * 151,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_352': {
            'samples': [0.0] * 53 + [0.254468348] * 151,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_353': {
            'samples': [0.0] * 52 + [-0.2081559] * 152,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_353': {
            'samples': [0.0] * 52 + [0.254468348] * 152,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_354': {
            'samples': [0.0] * 51 + [-0.2081559] * 153,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_354': {
            'samples': [0.0] * 51 + [0.254468348] * 153,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_355': {
            'samples': [0.0] * 50 + [-0.2081559] * 154,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_355': {
            'samples': [0.0] * 50 + [0.254468348] * 154,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_356': {
            'samples': [0.0] * 49 + [-0.2081559] * 155,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_356': {
            'samples': [0.0] * 49 + [0.254468348] * 155,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_357': {
            'samples': [0.0] * 48 + [-0.2081559] * 156,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_357': {
            'samples': [0.0] * 48 + [0.254468348] * 156,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_358': {
            'samples': [0.0] * 47 + [-0.2081559] * 157,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_358': {
            'samples': [0.0] * 47 + [0.254468348] * 157,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_359': {
            'samples': [0.0] * 46 + [-0.2081559] * 158,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_359': {
            'samples': [0.0] * 46 + [0.254468348] * 158,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_360': {
            'samples': [0.0] * 45 + [-0.2081559] * 159,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_360': {
            'samples': [0.0] * 45 + [0.254468348] * 159,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_361': {
            'samples': [0.0] * 44 + [-0.2081559] * 160,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_361': {
            'samples': [0.0] * 44 + [0.254468348] * 160,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_362': {
            'samples': [0.0] * 43 + [-0.2081559] * 161,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_362': {
            'samples': [0.0] * 43 + [0.254468348] * 161,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_363': {
            'samples': [0.0] * 42 + [-0.2081559] * 162,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_363': {
            'samples': [0.0] * 42 + [0.254468348] * 162,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_364': {
            'samples': [0.0] * 41 + [-0.2081559] * 163,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_364': {
            'samples': [0.0] * 41 + [0.254468348] * 163,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_365': {
            'samples': [0.0] * 40 + [-0.2081559] * 164,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_365': {
            'samples': [0.0] * 40 + [0.254468348] * 164,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_366': {
            'samples': [0.0] * 39 + [-0.2081559] * 165,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_366': {
            'samples': [0.0] * 39 + [0.254468348] * 165,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_367': {
            'samples': [0.0] * 38 + [-0.2081559] * 166,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_367': {
            'samples': [0.0] * 38 + [0.254468348] * 166,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_368': {
            'samples': [0.0] * 37 + [-0.2081559] * 167,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_368': {
            'samples': [0.0] * 37 + [0.254468348] * 167,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_369': {
            'samples': [0.0] * 36 + [-0.2081559] * 168,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_369': {
            'samples': [0.0] * 36 + [0.254468348] * 168,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_370': {
            'samples': [0.0] * 35 + [-0.2081559] * 169,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_370': {
            'samples': [0.0] * 35 + [0.254468348] * 169,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_371': {
            'samples': [0.0] * 34 + [-0.2081559] * 170,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_371': {
            'samples': [0.0] * 34 + [0.254468348] * 170,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_372': {
            'samples': [0.0] * 33 + [-0.2081559] * 171,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_372': {
            'samples': [0.0] * 33 + [0.254468348] * 171,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_373': {
            'samples': [0.0] * 32 + [-0.2081559] * 172,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_373': {
            'samples': [0.0] * 32 + [0.254468348] * 172,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_374': {
            'samples': [0.0] * 31 + [-0.2081559] * 173,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_374': {
            'samples': [0.0] * 31 + [0.254468348] * 173,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_375': {
            'samples': [0.0] * 30 + [-0.2081559] * 174,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_375': {
            'samples': [0.0] * 30 + [0.254468348] * 174,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_376': {
            'samples': [0.0] * 29 + [-0.2081559] * 175,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_376': {
            'samples': [0.0] * 29 + [0.254468348] * 175,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_377': {
            'samples': [0.0] * 28 + [-0.2081559] * 176,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_377': {
            'samples': [0.0] * 28 + [0.254468348] * 176,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_378': {
            'samples': [0.0] * 27 + [-0.2081559] * 177,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_378': {
            'samples': [0.0] * 27 + [0.254468348] * 177,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_379': {
            'samples': [0.0] * 26 + [-0.2081559] * 178,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_379': {
            'samples': [0.0] * 26 + [0.254468348] * 178,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_380': {
            'samples': [0.0] * 25 + [-0.2081559] * 179,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_380': {
            'samples': [0.0] * 25 + [0.254468348] * 179,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_381': {
            'samples': [0.0] * 24 + [-0.2081559] * 180,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_381': {
            'samples': [0.0] * 24 + [0.254468348] * 180,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_382': {
            'samples': [0.0] * 23 + [-0.2081559] * 181,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_382': {
            'samples': [0.0] * 23 + [0.254468348] * 181,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_383': {
            'samples': [0.0] * 22 + [-0.2081559] * 182,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_383': {
            'samples': [0.0] * 22 + [0.254468348] * 182,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_384': {
            'samples': [0.0] * 21 + [-0.2081559] * 183,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_384': {
            'samples': [0.0] * 21 + [0.254468348] * 183,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_385': {
            'samples': [0.0] * 20 + [-0.2081559] * 184,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_385': {
            'samples': [0.0] * 20 + [0.254468348] * 184,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_386': {
            'samples': [0.0] * 19 + [-0.2081559] * 185,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_386': {
            'samples': [0.0] * 19 + [0.254468348] * 185,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_387': {
            'samples': [0.0] * 18 + [-0.2081559] * 186,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_387': {
            'samples': [0.0] * 18 + [0.254468348] * 186,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_388': {
            'samples': [0.0] * 17 + [-0.2081559] * 187,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_388': {
            'samples': [0.0] * 17 + [0.254468348] * 187,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_389': {
            'samples': [0.0] * 16 + [-0.2081559] * 188,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_389': {
            'samples': [0.0] * 16 + [0.254468348] * 188,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_390': {
            'samples': [0.0] * 15 + [-0.2081559] * 189,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_390': {
            'samples': [0.0] * 15 + [0.254468348] * 189,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_391': {
            'samples': [0.0] * 14 + [-0.2081559] * 190,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_391': {
            'samples': [0.0] * 14 + [0.254468348] * 190,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_392': {
            'samples': [0.0] * 13 + [-0.2081559] * 191,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_392': {
            'samples': [0.0] * 13 + [0.254468348] * 191,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_393': {
            'samples': [0.0] * 12 + [-0.2081559] * 192,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_393': {
            'samples': [0.0] * 12 + [0.254468348] * 192,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_394': {
            'samples': [0.0] * 11 + [-0.2081559] * 193,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_394': {
            'samples': [0.0] * 11 + [0.254468348] * 193,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_395': {
            'samples': [0.0] * 10 + [-0.2081559] * 194,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_395': {
            'samples': [0.0] * 10 + [0.254468348] * 194,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_396': {
            'samples': [0.0] * 9 + [-0.2081559] * 195,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_396': {
            'samples': [0.0] * 9 + [0.254468348] * 195,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_397': {
            'samples': [0.0] * 8 + [-0.2081559] * 196,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_397': {
            'samples': [0.0] * 8 + [0.254468348] * 196,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_398': {
            'samples': [0.0] * 7 + [-0.2081559] * 197,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_398': {
            'samples': [0.0] * 7 + [0.254468348] * 197,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_399': {
            'samples': [0.0] * 6 + [-0.2081559] * 198,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_399': {
            'samples': [0.0] * 6 + [0.254468348] * 198,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_400': {
            'samples': [0.0] * 5 + [-0.2081559] * 199,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_400': {
            'samples': [0.0] * 5 + [0.254468348] * 199,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_401': {
            'samples': [0.0] * 4 + [-0.2081559] * 200,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_401': {
            'samples': [0.0] * 4 + [0.254468348] * 200,
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
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
        'cos_50': {
            'cosine': [(1.0, 100000)],
            'sine': [(0.0, 100000)],
        },
        'sin_50': {
            'cosine': [(0.0, 100000)],
            'sine': [(1.0, 100000)],
        },
        'cos_3us': {
            'cosine': [(1.0, 3000)],
            'sine': [(0.0, 3000)],
        },
        'sin_3us': {
            'cosine': [(0.0, 3000)],
            'sine': [(1.0, 3000)],
        },
        'cos_buffered': {
            'cosine': [(1.0, 3000000)],
            'sine': [(0.0, 3000000)],
        },
        'sin_buffered': {
            'cosine': [(0.0, 3000000)],
            'sine': [(1.0, 3000000)],
        },
        'cos_t2star': {
            'cosine': [(1.0, 15048)],
            'sine': [(0.0, 15048)],
        },
        'sin_t2star': {
            'cosine': [(0.0, 15048)],
            'sine': [(1.0, 15048)],
        },
        'cos_t2star_full_demod': {
            'cosine': [(0.005050505050505051, 15048)],
            'sine': [(0.0, 15048)],
        },
        'sin_t2star_full_demod': {
            'cosine': [(0.0, 15048)],
            'sine': [(0.005050505050505051, 15048)],
        },
    },
    'mixers': {},
}


