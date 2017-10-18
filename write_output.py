def write_output(time, HRinst, HRavg, btc, filename="assignment02_output.csv"):
    """Writes to text file time, instantaneous heart rate, average heart rate
    over user-specified interval, and when brady- or tachycardia occurred in
    the ECG trace

    :param time_HRinst: ndarray where first element is times and second element
     is instantaneous heart rates
    :param HRavg: list of average heart rates
    :param btc: list of characters to indicate patient status (-- means not
     enough data, T means tachycardia, B means bradycardia, and N means normal
    """

    file = open(filename, "w+")
    header = "Time (s), Instantaneous Heart Rate, Average Heart Rate," \
             " Brady/Tachycardia Occurrence\n"
    file.write(header)
    for i, hr in enumerate(HRavg):
        row = str(time[i]) + "," + str(HRinst[i]) + "," + str(HRavg[i]) + ","\
              + btc[i] + "\n"
        file.write(row)
    file.close()
