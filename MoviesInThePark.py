#Only thing is having to manually remove the out of format HTML Editor's note on Aug 19th Dreamgirls. Typical Dreamgirls.

import csv
from bs4 import BeautifulSoup
from urllib2 import urlopen

URL = 'http://www.thrillist.com/entertainment/chicago/free-outdoor-summer-movies-chicago'

html = urlopen(URL).read()
soup = BeautifulSoup(html, "lxml")

with open("MovieParks.tsv", "w") as f:
    categories = ['Location', 'Movie Title', 'Date', 'Amenities']
    writer = csv.DictWriter(f, delimiter = '\t', fieldnames = categories)
    writer.writeheader()

    root = soup.find_all("strong")
    for row in root:
        master_dict = {'Location':"", 'Movie Title':"", 'Date':"", 'Amenities':None}
        Date = row.text.encode('utf-8')
        master_dict['Date'] = Date
        for sibling in list(row.next_siblings)[:-1]:
            if sibling.name == "strong":                
                break
            if sibling.name == "em":
                MovieTitle = sibling.text.encode('utf-8')
                master_dict['Movie Title'] = MovieTitle
                for sibling2 in sibling.next_siblings:
                    if sibling2.name == "strong" or sibling2.name == "em":
                        break
                    if 'Location:' in sibling2:     
                        Location = sibling2.replace("Location: ","") + ", Chicago "
                        master_dict['Location'] = Location.encode('utf-8')
                    if 'Amenities:' in sibling2:
                        Amenities = sibling2.replace("Amenities: ","")
                        master_dict['Amenities'] = Amenities.encode('utf-8')
                writer.writerow(master_dict)
                master_dict = {}
                master_dict['Date'] = Date   
print 'Done here'