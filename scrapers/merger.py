from bs4 import BeautifulSoup
from slugify import slugify
from pprint import pprint
import re
import csv

import requests


with open("/Users/kevindenny/Documents/hiphopdb-map/scrapers/location_file_1.csv",'rb') as lfile:
  rf = csv.DictReader(lfile)
  for row in rf:
    pprint(rf)
