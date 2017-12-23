import csv
from pprint import pprint
import requests

artist_dict = {}

with open("artist_map.csv",'rb') as afile:
  rd = csv.DictReader(afile)
  for row in rd:
    artist_dict[row['Billboard Artist']] = row['map_artist']

# pprint(artist_dict)

citymap = {}

with open("US_Cities_Hip_Hop.csv",'rb') as dfile:
  rd = csv.DictReader(dfile)
  for row in rd:
    citymap[row['map_name']] = row['Name']


with open("Artist Locations.csv",'rb') as locfile:
  rd = csv.DictReader(locfile)
  for row in rd:
    tname = row['name']
    if tname in artist_dict:
      artist_name = artist_dict[tname]
      cname = row['city']
      if cname in citymap:
        city_name = citymap[cname]

        url = 'http://127.0.0.1:8000/artist/create/'

        ho = {
          'name': artist_name,
          'city': city_name
        }

        r = requests.post(url, json = ho)
        print(r.text)




