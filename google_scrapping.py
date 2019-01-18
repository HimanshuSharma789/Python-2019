import requests
from bs4 import BeautifulSoup as bsoup

from googlesearch import search
web_data = search("python", num=1, stop=1)

for web_page in web_data:
    url = requests.get(web_page)
    soup = bsoup(url.text, 'html.parser')
    para = soup.find_all('p')
    print("\n" + web_page + "\n")
    for data in para:
        print(data.text, end=" ")
    print("\n@@@@@@@@@@ ------------------------ @@@@@@@@@@@@@@@\n")
