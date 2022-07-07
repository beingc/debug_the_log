# coding=utf8
# desc: calculate the request cost time by the log

from datetime import datetime

InputFileName = 'input.log'
OutputFileName = 'output.csv'
LIST_1 = []

with open(InputFileName, 'r') as f:
    for line in f.readlines():
        time_str, flag = line.strip().split(',')
        LIST_1.append([flag, time_str])

for i in list(range(len(LIST_1))):
    flag_str, time_str1 = LIST_1[i]
    del LIST_1[i][0]
    for j in list(range(len(LIST_1))):
        if flag_str == LIST_1[j][0]:
            time_str2 = LIST_1[j][1]
            time_1 = datetime.strptime(time_str1, '%Y-%m-%d %H:%M:%S.%f')
            time_2 = datetime.strptime(time_str2, '%Y-%m-%d %H:%M:%S.%f')
            cost_time = (time_2 - time_1).microseconds // 1000
            line_str = "{},{},{},{}\n".format(flag_str, time_str1, time_str2, cost_time)
            # print("{},{},{},{}\n".format(flag_str, time_str1, time_str2, cost_time))
            with open(OutputFileName, 'a') as f:
                f.writelines(line_str)
