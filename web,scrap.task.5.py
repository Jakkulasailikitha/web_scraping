# import requests
# import json
# from bs4 import BeautifulSoup
# url=[]
# with open("2.task.json","r")as f:
#     a=json.load(f)
# for i in a:
#     url.append(i["movie_link"])
# e=url[:10] 
# l=[]
# for j in e:
#     rel=requests.get(j)
#     soup=BeautifulSoup(rel.content,"html.parser")
#     p=soup.find("script",type="application/ld+json").text
#     print(p)
#     b=json.loads(p)
#     print(b)
#     c=[]
#     for i in b:
#         c["name"]=b["name"]
#         c["director"]=[b["director"][0]["name"]]
#         c["country"]="india"
#         c["language"]=b["review"]["inLanguage"]
#         c["image"]=b["image"]
#         c["genre"]=b["genre"]
#         c["url"]=b["url"]
#     l.append(c)
# with open("task.5.json","w") as f:
#     json.dump(c,f,indent=7)


# import requests
# import json
# from bs4 import BeautifulSoup
# url_list=[]
# with open('2.task.json','r') as f:
#     a=json.load(f)
# for i in a:
#     url_list.append(i['link'])
# b=url_list[:10]
# details=['name','director','image','description','language','genre',]
# l=[]
# for j in b:
#     rel=requests.get(j)
#     soup=BeautifulSoup(rel.content,"html.parser")
#     con=soup.find('script',type='application/ld+json').text
#     h=json.loads(con)
#     dic={}
#     for k in h:
#         dic['name']=h['name']
#         dic['director']=h['director'][0]['name']
#         dic['image']=h['image']
#         dic['description']=h['description']
#         dic["language"]=h['review']['inLanguage']
#         dic['genre']=h['genre']
#         dic['country']='india'
#     l.append(dic)
# with open('5_task.json','w') as file:
#     json.dump(l,file,indent=8)

