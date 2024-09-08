import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
a=soup.find("script",type="application/ld+json").text
# print(a)
b=json.loads(a)
# print(b)
d={}
for k in b:
    if k=="url":
        c=b[k]
        d["id"]=c
print(d) 
with open("8.task.json","w")as f:
    json.dump(d,f,indent=8) 

