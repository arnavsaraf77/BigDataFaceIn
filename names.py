from faker import Faker
import random
import pandas as pd

# Create a Faker instance
fake = Faker()
df = pd.DataFrame(columns=["ID","Name"])

# Generate a list of 200,000 unique names and ID's
unique_names = set()
id_list = set()

while len(unique_names) < 200000:
    id_list.add(len(unique_names))
    unique_names.add(fake.name())

# Convert the set of unique names to a list
names_list = list(unique_names) 
id_lst = list(id_list)

df["ID"] = id_lst
df["Name"] = names_list

df.to_csv("Data/names.csv", index = False)
