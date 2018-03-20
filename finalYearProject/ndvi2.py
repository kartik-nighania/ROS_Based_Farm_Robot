# script to merge several individual Tiffs (bands) into one multiband GeoTiff
# and potentially do calculations like NDVI, albedo, etc...
# from: http://archive.publiclaboratory.org/peru/2011-01-18-lima-peru-morflex/misc/NDVI.py

# import the GDAL and numpy libraries
from osgeo import gdal
from numpy import *

# ***************************************************************
# ok lets load in the first 4 bands of Landsat imagery into their own numpy arrays
# the numpy arrays are named band1, band2, etc.
# I'm using the Boulder images that I provided you, but -
# alternatively you could change these file names to be Landast imagery that you downloaded

g = gdal.Open("pf.jpg") # blue band
band1 = g.ReadAsArray()
g = gdal.Open("pf.jpg") # green band
band2 = g.ReadAsArray()
g = gdal.Open("pf.jpg") # red band
band3 = g.ReadAsArray()
g = gdal.Open("pf.jpg") # near infrared band
band4 = g.ReadAsArray()

# ****************************************************************

# Lets do an NDVI calc
# NDVI = (nearInfrared - Red) / (nearInfrared + Red)

band4 = array(band4, dtype = float)  # change the array data type from integer to float to allow decimals
band3 = array(band3, dtype = float)

var1 = subtract(band4, band3) 
var2 = add(band4, band3)

ndvi = divide(var1,var2)

# ****************************************************************

# these variables will get information about the input Tiff so we can
# write out our new Tiff into the correct geographic space and with correct row/column dimensions

geo = g.GetGeoTransform()  # get the datum
proj = g.GetProjection()   # get the projection
shape = band1.shape        # get the image dimensions - format (row, col)

# ****************************************************************

# here we write out the new image, only one band to write out in this case

driver = gdal.GetDriverByName('GTiff')
dst_ds = driver.Create( "ndvi.tif", shape[1], shape[0], 1, gdal.GDT_Float32)
                                                         # here we set the variable dst_ds with 
                                                         # destination filename, number of columns and rows
                                                         # 1 is the number of bands we will write out
                                                         # gdal.GDT_Float32 is the data type - decimals
dst_ds.SetGeoTransform( geo ) # set the datum
dst_ds.SetProjection( proj )  # set the projection


dst_ds.GetRasterBand(1).WriteArray( ndvi)  # write numpy array band1 as the first band of the multiTiff - this is the blue band
stat = dst_ds.GetRasterBand(1).GetStatistics(1,1)  # get the band statistics (min, max, mean, standard deviation)
dst_ds.GetRasterBand(1).SetStatistics(stat[0], stat[1], stat[2], stat[3]) # set the stats we just got to the band
