
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"
request = requests.get(url)
# print(request.content)

soup = BeautifulSoup(request.text, 'lxml')
# soup.prettify()

# to extract table data
table_data = soup.find("table", class_="table table-sm table-hover screenertable")

data =[]
if table_data:
    # headers = table_data.find_all("th")
    row_data = table_data.find_all("tr")

   

    for row in row_data:
        cells = row.find_all(["th","td"])  # to get both header and table data
        
        row_data =[]   # temporaray list
        for cell in cells:
            clean_text = cell.get_text(strip =True)
            row_data.append(clean_text)
            text = row.text 
        data.append(row_data)

print(data)
print()
df = pd.DataFrame(data)
print(df)