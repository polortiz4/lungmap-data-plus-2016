from ECG_Class import ECG_Class
from take_average import average
from HRinst import HRinst
from tachybradycardia import bradycardia


def test_unpack():
    obj1 = ECG_Class('testclass.csv')
    print(obj1.name)
    print(type(obj1.data))
    assert obj1.name == 'testclass'
    assert len(obj1.time) == len(obj1.data[0][:])
    assert len(obj1.voltage) == len(obj1.data[0][:])
    assert type(obj1.data) == tuple


def test_defaults():
    obj1 = ECG_Class('testclass.csv')
    assert obj1.mins == 1
    assert obj1.outputfile == "testclass_output.txt"
    assert obj1.bradyT == 60
    assert obj1.tachyT == 100


def test_average():
    obj2 = ECG_Class('testclass.csv',avemins=2)
    assert obj2.mins == 2
    assert obj2.avg() == average(obj2.instHR,obj2.time,obj2.mins)

def test_btc():
    obj2 = ECG_Class('testclass.csv')
    obj3 = ECG_Class('testclass.csv',lowerThresh=50,upperThresh=110)
    assert obj2.bradyT == 60
    assert obj2.tachyT == 100
    assert obj3.bradyT == 50
    assert obj3.tachyT == 110
    #assert obj3.brady() == bradycardia()

def test_inst():
    import numpy as np
    obj1 = ECG_Class('testclass.csv')
    assert np.all(obj1.instHR == HRinst(obj1.data))