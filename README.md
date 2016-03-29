# openstreetmap-basemap-garmin
Create base maps for garmin devices using openstreetmap

## Requirements

  osmconvert: http://wiki.openstreetmap.org/wiki/Osmconvert

  mkgmap: http://www.mkgmap.org.uk/

  phyghtmap: http://wiki.openstreetmap.org/wiki/Phyghtmap
  
##Configuration

  Change OSMCONVERT_EXECUTABLE_PATH, MKGMAP_JAR_PATH, PHYGHTMAP_EXECUTABLE_PATH 
  
##Usage 

Get coordinates from openstreetmap

  http://www.openstreetmap.org/export


 |  |  |
------------ | ------------- | ------------- | -------------
 | maxlat |  |
minlon |  | maxlon |
 | minlat |  |


 
Arguments should be 
  **mapname minlon minlat maxlon maxlat**
