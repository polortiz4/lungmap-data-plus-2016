import numpy as np


def load_data(file):
    """ Loads the data in a file
    
    :param file: (string) The filename of the file where the ECG data is
    :returns: A matrix containing all the data from the file
    """

    if not file.endswith('.csv'):
        raise ValueError("file must be in .csv format")

    matrix = np.loadtxt(open(file), delimiter=",", skiprows=1)
    dims = np.shape(matrix)

    if len(dims) < 2 or dims[1] != 2:
        raise ValueError("file must have two columns (time and voltage)")

    matrix=(matrix[:,0],matrix[:,1])
    return matrix


if __name__ == "__main__":
    load_data('ECGTest.csv')

