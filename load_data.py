def load_data(file):
    """ Loads the data in a file

    :param file: (string) The filename of the file where the ECG data is
    :returns: A matrix containing all the data from the file
    """
    import numpy as np

    if not file.endswith('.csv'):
        raise ValueError("file must be in .csv format")

    matrix = np.loadtxt(open(file), delimiter=",", skiprows=1)
    dims = np.shape(matrix)

    if len(dims) < 2 or dims[1] != 2:
        raise ValueError("file must have two columns (time and voltage)")

    for item in matrix[:, 0]:
        if type(item) is not int:
            try:
                int(item)
            except:
                raise ValueError("files must only contain numbers")
    for item in matrix[:, 1]:
        if type(item) is not int:
            try:
                int(item)
            except:
                raise ValueError("files must only contain numbers")

    for i, item in enumerate(matrix[:, 1]):
        if item > 300:
            np.delete(matrix, [i][:])

    matrix = (matrix[:, 0], matrix[:, 1])
    return matrix


if __name__ == "__main__":
    load_data('ECGTest.csv')

