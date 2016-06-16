__author__ = 'tdwilkinson'

import numpy as np


class by_mag_comparison():
    def __init__(self, ref_magnitude, ref_sn, ref_exptime, target_sn, array_magnitudes):


        gain = 1.88 # needed?

        # want to incorporate some kind of sn adjustment
        # ratio_sn = ref_sn / target_sn
        # print 'sn ratio' , ratio_sn
        exptime = (target_sn * ref_exptime) / ref_sn
        print 't:', exptime

        # use ref_magnitude and array_magnitudes to do a comparison
        for mag in array_magnitudes:
            ratio_flux = 10. ** ((- ref_magnitude) / 2.5) / 10. ** ((-mag) / 2.5)
            # m1/m2 = t2/t1 >> t2 =  m1/m2 * t1
            new_exptime = ratio_flux * exptime

            print mag, new_exptime

        print 'mag 14.9 expect ~ 661.441 s'

