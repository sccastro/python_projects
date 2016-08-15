import glob
import pandas as pd
import numpy as np

path ='/Users/spencercastro/PycharmProjects/LBA_Data/Study1bChoice/Prepared_Data'
allFiles = glob.glob(path + "/*.csv")

### Lists we'll need later as well as pandas data frames
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
    filename = filename[74:]
    subid = str(filename[:3])
    cond = str(filename[4:6])


    df = pd.read_csv(filename,index_col=None, header=0)
    mapping = {'correct': 1, 'Wrong!!': 0, 'miss': -1}
    df = df.replace({'correct': mapping, 'Wrong!!': mapping, 'miss': mapping })

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

