import numpy as np

from write_output import write_output

time = np.transpose(np.array([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]))
HRinst = np.transpose(np.array([0., 80., 90., 90., 85., 80., 70., 68., 57.,
                                48.]))
HRavg = np.array([0., 80., 90., 90., 85., 80., 70., 68., 57., 48.])
btc = ['--', 'B', 'N', 'N', 'T', 'T', 'N', 'B', 'B', 'N']
test_data = (time, HRinst, HRavg, btc)
time_HRinst = np.column_stack((time, HRinst))
write_output(time_HRinst[:, 0], time_HRinst[:, 1], HRavg, btc)

data = []
data.append(np.loadtxt(open('assignment02_output.csv'),
                       delimiter=',', skiprows=1, usecols=0, dtype=float))
data.append(np.loadtxt(open('assignment02_output.csv'),
                       delimiter=',', skiprows=1, usecols=1, dtype=float))
data.append(np.loadtxt(open('assignment02_output.csv'),
                       delimiter=',', skiprows=1, usecols=2, dtype=float))
data.append(np.genfromtxt('assignment02_output.csv',
                          delimiter=',', skip_header=1, usecols=3, dtype=str))


def test_file_exists():
    try:
        file = open("assignment02_output.csv", 'r')
    except IOError:
        print("File does not exist!")
    finally:
        file.close()


def test_file_format():
    dims = np.shape(data)
    assert dims[0] == 4


def test_correct_numbers():
    assert [data[0][i] == test_data[0][i] for i in range(len(data[0]))]
    assert [data[1][i] == test_data[1][i] for i in range(len(data[1]))]
    assert [data[2][i] == test_data[2][i] for i in range(len(data[2]))]
    assert [data[3][i] == test_data[3][i] for i in range(len(data[3]))]


test_correct_numbers()
