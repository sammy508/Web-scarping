from bs4 import BeautifulSoup
import requests

url = "https://www.tutorialsfreak.com"

web = requests.get(url)
print(web.status_code)
# print(request.content)    
content = web.content

# Initialize beautiful soup create object
# here we pass context and parser
soup = BeautifulSoup(content, "html.parser")

pretiffy = soup.prettify().encode("ascii",'ignore').decode('ascii')  # it drops the asci num which acts as obstacle and broke program
print(pretiffy)

# to get anchor tag
print(soup.a)
print()
print(soup.title)   # scarpe title 
print(soup.p)  # paragraph


# to extract string only from tag using" navigable string"
st_p1 = soup.p.string  # it scarpe test of the paragraph tag
print(st_p1)   # \n on output means it indicating the new line on tag

print(soup.h1.string)


# Functions on Beautiful soups
# 1. Find()  and Find_all()

soup.find('p') # it  print 1st paragraph
soup.find_all('p')  # prints all the only paragraphs of websites

# comments Object

# Finding Elements BY class

class_data = soup.find("div",class_ ="header-logo-wrapper").find_all('p')
# p_in_div =class_data.find('p')
print(class_data)