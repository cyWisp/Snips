#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    page = requests.get('http://cybersherpa.net')
    soup = BeautifulSoup(page.text, 'html.parser')

    print(soup.h1)