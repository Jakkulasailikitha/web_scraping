# import requests
# from bs4 import BeautifulSoup

# url=("https://www.imdb.com/india/top-rated-indian-movies/")
# page=requests.get(url)
# soup=BeautifulSoup(page.text,'html.parser')
# scraped_movie=soup.find_all('td',class_="titleColumn")
# scraped_ratings=soup.find_all('td',class_="titleColumn")

# movie_name=[]
# for movie in scraped_movie:
#     movie=movie.get_text().replace("\n","")
#     movie=movie
#     movie_name.append(movie)
#     # print(movie_name)
# scraped_ratings=soup.find_all(class_="ratingColumn imdbRating")
# rating=[]
# for ratings in scraped_ratings:
#     ratings=ratings.get_text().replace("\n","")
#     ratings=ratings
#     rating.append(ratings)
#     # print(rating)
# i=0
# while i<len(movie_name):
#     print(movie_name[i],"=",rating[i])
#     i=i+1



import json
from bs4 import BeautifulSoup
import requests
page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(page.text,"html.parser")
def scrap_top_list():
    main_div=soup.find("div",class_="lister")  # table body 
    tbody=main_div.find("tbody",class_="lister-list")     
    # table rows
    trs=tbody.find_all("tr")     
    movie_ranks=[]
    movie_name=[]   
    year_of_release=[]
    movie_urls=[]
    movie_ratings=[]
    # using for loop to get the each each tr
    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        # return (position)
# print(scrap_top_list())        
        rank=""
        for i in position:
            if "." not in i:
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)
    # in this we are getting the ranks of yhe
    # movies
#     return movie_ranks
# print(scrap_top_list())
        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)
        # return title
# print(scrap_top_list() )
        year=tr.find("td",class_="titleColumn").span.get_text()
        year_of_release.append(year)
        
        imdb_rating=tr.find("td",class_="ratingColumn").strong.get_text()
        movie_ratings.append(imdb_rating)
        
        link=tr.find("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)
    top_movies=[]
    details={"position":"","name":"","year":"","rating":"","url":""}
    for i in range(0,len(movie_ranks)):
        details["position"]=int(movie_ranks[i])
        details["name"]=str(movie_name[i])
        year_of_release[i]=year_of_release[i][1:5]
        details["year"]=int(year_of_release[i])
        details["rating"]=float(movie_ratings[i])
        details["url"]=movie_urls[i]
        top_movies.append(details.copy())
        return(top_movies)
# print(scrap_top_list())
    with open("imdb 1_task.json","w") as f:
        json.dump(top_movies,f,indent=4)
scrap_top_list()



