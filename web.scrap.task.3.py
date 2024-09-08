# import json
# from bs4 import BeautifulSoup
# import requests
# page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
# soup=BeautifulSoup(page.text,"html.parser")
# top_movies=[]
# def scrap_top_list():
#     main_div=soup.find("div",class_="lister")  # table body 
#     tbody=main_div.find("tbody",class_="lister-list")     
#     # table rows
#     trs=tbody.find_all("tr")     
#     movie_ranks=[]
#     movie_name=[]   
#     year_of_release=[]
#     movie_urls=[]
#     movie_ratings=[]
#     # using for loop to get the each each tr
#     for tr in trs:
#         position=tr.find("td",class_="titleColumn").get_text().strip()
#         # return (position)
# # print(scrap_top_list())        
#         rank=""
#         for i in position:
#             if "." not in i:
#                 rank=rank+i
#             else:
#                 break
#         movie_ranks.append(rank)
#     # in this we are getting the ranks of yhe
#     # movies
# #     return movie_ranks
# # print(scrap_top_list())
#         title=tr.find("td",class_="titleColumn").a.get_text()
#         movie_name.append(title)
#         # return title
# # print(scrap_top_list() )
#         year=tr.find("td",class_="titleColumn").span.get_text()
#         year_of_release.append(year)
        
#         imdb_rating=tr.find("td",class_="ratingColumn").strong.get_text()
#         movie_ratings.append(imdb_rating)
        
#         link=tr.find("td",class_="titleColumn").a["href"]
#         movie_link="https://www.imdb.com"+link
#         movie_urls.append(movie_link)
#         details={"position":"","name":"","year":"","rating":"","url":""}
#     for i in range(0,len(movie_ranks)):
#         details["position"]=int(movie_ranks[i])
#         details["name"]=str(movie_name[i])
#         year_of_release[i]=year_of_release[i][1:5]
#         details["year"]=int(year_of_release[i])
#         details["rating"]=float(movie_ratings[i])
#         details["url"]=movie_urls[i]
#         top_movies.append(details.copy())
#     print(top_movies)
import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(rel.content,"html.parser")
movies=soup.find("tbody",class_="lister-list",).find_all("tr")
list=[]
for movie in movies:
    dic={"movie":"","year":"","rating":"","position":"","link":""}
    name=movie.find('td',class_="titleColumn").a.text
    ratings=movie.find('td',class_="ratingColumn imdbRating").strong.text
    position=movie.find("td",class_='titleColumn').get_text(strip=True).split('.')[0]
    year=movie.find("td",class_="titleColumn").span.text.strip("()")
   
    url=movie.find("td",class_="titleColumn").a["href"]
    link="https://www.midb.com/"+url
    
    dic["movie"]=name
    dic["year"]=year
    dic["rating"]=ratings
    dic["position"]=position
    dic["link"]=link
    list.append(dic)
dic={}
a=[]
b=[]
c=[]
d=[]
i=0
while i<len(list):
    if list[i]["year"] >="1960" and list[i]["year"]<="1969":
        a.append(list[i])
        dic["1960"]=a
    i=i+1
    print(a)
with open("task.3.json","w")as f:
    json.dump(dic,f,indent=8)




