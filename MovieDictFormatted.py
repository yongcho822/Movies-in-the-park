
# coding: utf-8

# In[22]:

import csv

with open("MovieParksGeocodeTest.tsv", "rU") as f:
    reader = csv.DictReader(f, delimiter = "\t")
    
    with open("MovieDictFormatted.csv", "w") as w:
        fields = ['Location', 'MovieDate', 'Formatted_Address', 'Lat', 'Lng']
        writer = csv.DictWriter(w, fieldnames = fields, delimiter = ",")
        writer.writeheader()
        
        for line in reader:
            datesplit = line["Date"].split("-")
            line["Date"] = "-".join((datesplit[1], datesplit[0]))
            line['MovieDate'] = line["Date"] + " " + line["Movie Title"]
            if 'Movie Title' in line: del line['Movie Title']
            if 'Date' in line: del line['Date']
            if 'Amenities' in line: del line['Amenities']

            writer.writerow(line)

