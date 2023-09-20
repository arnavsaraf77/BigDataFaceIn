import csv
import pandas as pd
import random 
from faker import Faker
import datetime
import itertools as i
import numpy as np

fake = Faker()

data = pd.DataFrame(columns=["FriendRel","PersonAID","PersonBID","DOF","DESC"])
 
# Import the data file into a dataframe 
dataFile = pd.read_csv("Data/Dataset1.csv") 
 
#Assign unique sequential number in the range 1 to 20,000,000 
relRange = range(0,20000000) 
data['FriendRel'] = relRange 

#Make 20,000,000 combinations from 200,000 values 

def MakeUniqueData(value):            
    pair = pd.DataFrame(columns=['A','B']) 
    
    pair['A'] = range(value) 
    pair['B'] = range(value) 
    
    random.shuffle(pair['A']) 
    random.shuffle(pair['B'])

    #pair = pair.apply(frozenset, axis=1)
    #print(pair.drop_duplicates().tolist())
    #pair = pair.drop_duplicates()

    yield pair

for i in range(100):
    datalist = list(MakeUniqueData(200000))

    copy = pd.DataFrame(columns=['A','B'])
    copy['A'] = datalist[0]['A']
    copy['B'] = datalist[0]['B']

    path = "t.csv"
    copy.to_csv(path, mode='a', index=False)
    print(i)

"""
for i in range(0,200):
    val1 = random.randint(0,200000)
    val2 = random.randint(0,200000)
    if(val1 == val2):
        --i
        continute
    else:
        data.loc[i,'PersonAID'] = dataFile['ID'][val1]
        data.loc[i,'PersonBID'] = dataFile['ID'][val2]
        data.loc[i,'DOF'] = fake.date_between(datetime.date(2000, 1, 1), datetime.date(2023, 1, 1))
        print(i)
"""

#l = np.array(random.sample((list)),200))

"""
def comb (iterable, r):
    for combination in i.combinations(iterable, r):
        yield combination

#v = comb(range(200000),2)

for combination in comb(range(200000),2):
    x = str(combination[0]) + "," + str(combination[1])
    print(x)
    f.write(x+"\n") 

#random.sample(l,20000000)
#print(l[0])c

#print(l)
#q = pd.DataFrame(l)

#print(data)
"""

