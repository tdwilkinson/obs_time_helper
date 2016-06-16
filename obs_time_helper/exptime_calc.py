__author__ = 'tdwilkinson'


class by_mag_comparison():
    def __init__(self, ref_magnitude, ref_sn, ref_exptime, target_sn, array_magnitudes):
        exptime = (target_sn * ref_exptime) / ref_sn
        print 'recommended exp time:', exptime

        # use ref_magnitude and array_magnitudes to do a comparison
        for mag in array_magnitudes:
            ratio_flux = 10. ** ((- ref_magnitude) / 2.5) / 10. ** ((-mag) / 2.5)
            # m1/m2 = t2/t1 >> t2 =  m1/m2 * t1
            new_exptime = ratio_flux * exptime

            print mag, new_exptime
