import csv
import pandas as pd
import random 
from faker import Faker
import datetime
import itertools as i
import numpy as np


datafile = pd.read_csv("Data/t.csv", low_memory=False)
print(len(datafile))

datafile = datafile.drop_duplicates()
print(len(datafile))

datafile = datafile.apply(frozenset, axis=1)
datafile = datafile.drop_duplicates().reset_index(drop=True)
datafile = datafile.apply(list)
print(len(datafile))

datafile.to_csv("Data/t2.csv",mode='w', index=False)

"""
A = list()
B = list()

for i in datafile_normal:
    A.append(i[0])
    B.append(i[1])

datafile = pd.DataFrame(columns=['A','B'])
datafile['A'] = A
datafile['B'] = B

datafile.to_csv("t2.csv", index = False)
"""

"""
data2 = pd.DataFrame(columns=['A','B'])
data2['A'] = [1,2,3,4,5,6]
data2['B'] = [5,6,4,2,1,2]

data2 = data2.apply(frozenset,axis=1)
data2 = data2.apply(list)

A = list()
for i in data2:
    A.append(i[0])

print(A)
"""