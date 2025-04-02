
# Here we will practice to handle the list data using beautiful soup

# have to fix later , still unable to handle list under dropdown 

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.tutorialsfreak.com/"
request = requests.get(url)
# print(request.content)

soup = BeautifulSoup(request.text, 'lxml')
soup.prettify()




# # to extract table data
parent_div = soup.find("div",class_ = "dropdown-3 d-none bg-white main-mega-dropdown online-classes-menu")
 
if parent_div:
    dropdown = parent_div.find('ul', class_ ='d-block border-right border-bottom-0 dropdown-menu-left-wrapper navbar-nav nav-tabs')

    if dropdown:
        menu_items = dropdown.find_all('li', class_ = "nav-item")

        for item in menu_items:
            print(item.get_text(strip=True))
    
    else:
        print("dropdown menu list not found")

else: 
    print("Parent container not found")






# list_data = parent_div.find("ul") if parent_div else None


# data = []

# if list_data:
#     list_items = [li.get_text(strip=True)for li in list_data.find_all("li")]
#     print(f"List items : {list_items}")
# else :
#  print("Not found")