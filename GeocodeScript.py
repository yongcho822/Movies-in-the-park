
# coding: utf-8

# In[8]:

#LETS GEOCODE THIS SHIIIIIIT
from urllib2 import urlopen
import csv
import json
from time import sleep

def geocode(address):
    url = ("http://maps.googleapis.com/maps/api/geocode/json?"
        "sensor=false&address={0}".format(address.strip().replace(" ", "+")))
    #print url
    return json.loads(urlopen(url).read())

with open("MovieParksFixed.tsv", "rU") as f:
    reader = csv.DictReader(f, delimiter = "\t")
    
    with open("MovieParksGeocode2.tsv","w") as w:
        fields = ['Location', 'Movie Title', 'Date', 'Amenities', 'Formatted_Address', 'Lat', 'Lng']
        writer = csv.DictWriter(w, fieldnames = fields, delimiter = "\t")
        writer.writeheader()
        
        for line in reader:
            print "Geocoding: {0}".format(line['Location'])
            response = geocode(line['Location'])
            print "got response"
            if "OK" in response['status']:
                #print "response ok"
                results = response.get("results")[0]
                line['Formatted_Address'] = results["formatted_address"]
                line['Lat'] = results["geometry"]["location"]["lat"]
                line['Lng'] = results["geometry"]["location"]["lng"]
            else:
                #print "not ok"
                line['Formatted_Address'] = ""
                line['Lat'] = ""
                line['Lng'] = ""
            sleep(1)
            writer.writerow(line)
print "Done here."


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



