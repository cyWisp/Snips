#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':

    url = input('Url: ')
    html = urlopen(url).read()

    bs = BeautifulSoup(html, 'html.parser')
    print('h1: {0}\nh2: {1}\nh3:{2}'.format(bs.h1, bs.h2, bs.h3))