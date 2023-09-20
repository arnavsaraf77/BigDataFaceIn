import csv
import pandas as pd
import random

file_names = ["names.csv","CountryAndCode.csv","Hobbies.csv"]

df = pd.DataFrame(columns=['ID','Name','Nationality','CountryCode','Hobby'])
dummydf = pd.DataFrame(columns=['ID','Name'])

temp = []

# Assigning Names and ID to the local Dataframe from the names.csv file
with open("Data/names.csv","r") as f:
    reader = csv.reader(f) 
    temp.extend(list(reader))

df.loc[:,'ID'] = [row[0] for row in temp]
df.loc[:,'Name'] = [row[1] for row in temp]
temp.clear()

# Assigning Nationaliy and country code to the local Dataframe from the CountryAndCodes.csv file 
with open("Data/CountryAndCode.csv","r") as f:
    reader = csv.reader(f) 
    temp.extend(list(reader))

for i in range(200000):
    print(i)
    df.loc[:,'Nationality'][i] = temp[random.randint(0,359)][0]
    df.loc[:,'CountryCode'][i] = temp[random.randint(0,359)][1]
temp.clear()

# Assigning Hobbies to the local Dataframe from the Hobby.csv file 
with open("Hobbies.csv","r") as f:
    reader = csv.reader(f) 
    temp.extend(list(reader))

for i in range(200000):
    print(i)
    df.loc[:,'Hobby'][i] = temp[random.randint(0,37)][0]

temp.clear()

df.to_csv("Data/Dataset1.csv", index = False)
print(df)



