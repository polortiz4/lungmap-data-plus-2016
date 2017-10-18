def HRinst(dataset, secperunit=60, peak_threshold=98, filt=True):
    """
    Takes the input data of the time and voltage to convert it into an array
    with time and instantaneous heart rate.

    :param dataset: (tuple) Two elements, each a 1xN ndarray for time and
     voltage values respectively
    :param secperunit: (int or double) Conversion from unit of time ndarray
     to seconds
    :param peak_threshold: (double) percentage of maximum peak to set
     thresholding
    :param filt: (boolean) true if user wants to filter data, false if not
    :returns: (ndarray) 2 columns. First column with time in s, second column
     with heart rate in BPM. Each element in the ndarray is a float.
    """
    import numpy as np
    from scipy import stats

    time = dataset[:][0]
    voltage = dataset[:][1]

    if filt:
        voltage = data_filter(voltage)

    thresholded = stats.threshold(voltage,
                                  np.percentile(voltage, peak_threshold))
    hrinst = np.zeros(len(thresholded))

    is_increasing = np.roll(thresholded, 1) <= thresholded
    will_decrease = np.roll(thresholded, -1) < thresholded
    is_maximum = is_increasing * will_decrease
    peakInd = np.asarray(np.where(is_maximum))

    for i, val in enumerate(thresholded):
        peaks = peakInd[peakInd < i]
        if i > peakInd[0][1]:
            hrinst[i] = \
                secperunit / (time[int(peaks[-1])] - time[int(peaks[-2])])
        else:
            hrinst[i] = 0

    hrinst[-1] = hrinst[-2]
    return hrinst


def data_filter(voltage, num_coef=8, hfreq=0.125, lfreq=0.0125):
    '''
    Filter the data using a band pass filter to smooth corners out and
    remove baseline drift

    :param voltage: (ndarray) of size 1xN with the voltage values
    :param num_coef: (int) order of the filter
    :param hfreq: (double) critical high frequency
    :param lfreq: (double) critical low frequency
    :return: (ndarray) of size 1xN with filtered voltage values
    '''
    from scipy import signal
    b, a = signal.butter(num_coef, hfreq, btype='low')
    c, d = signal.butter(num_coef, lfreq, btype='High')
    low_filt = signal.filtfilt(b, a, voltage)
    band_filt = signal.filtfilt(c, d, low_filt)

    return band_filt
