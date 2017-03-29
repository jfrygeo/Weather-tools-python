# MODIS-Link-Retrieve-py
This script allows a user to automatically download MODIS satellite from NOAA data to a local machine. The script could be run automatically via Windows Task Scheduler. One could download MODIS netCDF data daily and use it in a GIS, such as ArcGIS.

## MODIS
Moderate Resolution Imaging Spectroradiometer (MODIS) is an instrument aboard the Terra and Aqua satellites and acquires imagery in 36 spectral bands for analysis in global dynamics. For more information, please visit [NASA MODIS](https://modis.gsfc.nasa.gov/about/).

## Script
The script links to two data sources - 1.Sea Surface Temperature 2. Chlorophyll. These data can be combined to run analysis such as fish suitability. 

There are two scripts in this repo. One downloads data from:

<b> Data Access </b> http://oceandata.sci.gsfc.nasa.gov/MODIS-Aqua/Mapped

The other script downloads from:

<b> Data Access </b> http://coastwatch.pfeg.noaa.gov/erddap/files/
