import requests
import json
from bs4 import BeautifulSoup
l=[]
with open('5_task.json','r') as f:
    a=json.load(f)
i=0
d={}
while i<len(a):
    if a[i]["director"] in d:
        d[a[i]["director"]]+=1
    else:
        d[a[i]["director"]]=1
    i=i+1
with open("7_task.json","w")as f:
    json.dump(d,f,indent=8)
