from urllib.request import *
from bs4 import *

url = "https://worldpopulationreview.com/states"

web_page = urlopen(url).read().decode("UTF-8")

soup = BeautifulSoup(web_page, "html.parser")

my_6_divs = soup.find_all(name="div", attrs={"class":"relative my-6"})
for div in my_6_divs:
    possible_header = div.find(name='div', attrs={"class":"flex"}).text
    if possible_header == "50 states":
        state_table_div = div

state_table = state_table_div.find(name='table')
state_table_body = state_table.find(name='tbody')
state_tr_list = state_table_body.find_all(name='tr')

state_count = 0
for state_tr in state_tr_list:
    state_count += 1
    state_name = state_tr.find(name='th').text.strip()
    state_population = state_tr.find_all(name='td')[1].text.strip()
    print(f'{state_name}\t\t{state_population}')