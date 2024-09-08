# import requests
# from bs4 import BeautifulSoup
# import csv
# url="https://www.google.com/search?q=chocolates&rlz=1C1CHBF_enIN1020IN1020&oq=chocolates&aqs=chrome..69i57j0i457i512j0i402j0i512l3j0i131i433i512j0i433i512j0i512l2.8854j0j15&sourceid=chrome&ie=UTF-8"
# page=requests.get(url)
# # soup=BeautifulSoup(page.content,'html.parser')   parser:change the page one page to another pAGE
# # print(soup)   soup.prettify: we get the new lines
import requests 
from bs4 import BeautifulSoup
req = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
print(req)
# soup=BeautifulSoup(req.content,'html.parser')
# # print(soup.prettify())

# scraped_movies=soup.find_all('td', class_='titleColumn')
# scraped_rantings=soup.find_all('td',class_='titleColumn')
# # scraped_movies
# # parse movie name
# movies=[]
# for movie in scraped_movies:
#     movie=movie.get_text().replace("\n","")
#     movie=movie
#     movies.append(movie)  
#     #  print(movies)
  
# # scraping rating for movies
# scraped_ratings=soup.find_all('td',class_='ratingcolum imdbrating')
# # scraped_ratings

# # # parse ratings
# rating=[]
# for rating in scraped_ratings:
#     rating=rating.get_text().replace("\n",'')
#     rating=rating
#     rating
    
#     rating.append(rating)
#     # print(ratings)
# i=0
# l=[]
# while i<len(movies):
#     print(movies[i],"=",rating[i])
#     i=i+1
    

