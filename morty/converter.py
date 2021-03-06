from __future__ import division
import numpy as np
_NUM_CENTS_IN_OCTAVE = 1200.0


class Converter(object):
    @staticmethod
    def hz_to_cent(hz_track, ref_freq, min_freq=20.0):
        """--------------------------------------------------------------------
        Converts an array of Hertz values into cents.
        -----------------------------------------------------------------------
        hz_track : The 1-D array of Hertz values
        ref_freq : Reference frequency for cent conversion
        min_freq : The minimum frequency allowed (exclusive)
        --------------------------------------------------------------------"""
        # The 0 Hz values are removed, not only because they are meaningless,
        # but also logarithm of 0 is problematic.
        assert min_freq >= 0.0, 'min_freq cannot be less than 0'

        hz_track = np.array(hz_track).astype(float)

        # change values less than the min_freq to nan
        hz_track[hz_track <= min_freq] = np.nan

        return np.log2(hz_track / ref_freq) * _NUM_CENTS_IN_OCTAVE

    @staticmethod
    def cent_to_hz(cent_track, ref_freq):
        """--------------------------------------------------------------------
        Converts an array of cent values into Hertz.
        -----------------------------------------------------------------------
        cent_track  : The 1-D array of cent values
        ref_freq    : Reference frequency for cent conversion
        --------------------------------------------------------------------"""
        cent_track = np.array(cent_track).astype(float)

        return 2 ** (cent_track / _NUM_CENTS_IN_OCTAVE) * ref_freq
