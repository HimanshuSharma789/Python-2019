from bs4 import BeautifulSoup as bs
import requests
# search = input()
search = "Apple"
req = requests.get("https://en.wikipedia.org/wiki/"+search.capitalize())
soup = bs(req.text, 'html.parser')

# heading of wikipedia page
l = soup.find('h1', {"id": "firstHeading"})
print(l.text)

# moving to the position from where content starts
cont = soup.find("div", {"class": "mw-parser-output"}).find('table', {"class": "infobox biota"})

# to count number of iteration
t=0
# holds the first paragraph
cont = cont.find_next_sibling("p")

# to end the loop before the table of content (table class="toc")
while cont.name != "div":
    t=t+1
    print(cont.get_text())
    print(t)
    cont = cont.next_sibling
# for i in cont.next_sibling.next_siblings:
#     if i.name == "div":
#         break
#     t=t+1
#     print(t)
#     print(i.get.text())
