from pprint import pprint
import requests
import json

year = '2005'



def get_year_charts(year):
  url = 'http://127.0.0.1:8000/charts/year/' + year

  r = requests.get(url)
  pprint(r.text)

  a = json.loads(r.text)

  with open("{0}_charts.json".format(year),'wb') as jfile:
    json.dump(a, jfile)

get_year_charts(year)

