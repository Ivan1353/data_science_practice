#imports libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

#scrapes the data and defines variables
source=requests.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating")
soup = BeautifulSoup(source.text, "html.parser")

movies_string = soup.find("div", class_="lister-list").find_all("div", class_ = "lister-item-content")

movies = {
    "names":[],
    "ranks":[],
    "years":[],
    "runtimes":[],
    "genres":[],
}

#structures the data into a dictionary
for movie in movies_string:
    movies["names"].append(movie.find('h3', class_ = "lister-item-header").a.text)
    movies["ranks"].append(movie.find('span', class_="lister-item-index unbold text-primary").text.strip("."))
    movies["years"].append(movie.find('span', class_="lister-item-year text-muted unbold").text.strip("()"))
    movies["runtimes"].append(movie.find('span', class_="runtime").text.strip(" min"))
    movies["genres"].append(movie.find('span', class_="genre").text.strip().split(", "))


#transforms the dictionary into a pandas dataframe
pd_movies = pd.DataFrame.from_dict(movies)
pd_movies