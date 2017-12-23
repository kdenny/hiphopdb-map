from bs4 import BeautifulSoup
from slugify import slugify
from pprint import pprint
import re
import csv

import requests

def get_all_artists():

  anames = []

  for b in xrange(1,5):

    with open('outfile_rap_{0}.csv'.format(str(b)),'rb') as cfile:
        reader = csv.DictReader(cfile)
        for row in reader:
          if row['artist'].strip() not in anames:
            anames.append(row['artist'].strip())

  return anames


def write_artists(anames):
  with open('artist_map.csv','wb') as cfile:
        wr = csv.writer(cfile)
        wr.writerow(['Billboard Artist'])
        for row in anames:
          wr.writerow([row])


artists = get_all_artists()
write_artists(artists)
