
# # learn to scarpe e commerce site

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
request = requests.get(url)
print(request)

soup = BeautifulSoup(request.text,"lxml")
soup.prettify()

# print(soup.contents)

laptops = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")
print(f"Found {len(laptops)} laptops")
# print(laptops)

laptop_list = []
for laptop in laptops:
    if laptop :

        name = laptop.find('a', class_ = "title").text.strip()
        description = laptop.find('p', class_ = "description card-text").text.strip()
        price = laptop.find('span', itemprop = "price").text.strip()
        # print(f"{name} : {description} \n")
        # print(price)
        laptop_data = {
            "name":name,
            "price": price,
            "description":description
        }
        laptop_list.append(laptop_data)
print(f"Laptops : {name} : \n price: {price} \n description:  {description}")

# for item in laptop_list:

#     

df = pd.DataFrame(laptop_list)
print(df)

# To save file to excel file

excel_file_name = "Laptops_list_scarpe.xlsx"
df.to_excel(excel_file_name, index=False)
print(f"\nSuccessfully saved {len(laptop_list)} laptops to {excel_file_name}")
