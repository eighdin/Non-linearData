from urllib.request import *
from bs4 import *

url = "https://www.course-catalog.com/mercyhurst/C/2024-2025/degrees-by-department"

web_page = urlopen(url).read().decode("UTF-8")

soup = BeautifulSoup(web_page, "html.parser")

# dept_div_tag_list = soup.find_all(name='div', attrs={"class":"acc-title"})

# td_tag_list = soup.find_all(name="td", attrs={"data-label":"Program Name"})
# for object in td_tag_list:
#     print(object.text)

# table_tag_list = soup.find_all(name="table", attrs={"class":"normal-table"})
# for table_tag in table_tag_list:
#     print(table_tag["summary"])

# FIND ALL THE TABLES THAT CONTAIN THE DIFFERENT DEPARTMENT NAMES AND THEIR INFORMATION
table_tag_list = soup.find_all(name="table", attrs={"class":"normal-table"})
for table_tag in table_tag_list:
    print(table_tag["summary"]) # SHOWS THE DEPARTMENT NAMES

dept_name = input("\n\nEnter a department name: ")

# EACH TABLE IN THE TAG, IF IT MATCHES THE DEPARTMENT SELECTED, PRINT ALL OF THE PROGRAMS IN THAT DEPT
for table_tag in table_tag_list:
    if table_tag["summary"].lower() == dept_name.lower():
        print(f'Programs in {dept_name}: \n')
        
        # THIS WAY FINDS EACH table data TAG IN THE TABLE, AND PRINTS THE ONES WITH PROGRAM NAMES
        # for td_tag in table_tag.find_all(name="td", attrs={'data-label':'Program Name'}):
        #     print(td_tag.text.strip())
        
        # THIS WAY FINDS THE BODY TAG, AND THEN FINDS ALL THE table row TAGS AND PRINTS THE FIRST table data VALUE IN THE table row
        tbody_tag = table_tag.find('tbody')
        tr_tag_list = tbody_tag.find_all("tr")
        for tr_tag in tr_tag_list:
            td_tag = tr_tag.find("td")
            print(td_tag.text.strip())
        
        # td_tag_list = table_tag.find_all("td")
        # program_name_td_tag = td_tag_list[0]
        # print(program_name_td_tag.text.strip())

program_name = input('Choose a program name: ')
for tr_tag in tr_tag_list:
    td_tag = tr_tag.find("td")
    if td_tag.text.strip().lower() == program_name.lower():
        a_tag = td_tag.find('a')
        program_url = a_tag['href']
        break

program_web_page = urlopen(program_url).read().decode('UTF-8')
program_soup = BeautifulSoup(program_web_page, "html.parser")

crtm_div_tag_list = program_soup.find_all('div', attrs={'class':'crt-m'})
for course_row_div_tag in crtm_div_tag_list:
    course_id_div_tag = course_row_div_tag.find('div', attrs={'class':"crt-2"})
    course_name_div_tag = course_row_div_tag.find('div', attrs={'class':'crt-3'})
    print(course_row_div_tag.text.strip())
    if course_id_div_tag and course_name_div_tag:
        print(f'{course_id_div_tag.text.strip()} \t {course_name_div_tag.text.strip()}')