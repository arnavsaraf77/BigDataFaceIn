import numpy as np  
import pandas as pd
import random

FaceInPageData = pd.DataFrame(columns=['ID','Name','Nationality','CountryCode','Hobby'])


#Assign ID 
lst = []
for i in range(200000):
    lst.append(i)
FaceInPageData['ID'] = lst


#Assign Nationality 


#Print Results
print(FaceInPageData)


#Three separate data files
#FaceInPage: ID - unique sequential number (1 to 200,000)
#          : Name - Character of length between 10 to 20 
#          : Nationality - Character of length between 10 to 20 
#          : CountryCode - Number integer between 1 and 50 
#          : Hobby - Sequence of Character between 10 and 20 