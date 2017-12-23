import csv
import requests

# with open("US_Cities_Hip_Hop.csv",'rb') as locfile:
#   rd = csv.DictReader(locfile)
#   for row in rd:
#     new_city = {
#       'name': row['Name'],
#       'tid': int(row['T_ID']),
#       'state': row['State'],
#       'latitude': row['Latitude'],
#       'longitude': row['Longitude']
#     }
#
#     url = 'http://127.0.0.1:8000/cities/'
#
#     r = requests.post(url, json = new_city)
#     print(r.status_code)
#     print(r.text)

url = 'http://127.0.0.1:8000/cities/'

r = requests.get(url)
print(r.status_code)
print(r.text)
