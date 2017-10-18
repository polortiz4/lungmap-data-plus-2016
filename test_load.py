from load_data import load_data
import numpy as np
import pytest
import unittest


tester = load_data('data.csv')


def test_format():

    matrix = np.loadtxt(open('data.csv'), delimiter=",", skiprows=1)
    dims = np.shape(matrix)
    assert dims[1] == 2
    assert type(tester) is tuple
    assert len(tester) == 2


def test_columns_full():

    assert tester[0] != []
    assert tester[1] != []


class MyTestCase(unittest.TestCase):
    def test_datatype(self):
        self.assertRaises(ValueError, load_data, 'hello')

    def test_size(self):
        self.assertRaises(ValueError, load_data, 'onecol.csv')
