from ECG_Class import ECG_Class
from take_average import average
from HRinst import HRinst
from tachybradycardia import bradycardia, tachycardia
from glob import glob

files = glob('test_data*.csv')


def test_unpack():
    for f in files:
        obj1 = ECG_Class(f)
        assert obj1.name == f[:-4]
        assert len(obj1.time) == len(obj1.data[0][:])
        assert len(obj1.voltage) == len(obj1.data[0][:])
        assert type(obj1.data) == tuple


def test_defaults():
    for f in files:
        obj1 = ECG_Class(files[0])
        assert obj1.mins == 1
        assert obj1.outputfile == "test_data1_output.txt"
        assert obj1.bradyT == 60
        assert obj1.tachyT == 100


def test_average():
    for f in files:
        obj2 = ECG_Class(f, avemins=2)
        assert obj2.mins == 2
        assert obj2.avg() == average(obj2.instHR, obj2.time, obj2.mins)


def test_btc():
    for f in files:
        obj2 = ECG_Class(f)
        obj3 = ECG_Class(f, lowerThresh=50, upperThresh=110)
        assert obj2.bradyT == 60
        assert obj2.tachyT == 100
        assert obj3.bradyT == 50
        assert obj3.tachyT == 110
        assert obj3.brady() == bradycardia(obj3.instHR, obj3.bradyT)
        assert obj2.tachy() == tachycardia(obj2.instHR, obj2.tachyT)


def test_inst():
    import numpy as np
    for f in files:
        obj1 = ECG_Class(f)
        assert np.all(obj1.instHR == HRinst(obj1.data))
