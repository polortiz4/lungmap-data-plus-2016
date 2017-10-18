from load_data import load_data
import take_average as ta
import numpy as np
import pytest
import unittest

tup = load_data('TestAve.csv')
time = tup[0]
hr = tup[1]
mat = np.transpose(np.array([time, hr]))


def test_seglen():

    assert ta.get_interval(time, 1) == 60
    assert ta.get_interval(time, 3) == 180


def test_output():

    assert type(ta.average(hr, time, 3)) is list


class MyTestCase(unittest.TestCase):

    def test_seg(self):
        self.assertRaises(ValueError, ta.get_interval, mat, 1200)
