import csv
from pprint import pprint
import requests
import json

artist_dict = {}

with open("artist_map.csv",'rb') as afile:
  rd = csv.DictReader(afile)
  for row in rd:
    artist_dict[row['Billboard Artist']] = row['map_artist']

missing = []

with open("sources/outfile_rap_4.csv",'rb') as sfile:
  rd = csv.DictReader(sfile)
  for row in rd:
    if row['artist'].strip() in artist_dict:
      artist_name = artist_dict[row['artist'].strip()]

      url = 'http://127.0.0.1:8000/artist/get/'

      ho = {
        'artist': artist_name
      }

      r = requests.post(url, json = ho)
      # print(r.text)
      mo = json.loads(r.text)
      if 'data' in mo:
        missing.append(mo['artist'])
      else:
        hd = {
          'artist': artist_name,
          'name': row['name']
        }

        url2 = 'http://127.0.0.1:8000/track/find/'
        r2 = requests.post(url2, json = hd)
        rf = json.loads(r2.text)
        track_id = rf['id']

        weeko = {
          'week': row['week']
        }

        url3 = 'http://127.0.0.1:8000/week/'
        r3 = requests.post(url3, json = weeko)

        charto = {
          'week': row['week'],
          'rank': row['rank'],
          'track': track_id
        }

        url4 = 'http://127.0.0.1:8000/chart/'
        r4 = requests.post(url4, json = charto)




# pprint(missing)
#
# with open("sources/missing_artists.csv",'wb') as mfile:
#   rd = csv.writer(mfile)
#   for r in missing:
#     rd.writerow([r])

