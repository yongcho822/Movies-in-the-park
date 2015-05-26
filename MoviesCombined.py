from collections import OrderedDict
od = OrderedDict()
import csv

with open("MovieDictFormatted.csv") as f, open("MoviesCombined.csv", "w") as out:
    r = csv.reader(f)
    wr = csv.DictWriter(out, fieldnames=next(r))
    for row in r:
        loc, mov, form, lat, long = row
        od.setdefault(loc, dict(Location=loc, Lat=lat, Lng=long, MovieDate=[], Formatted_Address=form))
        od[loc]["MovieDate"].append(mov)
    wr.writeheader()
    for loc, vals in od.items():
        od[loc]["MovieDate"]= " ".join(od[loc]["MovieDate"])
        wr.writerow(vals)