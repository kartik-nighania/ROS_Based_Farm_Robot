import os
from flask import Flask,render_template,redirect, url_for, Response
import get_coord
app = Flask(__name__)



@app.route('/home')
def home():
	
	return render_template('homepage.html')

@app.route('/unzip')
def unzip():
	
	os.system("unzip $(pwd)/img -d $(pwd)/images/")
	
	return render_template('unzip.html')

@app.route('/stitch')
def stitch():
	os.system("docker run -it --rm -v $(pwd)/images/img:/code/images -v $(pwd)/output/odm_orthophoto:/code/odm_orthophoto -v $(pwd)/output/odm_texturing:/code/odm_texturing opendronemap/opendronemap")
	return render_template('stitch.html')

@app.route('/ndvi')
def ndvi():
	os.system("python ndvi.py")
	return render_template('ndvi.html')

@app.route('/coor')
def coor():
	os.system("python get_coord.py")
	return render_template('coor.html')

@app.route('/kml')
def kml():
	os.system("python kml.py")
	return render_template('kml.html')

@app.route('/shp')
def shp():
	os.system("python shp.py")
	return render_template('shp.html')




@app.route('/overlap')
def overlap():

    A, B = get_coord.getImageBounds('/app/output/odm_orthophoto.png'.format())
    print "A is",A
    print "\n\n"
    (xce, yce,zce) = A[0]
    (xlo,yla,z),(dlo,ela,f) = B  

    return render_template('ovelap2.html', xce=xce,yce=yce, xlo=xlo, yla=yla, dlo=dlo, ela=ela)

app.run(debug=True, threaded=True)
