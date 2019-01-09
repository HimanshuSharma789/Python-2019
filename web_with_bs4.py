from bs4 import BeautifulSoup as bs
import requests
# search = input()
search = "Apple"
req = requests.get("https://en.wikipedia.org/wiki/"+search.capitalize())
soup = bs(req.text, 'html.parser')
# print(soup.prettify())
l = soup.find('h1', {"id": "firstHeading"})
print(l.text)
cont = soup.find("div", {"class": "mw-parser-output"}).find('table', {"class": "infobox biota"})
# print(cont)
# for para in cont.find("p"):
#     soup.find
# print(l.get_text()+"\n")
# print(cont)
t=0
cont = cont.find_next_sibling("p")
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
