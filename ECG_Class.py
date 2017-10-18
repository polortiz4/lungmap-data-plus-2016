class ECG_Class(object):
    """This class treats a file containing ECG data as an object

    It has many associated methods that process and display this data

    :type filename: string
    :param filename: the name of the csv file with the ECG data

    :type avemins: double or int
    :param avemins: number of minutes to compute the average heart rate

    :type outName: string
    :param outName: name of output file

    :type lowerThresh: double or int
    :param lowerThresh: lower threshold for bradycardia

    :type upperThresh: double or int
    :param upperThresh: upper threshold for tachycardia
    """

    def __init__(self, filename, avemins=1, outName="_output.txt",
                 lowerThresh=60, upperThresh=100):
        '''
        Creates the variables associated with the class

        '''
        from load_data import load_data
        from HRinst import HRinst
        self.name = filename[:-4]
        self.mins = avemins
        self.bradyT = lowerThresh
        self.tachyT = upperThresh
        self.data = load_data(filename)
        self.time = self.data[:][0]
        self.voltage = self.data[:][1]
        self.instHR = HRinst(self.data)

        if outName == "_output.txt":
            self.outputfile = self.name + outName
        elif outName[-4:] == '.txt':
            self.outputfile = outName
        else:
            self.outputfile = outName + '.txt'

    def avg(self):
        '''
        :type return: tuple
        :return: average heart rate (
        '''
        from take_average import average

        return average(self.instHR, self.time, self.mins)

    def brady(self):
        from tachybradycardia import bradycardia
        brady = bradycardia(self.instHR, self.bradyT)
        return brady

    def tachy(self):
        from tachybradycardia import tachycardia
        tachy = tachycardia(self.instHR, self.tachyT)
        return tachy

    def output(self):

        """ Creates a file containing the output of these functions

        :param mins: (int) Number of minutes to take HR over
        :param filename: (str) optional name of file if you don't want
        :returns: An ndarray of average heart rate at each time point
        """

        from write_output import write_output

        ave = self.avg()
        b = self.brady()
        t = self.tachy()

        return write_output(self.time, self.instHR, ave, b, t, self.outputfile)
