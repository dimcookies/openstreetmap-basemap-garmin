import urllib2
import subprocess
import os 
from sys import argv, exit
import glob

OSMCONVERT_EXECUTABLE_PATH="../osmconvert"
MKGMAP_JAR_PATH="../mkgmap-r3336/mkgmap.jar"
PHYGHTMAP_EXECUTABLE_PATH="phyghtmap"

def saveWebServiceResponse(url, filename):
	response = urllib2.urlopen(url)
	content = response.read()
	with open(filename,"w") as f:
		f.write(content)

if len(argv) != 6:
	print "mapname 21.4050 39.4764 21.5681 39.5529"
	exit(-1)

mapname = argv[1]
assert float(argv[2]) < float(argv[4])
assert float(argv[3]) < float(argv[5])
coords = ",".join(argv[2:])


print "Downloading contour"
process = subprocess.Popen([PHYGHTMAP_EXECUTABLE_PATH, "-a", coords.replace(",",":"), "-o","cont"], stdout=subprocess.PIPE)
out, err = process.communicate()
contour_file = glob.glob("cont*.osm")[0]
print "Downloading places"
saveWebServiceResponse("http://overpass.osm.rambler.ru/cgi/xapi_meta?node[place=*][bbox=%s]" % (coords), "node.osm")
print "Downloading roads"
saveWebServiceResponse("http://overpass.osm.rambler.ru/cgi/xapi_meta?way[highway=*][bbox=%s]" % (coords), "way.osm")
print "Download compelete"

process = subprocess.Popen([OSMCONVERT_EXECUTABLE_PATH, "node.osm", "way.osm",contour_file], stdout=subprocess.PIPE)
out, err = process.communicate()
with open("mymap.osm","w") as f:
	f.write(out)

os.system("""java -jar %s --description="%s" --family-id=9999 --gmapsupp mymap.osm""" % (MKGMAP_JAR_PATH, mapname))

os.rename("gmapsupp.img", "gmapbmap.img")

os.remove("node.osm")
os.remove("way.osm")
os.remove("mymap.osm")
os.remove(contour_file)



     					
