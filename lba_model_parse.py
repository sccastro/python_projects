# import csv
# import pandas as pd


# csv.reader("lba_model2/RemoteChoice_001a.txt")
# pd.read_csv("lba_model2/RemoteChoice_001a.txt")

# data = []
# drt = []

# try:
#     with open('lba_model2/RemoteChoice_001a.txt', 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             data.append(row)
#         print data[0:1]
#         for line in data:
#             if line[0:1] == 'DRT':
#                 drt.append(line)
#         print len(drt)
# finally:
#     print "done"

""" fields to it and finally write to CSV. Here's Python 3.x solution (I think Python 2.7+ should suffice):"""
import csv
import re


def read_general("lba_model2/RemoteChoice_"):
    # Read general info to dict with 'PR 123'-like keys

    # Gerexp that will split row into ready-to-use dict
    re_name = re.compile(r'''
        (?P<Name>.+)
        \ --\  # Separator + space
        (?P<Division>.+)
        \  # Space
        \(
            (?P<Division_Abbreviation>.*)
        \)
        \  # Space
        (?P<Id>\d+)
        \  # Space
        \[Age:\  # Space at the end
            (?P<Age>\d+)
        \]
        ''', re.X)

    general = {}

    with open(fname, 'rt') as f:
        for line in f:
            line = line.strip()
            m = re_name.match(line)

            if m:
                # Name line, start new man
                man = m.groupdict()
                key = '%s %s' % (m.group('Division_Abbreviation'), m.group('Id'))
                general[key] = man

            elif line:
                # Non empty lines
                # Add values to dict
                key, value = line.split(': ', 1)
                man[key] = value

    return general


def add_bool_criteria(fname, field, general):
    # Append a field with YES/NO value

    with open(fname, 'rt') as f:
        yes_keys = set()

        # Phase one, gather all keys
        for line in f:
            line = line.strip()
            _, keys = line.split(': ', 1)

            yes_keys.update(keys.split(', '))

        # Fill data
        for key, man in general.items():  # iteritems() will be faster in Python 2.x
            man[field] = 'YES' if key in yes_keys else 'NO'


def save_csv(fname, general):
    with open(fname, 'wt') as f:
        # Gather field names
        all_fields = set()
        for value in general.values():
            all_fields.update(value.keys())

        # Write to csv
        w = csv.DictWriter(f, all_fields)
        w.writeheader()
        w.writerows(general.values())


def main():
    general = read_general('general.txt')
    add_bool_criteria('cars.txt', 'Car?', general)
    add_bool_criteria('house.txt', 'House?', general)
    from pprint import pprint
    pprint(general)
    save_csv('result.csv', general)


if __name__ == '__main__':
    main()
