import requests
import json
from bs4 import BeautifulSoup
url_list=[]
with open('5_task.json','r') as f:
    a=json.load(f)
d={}
i=0
eng=0
tel=0
hin=0
while i<len(a):
    if a[i]["language"]=="English":
        eng=eng+1
        d["English"]=eng
    else:
        d["English"]=eng
    if a[i]["language"]=="telugu":
        tel=tel+1
        d["telugu"]=tel
    else:
        d["telugu"]=tel
    if a[i]["language"]=="hindi":
        hin=hin+1
        d["hindi"]=hin
    else:
        d["hindi"]=hin
    i=i+1
with open("6_task.json","w")as f:
    json.dump(d,f,indent=8)
    