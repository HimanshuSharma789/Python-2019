"""
using google search module for searching a particular keyword form google and generate the links
using beautiful soup to extract the text from each web page in the link
for each web page -> generating the dict to determine the occurrence of words (count)
plotting the graph for top 10 words for each web page
"""


import matplotlib.pyplot as plt
import requests
import sys
from bs4 import BeautifulSoup as bsoup
from collections import OrderedDict
from googlesearch import search

# search the value on the web (google engine)
# return a list of links based on the arguments
web_data = search(sys.argv[1], num=1, stop=1)
# print(web_data)

# use one link at a time || looping through the list of link
for web_page in web_data:
    # get request
    url = requests.get(web_page)
    # get the content from the web page
    soup = bsoup(url.text, 'html.parser')
    # find all the paragraph for extracting the text
    para = soup.find_all('p')
    # prints the web page url
    print("\n" + web_page + "\n")

    # initialize the dictionary for storing each unique word
    di = {}
    # looping through each paragraph
    for data in para:
        # iterate through each word in the sentence || paragraph
        # (using split to break the sentence in words)
        for word in data.text.split():
            if word in di:
                # if word already present in dict increase the count
                di[word] = di[word] + 1
            else:
                # if word in found init the word with 1
                di[word] = 1

    # printing the dict for proof reading
    print(di)

    # sorting the dictionary on the basis of values in decreasing order
    # OrderedDict for maintaining the order for future use
    di = OrderedDict(sorted(di.items(), key=lambda x: x[1], reverse=True))
    # plot 10 values (x-axis) and top 10 occurrences form the dict (y-axis)
    plt.plot(range(10), list(di.values())[:10])
    # placing the x-axis labels
    plt.xticks(range(10), list(di.keys())[:10])
    plt.show()

    '''
    (optional)
    storing the data into the file
    place the given loop in above to get the data from web 
    and store it into file format for later use !! 
    '''
    # with open('google_scrap_data.txt', 'w') as file:
    #     for data in para:
    #         file.write(data.text)
    #         file.write("\n")
    #         print(data.text, end=" ")
    #     print("\n@@@@@@@@@@ ------------------------ @@@@@@@@@@@@@@@\n")
