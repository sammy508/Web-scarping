
# structured programme

import requests
from bs4 import BeautifulSoup

url = "https://www.tutorialsfreak.com"
web = requests.get(url)

content = web.content

# creting soup object
soup = BeautifulSoup(content,'html.parser')
pretiffy = soup.prettify().encode('ascii','ignore').decode('ascii')  # it drops the asci num which acts as obstacle and broke program

header_logo_div = soup.find("div", class_='banner-heading-wrapper')

if header_logo_div :
    p_tags = header_logo_div.find_all('p')

    if p_tags:
        print("paragraphs found in class")
        for p in p_tags:
         print(f" {p.text.strip()}")
    else:
        
        print("No paragraph tags found inside col-md-3")
else:
    print("Could not find div with cbanner-heading-wrapper'")

