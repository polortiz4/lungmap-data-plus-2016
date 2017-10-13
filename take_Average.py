import numpy as np


def get_interval(mat,mins):
    """
    gets the length in items in an array of each interval of the time that is inputed in minutes

    :param mat: (ndarray)
    :param mins: (int)
    :returns: length of the interval in float
    """

    time = mat[:,0]
    hr = mat[:,1]
    secs = mins*60
    seglen = 0
    for a in range(time.shape[0]):
        if time[a]>secs:
            seglen = a + 1
            break

    if seglen == 0:
        raise ValueError('not enough data for that long average')

    return seglen


def average(mat,mins):

    """
    gets the length in items in an array of each interval of the time that is inputed in minutes

    :param mat: (ndarray)
    :param mins: (int)
    :returns: list of same length as instantaneous hr that gives average HR at each time point
    """
    time = mat[:,0]
    hr = mat[:,1]
    secs = mins*60
    seglen = get_interval(mat,mins)
    print(seglen)
    averages = []
    for a in range(hr.shape[0]):
        if a<seglen:
            averages.append('calculating')
        else:
            curAve = np.mean(hr[a-seglen:a])
            averages.append(curAve)

    return averages

if __name__ == "__main__":
    average('TestAve.csv',1)