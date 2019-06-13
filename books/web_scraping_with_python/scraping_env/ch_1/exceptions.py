#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    
    return title

if __name__ == '__main__':

    title = getTitle("http://cybsherpa.net")

    if title == None:
        print("Title could not be found")
    else:
        print(title)