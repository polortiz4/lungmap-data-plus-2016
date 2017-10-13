from HRinst import HRinst
import numpy as np

dataset = (np.arange(0,29),np.array([0,1,2,1,0,-1,10,10,3,2,0,4,5,0,9,10,11,10,0,1,2,4,3,8.5,8.6,8,1,2,3]))
result = HRinst(dataset)
print(result)
def test_HRinst():
    assert type(result)== np.ndarray
    assert result.shape[1]==2
    assert np.all((result == (np.array([[  0.,   0.],
        [  1.,   0.],
        [  2.,   0.],
        [  3.,   0.],
        [  4.,   0.],
        [  5.,   0.],
        [  6.,   0.],
        [  7.,   0.],
        [  8.,   0.],
        [  9.,   0.],
        [ 10.,   0.],
        [ 11.,   0.],
        [ 12.,   0.],
        [ 13.,   0.],
        [ 14.,   0.],
        [ 15.,   0.],
        [ 16.,   0.],
        [ 17.,   20/3],
        [ 18.,   20/3],
        [ 19.,   20/3],
        [ 20.,   20/3],
        [ 21.,   20/3],
        [ 22.,   20/3],
        [ 23.,   20/3],
        [ 24.,   20/3],
        [ 25.,   7.5],
        [ 26.,   7.5],
        [ 27.,   7.5],
        [ 28.,   7.5]]))))
test_HRinst()