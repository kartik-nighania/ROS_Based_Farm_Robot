import shapefile
import get_coord
w = shapefile.Writer(shapefile.POINT) 
w.point(float(bounds[0][1]), float(bounds[0][0])) 
w.save('shapefiles/test/point')