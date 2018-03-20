from qgis.core import *
from qgis.analysis import *
import qgis.utils
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os
import sys

CUR_DIR = os.getcwd()
print CUR_DIR
app = QgsApplication([],True, None)
# app.setPrefixPath("/usr/bin/qgis", True)

print 'init'
app.initQgis()
print 'init done'

# create a reference to the QgsApplication, setting the
# second argument to False disables the GUI


# Write your code here to load some layers, use processing algorithms, etc.

# When your script is complete, call exitQgis() to remove the provider and
# layer registries from memory
def calculate():
    
    file_name =  CUR_DIR + "/output/odm_orthophoto/odm_orthophoto.tif"
    out_file = CUR_DIR + "/sample_output.jpg"
    out_file_ndvi = CUR_DIR + "/out_ndvi.jpg"
    try:
        
        file_info = QFileInfo(file_name)

        rasterName = file_info.baseName()
        print 'file_info',rasterName
        raster = QgsRasterLayer(file_name , rasterName)

        print raster

        if not raster.isValid(): print 'Invalid raster'

        ir = QgsRasterCalculatorEntry()
        r = QgsRasterCalculatorEntry()

        print ir, r

        ir.raster = raster
        r.raster = raster

        ir.bandNumber = 4
        r.bandNumber = 3

        ir.ref = rasterName + "@4"
        r.ref = rasterName + "@3"

        references = (ir.ref, r.ref, ir.ref, r.ref)
        exp = "1.0 * (%s - %s) / (%s + %s)" % references
        print exp
        #print 'here2'

        output = out_file

        e = raster.extent()
        w = raster.width()
        h = raster.height()
        # w = 250
        # h = 250
        entries = [ir,r]

        ndvi = QgsRasterCalculator(exp, output, "GTiff", e, w, h,
        entries)

        ndvi_res = ndvi.processCalculation()
        print ndvi_res
        print 'Completed NDVI analysis!'
        

    except Exception as e:
        print 'Exception: ', e


calculate()
app.exitQgis()
