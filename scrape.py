from bs4 import BeautifulSoup
import requests

source=requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(source.text, "html.parser")
movies = soup.find("tbody", class_ = "lister-list").find_all("tr")

movie_list = []

class Movie:
    def __init__(self, rank, name, year, rating):
        self.rank = rank
        self.name = name
        self.year = year
        self.rating = rating

    def __str__(self):
        return (f"{self.rank}. {self.name} ({self.year}) {self.rating}")

for movie in movies:
    name = movie.find('td', class_ = "titleColumn").a.text
    rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
    year = movie.find('td', class_="titleColumn").span.text.strip("()")
    rating = movie.find('td', class_="ratingColumn imdbRating").strong.text

    movie = Movie(rank, name, year, rating)
    movie_list.append(movie)