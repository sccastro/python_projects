import glob
import pandas as pd
import numpy as np

path ='C:/Users/cac20/PycharmProjects/python_projects/lba_model2/'
allFiles = glob.glob(path + "*.txt")

print len(allFiles[0])
# Lists we'll need later as well as pandas data frames
# filenameframe = pd.DataFrame()
frame = pd.DataFrame()
list_ = []
# conds = []
# rename = []
# subids = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010',
#           '011', '012', '013', '014', '015', '016', '017', '018', '019', '020']

# for filename in allFiles:
#     filename = filename[74:]
#     cond = str(filename[4:6])
#     conds.append(cond)
#
#
# i = 1



for filename in allFiles:
    filename = filename[58:]
    subid = str(filename[13:16])
    cond = str(filename[16])


    df = pd.read_csv(filename,index_col=None, header=0)
    mapping = {'correct': 1, 'Wrong!!': 0, 'miss': -1}
    df = df.replace({'correct': mapping, 'wrong': mapping, 'miss': mapping })

    if filename[:3] == subid:
        if filename[4:6] == 'Co':
            df['subid'] = subid
            df['condition'] = '1'
        elif filename[4:6] == 'ST':
            df['subid'] = subid
            df['condition'] = '2'
        else:
            df['subid'] = subid
            df['condition'] = '3'


    # df = pd.concat([pd.Series(i, name = "subid"),pd.Series(conds[i], name = "condition"), df], axis = 1)


    # i = i + 1

    list_.append(df)


frame = pd.concat(list_)

frame.to_csv('complete/complete_data.csv')

