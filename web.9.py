import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
a=soup.find("script",type="application/ld+json").text
# print(a)
b=json.loads(a)
with open("9.task.json","w")as f:
    json.dump(b,f,indent=8)