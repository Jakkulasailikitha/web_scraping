# import requests
# import json
# from bs4 import BeautifulSoup
# rel=requests.get("https://www.imdb.com/title/tt0066763/")
# soup=BeautifulSoup(rel.content,"html.parser")
# a=soup.find("script",type="application/ld+json").text
# print(a)
# b=json.loads(a)
# print(b)
# c={}
# for i in b:
#     c["name"]=b["name"]
#     c["director"]=[b["director"][0]["name"]]
#     c["country"]="india"
#     c["language"]=b["review"]["inLanguage"]
#     c["image"]=b["image"]
#     c["genre"]=b["genre"]
#     c["url"]=b["url"]
#     # c["runtime"]=b["runtime"][0]
# with open("task.4.json","w") as f:
#     json.dump(c,f,indent=7)
# a=input("enter the string:")
# # if a=="@"or"#"or"$"or"!" or a=="A"<="z":
# #     print("true")
# if a=="a"<="z" or a==1<=9:
#     print("false")
# elif a=="@"or"#"or"$"or"!" or a=="A"<="z":
#     print("true")


a=input("enter the string:")
if a in"a"<="z" or a in"1"<="9":
    print("false")
elif a=="@"or"#"or"$"or"!" or a=="A"<="z":
    print("true")
