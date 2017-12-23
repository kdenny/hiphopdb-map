from bs4 import BeautifulSoup
from slugify import slugify
from pprint import pprint
import re
import csv

import requests

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

def match_class(target):
  def do_match(tag):
      classes = tag.get('class', [])
      return all(c in classes for c in target)
  return do_match

results = []


# artists = ['A tribe called quest']

def write_file(tracks, heads, v):
  with open("location_file_map_{0}.csv",'wb') as cfile:
    rd = csv.DictWriter(cfile, fieldnames=heads)
    rd.writeheader()
    for tf in tracks:
      tj = {}
      tl = {}
      for i in tf:
        tj[i] = tf[i].encode('utf-8')
        # tl[i] = tf[i].encode('ascii', 'ignore').decode('ascii')

      rd.writerow(tj)

def get_results(artists):

  for artist in artists:
    artist_name = artist.replace(" ","_")

    url = 'https://en.wikipedia.org/wiki/' + artist_name

    r = requests.get(url, headers=headers)
    print(r.status_code)

    ct = 'infobox'

    if r.status_code == 200:

        data = r.text
        #
        # print(data)

        soup = BeautifulSoup(data)

        # count = 0
        # track_start = -1

        if len(soup.find_all(match_class([ct]))) > 0:
          a = soup.find_all(match_class([ct]))[0]

          words = ['birthplace', 'deathplace']
          grows = ['Residence', 'Home', 'Origin', 'Born', 'Home&nbsp;town']
          mrows = ['Years active']

          ao = {'name': artist, 'url': url}

          for w in words:

            i = a.find_all(match_class([w]))
            if len(i) > 0:
              iy = i[0]
              if len(iy.find_all('a')) > 0:
                link = iy.find_all('a')[0].contents[0]

                ao[w] = link

          for r in grows:

            t = '^{0}$'.format(r)
            locs = a.findAll(text=re.compile(t))
            if len(locs) > 0:
              for l in locs:
                larger = l.parent.parent
                # print(larger)
                if len(larger.find_all('a')) > 0:
                  this_loc = larger.find('a').contents[0]
                  ao[l] = this_loc


          results.append(ao)
        else:
          ao = {'name': artist}
          ao['origin'] = 'N/A'
          results.append(ao)
    else:
          ao = {'name': artist}
          ao['origin'] = 'N/A'
          results.append(ao)


  return results


# test_artists = ['A tribe called quest', '2Pac', 'Notorious B.I.G.', 'Jay Z', 'Kanye West', 'Kid Cudi', 'Travis Scott']

real_artists = []

anames = []
# for b in xrange(6,8):


with open('artist_map.csv','rb') as cfile:
  reader = csv.DictReader(cfile)
  for row in reader:
    if row['map_artist'] not in anames:
      anames.append(row['map_artist'])
    real_artists.append(row)

  # wf = get_results(real_artists)
  wf = get_results(anames)

  # pprint(wf)
  gkeys = []
  for f in wf:
    for g in f:
      if g not in gkeys:
        gkeys.append(g)

  write_file(wf, gkeys, 1)




