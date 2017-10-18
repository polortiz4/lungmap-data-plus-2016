def load_data(file):
    """ Loads the data in a file

    :param file: (string) The filename of the file where the ECG data is
    :returns: A matrix containing all the data from the file
    """
    import numpy as np
    import csv

    if not file.endswith('.csv'):
        raise ValueError("file must be in .csv format")
    try:
        matrix = np.loadtxt(open(file), delimiter=",", skiprows=1)
        dims = np.shape(matrix)
    except:
        mat_csv = csv.reader(open(file))
        count = 0
        arr = []
        for row in mat_csv:
            if row[0] == '' or row[1] == '':
                continue
            elif row[0][0].isalpha() or row[1][0].isalpha():
                continue
            else:
                arr.append([float(row[0]), float(row[1])])
                count += 1
        matrix = np.array(arr)
        dims = np.shape(matrix)
        print(matrix)

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
