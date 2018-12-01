#!/usr/bin/env python
#Foundatinos of Python Network Programming - Chapter 1 - search.py

from googlemaps import GoogleMaps

address = '11324 SW 132 PL, Miami, FL'
print GoogleMaps().address_to_latlng(address)
