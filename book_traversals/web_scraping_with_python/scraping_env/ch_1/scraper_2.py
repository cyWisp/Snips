#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':

    address = input('Url: ')
    html = urlopen(address)

    text = html.read()

    #reading the url into a beautifulSoup object
    bsObj = BeautifulSoup(text, 'html.parser') #<--- using html.read()
    print(bsObj.h1)