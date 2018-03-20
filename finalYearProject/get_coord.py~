from osgeo import gdal,osr

def getImageBounds(imgPath):
	source_path = imgPath
	src = gdal.Open('/home/rahulgunkar/Precision_farming-master/app/odm_orthophoto.tif')
	ulx, xres, xskew, uly, yskew, yres  = src.GetGeoTransform()
	lrx = ulx + (src.RasterXSize * xres)
	lry = uly + (src.RasterYSize * yres)
	cx = (lrx+ulx)/2
	cy = (lry+uly)/2
	

	# Setup the source projection - you can also import from epsg, proj4...
	source = osr.SpatialReference()
	source.ImportFromWkt(src.GetProjection())

	# The target projection
	target = osr.SpatialReference()
	target.ImportFromEPSG(4326)

	# Create the transform - this can be used repeatedly
	transform = osr.CoordinateTransformation(source, target)

	# Transform the point. You can also create an ogr geometry and use the more generic `point.Transform()`
	p1 = [ulx,lry]
	p2 = [lrx,uly]
	p = [p1,p2]
	center = transform.TransformPoint(cx,cy)
	bounds = transform.TransformPoints(p)
	return bounds,center

print getImageBounds('imgPath')
#print col_list[0][0][0]
#print col_list[0][0][1]
