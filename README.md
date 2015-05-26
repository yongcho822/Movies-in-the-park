# Movies-in-the-park
Webscraping Thrillist's Moves in the Park article to compile a CSV file to input for geocoding.


Order of execution:

1. MoviesInThePark.py - script to parse URL with BeautifulSoup and return TSV File

2. GeocodeScript.py - script to geocode TSV File using GoogleMaps API

3. MovieDictFormatted.py - script to delete columns (can only fit 2 in Mapbox marker info window), combine Movies and Date columns after reformatting the Date column, and delimit by commas instead of tabs to create a CSV file.

4. MoviesCombined.py - script to group by Location column so that all movies with the same Location are combined.

5.  TSV to GeoJSON.py - script to convert TSV file into GeoJSON format.
