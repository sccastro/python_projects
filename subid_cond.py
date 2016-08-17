import glob
import pandas as pd
import numpy as np
import csv

path ='C:/Users/cac20/PycharmProjects/python_projects/lba_model2/'
allFiles = glob.glob(path + "*.txt")


# Lists we'll need later as well as pandas data frames
# filenameframe = pd.DataFrame()
frame = pd.DataFrame()
drt_list = []
# conds = []
# rename = []
# subids = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010',
#           '011', '012', '013', '014', '015', '016', '017', '018', '019', '020']

# for filename in allFiles:
#     filename = filename[74:]
#     cond = str(filename[4:6])
#     conds.append(cond)
#
# i = 1

for change in allFiles:
    with open(change, 'r') as f:
        change = change[58:]
        subid = str(change[13:16])
        cond = str(change[16])
        data = f.readlines()
        for line in data:
            line = line.split()
            line.insert(0, subid + cond)
            for spot in line:
                if spot[0:3] == 'DRT':
                    drt_list.append(line)

print drt_list[0:2]



with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(drt_list)

    # in_txt = np.genfromtxt(change, delimiter=',', dtype=str)
    # print in_txt
    # out_csv = csv.writer(open(change, 'wb'))
    #
    # out_csv.writerows(in_txt)





    # df = pd.read_csv(filename,index_col=None, header=0)
    # mapping = {'correct': 1, 'wrong': 0, 'miss': -1}
    # df = df.replace({'correct': mapping, 'wrong': mapping, 'miss': mapping })
    #
    # if filename[13:16] == subid:
    #     if filename[16] == 'a':
    #         df['subid'] = subid
    #         df['condition'] = '1'
    #     else:
    #         df['subid'] = subid
    #         df['condition'] = '2'


    # df = pd.concat([pd.Series(i, name = "subid"),pd.Series(conds[i], name = "condition"), df], axis = 1)


    # i = i + 1

    # list_.append(df)



# frame.to_csv('complete/complete_data.csv')

