import requests
import pandas as pd  
import re
from bs4 import BeautifulSoup

# Get the URL of the Wikipedia page with the list of nationalities
url = "https://countrycode.org/"

# Make a request to the URL
response = requests.get(url)

lst = []
new_clist = []
new_cclist = []

# Parse the response as HTML
soup = BeautifulSoup(response.content, "html.parser")

for tag in soup.find_all(re.compile("^td")):
    lst.append(tag.text)

for i in range(0, len(lst),6):
    new_clist.append(lst[i])
    new_cclist.append(lst[i+1])

df = pd.DataFrame({'Country': new_clist, 'CountryCode': new_cclist})
print(df)

df.to_csv('Data/CountryAndCode.csv',index = False)





#for i in lst.length:



