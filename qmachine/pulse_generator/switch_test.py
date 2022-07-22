
# Single QUA script generated at 2022-07-22 09:39:07.436142
# QUA library version: 0.3.7

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    a1 = declare(fixed, value=[1.0, 0.9444444444444444, 0.8888888888888888, 0.8333333333333334, 0.7777777777777778, 0.7222222222222222, 0.6666666666666667, 0.6111111111111112, 0.5555555555555556, 0.5])
    with for_(v2,0,v2<10,v2+1):
        with for_(v1,0,v1<200,v1+1):
            with if_(v1==0, unsafe=True):
                align("gate_29", "gate_36")
                play("baked_Op_0"*amp(a1[v2]), "gate_29")
                play("baked_Op_0"*amp(a1[v2]), "gate_36")
            with elif_(v1==1):
                align("gate_29", "gate_36")
                play("baked_Op_1"*amp(a1[v2]), "gate_29")
                play("baked_Op_1"*amp(a1[v2]), "gate_36")
            with elif_(v1==2):
                align("gate_29", "gate_36")
                play("baked_Op_2"*amp(a1[v2]), "gate_29")
                play("baked_Op_2"*amp(a1[v2]), "gate_36")
            with elif_(v1==3):
                align("gate_29", "gate_36")
                play("baked_Op_3"*amp(a1[v2]), "gate_29")
                play("baked_Op_3"*amp(a1[v2]), "gate_36")
            with elif_(v1==4):
                align("gate_29", "gate_36")
                play("baked_Op_4"*amp(a1[v2]), "gate_29")
                play("baked_Op_4"*amp(a1[v2]), "gate_36")
            with elif_(v1==5):
                align("gate_29", "gate_36")
                play("baked_Op_5"*amp(a1[v2]), "gate_29")
                play("baked_Op_5"*amp(a1[v2]), "gate_36")
            with elif_(v1==6):
                align("gate_29", "gate_36")
                play("baked_Op_6"*amp(a1[v2]), "gate_29")
                play("baked_Op_6"*amp(a1[v2]), "gate_36")
            with elif_(v1==7):
                align("gate_29", "gate_36")
                play("baked_Op_7"*amp(a1[v2]), "gate_29")
                play("baked_Op_7"*amp(a1[v2]), "gate_36")
            with elif_(v1==8):
                align("gate_29", "gate_36")
                play("baked_Op_8"*amp(a1[v2]), "gate_29")
                play("baked_Op_8"*amp(a1[v2]), "gate_36")
            with elif_(v1==9):
                align("gate_29", "gate_36")
                play("baked_Op_9"*amp(a1[v2]), "gate_29")
                play("baked_Op_9"*amp(a1[v2]), "gate_36")
            with elif_(v1==10):
                align("gate_29", "gate_36")
                play("baked_Op_10"*amp(a1[v2]), "gate_29")
                play("baked_Op_10"*amp(a1[v2]), "gate_36")
            with elif_(v1==11):
                align("gate_29", "gate_36")
                play("baked_Op_11"*amp(a1[v2]), "gate_29")
                play("baked_Op_11"*amp(a1[v2]), "gate_36")
            with elif_(v1==12):
                align("gate_29", "gate_36")
                play("baked_Op_12"*amp(a1[v2]), "gate_29")
                play("baked_Op_12"*amp(a1[v2]), "gate_36")
            with elif_(v1==13):
                align("gate_29", "gate_36")
                play("baked_Op_13"*amp(a1[v2]), "gate_29")
                play("baked_Op_13"*amp(a1[v2]), "gate_36")
            with elif_(v1==14):
                align("gate_29", "gate_36")
                play("baked_Op_14"*amp(a1[v2]), "gate_29")
                play("baked_Op_14"*amp(a1[v2]), "gate_36")
            with elif_(v1==15):
                align("gate_29", "gate_36")
                play("baked_Op_15"*amp(a1[v2]), "gate_29")
                play("baked_Op_15"*amp(a1[v2]), "gate_36")
            with elif_(v1==16):
                align("gate_29", "gate_36")
                play("baked_Op_16"*amp(a1[v2]), "gate_29")
                play("baked_Op_16"*amp(a1[v2]), "gate_36")
            with elif_(v1==17):
                align("gate_29", "gate_36")
                play("baked_Op_17"*amp(a1[v2]), "gate_29")
                play("baked_Op_17"*amp(a1[v2]), "gate_36")
            with elif_(v1==18):
                align("gate_29", "gate_36")
                play("baked_Op_18"*amp(a1[v2]), "gate_29")
                play("baked_Op_18"*amp(a1[v2]), "gate_36")
            with elif_(v1==19):
                align("gate_29", "gate_36")
                play("baked_Op_19"*amp(a1[v2]), "gate_29")
                play("baked_Op_19"*amp(a1[v2]), "gate_36")
            with elif_(v1==20):
                align("gate_29", "gate_36")
                play("baked_Op_20"*amp(a1[v2]), "gate_29")
                play("baked_Op_20"*amp(a1[v2]), "gate_36")
            with elif_(v1==21):
                align("gate_29", "gate_36")
                play("baked_Op_21"*amp(a1[v2]), "gate_29")
                play("baked_Op_21"*amp(a1[v2]), "gate_36")
            with elif_(v1==22):
                align("gate_29", "gate_36")
                play("baked_Op_22"*amp(a1[v2]), "gate_29")
                play("baked_Op_22"*amp(a1[v2]), "gate_36")
            with elif_(v1==23):
                align("gate_29", "gate_36")
                play("baked_Op_23"*amp(a1[v2]), "gate_29")
                play("baked_Op_23"*amp(a1[v2]), "gate_36")
            with elif_(v1==24):
                align("gate_29", "gate_36")
                play("baked_Op_24"*amp(a1[v2]), "gate_29")
                play("baked_Op_24"*amp(a1[v2]), "gate_36")
            with elif_(v1==25):
                align("gate_29", "gate_36")
                play("baked_Op_25"*amp(a1[v2]), "gate_29")
                play("baked_Op_25"*amp(a1[v2]), "gate_36")
            with elif_(v1==26):
                align("gate_29", "gate_36")
                play("baked_Op_26"*amp(a1[v2]), "gate_29")
                play("baked_Op_26"*amp(a1[v2]), "gate_36")
            with elif_(v1==27):
                align("gate_29", "gate_36")
                play("baked_Op_27"*amp(a1[v2]), "gate_29")
                play("baked_Op_27"*amp(a1[v2]), "gate_36")
            with elif_(v1==28):
                align("gate_29", "gate_36")
                play("baked_Op_28"*amp(a1[v2]), "gate_29")
                play("baked_Op_28"*amp(a1[v2]), "gate_36")
            with elif_(v1==29):
                align("gate_29", "gate_36")
                play("baked_Op_29"*amp(a1[v2]), "gate_29")
                play("baked_Op_29"*amp(a1[v2]), "gate_36")
            with elif_(v1==30):
                align("gate_29", "gate_36")
                play("baked_Op_30"*amp(a1[v2]), "gate_29")
                play("baked_Op_30"*amp(a1[v2]), "gate_36")
            with elif_(v1==31):
                align("gate_29", "gate_36")
                play("baked_Op_31"*amp(a1[v2]), "gate_29")
                play("baked_Op_31"*amp(a1[v2]), "gate_36")
            with elif_(v1==32):
                align("gate_29", "gate_36")
                play("baked_Op_32"*amp(a1[v2]), "gate_29")
                play("baked_Op_32"*amp(a1[v2]), "gate_36")
            with elif_(v1==33):
                align("gate_29", "gate_36")
                play("baked_Op_33"*amp(a1[v2]), "gate_29")
                play("baked_Op_33"*amp(a1[v2]), "gate_36")
            with elif_(v1==34):
                align("gate_29", "gate_36")
                play("baked_Op_34"*amp(a1[v2]), "gate_29")
                play("baked_Op_34"*amp(a1[v2]), "gate_36")
            with elif_(v1==35):
                align("gate_29", "gate_36")
                play("baked_Op_35"*amp(a1[v2]), "gate_29")
                play("baked_Op_35"*amp(a1[v2]), "gate_36")
            with elif_(v1==36):
                align("gate_29", "gate_36")
                play("baked_Op_36"*amp(a1[v2]), "gate_29")
                play("baked_Op_36"*amp(a1[v2]), "gate_36")
            with elif_(v1==37):
                align("gate_29", "gate_36")
                play("baked_Op_37"*amp(a1[v2]), "gate_29")
                play("baked_Op_37"*amp(a1[v2]), "gate_36")
            with elif_(v1==38):
                align("gate_29", "gate_36")
                play("baked_Op_38"*amp(a1[v2]), "gate_29")
                play("baked_Op_38"*amp(a1[v2]), "gate_36")
            with elif_(v1==39):
                align("gate_29", "gate_36")
                play("baked_Op_39"*amp(a1[v2]), "gate_29")
                play("baked_Op_39"*amp(a1[v2]), "gate_36")
            with elif_(v1==40):
                align("gate_29", "gate_36")
                play("baked_Op_40"*amp(a1[v2]), "gate_29")
                play("baked_Op_40"*amp(a1[v2]), "gate_36")
            with elif_(v1==41):
                align("gate_29", "gate_36")
                play("baked_Op_41"*amp(a1[v2]), "gate_29")
                play("baked_Op_41"*amp(a1[v2]), "gate_36")
            with elif_(v1==42):
                align("gate_29", "gate_36")
                play("baked_Op_42"*amp(a1[v2]), "gate_29")
                play("baked_Op_42"*amp(a1[v2]), "gate_36")
            with elif_(v1==43):
                align("gate_29", "gate_36")
                play("baked_Op_43"*amp(a1[v2]), "gate_29")
                play("baked_Op_43"*amp(a1[v2]), "gate_36")
            with elif_(v1==44):
                align("gate_29", "gate_36")
                play("baked_Op_44"*amp(a1[v2]), "gate_29")
                play("baked_Op_44"*amp(a1[v2]), "gate_36")
            with elif_(v1==45):
                align("gate_29", "gate_36")
                play("baked_Op_45"*amp(a1[v2]), "gate_29")
                play("baked_Op_45"*amp(a1[v2]), "gate_36")
            with elif_(v1==46):
                align("gate_29", "gate_36")
                play("baked_Op_46"*amp(a1[v2]), "gate_29")
                play("baked_Op_46"*amp(a1[v2]), "gate_36")
            with elif_(v1==47):
                align("gate_29", "gate_36")
                play("baked_Op_47"*amp(a1[v2]), "gate_29")
                play("baked_Op_47"*amp(a1[v2]), "gate_36")
            with elif_(v1==48):
                align("gate_29", "gate_36")
                play("baked_Op_48"*amp(a1[v2]), "gate_29")
                play("baked_Op_48"*amp(a1[v2]), "gate_36")
            with elif_(v1==49):
                align("gate_29", "gate_36")
                play("baked_Op_49"*amp(a1[v2]), "gate_29")
                play("baked_Op_49"*amp(a1[v2]), "gate_36")
            with elif_(v1==50):
                align("gate_29", "gate_36")
                play("baked_Op_50"*amp(a1[v2]), "gate_29")
                play("baked_Op_50"*amp(a1[v2]), "gate_36")
            with elif_(v1==51):
                align("gate_29", "gate_36")
                play("baked_Op_51"*amp(a1[v2]), "gate_29")
                play("baked_Op_51"*amp(a1[v2]), "gate_36")
            with elif_(v1==52):
                align("gate_29", "gate_36")
                play("baked_Op_52"*amp(a1[v2]), "gate_29")
                play("baked_Op_52"*amp(a1[v2]), "gate_36")
            with elif_(v1==53):
                align("gate_29", "gate_36")
                play("baked_Op_53"*amp(a1[v2]), "gate_29")
                play("baked_Op_53"*amp(a1[v2]), "gate_36")
            with elif_(v1==54):
                align("gate_29", "gate_36")
                play("baked_Op_54"*amp(a1[v2]), "gate_29")
                play("baked_Op_54"*amp(a1[v2]), "gate_36")
            with elif_(v1==55):
                align("gate_29", "gate_36")
                play("baked_Op_55"*amp(a1[v2]), "gate_29")
                play("baked_Op_55"*amp(a1[v2]), "gate_36")
            with elif_(v1==56):
                align("gate_29", "gate_36")
                play("baked_Op_56"*amp(a1[v2]), "gate_29")
                play("baked_Op_56"*amp(a1[v2]), "gate_36")
            with elif_(v1==57):
                align("gate_29", "gate_36")
                play("baked_Op_57"*amp(a1[v2]), "gate_29")
                play("baked_Op_57"*amp(a1[v2]), "gate_36")
            with elif_(v1==58):
                align("gate_29", "gate_36")
                play("baked_Op_58"*amp(a1[v2]), "gate_29")
                play("baked_Op_58"*amp(a1[v2]), "gate_36")
            with elif_(v1==59):
                align("gate_29", "gate_36")
                play("baked_Op_59"*amp(a1[v2]), "gate_29")
                play("baked_Op_59"*amp(a1[v2]), "gate_36")
            with elif_(v1==60):
                align("gate_29", "gate_36")
                play("baked_Op_60"*amp(a1[v2]), "gate_29")
                play("baked_Op_60"*amp(a1[v2]), "gate_36")
            with elif_(v1==61):
                align("gate_29", "gate_36")
                play("baked_Op_61"*amp(a1[v2]), "gate_29")
                play("baked_Op_61"*amp(a1[v2]), "gate_36")
            with elif_(v1==62):
                align("gate_29", "gate_36")
                play("baked_Op_62"*amp(a1[v2]), "gate_29")
                play("baked_Op_62"*amp(a1[v2]), "gate_36")
            with elif_(v1==63):
                align("gate_29", "gate_36")
                play("baked_Op_63"*amp(a1[v2]), "gate_29")
                play("baked_Op_63"*amp(a1[v2]), "gate_36")
            with elif_(v1==64):
                align("gate_29", "gate_36")
                play("baked_Op_64"*amp(a1[v2]), "gate_29")
                play("baked_Op_64"*amp(a1[v2]), "gate_36")
            with elif_(v1==65):
                align("gate_29", "gate_36")
                play("baked_Op_65"*amp(a1[v2]), "gate_29")
                play("baked_Op_65"*amp(a1[v2]), "gate_36")
            with elif_(v1==66):
                align("gate_29", "gate_36")
                play("baked_Op_66"*amp(a1[v2]), "gate_29")
                play("baked_Op_66"*amp(a1[v2]), "gate_36")
            with elif_(v1==67):
                align("gate_29", "gate_36")
                play("baked_Op_67"*amp(a1[v2]), "gate_29")
                play("baked_Op_67"*amp(a1[v2]), "gate_36")
            with elif_(v1==68):
                align("gate_29", "gate_36")
                play("baked_Op_68"*amp(a1[v2]), "gate_29")
                play("baked_Op_68"*amp(a1[v2]), "gate_36")
            with elif_(v1==69):
                align("gate_29", "gate_36")
                play("baked_Op_69"*amp(a1[v2]), "gate_29")
                play("baked_Op_69"*amp(a1[v2]), "gate_36")
            with elif_(v1==70):
                align("gate_29", "gate_36")
                play("baked_Op_70"*amp(a1[v2]), "gate_29")
                play("baked_Op_70"*amp(a1[v2]), "gate_36")
            with elif_(v1==71):
                align("gate_29", "gate_36")
                play("baked_Op_71"*amp(a1[v2]), "gate_29")
                play("baked_Op_71"*amp(a1[v2]), "gate_36")
            with elif_(v1==72):
                align("gate_29", "gate_36")
                play("baked_Op_72"*amp(a1[v2]), "gate_29")
                play("baked_Op_72"*amp(a1[v2]), "gate_36")
            with elif_(v1==73):
                align("gate_29", "gate_36")
                play("baked_Op_73"*amp(a1[v2]), "gate_29")
                play("baked_Op_73"*amp(a1[v2]), "gate_36")
            with elif_(v1==74):
                align("gate_29", "gate_36")
                play("baked_Op_74"*amp(a1[v2]), "gate_29")
                play("baked_Op_74"*amp(a1[v2]), "gate_36")
            with elif_(v1==75):
                align("gate_29", "gate_36")
                play("baked_Op_75"*amp(a1[v2]), "gate_29")
                play("baked_Op_75"*amp(a1[v2]), "gate_36")
            with elif_(v1==76):
                align("gate_29", "gate_36")
                play("baked_Op_76"*amp(a1[v2]), "gate_29")
                play("baked_Op_76"*amp(a1[v2]), "gate_36")
            with elif_(v1==77):
                align("gate_29", "gate_36")
                play("baked_Op_77"*amp(a1[v2]), "gate_29")
                play("baked_Op_77"*amp(a1[v2]), "gate_36")
            with elif_(v1==78):
                align("gate_29", "gate_36")
                play("baked_Op_78"*amp(a1[v2]), "gate_29")
                play("baked_Op_78"*amp(a1[v2]), "gate_36")
            with elif_(v1==79):
                align("gate_29", "gate_36")
                play("baked_Op_79"*amp(a1[v2]), "gate_29")
                play("baked_Op_79"*amp(a1[v2]), "gate_36")
            with elif_(v1==80):
                align("gate_29", "gate_36")
                play("baked_Op_80"*amp(a1[v2]), "gate_29")
                play("baked_Op_80"*amp(a1[v2]), "gate_36")
            with elif_(v1==81):
                align("gate_29", "gate_36")
                play("baked_Op_81"*amp(a1[v2]), "gate_29")
                play("baked_Op_81"*amp(a1[v2]), "gate_36")
            with elif_(v1==82):
                align("gate_29", "gate_36")
                play("baked_Op_82"*amp(a1[v2]), "gate_29")
                play("baked_Op_82"*amp(a1[v2]), "gate_36")
            with elif_(v1==83):
                align("gate_29", "gate_36")
                play("baked_Op_83"*amp(a1[v2]), "gate_29")
                play("baked_Op_83"*amp(a1[v2]), "gate_36")
            with elif_(v1==84):
                align("gate_29", "gate_36")
                play("baked_Op_84"*amp(a1[v2]), "gate_29")
                play("baked_Op_84"*amp(a1[v2]), "gate_36")
            with elif_(v1==85):
                align("gate_29", "gate_36")
                play("baked_Op_85"*amp(a1[v2]), "gate_29")
                play("baked_Op_85"*amp(a1[v2]), "gate_36")
            with elif_(v1==86):
                align("gate_29", "gate_36")
                play("baked_Op_86"*amp(a1[v2]), "gate_29")
                play("baked_Op_86"*amp(a1[v2]), "gate_36")
            with elif_(v1==87):
                align("gate_29", "gate_36")
                play("baked_Op_87"*amp(a1[v2]), "gate_29")
                play("baked_Op_87"*amp(a1[v2]), "gate_36")
            with elif_(v1==88):
                align("gate_29", "gate_36")
                play("baked_Op_88"*amp(a1[v2]), "gate_29")
                play("baked_Op_88"*amp(a1[v2]), "gate_36")
            with elif_(v1==89):
                align("gate_29", "gate_36")
                play("baked_Op_89"*amp(a1[v2]), "gate_29")
                play("baked_Op_89"*amp(a1[v2]), "gate_36")
            with elif_(v1==90):
                align("gate_29", "gate_36")
                play("baked_Op_90"*amp(a1[v2]), "gate_29")
                play("baked_Op_90"*amp(a1[v2]), "gate_36")
            with elif_(v1==91):
                align("gate_29", "gate_36")
                play("baked_Op_91"*amp(a1[v2]), "gate_29")
                play("baked_Op_91"*amp(a1[v2]), "gate_36")
            with elif_(v1==92):
                align("gate_29", "gate_36")
                play("baked_Op_92"*amp(a1[v2]), "gate_29")
                play("baked_Op_92"*amp(a1[v2]), "gate_36")
            with elif_(v1==93):
                align("gate_29", "gate_36")
                play("baked_Op_93"*amp(a1[v2]), "gate_29")
                play("baked_Op_93"*amp(a1[v2]), "gate_36")
            with elif_(v1==94):
                align("gate_29", "gate_36")
                play("baked_Op_94"*amp(a1[v2]), "gate_29")
                play("baked_Op_94"*amp(a1[v2]), "gate_36")
            with elif_(v1==95):
                align("gate_29", "gate_36")
                play("baked_Op_95"*amp(a1[v2]), "gate_29")
                play("baked_Op_95"*amp(a1[v2]), "gate_36")
            with elif_(v1==96):
                align("gate_29", "gate_36")
                play("baked_Op_96"*amp(a1[v2]), "gate_29")
                play("baked_Op_96"*amp(a1[v2]), "gate_36")
            with elif_(v1==97):
                align("gate_29", "gate_36")
                play("baked_Op_97"*amp(a1[v2]), "gate_29")
                play("baked_Op_97"*amp(a1[v2]), "gate_36")
            with elif_(v1==98):
                align("gate_29", "gate_36")
                play("baked_Op_98"*amp(a1[v2]), "gate_29")
                play("baked_Op_98"*amp(a1[v2]), "gate_36")
            with elif_(v1==99):
                align("gate_29", "gate_36")
                play("baked_Op_99"*amp(a1[v2]), "gate_29")
                play("baked_Op_99"*amp(a1[v2]), "gate_36")
            with elif_(v1==100):
                align("gate_29", "gate_36")
                play("baked_Op_100"*amp(a1[v2]), "gate_29")
                play("baked_Op_100"*amp(a1[v2]), "gate_36")
            with elif_(v1==101):
                align("gate_29", "gate_36")
                play("baked_Op_101"*amp(a1[v2]), "gate_29")
                play("baked_Op_101"*amp(a1[v2]), "gate_36")
            with elif_(v1==102):
                align("gate_29", "gate_36")
                play("baked_Op_102"*amp(a1[v2]), "gate_29")
                play("baked_Op_102"*amp(a1[v2]), "gate_36")
            with elif_(v1==103):
                align("gate_29", "gate_36")
                play("baked_Op_103"*amp(a1[v2]), "gate_29")
                play("baked_Op_103"*amp(a1[v2]), "gate_36")
            with elif_(v1==104):
                align("gate_29", "gate_36")
                play("baked_Op_104"*amp(a1[v2]), "gate_29")
                play("baked_Op_104"*amp(a1[v2]), "gate_36")
            with elif_(v1==105):
                align("gate_29", "gate_36")
                play("baked_Op_105"*amp(a1[v2]), "gate_29")
                play("baked_Op_105"*amp(a1[v2]), "gate_36")
            with elif_(v1==106):
                align("gate_29", "gate_36")
                play("baked_Op_106"*amp(a1[v2]), "gate_29")
                play("baked_Op_106"*amp(a1[v2]), "gate_36")
            with elif_(v1==107):
                align("gate_29", "gate_36")
                play("baked_Op_107"*amp(a1[v2]), "gate_29")
                play("baked_Op_107"*amp(a1[v2]), "gate_36")
            with elif_(v1==108):
                align("gate_29", "gate_36")
                play("baked_Op_108"*amp(a1[v2]), "gate_29")
                play("baked_Op_108"*amp(a1[v2]), "gate_36")
            with elif_(v1==109):
                align("gate_29", "gate_36")
                play("baked_Op_109"*amp(a1[v2]), "gate_29")
                play("baked_Op_109"*amp(a1[v2]), "gate_36")
            with elif_(v1==110):
                align("gate_29", "gate_36")
                play("baked_Op_110"*amp(a1[v2]), "gate_29")
                play("baked_Op_110"*amp(a1[v2]), "gate_36")
            with elif_(v1==111):
                align("gate_29", "gate_36")
                play("baked_Op_111"*amp(a1[v2]), "gate_29")
                play("baked_Op_111"*amp(a1[v2]), "gate_36")
            with elif_(v1==112):
                align("gate_29", "gate_36")
                play("baked_Op_112"*amp(a1[v2]), "gate_29")
                play("baked_Op_112"*amp(a1[v2]), "gate_36")
            with elif_(v1==113):
                align("gate_29", "gate_36")
                play("baked_Op_113"*amp(a1[v2]), "gate_29")
                play("baked_Op_113"*amp(a1[v2]), "gate_36")
            with elif_(v1==114):
                align("gate_29", "gate_36")
                play("baked_Op_114"*amp(a1[v2]), "gate_29")
                play("baked_Op_114"*amp(a1[v2]), "gate_36")
            with elif_(v1==115):
                align("gate_29", "gate_36")
                play("baked_Op_115"*amp(a1[v2]), "gate_29")
                play("baked_Op_115"*amp(a1[v2]), "gate_36")
            with elif_(v1==116):
                align("gate_29", "gate_36")
                play("baked_Op_116"*amp(a1[v2]), "gate_29")
                play("baked_Op_116"*amp(a1[v2]), "gate_36")
            with elif_(v1==117):
                align("gate_29", "gate_36")
                play("baked_Op_117"*amp(a1[v2]), "gate_29")
                play("baked_Op_117"*amp(a1[v2]), "gate_36")
            with elif_(v1==118):
                align("gate_29", "gate_36")
                play("baked_Op_118"*amp(a1[v2]), "gate_29")
                play("baked_Op_118"*amp(a1[v2]), "gate_36")
            with elif_(v1==119):
                align("gate_29", "gate_36")
                play("baked_Op_119"*amp(a1[v2]), "gate_29")
                play("baked_Op_119"*amp(a1[v2]), "gate_36")
            with elif_(v1==120):
                align("gate_29", "gate_36")
                play("baked_Op_120"*amp(a1[v2]), "gate_29")
                play("baked_Op_120"*amp(a1[v2]), "gate_36")
            with elif_(v1==121):
                align("gate_29", "gate_36")
                play("baked_Op_121"*amp(a1[v2]), "gate_29")
                play("baked_Op_121"*amp(a1[v2]), "gate_36")
            with elif_(v1==122):
                align("gate_29", "gate_36")
                play("baked_Op_122"*amp(a1[v2]), "gate_29")
                play("baked_Op_122"*amp(a1[v2]), "gate_36")
            with elif_(v1==123):
                align("gate_29", "gate_36")
                play("baked_Op_123"*amp(a1[v2]), "gate_29")
                play("baked_Op_123"*amp(a1[v2]), "gate_36")
            with elif_(v1==124):
                align("gate_29", "gate_36")
                play("baked_Op_124"*amp(a1[v2]), "gate_29")
                play("baked_Op_124"*amp(a1[v2]), "gate_36")
            with elif_(v1==125):
                align("gate_29", "gate_36")
                play("baked_Op_125"*amp(a1[v2]), "gate_29")
                play("baked_Op_125"*amp(a1[v2]), "gate_36")
            with elif_(v1==126):
                align("gate_29", "gate_36")
                play("baked_Op_126"*amp(a1[v2]), "gate_29")
                play("baked_Op_126"*amp(a1[v2]), "gate_36")
            with elif_(v1==127):
                align("gate_29", "gate_36")
                play("baked_Op_127"*amp(a1[v2]), "gate_29")
                play("baked_Op_127"*amp(a1[v2]), "gate_36")
            with elif_(v1==128):
                align("gate_29", "gate_36")
                play("baked_Op_128"*amp(a1[v2]), "gate_29")
                play("baked_Op_128"*amp(a1[v2]), "gate_36")
            with elif_(v1==129):
                align("gate_29", "gate_36")
                play("baked_Op_129"*amp(a1[v2]), "gate_29")
                play("baked_Op_129"*amp(a1[v2]), "gate_36")
            with elif_(v1==130):
                align("gate_29", "gate_36")
                play("baked_Op_130"*amp(a1[v2]), "gate_29")
                play("baked_Op_130"*amp(a1[v2]), "gate_36")
            with elif_(v1==131):
                align("gate_29", "gate_36")
                play("baked_Op_131"*amp(a1[v2]), "gate_29")
                play("baked_Op_131"*amp(a1[v2]), "gate_36")
            with elif_(v1==132):
                align("gate_29", "gate_36")
                play("baked_Op_132"*amp(a1[v2]), "gate_29")
                play("baked_Op_132"*amp(a1[v2]), "gate_36")
            with elif_(v1==133):
                align("gate_29", "gate_36")
                play("baked_Op_133"*amp(a1[v2]), "gate_29")
                play("baked_Op_133"*amp(a1[v2]), "gate_36")
            with elif_(v1==134):
                align("gate_29", "gate_36")
                play("baked_Op_134"*amp(a1[v2]), "gate_29")
                play("baked_Op_134"*amp(a1[v2]), "gate_36")
            with elif_(v1==135):
                align("gate_29", "gate_36")
                play("baked_Op_135"*amp(a1[v2]), "gate_29")
                play("baked_Op_135"*amp(a1[v2]), "gate_36")
            with elif_(v1==136):
                align("gate_29", "gate_36")
                play("baked_Op_136"*amp(a1[v2]), "gate_29")
                play("baked_Op_136"*amp(a1[v2]), "gate_36")
            with elif_(v1==137):
                align("gate_29", "gate_36")
                play("baked_Op_137"*amp(a1[v2]), "gate_29")
                play("baked_Op_137"*amp(a1[v2]), "gate_36")
            with elif_(v1==138):
                align("gate_29", "gate_36")
                play("baked_Op_138"*amp(a1[v2]), "gate_29")
                play("baked_Op_138"*amp(a1[v2]), "gate_36")
            with elif_(v1==139):
                align("gate_29", "gate_36")
                play("baked_Op_139"*amp(a1[v2]), "gate_29")
                play("baked_Op_139"*amp(a1[v2]), "gate_36")
            with elif_(v1==140):
                align("gate_29", "gate_36")
                play("baked_Op_140"*amp(a1[v2]), "gate_29")
                play("baked_Op_140"*amp(a1[v2]), "gate_36")
            with elif_(v1==141):
                align("gate_29", "gate_36")
                play("baked_Op_141"*amp(a1[v2]), "gate_29")
                play("baked_Op_141"*amp(a1[v2]), "gate_36")
            with elif_(v1==142):
                align("gate_29", "gate_36")
                play("baked_Op_142"*amp(a1[v2]), "gate_29")
                play("baked_Op_142"*amp(a1[v2]), "gate_36")
            with elif_(v1==143):
                align("gate_29", "gate_36")
                play("baked_Op_143"*amp(a1[v2]), "gate_29")
                play("baked_Op_143"*amp(a1[v2]), "gate_36")
            with elif_(v1==144):
                align("gate_29", "gate_36")
                play("baked_Op_144"*amp(a1[v2]), "gate_29")
                play("baked_Op_144"*amp(a1[v2]), "gate_36")
            with elif_(v1==145):
                align("gate_29", "gate_36")
                play("baked_Op_145"*amp(a1[v2]), "gate_29")
                play("baked_Op_145"*amp(a1[v2]), "gate_36")
            with elif_(v1==146):
                align("gate_29", "gate_36")
                play("baked_Op_146"*amp(a1[v2]), "gate_29")
                play("baked_Op_146"*amp(a1[v2]), "gate_36")
            with elif_(v1==147):
                align("gate_29", "gate_36")
                play("baked_Op_147"*amp(a1[v2]), "gate_29")
                play("baked_Op_147"*amp(a1[v2]), "gate_36")
            with elif_(v1==148):
                align("gate_29", "gate_36")
                play("baked_Op_148"*amp(a1[v2]), "gate_29")
                play("baked_Op_148"*amp(a1[v2]), "gate_36")
            with elif_(v1==149):
                align("gate_29", "gate_36")
                play("baked_Op_149"*amp(a1[v2]), "gate_29")
                play("baked_Op_149"*amp(a1[v2]), "gate_36")
            with elif_(v1==150):
                align("gate_29", "gate_36")
                play("baked_Op_150"*amp(a1[v2]), "gate_29")
                play("baked_Op_150"*amp(a1[v2]), "gate_36")
            with elif_(v1==151):
                align("gate_29", "gate_36")
                play("baked_Op_151"*amp(a1[v2]), "gate_29")
                play("baked_Op_151"*amp(a1[v2]), "gate_36")
            with elif_(v1==152):
                align("gate_29", "gate_36")
                play("baked_Op_152"*amp(a1[v2]), "gate_29")
                play("baked_Op_152"*amp(a1[v2]), "gate_36")
            with elif_(v1==153):
                align("gate_29", "gate_36")
                play("baked_Op_153"*amp(a1[v2]), "gate_29")
                play("baked_Op_153"*amp(a1[v2]), "gate_36")
            with elif_(v1==154):
                align("gate_29", "gate_36")
                play("baked_Op_154"*amp(a1[v2]), "gate_29")
                play("baked_Op_154"*amp(a1[v2]), "gate_36")
            with elif_(v1==155):
                align("gate_29", "gate_36")
                play("baked_Op_155"*amp(a1[v2]), "gate_29")
                play("baked_Op_155"*amp(a1[v2]), "gate_36")
            with elif_(v1==156):
                align("gate_29", "gate_36")
                play("baked_Op_156"*amp(a1[v2]), "gate_29")
                play("baked_Op_156"*amp(a1[v2]), "gate_36")
            with elif_(v1==157):
                align("gate_29", "gate_36")
                play("baked_Op_157"*amp(a1[v2]), "gate_29")
                play("baked_Op_157"*amp(a1[v2]), "gate_36")
            with elif_(v1==158):
                align("gate_29", "gate_36")
                play("baked_Op_158"*amp(a1[v2]), "gate_29")
                play("baked_Op_158"*amp(a1[v2]), "gate_36")
            with elif_(v1==159):
                align("gate_29", "gate_36")
                play("baked_Op_159"*amp(a1[v2]), "gate_29")
                play("baked_Op_159"*amp(a1[v2]), "gate_36")
            with elif_(v1==160):
                align("gate_29", "gate_36")
                play("baked_Op_160"*amp(a1[v2]), "gate_29")
                play("baked_Op_160"*amp(a1[v2]), "gate_36")
            with elif_(v1==161):
                align("gate_29", "gate_36")
                play("baked_Op_161"*amp(a1[v2]), "gate_29")
                play("baked_Op_161"*amp(a1[v2]), "gate_36")
            with elif_(v1==162):
                align("gate_29", "gate_36")
                play("baked_Op_162"*amp(a1[v2]), "gate_29")
                play("baked_Op_162"*amp(a1[v2]), "gate_36")
            with elif_(v1==163):
                align("gate_29", "gate_36")
                play("baked_Op_163"*amp(a1[v2]), "gate_29")
                play("baked_Op_163"*amp(a1[v2]), "gate_36")
            with elif_(v1==164):
                align("gate_29", "gate_36")
                play("baked_Op_164"*amp(a1[v2]), "gate_29")
                play("baked_Op_164"*amp(a1[v2]), "gate_36")
            with elif_(v1==165):
                align("gate_29", "gate_36")
                play("baked_Op_165"*amp(a1[v2]), "gate_29")
                play("baked_Op_165"*amp(a1[v2]), "gate_36")
            with elif_(v1==166):
                align("gate_29", "gate_36")
                play("baked_Op_166"*amp(a1[v2]), "gate_29")
                play("baked_Op_166"*amp(a1[v2]), "gate_36")
            with elif_(v1==167):
                align("gate_29", "gate_36")
                play("baked_Op_167"*amp(a1[v2]), "gate_29")
                play("baked_Op_167"*amp(a1[v2]), "gate_36")
            with elif_(v1==168):
                align("gate_29", "gate_36")
                play("baked_Op_168"*amp(a1[v2]), "gate_29")
                play("baked_Op_168"*amp(a1[v2]), "gate_36")
            with elif_(v1==169):
                align("gate_29", "gate_36")
                play("baked_Op_169"*amp(a1[v2]), "gate_29")
                play("baked_Op_169"*amp(a1[v2]), "gate_36")
            with elif_(v1==170):
                align("gate_29", "gate_36")
                play("baked_Op_170"*amp(a1[v2]), "gate_29")
                play("baked_Op_170"*amp(a1[v2]), "gate_36")
            with elif_(v1==171):
                align("gate_29", "gate_36")
                play("baked_Op_171"*amp(a1[v2]), "gate_29")
                play("baked_Op_171"*amp(a1[v2]), "gate_36")
            with elif_(v1==172):
                align("gate_29", "gate_36")
                play("baked_Op_172"*amp(a1[v2]), "gate_29")
                play("baked_Op_172"*amp(a1[v2]), "gate_36")
            with elif_(v1==173):
                align("gate_29", "gate_36")
                play("baked_Op_173"*amp(a1[v2]), "gate_29")
                play("baked_Op_173"*amp(a1[v2]), "gate_36")
            with elif_(v1==174):
                align("gate_29", "gate_36")
                play("baked_Op_174"*amp(a1[v2]), "gate_29")
                play("baked_Op_174"*amp(a1[v2]), "gate_36")
            with elif_(v1==175):
                align("gate_29", "gate_36")
                play("baked_Op_175"*amp(a1[v2]), "gate_29")
                play("baked_Op_175"*amp(a1[v2]), "gate_36")
            with elif_(v1==176):
                align("gate_29", "gate_36")
                play("baked_Op_176"*amp(a1[v2]), "gate_29")
                play("baked_Op_176"*amp(a1[v2]), "gate_36")
            with elif_(v1==177):
                align("gate_29", "gate_36")
                play("baked_Op_177"*amp(a1[v2]), "gate_29")
                play("baked_Op_177"*amp(a1[v2]), "gate_36")
            with elif_(v1==178):
                align("gate_29", "gate_36")
                play("baked_Op_178"*amp(a1[v2]), "gate_29")
                play("baked_Op_178"*amp(a1[v2]), "gate_36")
            with elif_(v1==179):
                align("gate_29", "gate_36")
                play("baked_Op_179"*amp(a1[v2]), "gate_29")
                play("baked_Op_179"*amp(a1[v2]), "gate_36")
            with elif_(v1==180):
                align("gate_29", "gate_36")
                play("baked_Op_180"*amp(a1[v2]), "gate_29")
                play("baked_Op_180"*amp(a1[v2]), "gate_36")
            with elif_(v1==181):
                align("gate_29", "gate_36")
                play("baked_Op_181"*amp(a1[v2]), "gate_29")
                play("baked_Op_181"*amp(a1[v2]), "gate_36")
            with elif_(v1==182):
                align("gate_29", "gate_36")
                play("baked_Op_182"*amp(a1[v2]), "gate_29")
                play("baked_Op_182"*amp(a1[v2]), "gate_36")
            with elif_(v1==183):
                align("gate_29", "gate_36")
                play("baked_Op_183"*amp(a1[v2]), "gate_29")
                play("baked_Op_183"*amp(a1[v2]), "gate_36")
            with elif_(v1==184):
                align("gate_29", "gate_36")
                play("baked_Op_184"*amp(a1[v2]), "gate_29")
                play("baked_Op_184"*amp(a1[v2]), "gate_36")
            with elif_(v1==185):
                align("gate_29", "gate_36")
                play("baked_Op_185"*amp(a1[v2]), "gate_29")
                play("baked_Op_185"*amp(a1[v2]), "gate_36")
            with elif_(v1==186):
                align("gate_29", "gate_36")
                play("baked_Op_186"*amp(a1[v2]), "gate_29")
                play("baked_Op_186"*amp(a1[v2]), "gate_36")
            with elif_(v1==187):
                align("gate_29", "gate_36")
                play("baked_Op_187"*amp(a1[v2]), "gate_29")
                play("baked_Op_187"*amp(a1[v2]), "gate_36")
            with elif_(v1==188):
                align("gate_29", "gate_36")
                play("baked_Op_188"*amp(a1[v2]), "gate_29")
                play("baked_Op_188"*amp(a1[v2]), "gate_36")
            with elif_(v1==189):
                align("gate_29", "gate_36")
                play("baked_Op_189"*amp(a1[v2]), "gate_29")
                play("baked_Op_189"*amp(a1[v2]), "gate_36")
            with elif_(v1==190):
                align("gate_29", "gate_36")
                play("baked_Op_190"*amp(a1[v2]), "gate_29")
                play("baked_Op_190"*amp(a1[v2]), "gate_36")
            with elif_(v1==191):
                align("gate_29", "gate_36")
                play("baked_Op_191"*amp(a1[v2]), "gate_29")
                play("baked_Op_191"*amp(a1[v2]), "gate_36")
            with elif_(v1==192):
                align("gate_29", "gate_36")
                play("baked_Op_192"*amp(a1[v2]), "gate_29")
                play("baked_Op_192"*amp(a1[v2]), "gate_36")
            with elif_(v1==193):
                align("gate_29", "gate_36")
                play("baked_Op_193"*amp(a1[v2]), "gate_29")
                play("baked_Op_193"*amp(a1[v2]), "gate_36")
            with elif_(v1==194):
                align("gate_29", "gate_36")
                play("baked_Op_194"*amp(a1[v2]), "gate_29")
                play("baked_Op_194"*amp(a1[v2]), "gate_36")
            with elif_(v1==195):
                align("gate_29", "gate_36")
                play("baked_Op_195"*amp(a1[v2]), "gate_29")
                play("baked_Op_195"*amp(a1[v2]), "gate_36")
            with elif_(v1==196):
                align("gate_29", "gate_36")
                play("baked_Op_196"*amp(a1[v2]), "gate_29")
                play("baked_Op_196"*amp(a1[v2]), "gate_36")
            with elif_(v1==197):
                align("gate_29", "gate_36")
                play("baked_Op_197"*amp(a1[v2]), "gate_29")
                play("baked_Op_197"*amp(a1[v2]), "gate_36")
            with elif_(v1==198):
                align("gate_29", "gate_36")
                play("baked_Op_198"*amp(a1[v2]), "gate_29")
                play("baked_Op_198"*amp(a1[v2]), "gate_36")
            with elif_(v1==199):
                align("gate_29", "gate_36")
                play("baked_Op_199"*amp(a1[v2]), "gate_29")
                play("baked_Op_199"*amp(a1[v2]), "gate_36")
            play("CW"*amp(0.4), "gate_36", duration=100)
            play("CW"*amp(-0.4), "gate_29", duration=100)
            ramp_to_zero("gate_36", 1)
            ramp_to_zero("gate_29", 1)


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
            'samples': [0.0] * 202 + [-0.2081559, 0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_1': {
            'type': 'arbitrary',
            'samples': [0.0] * 202 + [0.254468348, 0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_2': {
            'type': 'arbitrary',
            'samples': [0.0] * 201 + [-0.2081559] * 2 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_2': {
            'type': 'arbitrary',
            'samples': [0.0] * 201 + [0.254468348] * 2 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_3': {
            'type': 'arbitrary',
            'samples': [0.0] * 200 + [-0.2081559] * 3 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_3': {
            'type': 'arbitrary',
            'samples': [0.0] * 200 + [0.254468348] * 3 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_4': {
            'type': 'arbitrary',
            'samples': [0.0] * 199 + [-0.2081559] * 4 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_4': {
            'type': 'arbitrary',
            'samples': [0.0] * 199 + [0.254468348] * 4 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_5': {
            'type': 'arbitrary',
            'samples': [0.0] * 198 + [-0.2081559] * 5 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_5': {
            'type': 'arbitrary',
            'samples': [0.0] * 198 + [0.254468348] * 5 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_6': {
            'type': 'arbitrary',
            'samples': [0.0] * 197 + [-0.2081559] * 6 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_6': {
            'type': 'arbitrary',
            'samples': [0.0] * 197 + [0.254468348] * 6 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_7': {
            'type': 'arbitrary',
            'samples': [0.0] * 196 + [-0.2081559] * 7 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_7': {
            'type': 'arbitrary',
            'samples': [0.0] * 196 + [0.254468348] * 7 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_8': {
            'type': 'arbitrary',
            'samples': [0.0] * 195 + [-0.2081559] * 8 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_8': {
            'type': 'arbitrary',
            'samples': [0.0] * 195 + [0.254468348] * 8 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_9': {
            'type': 'arbitrary',
            'samples': [0.0] * 194 + [-0.2081559] * 9 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_9': {
            'type': 'arbitrary',
            'samples': [0.0] * 194 + [0.254468348] * 9 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_10': {
            'type': 'arbitrary',
            'samples': [0.0] * 193 + [-0.2081559] * 10 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_10': {
            'type': 'arbitrary',
            'samples': [0.0] * 193 + [0.254468348] * 10 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_11': {
            'type': 'arbitrary',
            'samples': [0.0] * 192 + [-0.2081559] * 11 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_11': {
            'type': 'arbitrary',
            'samples': [0.0] * 192 + [0.254468348] * 11 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_12': {
            'type': 'arbitrary',
            'samples': [0.0] * 191 + [-0.2081559] * 12 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_12': {
            'type': 'arbitrary',
            'samples': [0.0] * 191 + [0.254468348] * 12 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_13': {
            'type': 'arbitrary',
            'samples': [0.0] * 190 + [-0.2081559] * 13 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_13': {
            'type': 'arbitrary',
            'samples': [0.0] * 190 + [0.254468348] * 13 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_14': {
            'type': 'arbitrary',
            'samples': [0.0] * 189 + [-0.2081559] * 14 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_14': {
            'type': 'arbitrary',
            'samples': [0.0] * 189 + [0.254468348] * 14 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_15': {
            'type': 'arbitrary',
            'samples': [0.0] * 188 + [-0.2081559] * 15 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_15': {
            'type': 'arbitrary',
            'samples': [0.0] * 188 + [0.254468348] * 15 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_16': {
            'type': 'arbitrary',
            'samples': [0.0] * 187 + [-0.2081559] * 16 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_16': {
            'type': 'arbitrary',
            'samples': [0.0] * 187 + [0.254468348] * 16 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_17': {
            'type': 'arbitrary',
            'samples': [0.0] * 186 + [-0.2081559] * 17 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_17': {
            'type': 'arbitrary',
            'samples': [0.0] * 186 + [0.254468348] * 17 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_18': {
            'type': 'arbitrary',
            'samples': [0.0] * 185 + [-0.2081559] * 18 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_18': {
            'type': 'arbitrary',
            'samples': [0.0] * 185 + [0.254468348] * 18 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_19': {
            'type': 'arbitrary',
            'samples': [0.0] * 184 + [-0.2081559] * 19 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_19': {
            'type': 'arbitrary',
            'samples': [0.0] * 184 + [0.254468348] * 19 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_20': {
            'type': 'arbitrary',
            'samples': [0.0] * 183 + [-0.2081559] * 20 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_20': {
            'type': 'arbitrary',
            'samples': [0.0] * 183 + [0.254468348] * 20 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_21': {
            'type': 'arbitrary',
            'samples': [0.0] * 182 + [-0.2081559] * 21 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_21': {
            'type': 'arbitrary',
            'samples': [0.0] * 182 + [0.254468348] * 21 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_22': {
            'type': 'arbitrary',
            'samples': [0.0] * 181 + [-0.2081559] * 22 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_22': {
            'type': 'arbitrary',
            'samples': [0.0] * 181 + [0.254468348] * 22 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_23': {
            'type': 'arbitrary',
            'samples': [0.0] * 180 + [-0.2081559] * 23 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_23': {
            'type': 'arbitrary',
            'samples': [0.0] * 180 + [0.254468348] * 23 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_24': {
            'type': 'arbitrary',
            'samples': [0.0] * 179 + [-0.2081559] * 24 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_24': {
            'type': 'arbitrary',
            'samples': [0.0] * 179 + [0.254468348] * 24 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_25': {
            'type': 'arbitrary',
            'samples': [0.0] * 178 + [-0.2081559] * 25 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_25': {
            'type': 'arbitrary',
            'samples': [0.0] * 178 + [0.254468348] * 25 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_26': {
            'type': 'arbitrary',
            'samples': [0.0] * 177 + [-0.2081559] * 26 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_26': {
            'type': 'arbitrary',
            'samples': [0.0] * 177 + [0.254468348] * 26 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_27': {
            'type': 'arbitrary',
            'samples': [0.0] * 176 + [-0.2081559] * 27 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_27': {
            'type': 'arbitrary',
            'samples': [0.0] * 176 + [0.254468348] * 27 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_28': {
            'type': 'arbitrary',
            'samples': [0.0] * 175 + [-0.2081559] * 28 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_28': {
            'type': 'arbitrary',
            'samples': [0.0] * 175 + [0.254468348] * 28 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_29': {
            'type': 'arbitrary',
            'samples': [0.0] * 174 + [-0.2081559] * 29 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_29': {
            'type': 'arbitrary',
            'samples': [0.0] * 174 + [0.254468348] * 29 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_30': {
            'type': 'arbitrary',
            'samples': [0.0] * 173 + [-0.2081559] * 30 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_30': {
            'type': 'arbitrary',
            'samples': [0.0] * 173 + [0.254468348] * 30 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_31': {
            'type': 'arbitrary',
            'samples': [0.0] * 172 + [-0.2081559] * 31 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_31': {
            'type': 'arbitrary',
            'samples': [0.0] * 172 + [0.254468348] * 31 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_32': {
            'type': 'arbitrary',
            'samples': [0.0] * 171 + [-0.2081559] * 32 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_32': {
            'type': 'arbitrary',
            'samples': [0.0] * 171 + [0.254468348] * 32 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_33': {
            'type': 'arbitrary',
            'samples': [0.0] * 170 + [-0.2081559] * 33 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_33': {
            'type': 'arbitrary',
            'samples': [0.0] * 170 + [0.254468348] * 33 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_34': {
            'type': 'arbitrary',
            'samples': [0.0] * 169 + [-0.2081559] * 34 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_34': {
            'type': 'arbitrary',
            'samples': [0.0] * 169 + [0.254468348] * 34 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_35': {
            'type': 'arbitrary',
            'samples': [0.0] * 168 + [-0.2081559] * 35 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_35': {
            'type': 'arbitrary',
            'samples': [0.0] * 168 + [0.254468348] * 35 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_36': {
            'type': 'arbitrary',
            'samples': [0.0] * 167 + [-0.2081559] * 36 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_36': {
            'type': 'arbitrary',
            'samples': [0.0] * 167 + [0.254468348] * 36 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_37': {
            'type': 'arbitrary',
            'samples': [0.0] * 166 + [-0.2081559] * 37 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_37': {
            'type': 'arbitrary',
            'samples': [0.0] * 166 + [0.254468348] * 37 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_38': {
            'type': 'arbitrary',
            'samples': [0.0] * 165 + [-0.2081559] * 38 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_38': {
            'type': 'arbitrary',
            'samples': [0.0] * 165 + [0.254468348] * 38 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_39': {
            'type': 'arbitrary',
            'samples': [0.0] * 164 + [-0.2081559] * 39 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_39': {
            'type': 'arbitrary',
            'samples': [0.0] * 164 + [0.254468348] * 39 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_40': {
            'type': 'arbitrary',
            'samples': [0.0] * 163 + [-0.2081559] * 40 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_40': {
            'type': 'arbitrary',
            'samples': [0.0] * 163 + [0.254468348] * 40 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_41': {
            'type': 'arbitrary',
            'samples': [0.0] * 162 + [-0.2081559] * 41 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_41': {
            'type': 'arbitrary',
            'samples': [0.0] * 162 + [0.254468348] * 41 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_42': {
            'type': 'arbitrary',
            'samples': [0.0] * 161 + [-0.2081559] * 42 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_42': {
            'type': 'arbitrary',
            'samples': [0.0] * 161 + [0.254468348] * 42 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_43': {
            'type': 'arbitrary',
            'samples': [0.0] * 160 + [-0.2081559] * 43 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_43': {
            'type': 'arbitrary',
            'samples': [0.0] * 160 + [0.254468348] * 43 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_44': {
            'type': 'arbitrary',
            'samples': [0.0] * 159 + [-0.2081559] * 44 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_44': {
            'type': 'arbitrary',
            'samples': [0.0] * 159 + [0.254468348] * 44 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_45': {
            'type': 'arbitrary',
            'samples': [0.0] * 158 + [-0.2081559] * 45 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_45': {
            'type': 'arbitrary',
            'samples': [0.0] * 158 + [0.254468348] * 45 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_46': {
            'type': 'arbitrary',
            'samples': [0.0] * 157 + [-0.2081559] * 46 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_46': {
            'type': 'arbitrary',
            'samples': [0.0] * 157 + [0.254468348] * 46 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_47': {
            'type': 'arbitrary',
            'samples': [0.0] * 156 + [-0.2081559] * 47 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_47': {
            'type': 'arbitrary',
            'samples': [0.0] * 156 + [0.254468348] * 47 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_48': {
            'type': 'arbitrary',
            'samples': [0.0] * 155 + [-0.2081559] * 48 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_48': {
            'type': 'arbitrary',
            'samples': [0.0] * 155 + [0.254468348] * 48 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_49': {
            'type': 'arbitrary',
            'samples': [0.0] * 154 + [-0.2081559] * 49 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_49': {
            'type': 'arbitrary',
            'samples': [0.0] * 154 + [0.254468348] * 49 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_50': {
            'type': 'arbitrary',
            'samples': [0.0] * 153 + [-0.2081559] * 50 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_50': {
            'type': 'arbitrary',
            'samples': [0.0] * 153 + [0.254468348] * 50 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_51': {
            'type': 'arbitrary',
            'samples': [0.0] * 152 + [-0.2081559] * 51 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_51': {
            'type': 'arbitrary',
            'samples': [0.0] * 152 + [0.254468348] * 51 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_52': {
            'type': 'arbitrary',
            'samples': [0.0] * 151 + [-0.2081559] * 52 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_52': {
            'type': 'arbitrary',
            'samples': [0.0] * 151 + [0.254468348] * 52 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_53': {
            'type': 'arbitrary',
            'samples': [0.0] * 150 + [-0.2081559] * 53 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_53': {
            'type': 'arbitrary',
            'samples': [0.0] * 150 + [0.254468348] * 53 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_54': {
            'type': 'arbitrary',
            'samples': [0.0] * 149 + [-0.2081559] * 54 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_54': {
            'type': 'arbitrary',
            'samples': [0.0] * 149 + [0.254468348] * 54 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_55': {
            'type': 'arbitrary',
            'samples': [0.0] * 148 + [-0.2081559] * 55 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_55': {
            'type': 'arbitrary',
            'samples': [0.0] * 148 + [0.254468348] * 55 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_56': {
            'type': 'arbitrary',
            'samples': [0.0] * 147 + [-0.2081559] * 56 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_56': {
            'type': 'arbitrary',
            'samples': [0.0] * 147 + [0.254468348] * 56 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_57': {
            'type': 'arbitrary',
            'samples': [0.0] * 146 + [-0.2081559] * 57 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_57': {
            'type': 'arbitrary',
            'samples': [0.0] * 146 + [0.254468348] * 57 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_58': {
            'type': 'arbitrary',
            'samples': [0.0] * 145 + [-0.2081559] * 58 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_58': {
            'type': 'arbitrary',
            'samples': [0.0] * 145 + [0.254468348] * 58 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_59': {
            'type': 'arbitrary',
            'samples': [0.0] * 144 + [-0.2081559] * 59 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_59': {
            'type': 'arbitrary',
            'samples': [0.0] * 144 + [0.254468348] * 59 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_60': {
            'type': 'arbitrary',
            'samples': [0.0] * 143 + [-0.2081559] * 60 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_60': {
            'type': 'arbitrary',
            'samples': [0.0] * 143 + [0.254468348] * 60 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_61': {
            'type': 'arbitrary',
            'samples': [0.0] * 142 + [-0.2081559] * 61 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_61': {
            'type': 'arbitrary',
            'samples': [0.0] * 142 + [0.254468348] * 61 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_62': {
            'type': 'arbitrary',
            'samples': [0.0] * 141 + [-0.2081559] * 62 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_62': {
            'type': 'arbitrary',
            'samples': [0.0] * 141 + [0.254468348] * 62 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_63': {
            'type': 'arbitrary',
            'samples': [0.0] * 140 + [-0.2081559] * 63 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_63': {
            'type': 'arbitrary',
            'samples': [0.0] * 140 + [0.254468348] * 63 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_64': {
            'type': 'arbitrary',
            'samples': [0.0] * 139 + [-0.2081559] * 64 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_64': {
            'type': 'arbitrary',
            'samples': [0.0] * 139 + [0.254468348] * 64 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_65': {
            'type': 'arbitrary',
            'samples': [0.0] * 138 + [-0.2081559] * 65 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_65': {
            'type': 'arbitrary',
            'samples': [0.0] * 138 + [0.254468348] * 65 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_66': {
            'type': 'arbitrary',
            'samples': [0.0] * 137 + [-0.2081559] * 66 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_66': {
            'type': 'arbitrary',
            'samples': [0.0] * 137 + [0.254468348] * 66 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_67': {
            'type': 'arbitrary',
            'samples': [0.0] * 136 + [-0.2081559] * 67 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_67': {
            'type': 'arbitrary',
            'samples': [0.0] * 136 + [0.254468348] * 67 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_68': {
            'type': 'arbitrary',
            'samples': [0.0] * 135 + [-0.2081559] * 68 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_68': {
            'type': 'arbitrary',
            'samples': [0.0] * 135 + [0.254468348] * 68 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_69': {
            'type': 'arbitrary',
            'samples': [0.0] * 134 + [-0.2081559] * 69 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_69': {
            'type': 'arbitrary',
            'samples': [0.0] * 134 + [0.254468348] * 69 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_70': {
            'type': 'arbitrary',
            'samples': [0.0] * 133 + [-0.2081559] * 70 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_70': {
            'type': 'arbitrary',
            'samples': [0.0] * 133 + [0.254468348] * 70 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_71': {
            'type': 'arbitrary',
            'samples': [0.0] * 132 + [-0.2081559] * 71 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_71': {
            'type': 'arbitrary',
            'samples': [0.0] * 132 + [0.254468348] * 71 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_72': {
            'type': 'arbitrary',
            'samples': [0.0] * 131 + [-0.2081559] * 72 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_72': {
            'type': 'arbitrary',
            'samples': [0.0] * 131 + [0.254468348] * 72 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_73': {
            'type': 'arbitrary',
            'samples': [0.0] * 130 + [-0.2081559] * 73 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_73': {
            'type': 'arbitrary',
            'samples': [0.0] * 130 + [0.254468348] * 73 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_74': {
            'type': 'arbitrary',
            'samples': [0.0] * 129 + [-0.2081559] * 74 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_74': {
            'type': 'arbitrary',
            'samples': [0.0] * 129 + [0.254468348] * 74 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_75': {
            'type': 'arbitrary',
            'samples': [0.0] * 128 + [-0.2081559] * 75 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_75': {
            'type': 'arbitrary',
            'samples': [0.0] * 128 + [0.254468348] * 75 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_76': {
            'type': 'arbitrary',
            'samples': [0.0] * 127 + [-0.2081559] * 76 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_76': {
            'type': 'arbitrary',
            'samples': [0.0] * 127 + [0.254468348] * 76 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_77': {
            'type': 'arbitrary',
            'samples': [0.0] * 126 + [-0.2081559] * 77 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_77': {
            'type': 'arbitrary',
            'samples': [0.0] * 126 + [0.254468348] * 77 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_78': {
            'type': 'arbitrary',
            'samples': [0.0] * 125 + [-0.2081559] * 78 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_78': {
            'type': 'arbitrary',
            'samples': [0.0] * 125 + [0.254468348] * 78 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_79': {
            'type': 'arbitrary',
            'samples': [0.0] * 124 + [-0.2081559] * 79 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_79': {
            'type': 'arbitrary',
            'samples': [0.0] * 124 + [0.254468348] * 79 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_80': {
            'type': 'arbitrary',
            'samples': [0.0] * 123 + [-0.2081559] * 80 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_80': {
            'type': 'arbitrary',
            'samples': [0.0] * 123 + [0.254468348] * 80 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_81': {
            'type': 'arbitrary',
            'samples': [0.0] * 122 + [-0.2081559] * 81 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_81': {
            'type': 'arbitrary',
            'samples': [0.0] * 122 + [0.254468348] * 81 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_82': {
            'type': 'arbitrary',
            'samples': [0.0] * 121 + [-0.2081559] * 82 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_82': {
            'type': 'arbitrary',
            'samples': [0.0] * 121 + [0.254468348] * 82 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_83': {
            'type': 'arbitrary',
            'samples': [0.0] * 120 + [-0.2081559] * 83 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_83': {
            'type': 'arbitrary',
            'samples': [0.0] * 120 + [0.254468348] * 83 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_84': {
            'type': 'arbitrary',
            'samples': [0.0] * 119 + [-0.2081559] * 84 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_84': {
            'type': 'arbitrary',
            'samples': [0.0] * 119 + [0.254468348] * 84 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_85': {
            'type': 'arbitrary',
            'samples': [0.0] * 118 + [-0.2081559] * 85 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_85': {
            'type': 'arbitrary',
            'samples': [0.0] * 118 + [0.254468348] * 85 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_86': {
            'type': 'arbitrary',
            'samples': [0.0] * 117 + [-0.2081559] * 86 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_86': {
            'type': 'arbitrary',
            'samples': [0.0] * 117 + [0.254468348] * 86 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_87': {
            'type': 'arbitrary',
            'samples': [0.0] * 116 + [-0.2081559] * 87 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_87': {
            'type': 'arbitrary',
            'samples': [0.0] * 116 + [0.254468348] * 87 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_88': {
            'type': 'arbitrary',
            'samples': [0.0] * 115 + [-0.2081559] * 88 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_88': {
            'type': 'arbitrary',
            'samples': [0.0] * 115 + [0.254468348] * 88 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_89': {
            'type': 'arbitrary',
            'samples': [0.0] * 114 + [-0.2081559] * 89 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_89': {
            'type': 'arbitrary',
            'samples': [0.0] * 114 + [0.254468348] * 89 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_90': {
            'type': 'arbitrary',
            'samples': [0.0] * 113 + [-0.2081559] * 90 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_90': {
            'type': 'arbitrary',
            'samples': [0.0] * 113 + [0.254468348] * 90 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_91': {
            'type': 'arbitrary',
            'samples': [0.0] * 112 + [-0.2081559] * 91 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_91': {
            'type': 'arbitrary',
            'samples': [0.0] * 112 + [0.254468348] * 91 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_92': {
            'type': 'arbitrary',
            'samples': [0.0] * 111 + [-0.2081559] * 92 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_92': {
            'type': 'arbitrary',
            'samples': [0.0] * 111 + [0.254468348] * 92 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_93': {
            'type': 'arbitrary',
            'samples': [0.0] * 110 + [-0.2081559] * 93 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_93': {
            'type': 'arbitrary',
            'samples': [0.0] * 110 + [0.254468348] * 93 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_94': {
            'type': 'arbitrary',
            'samples': [0.0] * 109 + [-0.2081559] * 94 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_94': {
            'type': 'arbitrary',
            'samples': [0.0] * 109 + [0.254468348] * 94 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_95': {
            'type': 'arbitrary',
            'samples': [0.0] * 108 + [-0.2081559] * 95 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_95': {
            'type': 'arbitrary',
            'samples': [0.0] * 108 + [0.254468348] * 95 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_96': {
            'type': 'arbitrary',
            'samples': [0.0] * 107 + [-0.2081559] * 96 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_96': {
            'type': 'arbitrary',
            'samples': [0.0] * 107 + [0.254468348] * 96 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_97': {
            'type': 'arbitrary',
            'samples': [0.0] * 106 + [-0.2081559] * 97 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_97': {
            'type': 'arbitrary',
            'samples': [0.0] * 106 + [0.254468348] * 97 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_98': {
            'type': 'arbitrary',
            'samples': [0.0] * 105 + [-0.2081559] * 98 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_98': {
            'type': 'arbitrary',
            'samples': [0.0] * 105 + [0.254468348] * 98 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_99': {
            'type': 'arbitrary',
            'samples': [0.0] * 104 + [-0.2081559] * 99 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_99': {
            'type': 'arbitrary',
            'samples': [0.0] * 104 + [0.254468348] * 99 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_100': {
            'type': 'arbitrary',
            'samples': [0.0] * 103 + [-0.2081559] * 100 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_100': {
            'type': 'arbitrary',
            'samples': [0.0] * 103 + [0.254468348] * 100 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_101': {
            'type': 'arbitrary',
            'samples': [0.0] * 102 + [-0.2081559] * 101 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_101': {
            'type': 'arbitrary',
            'samples': [0.0] * 102 + [0.254468348] * 101 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_102': {
            'type': 'arbitrary',
            'samples': [0.0] * 101 + [-0.2081559] * 102 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_102': {
            'type': 'arbitrary',
            'samples': [0.0] * 101 + [0.254468348] * 102 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_103': {
            'type': 'arbitrary',
            'samples': [0.0] * 100 + [-0.2081559] * 103 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_103': {
            'type': 'arbitrary',
            'samples': [0.0] * 100 + [0.254468348] * 103 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_104': {
            'type': 'arbitrary',
            'samples': [0.0] * 99 + [-0.2081559] * 104 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_104': {
            'type': 'arbitrary',
            'samples': [0.0] * 99 + [0.254468348] * 104 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_105': {
            'type': 'arbitrary',
            'samples': [0.0] * 98 + [-0.2081559] * 105 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_105': {
            'type': 'arbitrary',
            'samples': [0.0] * 98 + [0.254468348] * 105 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_106': {
            'type': 'arbitrary',
            'samples': [0.0] * 97 + [-0.2081559] * 106 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_106': {
            'type': 'arbitrary',
            'samples': [0.0] * 97 + [0.254468348] * 106 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_107': {
            'type': 'arbitrary',
            'samples': [0.0] * 96 + [-0.2081559] * 107 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_107': {
            'type': 'arbitrary',
            'samples': [0.0] * 96 + [0.254468348] * 107 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_108': {
            'type': 'arbitrary',
            'samples': [0.0] * 95 + [-0.2081559] * 108 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_108': {
            'type': 'arbitrary',
            'samples': [0.0] * 95 + [0.254468348] * 108 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_109': {
            'type': 'arbitrary',
            'samples': [0.0] * 94 + [-0.2081559] * 109 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_109': {
            'type': 'arbitrary',
            'samples': [0.0] * 94 + [0.254468348] * 109 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_110': {
            'type': 'arbitrary',
            'samples': [0.0] * 93 + [-0.2081559] * 110 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_110': {
            'type': 'arbitrary',
            'samples': [0.0] * 93 + [0.254468348] * 110 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_111': {
            'type': 'arbitrary',
            'samples': [0.0] * 92 + [-0.2081559] * 111 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_111': {
            'type': 'arbitrary',
            'samples': [0.0] * 92 + [0.254468348] * 111 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_112': {
            'type': 'arbitrary',
            'samples': [0.0] * 91 + [-0.2081559] * 112 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_112': {
            'type': 'arbitrary',
            'samples': [0.0] * 91 + [0.254468348] * 112 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_113': {
            'type': 'arbitrary',
            'samples': [0.0] * 90 + [-0.2081559] * 113 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_113': {
            'type': 'arbitrary',
            'samples': [0.0] * 90 + [0.254468348] * 113 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_114': {
            'type': 'arbitrary',
            'samples': [0.0] * 89 + [-0.2081559] * 114 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_114': {
            'type': 'arbitrary',
            'samples': [0.0] * 89 + [0.254468348] * 114 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_115': {
            'type': 'arbitrary',
            'samples': [0.0] * 88 + [-0.2081559] * 115 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_115': {
            'type': 'arbitrary',
            'samples': [0.0] * 88 + [0.254468348] * 115 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_116': {
            'type': 'arbitrary',
            'samples': [0.0] * 87 + [-0.2081559] * 116 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_116': {
            'type': 'arbitrary',
            'samples': [0.0] * 87 + [0.254468348] * 116 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_117': {
            'type': 'arbitrary',
            'samples': [0.0] * 86 + [-0.2081559] * 117 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_117': {
            'type': 'arbitrary',
            'samples': [0.0] * 86 + [0.254468348] * 117 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_118': {
            'type': 'arbitrary',
            'samples': [0.0] * 85 + [-0.2081559] * 118 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_118': {
            'type': 'arbitrary',
            'samples': [0.0] * 85 + [0.254468348] * 118 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_119': {
            'type': 'arbitrary',
            'samples': [0.0] * 84 + [-0.2081559] * 119 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_119': {
            'type': 'arbitrary',
            'samples': [0.0] * 84 + [0.254468348] * 119 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_120': {
            'type': 'arbitrary',
            'samples': [0.0] * 83 + [-0.2081559] * 120 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_120': {
            'type': 'arbitrary',
            'samples': [0.0] * 83 + [0.254468348] * 120 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_121': {
            'type': 'arbitrary',
            'samples': [0.0] * 82 + [-0.2081559] * 121 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_121': {
            'type': 'arbitrary',
            'samples': [0.0] * 82 + [0.254468348] * 121 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_122': {
            'type': 'arbitrary',
            'samples': [0.0] * 81 + [-0.2081559] * 122 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_122': {
            'type': 'arbitrary',
            'samples': [0.0] * 81 + [0.254468348] * 122 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_123': {
            'type': 'arbitrary',
            'samples': [0.0] * 80 + [-0.2081559] * 123 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_123': {
            'type': 'arbitrary',
            'samples': [0.0] * 80 + [0.254468348] * 123 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_124': {
            'type': 'arbitrary',
            'samples': [0.0] * 79 + [-0.2081559] * 124 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_124': {
            'type': 'arbitrary',
            'samples': [0.0] * 79 + [0.254468348] * 124 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_125': {
            'type': 'arbitrary',
            'samples': [0.0] * 78 + [-0.2081559] * 125 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_125': {
            'type': 'arbitrary',
            'samples': [0.0] * 78 + [0.254468348] * 125 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_126': {
            'type': 'arbitrary',
            'samples': [0.0] * 77 + [-0.2081559] * 126 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_126': {
            'type': 'arbitrary',
            'samples': [0.0] * 77 + [0.254468348] * 126 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_127': {
            'type': 'arbitrary',
            'samples': [0.0] * 76 + [-0.2081559] * 127 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_127': {
            'type': 'arbitrary',
            'samples': [0.0] * 76 + [0.254468348] * 127 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_128': {
            'type': 'arbitrary',
            'samples': [0.0] * 75 + [-0.2081559] * 128 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_128': {
            'type': 'arbitrary',
            'samples': [0.0] * 75 + [0.254468348] * 128 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_129': {
            'type': 'arbitrary',
            'samples': [0.0] * 74 + [-0.2081559] * 129 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_129': {
            'type': 'arbitrary',
            'samples': [0.0] * 74 + [0.254468348] * 129 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_130': {
            'type': 'arbitrary',
            'samples': [0.0] * 73 + [-0.2081559] * 130 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_130': {
            'type': 'arbitrary',
            'samples': [0.0] * 73 + [0.254468348] * 130 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_131': {
            'type': 'arbitrary',
            'samples': [0.0] * 72 + [-0.2081559] * 131 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_131': {
            'type': 'arbitrary',
            'samples': [0.0] * 72 + [0.254468348] * 131 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_132': {
            'type': 'arbitrary',
            'samples': [0.0] * 71 + [-0.2081559] * 132 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_132': {
            'type': 'arbitrary',
            'samples': [0.0] * 71 + [0.254468348] * 132 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_133': {
            'type': 'arbitrary',
            'samples': [0.0] * 70 + [-0.2081559] * 133 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_133': {
            'type': 'arbitrary',
            'samples': [0.0] * 70 + [0.254468348] * 133 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_134': {
            'type': 'arbitrary',
            'samples': [0.0] * 69 + [-0.2081559] * 134 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_134': {
            'type': 'arbitrary',
            'samples': [0.0] * 69 + [0.254468348] * 134 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_135': {
            'type': 'arbitrary',
            'samples': [0.0] * 68 + [-0.2081559] * 135 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_135': {
            'type': 'arbitrary',
            'samples': [0.0] * 68 + [0.254468348] * 135 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_136': {
            'type': 'arbitrary',
            'samples': [0.0] * 67 + [-0.2081559] * 136 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_136': {
            'type': 'arbitrary',
            'samples': [0.0] * 67 + [0.254468348] * 136 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_137': {
            'type': 'arbitrary',
            'samples': [0.0] * 66 + [-0.2081559] * 137 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_137': {
            'type': 'arbitrary',
            'samples': [0.0] * 66 + [0.254468348] * 137 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_138': {
            'type': 'arbitrary',
            'samples': [0.0] * 65 + [-0.2081559] * 138 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_138': {
            'type': 'arbitrary',
            'samples': [0.0] * 65 + [0.254468348] * 138 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_139': {
            'type': 'arbitrary',
            'samples': [0.0] * 64 + [-0.2081559] * 139 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_139': {
            'type': 'arbitrary',
            'samples': [0.0] * 64 + [0.254468348] * 139 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_140': {
            'type': 'arbitrary',
            'samples': [0.0] * 63 + [-0.2081559] * 140 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_140': {
            'type': 'arbitrary',
            'samples': [0.0] * 63 + [0.254468348] * 140 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_141': {
            'type': 'arbitrary',
            'samples': [0.0] * 62 + [-0.2081559] * 141 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_141': {
            'type': 'arbitrary',
            'samples': [0.0] * 62 + [0.254468348] * 141 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_142': {
            'type': 'arbitrary',
            'samples': [0.0] * 61 + [-0.2081559] * 142 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_142': {
            'type': 'arbitrary',
            'samples': [0.0] * 61 + [0.254468348] * 142 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_143': {
            'type': 'arbitrary',
            'samples': [0.0] * 60 + [-0.2081559] * 143 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_143': {
            'type': 'arbitrary',
            'samples': [0.0] * 60 + [0.254468348] * 143 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_144': {
            'type': 'arbitrary',
            'samples': [0.0] * 59 + [-0.2081559] * 144 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_144': {
            'type': 'arbitrary',
            'samples': [0.0] * 59 + [0.254468348] * 144 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_145': {
            'type': 'arbitrary',
            'samples': [0.0] * 58 + [-0.2081559] * 145 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_145': {
            'type': 'arbitrary',
            'samples': [0.0] * 58 + [0.254468348] * 145 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_146': {
            'type': 'arbitrary',
            'samples': [0.0] * 57 + [-0.2081559] * 146 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_146': {
            'type': 'arbitrary',
            'samples': [0.0] * 57 + [0.254468348] * 146 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_147': {
            'type': 'arbitrary',
            'samples': [0.0] * 56 + [-0.2081559] * 147 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_147': {
            'type': 'arbitrary',
            'samples': [0.0] * 56 + [0.254468348] * 147 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_148': {
            'type': 'arbitrary',
            'samples': [0.0] * 55 + [-0.2081559] * 148 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_148': {
            'type': 'arbitrary',
            'samples': [0.0] * 55 + [0.254468348] * 148 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_149': {
            'type': 'arbitrary',
            'samples': [0.0] * 54 + [-0.2081559] * 149 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_149': {
            'type': 'arbitrary',
            'samples': [0.0] * 54 + [0.254468348] * 149 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_150': {
            'type': 'arbitrary',
            'samples': [0.0] * 53 + [-0.2081559] * 150 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_150': {
            'type': 'arbitrary',
            'samples': [0.0] * 53 + [0.254468348] * 150 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_151': {
            'type': 'arbitrary',
            'samples': [0.0] * 52 + [-0.2081559] * 151 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_151': {
            'type': 'arbitrary',
            'samples': [0.0] * 52 + [0.254468348] * 151 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_152': {
            'type': 'arbitrary',
            'samples': [0.0] * 51 + [-0.2081559] * 152 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_152': {
            'type': 'arbitrary',
            'samples': [0.0] * 51 + [0.254468348] * 152 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_153': {
            'type': 'arbitrary',
            'samples': [0.0] * 50 + [-0.2081559] * 153 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_153': {
            'type': 'arbitrary',
            'samples': [0.0] * 50 + [0.254468348] * 153 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_154': {
            'type': 'arbitrary',
            'samples': [0.0] * 49 + [-0.2081559] * 154 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_154': {
            'type': 'arbitrary',
            'samples': [0.0] * 49 + [0.254468348] * 154 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_155': {
            'type': 'arbitrary',
            'samples': [0.0] * 48 + [-0.2081559] * 155 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_155': {
            'type': 'arbitrary',
            'samples': [0.0] * 48 + [0.254468348] * 155 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_156': {
            'type': 'arbitrary',
            'samples': [0.0] * 47 + [-0.2081559] * 156 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_156': {
            'type': 'arbitrary',
            'samples': [0.0] * 47 + [0.254468348] * 156 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_157': {
            'type': 'arbitrary',
            'samples': [0.0] * 46 + [-0.2081559] * 157 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_157': {
            'type': 'arbitrary',
            'samples': [0.0] * 46 + [0.254468348] * 157 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_158': {
            'type': 'arbitrary',
            'samples': [0.0] * 45 + [-0.2081559] * 158 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_158': {
            'type': 'arbitrary',
            'samples': [0.0] * 45 + [0.254468348] * 158 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_159': {
            'type': 'arbitrary',
            'samples': [0.0] * 44 + [-0.2081559] * 159 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_159': {
            'type': 'arbitrary',
            'samples': [0.0] * 44 + [0.254468348] * 159 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_160': {
            'type': 'arbitrary',
            'samples': [0.0] * 43 + [-0.2081559] * 160 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_160': {
            'type': 'arbitrary',
            'samples': [0.0] * 43 + [0.254468348] * 160 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_161': {
            'type': 'arbitrary',
            'samples': [0.0] * 42 + [-0.2081559] * 161 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_161': {
            'type': 'arbitrary',
            'samples': [0.0] * 42 + [0.254468348] * 161 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_162': {
            'type': 'arbitrary',
            'samples': [0.0] * 41 + [-0.2081559] * 162 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_162': {
            'type': 'arbitrary',
            'samples': [0.0] * 41 + [0.254468348] * 162 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_163': {
            'type': 'arbitrary',
            'samples': [0.0] * 40 + [-0.2081559] * 163 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_163': {
            'type': 'arbitrary',
            'samples': [0.0] * 40 + [0.254468348] * 163 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_164': {
            'type': 'arbitrary',
            'samples': [0.0] * 39 + [-0.2081559] * 164 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_164': {
            'type': 'arbitrary',
            'samples': [0.0] * 39 + [0.254468348] * 164 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_165': {
            'type': 'arbitrary',
            'samples': [0.0] * 38 + [-0.2081559] * 165 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_165': {
            'type': 'arbitrary',
            'samples': [0.0] * 38 + [0.254468348] * 165 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_166': {
            'type': 'arbitrary',
            'samples': [0.0] * 37 + [-0.2081559] * 166 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_166': {
            'type': 'arbitrary',
            'samples': [0.0] * 37 + [0.254468348] * 166 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_167': {
            'type': 'arbitrary',
            'samples': [0.0] * 36 + [-0.2081559] * 167 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_167': {
            'type': 'arbitrary',
            'samples': [0.0] * 36 + [0.254468348] * 167 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_168': {
            'type': 'arbitrary',
            'samples': [0.0] * 35 + [-0.2081559] * 168 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_168': {
            'type': 'arbitrary',
            'samples': [0.0] * 35 + [0.254468348] * 168 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_169': {
            'type': 'arbitrary',
            'samples': [0.0] * 34 + [-0.2081559] * 169 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_169': {
            'type': 'arbitrary',
            'samples': [0.0] * 34 + [0.254468348] * 169 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_170': {
            'type': 'arbitrary',
            'samples': [0.0] * 33 + [-0.2081559] * 170 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_170': {
            'type': 'arbitrary',
            'samples': [0.0] * 33 + [0.254468348] * 170 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_171': {
            'type': 'arbitrary',
            'samples': [0.0] * 32 + [-0.2081559] * 171 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_171': {
            'type': 'arbitrary',
            'samples': [0.0] * 32 + [0.254468348] * 171 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_172': {
            'type': 'arbitrary',
            'samples': [0.0] * 31 + [-0.2081559] * 172 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_172': {
            'type': 'arbitrary',
            'samples': [0.0] * 31 + [0.254468348] * 172 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_173': {
            'type': 'arbitrary',
            'samples': [0.0] * 30 + [-0.2081559] * 173 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_173': {
            'type': 'arbitrary',
            'samples': [0.0] * 30 + [0.254468348] * 173 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_174': {
            'type': 'arbitrary',
            'samples': [0.0] * 29 + [-0.2081559] * 174 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_174': {
            'type': 'arbitrary',
            'samples': [0.0] * 29 + [0.254468348] * 174 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_175': {
            'type': 'arbitrary',
            'samples': [0.0] * 28 + [-0.2081559] * 175 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_175': {
            'type': 'arbitrary',
            'samples': [0.0] * 28 + [0.254468348] * 175 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_176': {
            'type': 'arbitrary',
            'samples': [0.0] * 27 + [-0.2081559] * 176 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_176': {
            'type': 'arbitrary',
            'samples': [0.0] * 27 + [0.254468348] * 176 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_177': {
            'type': 'arbitrary',
            'samples': [0.0] * 26 + [-0.2081559] * 177 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_177': {
            'type': 'arbitrary',
            'samples': [0.0] * 26 + [0.254468348] * 177 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_178': {
            'type': 'arbitrary',
            'samples': [0.0] * 25 + [-0.2081559] * 178 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_178': {
            'type': 'arbitrary',
            'samples': [0.0] * 25 + [0.254468348] * 178 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_179': {
            'type': 'arbitrary',
            'samples': [0.0] * 24 + [-0.2081559] * 179 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_179': {
            'type': 'arbitrary',
            'samples': [0.0] * 24 + [0.254468348] * 179 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_180': {
            'type': 'arbitrary',
            'samples': [0.0] * 23 + [-0.2081559] * 180 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_180': {
            'type': 'arbitrary',
            'samples': [0.0] * 23 + [0.254468348] * 180 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_181': {
            'type': 'arbitrary',
            'samples': [0.0] * 22 + [-0.2081559] * 181 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_181': {
            'type': 'arbitrary',
            'samples': [0.0] * 22 + [0.254468348] * 181 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_182': {
            'type': 'arbitrary',
            'samples': [0.0] * 21 + [-0.2081559] * 182 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_182': {
            'type': 'arbitrary',
            'samples': [0.0] * 21 + [0.254468348] * 182 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_183': {
            'type': 'arbitrary',
            'samples': [0.0] * 20 + [-0.2081559] * 183 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_183': {
            'type': 'arbitrary',
            'samples': [0.0] * 20 + [0.254468348] * 183 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_184': {
            'type': 'arbitrary',
            'samples': [0.0] * 19 + [-0.2081559] * 184 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_184': {
            'type': 'arbitrary',
            'samples': [0.0] * 19 + [0.254468348] * 184 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_185': {
            'type': 'arbitrary',
            'samples': [0.0] * 18 + [-0.2081559] * 185 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_185': {
            'type': 'arbitrary',
            'samples': [0.0] * 18 + [0.254468348] * 185 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_186': {
            'type': 'arbitrary',
            'samples': [0.0] * 17 + [-0.2081559] * 186 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_186': {
            'type': 'arbitrary',
            'samples': [0.0] * 17 + [0.254468348] * 186 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_187': {
            'type': 'arbitrary',
            'samples': [0.0] * 16 + [-0.2081559] * 187 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_187': {
            'type': 'arbitrary',
            'samples': [0.0] * 16 + [0.254468348] * 187 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_188': {
            'type': 'arbitrary',
            'samples': [0.0] * 15 + [-0.2081559] * 188 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_188': {
            'type': 'arbitrary',
            'samples': [0.0] * 15 + [0.254468348] * 188 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_189': {
            'type': 'arbitrary',
            'samples': [0.0] * 14 + [-0.2081559] * 189 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_189': {
            'type': 'arbitrary',
            'samples': [0.0] * 14 + [0.254468348] * 189 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_190': {
            'type': 'arbitrary',
            'samples': [0.0] * 13 + [-0.2081559] * 190 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_190': {
            'type': 'arbitrary',
            'samples': [0.0] * 13 + [0.254468348] * 190 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_191': {
            'type': 'arbitrary',
            'samples': [0.0] * 12 + [-0.2081559] * 191 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_191': {
            'type': 'arbitrary',
            'samples': [0.0] * 12 + [0.254468348] * 191 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_192': {
            'type': 'arbitrary',
            'samples': [0.0] * 11 + [-0.2081559] * 192 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_192': {
            'type': 'arbitrary',
            'samples': [0.0] * 11 + [0.254468348] * 192 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_193': {
            'type': 'arbitrary',
            'samples': [0.0] * 10 + [-0.2081559] * 193 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_193': {
            'type': 'arbitrary',
            'samples': [0.0] * 10 + [0.254468348] * 193 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_194': {
            'type': 'arbitrary',
            'samples': [0.0] * 9 + [-0.2081559] * 194 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_194': {
            'type': 'arbitrary',
            'samples': [0.0] * 9 + [0.254468348] * 194 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_195': {
            'type': 'arbitrary',
            'samples': [0.0] * 8 + [-0.2081559] * 195 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_195': {
            'type': 'arbitrary',
            'samples': [0.0] * 8 + [0.254468348] * 195 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_196': {
            'type': 'arbitrary',
            'samples': [0.0] * 7 + [-0.2081559] * 196 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_196': {
            'type': 'arbitrary',
            'samples': [0.0] * 7 + [0.254468348] * 196 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_197': {
            'type': 'arbitrary',
            'samples': [0.0] * 6 + [-0.2081559] * 197 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_197': {
            'type': 'arbitrary',
            'samples': [0.0] * 6 + [0.254468348] * 197 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_198': {
            'type': 'arbitrary',
            'samples': [0.0] * 5 + [-0.2081559] * 198 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_198': {
            'type': 'arbitrary',
            'samples': [0.0] * 5 + [0.254468348] * 198 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_199': {
            'type': 'arbitrary',
            'samples': [0.0] * 4 + [-0.2081559] * 199 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_199': {
            'type': 'arbitrary',
            'samples': [0.0] * 4 + [0.254468348] * 199 + [0.0],
            'is_overridable': False,
        },
        'gate_29_baked_wf_200': {
            'type': 'arbitrary',
            'samples': [0.0] * 3 + [-0.2081559] * 200 + [0.0],
            'is_overridable': False,
        },
        'gate_36_baked_wf_200': {
            'type': 'arbitrary',
            'samples': [0.0] * 3 + [0.254468348] * 200 + [0.0],
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
            'samples': [0.0] * 202 + [-0.2081559, 0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_1': {
            'samples': [0.0] * 202 + [0.254468348, 0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_2': {
            'samples': [0.0] * 201 + [-0.2081559] * 2 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_2': {
            'samples': [0.0] * 201 + [0.254468348] * 2 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_3': {
            'samples': [0.0] * 200 + [-0.2081559] * 3 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_3': {
            'samples': [0.0] * 200 + [0.254468348] * 3 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_4': {
            'samples': [0.0] * 199 + [-0.2081559] * 4 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_4': {
            'samples': [0.0] * 199 + [0.254468348] * 4 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_5': {
            'samples': [0.0] * 198 + [-0.2081559] * 5 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_5': {
            'samples': [0.0] * 198 + [0.254468348] * 5 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_6': {
            'samples': [0.0] * 197 + [-0.2081559] * 6 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_6': {
            'samples': [0.0] * 197 + [0.254468348] * 6 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_7': {
            'samples': [0.0] * 196 + [-0.2081559] * 7 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_7': {
            'samples': [0.0] * 196 + [0.254468348] * 7 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_8': {
            'samples': [0.0] * 195 + [-0.2081559] * 8 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_8': {
            'samples': [0.0] * 195 + [0.254468348] * 8 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_9': {
            'samples': [0.0] * 194 + [-0.2081559] * 9 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_9': {
            'samples': [0.0] * 194 + [0.254468348] * 9 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_10': {
            'samples': [0.0] * 193 + [-0.2081559] * 10 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_10': {
            'samples': [0.0] * 193 + [0.254468348] * 10 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_11': {
            'samples': [0.0] * 192 + [-0.2081559] * 11 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_11': {
            'samples': [0.0] * 192 + [0.254468348] * 11 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_12': {
            'samples': [0.0] * 191 + [-0.2081559] * 12 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_12': {
            'samples': [0.0] * 191 + [0.254468348] * 12 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_13': {
            'samples': [0.0] * 190 + [-0.2081559] * 13 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_13': {
            'samples': [0.0] * 190 + [0.254468348] * 13 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_14': {
            'samples': [0.0] * 189 + [-0.2081559] * 14 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_14': {
            'samples': [0.0] * 189 + [0.254468348] * 14 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_15': {
            'samples': [0.0] * 188 + [-0.2081559] * 15 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_15': {
            'samples': [0.0] * 188 + [0.254468348] * 15 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_16': {
            'samples': [0.0] * 187 + [-0.2081559] * 16 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_16': {
            'samples': [0.0] * 187 + [0.254468348] * 16 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_17': {
            'samples': [0.0] * 186 + [-0.2081559] * 17 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_17': {
            'samples': [0.0] * 186 + [0.254468348] * 17 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_18': {
            'samples': [0.0] * 185 + [-0.2081559] * 18 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_18': {
            'samples': [0.0] * 185 + [0.254468348] * 18 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_19': {
            'samples': [0.0] * 184 + [-0.2081559] * 19 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_19': {
            'samples': [0.0] * 184 + [0.254468348] * 19 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_20': {
            'samples': [0.0] * 183 + [-0.2081559] * 20 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_20': {
            'samples': [0.0] * 183 + [0.254468348] * 20 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_21': {
            'samples': [0.0] * 182 + [-0.2081559] * 21 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_21': {
            'samples': [0.0] * 182 + [0.254468348] * 21 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_22': {
            'samples': [0.0] * 181 + [-0.2081559] * 22 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_22': {
            'samples': [0.0] * 181 + [0.254468348] * 22 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_23': {
            'samples': [0.0] * 180 + [-0.2081559] * 23 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_23': {
            'samples': [0.0] * 180 + [0.254468348] * 23 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_24': {
            'samples': [0.0] * 179 + [-0.2081559] * 24 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_24': {
            'samples': [0.0] * 179 + [0.254468348] * 24 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_25': {
            'samples': [0.0] * 178 + [-0.2081559] * 25 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_25': {
            'samples': [0.0] * 178 + [0.254468348] * 25 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_26': {
            'samples': [0.0] * 177 + [-0.2081559] * 26 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_26': {
            'samples': [0.0] * 177 + [0.254468348] * 26 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_27': {
            'samples': [0.0] * 176 + [-0.2081559] * 27 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_27': {
            'samples': [0.0] * 176 + [0.254468348] * 27 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_28': {
            'samples': [0.0] * 175 + [-0.2081559] * 28 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_28': {
            'samples': [0.0] * 175 + [0.254468348] * 28 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_29': {
            'samples': [0.0] * 174 + [-0.2081559] * 29 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_29': {
            'samples': [0.0] * 174 + [0.254468348] * 29 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_30': {
            'samples': [0.0] * 173 + [-0.2081559] * 30 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_30': {
            'samples': [0.0] * 173 + [0.254468348] * 30 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_31': {
            'samples': [0.0] * 172 + [-0.2081559] * 31 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_31': {
            'samples': [0.0] * 172 + [0.254468348] * 31 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_32': {
            'samples': [0.0] * 171 + [-0.2081559] * 32 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_32': {
            'samples': [0.0] * 171 + [0.254468348] * 32 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_33': {
            'samples': [0.0] * 170 + [-0.2081559] * 33 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_33': {
            'samples': [0.0] * 170 + [0.254468348] * 33 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_34': {
            'samples': [0.0] * 169 + [-0.2081559] * 34 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_34': {
            'samples': [0.0] * 169 + [0.254468348] * 34 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_35': {
            'samples': [0.0] * 168 + [-0.2081559] * 35 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_35': {
            'samples': [0.0] * 168 + [0.254468348] * 35 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_36': {
            'samples': [0.0] * 167 + [-0.2081559] * 36 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_36': {
            'samples': [0.0] * 167 + [0.254468348] * 36 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_37': {
            'samples': [0.0] * 166 + [-0.2081559] * 37 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_37': {
            'samples': [0.0] * 166 + [0.254468348] * 37 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_38': {
            'samples': [0.0] * 165 + [-0.2081559] * 38 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_38': {
            'samples': [0.0] * 165 + [0.254468348] * 38 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_39': {
            'samples': [0.0] * 164 + [-0.2081559] * 39 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_39': {
            'samples': [0.0] * 164 + [0.254468348] * 39 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_40': {
            'samples': [0.0] * 163 + [-0.2081559] * 40 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_40': {
            'samples': [0.0] * 163 + [0.254468348] * 40 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_41': {
            'samples': [0.0] * 162 + [-0.2081559] * 41 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_41': {
            'samples': [0.0] * 162 + [0.254468348] * 41 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_42': {
            'samples': [0.0] * 161 + [-0.2081559] * 42 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_42': {
            'samples': [0.0] * 161 + [0.254468348] * 42 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_43': {
            'samples': [0.0] * 160 + [-0.2081559] * 43 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_43': {
            'samples': [0.0] * 160 + [0.254468348] * 43 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_44': {
            'samples': [0.0] * 159 + [-0.2081559] * 44 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_44': {
            'samples': [0.0] * 159 + [0.254468348] * 44 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_45': {
            'samples': [0.0] * 158 + [-0.2081559] * 45 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_45': {
            'samples': [0.0] * 158 + [0.254468348] * 45 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_46': {
            'samples': [0.0] * 157 + [-0.2081559] * 46 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_46': {
            'samples': [0.0] * 157 + [0.254468348] * 46 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_47': {
            'samples': [0.0] * 156 + [-0.2081559] * 47 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_47': {
            'samples': [0.0] * 156 + [0.254468348] * 47 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_48': {
            'samples': [0.0] * 155 + [-0.2081559] * 48 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_48': {
            'samples': [0.0] * 155 + [0.254468348] * 48 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_49': {
            'samples': [0.0] * 154 + [-0.2081559] * 49 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_49': {
            'samples': [0.0] * 154 + [0.254468348] * 49 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_50': {
            'samples': [0.0] * 153 + [-0.2081559] * 50 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_50': {
            'samples': [0.0] * 153 + [0.254468348] * 50 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_51': {
            'samples': [0.0] * 152 + [-0.2081559] * 51 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_51': {
            'samples': [0.0] * 152 + [0.254468348] * 51 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_52': {
            'samples': [0.0] * 151 + [-0.2081559] * 52 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_52': {
            'samples': [0.0] * 151 + [0.254468348] * 52 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_53': {
            'samples': [0.0] * 150 + [-0.2081559] * 53 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_53': {
            'samples': [0.0] * 150 + [0.254468348] * 53 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_54': {
            'samples': [0.0] * 149 + [-0.2081559] * 54 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_54': {
            'samples': [0.0] * 149 + [0.254468348] * 54 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_55': {
            'samples': [0.0] * 148 + [-0.2081559] * 55 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_55': {
            'samples': [0.0] * 148 + [0.254468348] * 55 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_56': {
            'samples': [0.0] * 147 + [-0.2081559] * 56 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_56': {
            'samples': [0.0] * 147 + [0.254468348] * 56 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_57': {
            'samples': [0.0] * 146 + [-0.2081559] * 57 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_57': {
            'samples': [0.0] * 146 + [0.254468348] * 57 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_58': {
            'samples': [0.0] * 145 + [-0.2081559] * 58 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_58': {
            'samples': [0.0] * 145 + [0.254468348] * 58 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_59': {
            'samples': [0.0] * 144 + [-0.2081559] * 59 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_59': {
            'samples': [0.0] * 144 + [0.254468348] * 59 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_60': {
            'samples': [0.0] * 143 + [-0.2081559] * 60 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_60': {
            'samples': [0.0] * 143 + [0.254468348] * 60 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_61': {
            'samples': [0.0] * 142 + [-0.2081559] * 61 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_61': {
            'samples': [0.0] * 142 + [0.254468348] * 61 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_62': {
            'samples': [0.0] * 141 + [-0.2081559] * 62 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_62': {
            'samples': [0.0] * 141 + [0.254468348] * 62 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_63': {
            'samples': [0.0] * 140 + [-0.2081559] * 63 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_63': {
            'samples': [0.0] * 140 + [0.254468348] * 63 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_64': {
            'samples': [0.0] * 139 + [-0.2081559] * 64 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_64': {
            'samples': [0.0] * 139 + [0.254468348] * 64 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_65': {
            'samples': [0.0] * 138 + [-0.2081559] * 65 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_65': {
            'samples': [0.0] * 138 + [0.254468348] * 65 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_66': {
            'samples': [0.0] * 137 + [-0.2081559] * 66 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_66': {
            'samples': [0.0] * 137 + [0.254468348] * 66 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_67': {
            'samples': [0.0] * 136 + [-0.2081559] * 67 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_67': {
            'samples': [0.0] * 136 + [0.254468348] * 67 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_68': {
            'samples': [0.0] * 135 + [-0.2081559] * 68 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_68': {
            'samples': [0.0] * 135 + [0.254468348] * 68 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_69': {
            'samples': [0.0] * 134 + [-0.2081559] * 69 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_69': {
            'samples': [0.0] * 134 + [0.254468348] * 69 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_70': {
            'samples': [0.0] * 133 + [-0.2081559] * 70 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_70': {
            'samples': [0.0] * 133 + [0.254468348] * 70 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_71': {
            'samples': [0.0] * 132 + [-0.2081559] * 71 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_71': {
            'samples': [0.0] * 132 + [0.254468348] * 71 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_72': {
            'samples': [0.0] * 131 + [-0.2081559] * 72 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_72': {
            'samples': [0.0] * 131 + [0.254468348] * 72 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_73': {
            'samples': [0.0] * 130 + [-0.2081559] * 73 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_73': {
            'samples': [0.0] * 130 + [0.254468348] * 73 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_74': {
            'samples': [0.0] * 129 + [-0.2081559] * 74 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_74': {
            'samples': [0.0] * 129 + [0.254468348] * 74 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_75': {
            'samples': [0.0] * 128 + [-0.2081559] * 75 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_75': {
            'samples': [0.0] * 128 + [0.254468348] * 75 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_76': {
            'samples': [0.0] * 127 + [-0.2081559] * 76 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_76': {
            'samples': [0.0] * 127 + [0.254468348] * 76 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_77': {
            'samples': [0.0] * 126 + [-0.2081559] * 77 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_77': {
            'samples': [0.0] * 126 + [0.254468348] * 77 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_78': {
            'samples': [0.0] * 125 + [-0.2081559] * 78 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_78': {
            'samples': [0.0] * 125 + [0.254468348] * 78 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_79': {
            'samples': [0.0] * 124 + [-0.2081559] * 79 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_79': {
            'samples': [0.0] * 124 + [0.254468348] * 79 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_80': {
            'samples': [0.0] * 123 + [-0.2081559] * 80 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_80': {
            'samples': [0.0] * 123 + [0.254468348] * 80 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_81': {
            'samples': [0.0] * 122 + [-0.2081559] * 81 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_81': {
            'samples': [0.0] * 122 + [0.254468348] * 81 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_82': {
            'samples': [0.0] * 121 + [-0.2081559] * 82 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_82': {
            'samples': [0.0] * 121 + [0.254468348] * 82 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_83': {
            'samples': [0.0] * 120 + [-0.2081559] * 83 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_83': {
            'samples': [0.0] * 120 + [0.254468348] * 83 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_84': {
            'samples': [0.0] * 119 + [-0.2081559] * 84 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_84': {
            'samples': [0.0] * 119 + [0.254468348] * 84 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_85': {
            'samples': [0.0] * 118 + [-0.2081559] * 85 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_85': {
            'samples': [0.0] * 118 + [0.254468348] * 85 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_86': {
            'samples': [0.0] * 117 + [-0.2081559] * 86 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_86': {
            'samples': [0.0] * 117 + [0.254468348] * 86 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_87': {
            'samples': [0.0] * 116 + [-0.2081559] * 87 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_87': {
            'samples': [0.0] * 116 + [0.254468348] * 87 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_88': {
            'samples': [0.0] * 115 + [-0.2081559] * 88 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_88': {
            'samples': [0.0] * 115 + [0.254468348] * 88 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_89': {
            'samples': [0.0] * 114 + [-0.2081559] * 89 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_89': {
            'samples': [0.0] * 114 + [0.254468348] * 89 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_90': {
            'samples': [0.0] * 113 + [-0.2081559] * 90 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_90': {
            'samples': [0.0] * 113 + [0.254468348] * 90 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_91': {
            'samples': [0.0] * 112 + [-0.2081559] * 91 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_91': {
            'samples': [0.0] * 112 + [0.254468348] * 91 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_92': {
            'samples': [0.0] * 111 + [-0.2081559] * 92 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_92': {
            'samples': [0.0] * 111 + [0.254468348] * 92 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_93': {
            'samples': [0.0] * 110 + [-0.2081559] * 93 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_93': {
            'samples': [0.0] * 110 + [0.254468348] * 93 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_94': {
            'samples': [0.0] * 109 + [-0.2081559] * 94 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_94': {
            'samples': [0.0] * 109 + [0.254468348] * 94 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_95': {
            'samples': [0.0] * 108 + [-0.2081559] * 95 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_95': {
            'samples': [0.0] * 108 + [0.254468348] * 95 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_96': {
            'samples': [0.0] * 107 + [-0.2081559] * 96 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_96': {
            'samples': [0.0] * 107 + [0.254468348] * 96 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_97': {
            'samples': [0.0] * 106 + [-0.2081559] * 97 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_97': {
            'samples': [0.0] * 106 + [0.254468348] * 97 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_98': {
            'samples': [0.0] * 105 + [-0.2081559] * 98 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_98': {
            'samples': [0.0] * 105 + [0.254468348] * 98 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_99': {
            'samples': [0.0] * 104 + [-0.2081559] * 99 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_99': {
            'samples': [0.0] * 104 + [0.254468348] * 99 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_100': {
            'samples': [0.0] * 103 + [-0.2081559] * 100 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_100': {
            'samples': [0.0] * 103 + [0.254468348] * 100 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_101': {
            'samples': [0.0] * 102 + [-0.2081559] * 101 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_101': {
            'samples': [0.0] * 102 + [0.254468348] * 101 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_102': {
            'samples': [0.0] * 101 + [-0.2081559] * 102 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_102': {
            'samples': [0.0] * 101 + [0.254468348] * 102 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_103': {
            'samples': [0.0] * 100 + [-0.2081559] * 103 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_103': {
            'samples': [0.0] * 100 + [0.254468348] * 103 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_104': {
            'samples': [0.0] * 99 + [-0.2081559] * 104 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_104': {
            'samples': [0.0] * 99 + [0.254468348] * 104 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_105': {
            'samples': [0.0] * 98 + [-0.2081559] * 105 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_105': {
            'samples': [0.0] * 98 + [0.254468348] * 105 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_106': {
            'samples': [0.0] * 97 + [-0.2081559] * 106 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_106': {
            'samples': [0.0] * 97 + [0.254468348] * 106 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_107': {
            'samples': [0.0] * 96 + [-0.2081559] * 107 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_107': {
            'samples': [0.0] * 96 + [0.254468348] * 107 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_108': {
            'samples': [0.0] * 95 + [-0.2081559] * 108 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_108': {
            'samples': [0.0] * 95 + [0.254468348] * 108 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_109': {
            'samples': [0.0] * 94 + [-0.2081559] * 109 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_109': {
            'samples': [0.0] * 94 + [0.254468348] * 109 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_110': {
            'samples': [0.0] * 93 + [-0.2081559] * 110 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_110': {
            'samples': [0.0] * 93 + [0.254468348] * 110 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_111': {
            'samples': [0.0] * 92 + [-0.2081559] * 111 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_111': {
            'samples': [0.0] * 92 + [0.254468348] * 111 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_112': {
            'samples': [0.0] * 91 + [-0.2081559] * 112 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_112': {
            'samples': [0.0] * 91 + [0.254468348] * 112 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_113': {
            'samples': [0.0] * 90 + [-0.2081559] * 113 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_113': {
            'samples': [0.0] * 90 + [0.254468348] * 113 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_114': {
            'samples': [0.0] * 89 + [-0.2081559] * 114 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_114': {
            'samples': [0.0] * 89 + [0.254468348] * 114 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_115': {
            'samples': [0.0] * 88 + [-0.2081559] * 115 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_115': {
            'samples': [0.0] * 88 + [0.254468348] * 115 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_116': {
            'samples': [0.0] * 87 + [-0.2081559] * 116 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_116': {
            'samples': [0.0] * 87 + [0.254468348] * 116 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_117': {
            'samples': [0.0] * 86 + [-0.2081559] * 117 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_117': {
            'samples': [0.0] * 86 + [0.254468348] * 117 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_118': {
            'samples': [0.0] * 85 + [-0.2081559] * 118 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_118': {
            'samples': [0.0] * 85 + [0.254468348] * 118 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_119': {
            'samples': [0.0] * 84 + [-0.2081559] * 119 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_119': {
            'samples': [0.0] * 84 + [0.254468348] * 119 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_120': {
            'samples': [0.0] * 83 + [-0.2081559] * 120 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_120': {
            'samples': [0.0] * 83 + [0.254468348] * 120 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_121': {
            'samples': [0.0] * 82 + [-0.2081559] * 121 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_121': {
            'samples': [0.0] * 82 + [0.254468348] * 121 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_122': {
            'samples': [0.0] * 81 + [-0.2081559] * 122 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_122': {
            'samples': [0.0] * 81 + [0.254468348] * 122 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_123': {
            'samples': [0.0] * 80 + [-0.2081559] * 123 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_123': {
            'samples': [0.0] * 80 + [0.254468348] * 123 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_124': {
            'samples': [0.0] * 79 + [-0.2081559] * 124 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_124': {
            'samples': [0.0] * 79 + [0.254468348] * 124 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_125': {
            'samples': [0.0] * 78 + [-0.2081559] * 125 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_125': {
            'samples': [0.0] * 78 + [0.254468348] * 125 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_126': {
            'samples': [0.0] * 77 + [-0.2081559] * 126 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_126': {
            'samples': [0.0] * 77 + [0.254468348] * 126 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_127': {
            'samples': [0.0] * 76 + [-0.2081559] * 127 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_127': {
            'samples': [0.0] * 76 + [0.254468348] * 127 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_128': {
            'samples': [0.0] * 75 + [-0.2081559] * 128 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_128': {
            'samples': [0.0] * 75 + [0.254468348] * 128 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_129': {
            'samples': [0.0] * 74 + [-0.2081559] * 129 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_129': {
            'samples': [0.0] * 74 + [0.254468348] * 129 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_130': {
            'samples': [0.0] * 73 + [-0.2081559] * 130 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_130': {
            'samples': [0.0] * 73 + [0.254468348] * 130 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_131': {
            'samples': [0.0] * 72 + [-0.2081559] * 131 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_131': {
            'samples': [0.0] * 72 + [0.254468348] * 131 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_132': {
            'samples': [0.0] * 71 + [-0.2081559] * 132 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_132': {
            'samples': [0.0] * 71 + [0.254468348] * 132 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_133': {
            'samples': [0.0] * 70 + [-0.2081559] * 133 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_133': {
            'samples': [0.0] * 70 + [0.254468348] * 133 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_134': {
            'samples': [0.0] * 69 + [-0.2081559] * 134 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_134': {
            'samples': [0.0] * 69 + [0.254468348] * 134 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_135': {
            'samples': [0.0] * 68 + [-0.2081559] * 135 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_135': {
            'samples': [0.0] * 68 + [0.254468348] * 135 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_136': {
            'samples': [0.0] * 67 + [-0.2081559] * 136 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_136': {
            'samples': [0.0] * 67 + [0.254468348] * 136 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_137': {
            'samples': [0.0] * 66 + [-0.2081559] * 137 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_137': {
            'samples': [0.0] * 66 + [0.254468348] * 137 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_138': {
            'samples': [0.0] * 65 + [-0.2081559] * 138 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_138': {
            'samples': [0.0] * 65 + [0.254468348] * 138 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_139': {
            'samples': [0.0] * 64 + [-0.2081559] * 139 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_139': {
            'samples': [0.0] * 64 + [0.254468348] * 139 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_140': {
            'samples': [0.0] * 63 + [-0.2081559] * 140 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_140': {
            'samples': [0.0] * 63 + [0.254468348] * 140 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_141': {
            'samples': [0.0] * 62 + [-0.2081559] * 141 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_141': {
            'samples': [0.0] * 62 + [0.254468348] * 141 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_142': {
            'samples': [0.0] * 61 + [-0.2081559] * 142 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_142': {
            'samples': [0.0] * 61 + [0.254468348] * 142 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_143': {
            'samples': [0.0] * 60 + [-0.2081559] * 143 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_143': {
            'samples': [0.0] * 60 + [0.254468348] * 143 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_144': {
            'samples': [0.0] * 59 + [-0.2081559] * 144 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_144': {
            'samples': [0.0] * 59 + [0.254468348] * 144 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_145': {
            'samples': [0.0] * 58 + [-0.2081559] * 145 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_145': {
            'samples': [0.0] * 58 + [0.254468348] * 145 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_146': {
            'samples': [0.0] * 57 + [-0.2081559] * 146 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_146': {
            'samples': [0.0] * 57 + [0.254468348] * 146 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_147': {
            'samples': [0.0] * 56 + [-0.2081559] * 147 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_147': {
            'samples': [0.0] * 56 + [0.254468348] * 147 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_148': {
            'samples': [0.0] * 55 + [-0.2081559] * 148 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_148': {
            'samples': [0.0] * 55 + [0.254468348] * 148 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_149': {
            'samples': [0.0] * 54 + [-0.2081559] * 149 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_149': {
            'samples': [0.0] * 54 + [0.254468348] * 149 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_150': {
            'samples': [0.0] * 53 + [-0.2081559] * 150 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_150': {
            'samples': [0.0] * 53 + [0.254468348] * 150 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_151': {
            'samples': [0.0] * 52 + [-0.2081559] * 151 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_151': {
            'samples': [0.0] * 52 + [0.254468348] * 151 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_152': {
            'samples': [0.0] * 51 + [-0.2081559] * 152 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_152': {
            'samples': [0.0] * 51 + [0.254468348] * 152 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_153': {
            'samples': [0.0] * 50 + [-0.2081559] * 153 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_153': {
            'samples': [0.0] * 50 + [0.254468348] * 153 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_154': {
            'samples': [0.0] * 49 + [-0.2081559] * 154 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_154': {
            'samples': [0.0] * 49 + [0.254468348] * 154 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_155': {
            'samples': [0.0] * 48 + [-0.2081559] * 155 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_155': {
            'samples': [0.0] * 48 + [0.254468348] * 155 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_156': {
            'samples': [0.0] * 47 + [-0.2081559] * 156 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_156': {
            'samples': [0.0] * 47 + [0.254468348] * 156 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_157': {
            'samples': [0.0] * 46 + [-0.2081559] * 157 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_157': {
            'samples': [0.0] * 46 + [0.254468348] * 157 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_158': {
            'samples': [0.0] * 45 + [-0.2081559] * 158 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_158': {
            'samples': [0.0] * 45 + [0.254468348] * 158 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_159': {
            'samples': [0.0] * 44 + [-0.2081559] * 159 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_159': {
            'samples': [0.0] * 44 + [0.254468348] * 159 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_160': {
            'samples': [0.0] * 43 + [-0.2081559] * 160 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_160': {
            'samples': [0.0] * 43 + [0.254468348] * 160 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_161': {
            'samples': [0.0] * 42 + [-0.2081559] * 161 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_161': {
            'samples': [0.0] * 42 + [0.254468348] * 161 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_162': {
            'samples': [0.0] * 41 + [-0.2081559] * 162 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_162': {
            'samples': [0.0] * 41 + [0.254468348] * 162 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_163': {
            'samples': [0.0] * 40 + [-0.2081559] * 163 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_163': {
            'samples': [0.0] * 40 + [0.254468348] * 163 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_164': {
            'samples': [0.0] * 39 + [-0.2081559] * 164 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_164': {
            'samples': [0.0] * 39 + [0.254468348] * 164 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_165': {
            'samples': [0.0] * 38 + [-0.2081559] * 165 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_165': {
            'samples': [0.0] * 38 + [0.254468348] * 165 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_166': {
            'samples': [0.0] * 37 + [-0.2081559] * 166 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_166': {
            'samples': [0.0] * 37 + [0.254468348] * 166 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_167': {
            'samples': [0.0] * 36 + [-0.2081559] * 167 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_167': {
            'samples': [0.0] * 36 + [0.254468348] * 167 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_168': {
            'samples': [0.0] * 35 + [-0.2081559] * 168 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_168': {
            'samples': [0.0] * 35 + [0.254468348] * 168 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_169': {
            'samples': [0.0] * 34 + [-0.2081559] * 169 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_169': {
            'samples': [0.0] * 34 + [0.254468348] * 169 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_170': {
            'samples': [0.0] * 33 + [-0.2081559] * 170 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_170': {
            'samples': [0.0] * 33 + [0.254468348] * 170 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_171': {
            'samples': [0.0] * 32 + [-0.2081559] * 171 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_171': {
            'samples': [0.0] * 32 + [0.254468348] * 171 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_172': {
            'samples': [0.0] * 31 + [-0.2081559] * 172 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_172': {
            'samples': [0.0] * 31 + [0.254468348] * 172 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_173': {
            'samples': [0.0] * 30 + [-0.2081559] * 173 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_173': {
            'samples': [0.0] * 30 + [0.254468348] * 173 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_174': {
            'samples': [0.0] * 29 + [-0.2081559] * 174 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_174': {
            'samples': [0.0] * 29 + [0.254468348] * 174 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_175': {
            'samples': [0.0] * 28 + [-0.2081559] * 175 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_175': {
            'samples': [0.0] * 28 + [0.254468348] * 175 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_176': {
            'samples': [0.0] * 27 + [-0.2081559] * 176 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_176': {
            'samples': [0.0] * 27 + [0.254468348] * 176 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_177': {
            'samples': [0.0] * 26 + [-0.2081559] * 177 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_177': {
            'samples': [0.0] * 26 + [0.254468348] * 177 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_178': {
            'samples': [0.0] * 25 + [-0.2081559] * 178 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_178': {
            'samples': [0.0] * 25 + [0.254468348] * 178 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_179': {
            'samples': [0.0] * 24 + [-0.2081559] * 179 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_179': {
            'samples': [0.0] * 24 + [0.254468348] * 179 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_180': {
            'samples': [0.0] * 23 + [-0.2081559] * 180 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_180': {
            'samples': [0.0] * 23 + [0.254468348] * 180 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_181': {
            'samples': [0.0] * 22 + [-0.2081559] * 181 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_181': {
            'samples': [0.0] * 22 + [0.254468348] * 181 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_182': {
            'samples': [0.0] * 21 + [-0.2081559] * 182 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_182': {
            'samples': [0.0] * 21 + [0.254468348] * 182 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_183': {
            'samples': [0.0] * 20 + [-0.2081559] * 183 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_183': {
            'samples': [0.0] * 20 + [0.254468348] * 183 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_184': {
            'samples': [0.0] * 19 + [-0.2081559] * 184 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_184': {
            'samples': [0.0] * 19 + [0.254468348] * 184 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_185': {
            'samples': [0.0] * 18 + [-0.2081559] * 185 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_185': {
            'samples': [0.0] * 18 + [0.254468348] * 185 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_186': {
            'samples': [0.0] * 17 + [-0.2081559] * 186 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_186': {
            'samples': [0.0] * 17 + [0.254468348] * 186 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_187': {
            'samples': [0.0] * 16 + [-0.2081559] * 187 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_187': {
            'samples': [0.0] * 16 + [0.254468348] * 187 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_188': {
            'samples': [0.0] * 15 + [-0.2081559] * 188 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_188': {
            'samples': [0.0] * 15 + [0.254468348] * 188 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_189': {
            'samples': [0.0] * 14 + [-0.2081559] * 189 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_189': {
            'samples': [0.0] * 14 + [0.254468348] * 189 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_190': {
            'samples': [0.0] * 13 + [-0.2081559] * 190 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_190': {
            'samples': [0.0] * 13 + [0.254468348] * 190 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_191': {
            'samples': [0.0] * 12 + [-0.2081559] * 191 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_191': {
            'samples': [0.0] * 12 + [0.254468348] * 191 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_192': {
            'samples': [0.0] * 11 + [-0.2081559] * 192 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_192': {
            'samples': [0.0] * 11 + [0.254468348] * 192 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_193': {
            'samples': [0.0] * 10 + [-0.2081559] * 193 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_193': {
            'samples': [0.0] * 10 + [0.254468348] * 193 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_194': {
            'samples': [0.0] * 9 + [-0.2081559] * 194 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_194': {
            'samples': [0.0] * 9 + [0.254468348] * 194 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_195': {
            'samples': [0.0] * 8 + [-0.2081559] * 195 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_195': {
            'samples': [0.0] * 8 + [0.254468348] * 195 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_196': {
            'samples': [0.0] * 7 + [-0.2081559] * 196 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_196': {
            'samples': [0.0] * 7 + [0.254468348] * 196 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_197': {
            'samples': [0.0] * 6 + [-0.2081559] * 197 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_197': {
            'samples': [0.0] * 6 + [0.254468348] * 197 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_198': {
            'samples': [0.0] * 5 + [-0.2081559] * 198 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_198': {
            'samples': [0.0] * 5 + [0.254468348] * 198 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_199': {
            'samples': [0.0] * 4 + [-0.2081559] * 199 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_199': {
            'samples': [0.0] * 4 + [0.254468348] * 199 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_29_baked_wf_200': {
            'samples': [0.0] * 3 + [-0.2081559] * 200 + [0.0],
            'type': 'arbitrary',
            'is_overridable': False,
            'max_allowed_error': 0.0001,
        },
        'gate_36_baked_wf_200': {
            'samples': [0.0] * 3 + [0.254468348] * 200 + [0.0],
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


