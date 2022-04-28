import numpy as np

def calculate_conversion(dB,gate=True):
    """ 
    given 25dB attenuation on SMA8, we need to use the formula <br>
    dB = 20 log (V2/V1) <br>
    to calculate the division factor <br>
    <br>
    10**(dB/20) = V2/V1 <br>
    with dB=-55 we get a conversion factor: (here taken the inverse of to use for the output of the OPX)
    """
    if gate:
        print('factor 2 included to account for high impedance of gates')
        return 1/(10**(dB/20))/2
    else: 
        return 1/(10**(dB/20))