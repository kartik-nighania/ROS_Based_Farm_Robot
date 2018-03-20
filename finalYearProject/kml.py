import csv
import simplekml


inputfile = csv.reader(open('coor.csv','r'))
kml=simplekml.Kml()

for row in inputfile:
  kml.newpoint(coords=[(row[0],row[1])])

kml.save('coordinates.kml')

