# import requests
# import json
# from bs4 import BeautifulSoup
# l=[]
# with open('5_task.json','r') as f:
#     a=json.load(f)
# i=0
# d={}
# while i<len(a):
#     if a[i]["director"] in d:
#         d[a[i]["director"]]+=1
#     else:
#         d[a[i]["director"]]=1
#     i=i+1
# with open("7_task.json","w")as f:
#     json.dump(d,f,indent=8)




import json
with open("imdb 5_task.json","r") as file:
    a=json.load(file)
dic={}
d={}
i=0
eng=0
hin=0
tel=0
while i<len(a):
    if a[i]['director']=="Madhavan":
        if a[i]['language']=='English':
            eng=eng+1
            dic['english']=eng
        if  a[i]['language']=='Hindi':
            hin=hin+1
            dic['Hindi']=hin
        if  a[i]['language']=='Telugu':
            tel=tel+1
            dic['Telugu']=tel
    if a[i]['director']=='Sundar C.':
        if a[i]['language']=='English':
            eng=eng+1
            dic['english']=eng
        if  a[i]['language']=='Hindi':
            hin=hin+1
            dic['Hindi']=hin
        if  a[i]['language']=='Telugu':
            tel=tel+1
            dic['Telugu']=tel
    if a[i]['director']=='Mani Ratnam':
        if a[i]['language']=='English':
            eng=eng+1
            dic['english']=eng
        if  a[i]['language']=='Hindi':
            hin=hin+1
            dic['Hindi']=hin
        if  a[i]['language']=='Telugu':
            tel=tel+1
            dic['Telugu']=tel
    i+=1
    d["Madhavan"]=dic
    d['Sundar C.']=dic
    d['Mani Ratnam']=dic
with open("imdb 10_task.json","w") as file:
    json.dump(d,file,indent=6)