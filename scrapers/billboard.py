from bs4 import BeautifulSoup
from slugify import slugify
from pprint import pprint
import csv

import requests
import datetime
import time

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# artist = slugify(artist)
# track = slugify(track)

def match_class(target):
  def do_match(tag):
      classes = tag.get('class', [])
      return all(c in classes for c in target)
  return do_match




ud = {
  'https://www.billboard.com/charts/rap-song/': 'Rap Songs',
  'https://www.billboard.com/charts/r-b-hip-hop-songs/': 'R&B and Hip Hop Songs'
}

# urls = ['https://www.billboard.com/charts/rap-song/', 'https://www.billboard.com/charts/r-b-hip-hop-songs/', 'https://www.billboard.com/charts/hot-100/']
# urls = ['https://www.billboard.com/charts/rap-song/', 'https://www.billboard.com/charts/r-b-hip-hop-songs/']
urls = ['https://www.billboard.com/charts/rap-song/']


def write_file(tracks, v):
  heads = tracks[0].keys()
  with open("outfile_rap_{0}.csv".format(v),'wb') as cfile:
    rd = csv.DictWriter(cfile, fieldnames=heads)
    rd.writeheader()
    for tf in tracks:
      rd.writerow(tf)






# aa
#
# # weeks = ['1993-03-11']
# # mdate = '1997-03-11'
# # v = '2'
# # today = datetime.datetime.strptime(mdate, "%Y-%m-%d")
#
# # weeks = ['1997-03-11']
# # mdate = '2001-03-11'
# # v = '3'
# # today = datetime.datetime.strptime(mdate, "%Y-%m-%d")
#
# # weeks = ['2001-03-11']
# # mdate = '2005-03-11'
# # v = '4'
# # today = datetime.datetime.strptime(mdate, "%Y-%m-%d")
#
# # weeks = ['2005-03-11']
# # mdate = '2009-03-11'
# # v = '5'
# # today = datetime.datetime.strptime(mdate, "%Y-%m-%d")
#
# # weeks = ['2009-03-11']
# # mdate = '2013-03-11'
# # v = '6'
# # today = datetime.datetime.strptime(mdate, "%Y-%m-%d")
#
# weeks = ['2013-03-11']
# v = '7'
# today = datetime.datetime.now()

def scrape_billboard(weeks, v, today):


  tracks = []

  cdate = weeks[0]

  # today = datetime.datetime.now()
  date_obj = datetime.datetime.strptime(cdate, "%Y-%m-%d")

  while date_obj < today:
    new_date = datetime.datetime.strptime(cdate, "%Y-%m-%d")
    date_obj = new_date + datetime.timedelta(days=7)
    pdate = datetime.datetime.strftime(date_obj, "%Y-%m-%d")
    weeks.append(pdate)
    cdate = pdate


  for week in weeks:
    print(week)
    tnames = []
    for core_url in urls:
      r = requests.get(core_url + week, headers=headers)
      if r.status_code == 200:

        data = r.text
        #
        # print(data)

        soup = BeautifulSoup(data)

        # count = 0
        # track_start = -1

        for article in soup.find_all('article'):

          track_name = article.find_all(match_class(["chart-row__song"]))
          if len(track_name) > 0:
            tr = str(track_name[0].contents[0])
            this_track = {
              'name': tr,
              'week': week,
              'chart': ud[core_url]
            }
            if this_track['name'] not in tnames:
              tnames.append(this_track['name'])
            tracks.append(this_track)

          artist_name = article.find_all(match_class(["chart-row__artist"]))
          if len(artist_name) > 0:
            ar = str(artist_name[0].contents[0]).replace("\n","")
            aty = ar.split("feat")[0].split("Feat")[0]
            this_track['artist'] = aty
          rank = article.find_all(match_class(["chart-row__current-week"]))
          if len(rank) > 0:
            ro = str(rank[0].contents[0])
            this_track['rank'] = ro
  write_file(tracks, v)



# weeks = ['1989-03-11']
# mdate = '1997-03-11'
# v = '1'
# today = datetime.datetime.strptime(mdate, "%Y-%m-%d")

# weeks = ['1997-03-11']
# mdate = '2005-03-11'
# v = '2'
# today = datetime.datetime.strptime(mdate, "%Y-%m-%d")

# weeks = ['2005-03-11']
# mdate = '2013-03-11'
# v = '3'
# today = datetime.datetime.strptime(mdate, "%Y-%m-%d")

weeks = ['2013-03-11']
v = '4'
today = datetime.datetime.now()
#


scrape_billboard(weeks, v, today)
