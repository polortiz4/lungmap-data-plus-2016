from load_data import load_data
import numpy as np


def get_interval(time,mins=1):

    """  Figures out how many points in mins minutes
    :param time: (ndarray) An array of times
    :param mins: (int) Number of minutes to take HR over
    :returns: The length in data points of mins minutes
    """

    secs = mins*60
    seglen = 0
    for a in range(time.shape[0]):
        if time[a]>secs:
            seglen = a + 1
            break

    if seglen == 0:
        raise ValueError('not enough data for that long average')

    return seglen


def average(hr,time,mins=1):

    """ Takes a running average of HR data
    :param hr: (ndarray) An array of heart rates
    :param mins: (int) Number of minutes to take HR over
    :returns: An ndarray of average heart rate at each time point
    """

    seglen = get_interval(time,mins)
    averages = []
    for a, val in enumerate(hr):
        if a<seglen:
            averages.append('calculating')
        else:
            curAve = np.mean(hr[a-seglen:a])
            averages.append(curAve)

    return averages

if __name__ == "__main__":
    average()
