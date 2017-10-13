from load_data import load_data
import pytest
import unittest


tester = load_data('data.csv')

def test_format():

    assert type(tester) is tuple
    assert len(tester) == 2


def test_columns_full():

    assert tester[0] != []
    assert tester[1] != []

class MyTestCase(unittest.TestCase):
    def test_datatype(dtype):
        dtype.assertRaises(ValueError, load_data, 'hello')

    def test_size(size):
        size.assertRaises(ValueError, load_data, 'onecol.csv')
