
# coding: utf-8

# In[22]:

#Converting TSV File into GeoJSON Format

import json
import csv

def create_map(datafile):
    geo_map = {"type":"FeatureCollection"}
    item_list = []
    with open(datafile, 'r') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter = '\t')
        
        for i, line in enumerate(reader):
            data = {}
            data['type'] = 'Feature'
            data['id'] = i
            data['properties']={'name': line['Location'],
                                'title': line['Movie Title'],
                                'date': line['Date'],
                               'description': line['Amenities']}
            data['geometry'] = {'type':'Point',
                                'coordinates':(float(line['Lng']),float(line['Lat']))}
            item_list.append(data)

        for point in item_list:
            geo_map.setdefault('features', []).append(point)

        with open("thedamngeojson.geojson", 'w') as f:
            f.write(json.dumps(geo_map,encoding="ISO-8859-1"))
            
create_map('MovieParksGeocodeTest.tsv')

print "We\'re done here."


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

<div class='googft-info-window'>
<b>Location:</b> {Location}<br>
<b>Movie Title:</b> {Movie Title}<br>
<b>Date:</b> {Date}<br>
<b>Amenities:</b> {Amenities}
</div>


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



