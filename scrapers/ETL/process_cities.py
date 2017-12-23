import csv


cdict = {}
cities = []



with open("Artist Locations.csv",'rb') as locfile:
  rd = csv.DictReader(locfile)
  for row in rd:
    cname = row['city']
    if cname not in cdict:
      cdict[cname] = {}
      cdict[cname]['id'] = len(cdict)
      cdict[cname]['name'] = cname
      cdict[cname]['t_artist_count'] = 1
    else:
      cdict[cname]['t_artist_count'] += 1


for m in cdict:
  cities.append(cdict[m])

with open("city_list.csv",'wb') as ofile:
  w = csv.DictWriter(ofile, fieldnames=['id', 'name', 't_artist_count'])
  for ct in cities:
    w.writerow(ct)
