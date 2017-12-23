import json
from pprint import pprint
import requests

nested_data = {}

def get_year_charts(year):
  url = 'http://127.0.0.1:8000/charts/year/' + year

  r = requests.get(url)
  pprint(r.text)

  a = json.loads(r.text)

  with open("{0}_charts.json".format(year),'wb') as jfile:
    json.dump(a, jfile)

def calc_scores(data):

  city_scores = {}
  for chart in data:
    city = chart['track']['artist']['city']
    artist = chart['track']['artist']['name']
    if city not in city_scores:
      city_scores[city] = {
        'count': 1,
        'score': (25- chart['position']),
        'artists': [artist]
      }
    else:
      city_scores[city]['count'] += 1
      city_scores[city]['score'] += (25- chart['position'])

      if artist not in city_scores[city]['artists']:
        city_scores[city]['artists'].append(artist)

  return city_scores

city_scores = {}
for year in xrange(1989,2018):
  yr = str(year)
  # get_year_charts(yr)
  with open("{0}_charts.json".format(yr),'rb') as jfile:
    data = json.load(jfile)
    pprint(data)

    city_scores[yr] = calc_scores(data)


with open("city_scores_by_year.json",'wb') as kfile:
    json.dump(city_scores, kfile)




    # pprint(city_scores)

    # week = chart['week']['date_id']
    # if week not in nested_data:
    #   nested_data[week] = {}
    # rank = chart['position']
    # if rank not in nested_data[week]:
    #   nested_data[week][rank] = {
    #     'artist': chart['track']['artist']['name'],
    #     'city': chart['track']['artist']['city'],
    #     'track': chart['track']['name']
    #   }




# with open("{0}_charts_transformed.json".format('1994'),'wb') as jofile:
#   json.dump(nested_data, jofile)
