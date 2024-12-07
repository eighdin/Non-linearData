from urllib.request import *
from bs4 import *

url = "http://books.toscrape.com/"

web_page = urlopen(url).read().decode("UTF-8")

soup = BeautifulSoup(web_page, "html.parser")

section = soup.find(name="section")
books_ol = section.find(name='ol')

book_li_list = books_ol.find_all(name='li')
for book_li in book_li_list:
    book_title = book_li.find(name='h3').find(name='a')['title'].strip()
    book_price = book_li.find(name='p', attrs={"class":"price_color"}).text.strip()
    print(f'''
        Title: {book_title}
        \tPrice: {book_price}''')
