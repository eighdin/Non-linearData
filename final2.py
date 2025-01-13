from urllib.request import *
from bs4 import *

url = "https://www.moviecrow.com/telugu/list-of-movies/2022"

web_page = urlopen(url).read().decode("UTF-8")

soup = BeautifulSoup(web_page, "html.parser")

page_content = soup.find(name='div', attrs={"id":"page-content"})
movie_box_div_list = page_content.find_all(name='div', attrs={"class":"movie_box"})
for movie_box_div in movie_box_div_list:
    about_film_div = movie_box_div.find(name='div', attrs={"class":"about_film"})
    film_name_div = about_film_div.find(name='div', attrs={"class":"film_name"})
    info_entries = about_film_div.find_all(name='li')
    
    movie_title = film_name_div.find(name='h1').text.strip()
    movie_release_date = film_name_div.find(name='h6').text.strip()
    movie_music_director = info_entries[1].find(name='span', attrs={"itemprop":"name"}).text.strip()
    
    print(f'MOVIE: {movie_title} RELEASE DATE: {movie_release_date} MUSIC DIRECTOR: {movie_music_director}')