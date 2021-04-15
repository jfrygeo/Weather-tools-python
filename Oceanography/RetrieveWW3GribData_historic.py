#-------------------------------------------------------------------------------
# Name:  Retrieve WW3 Model data - historic
# Purpose: Downloads a Grib file From NOAA NOMADS
# Author:      John Fry
#               DC Technology Office, Defense Team
# Created:     04.11.2019
# Copyright:   (c) john6807 2019
# Licence:     <your licence>
# Updated 1/25/15 for multi-grid changes in NOAA's website.
# Updated 1/28/15 found smaller dataset to link to
# Updated 4/11/2019 loop through historic data
#-------------------------------------------------------------------------------

#Modules


import  os , sys, requests, time, datetime, arcpy

# What Python?
sysver = sys.version


# Prepare folders
scriptPath = sys.path[0]
downloadfolder = "C:\Users\john6807\Box Sync\MyDocs\Customer\CNMOC\CRADA\Template4_RogueWaves\Provided_Data\Data\WW3"
#downloadfolder = str(os.path.join(scriptPath) + r"\scratch\WW3")


"https://data.nodc.noaa.gov/thredds/fileServer/ncep/nww3/2010/08/glo_30m/multi_1.glo_30m.hs.201008.grb2"

#Base Url where GRIB2 data resides
# Original URL urlNWW3 = "http://nomads.ncep.noaa.gov/pub/data/nccf/com/wave/prod/multi_1.20150128/nww3.t00z.grib.grib2"
# Going to Parse URL string to allow for the date to be inserted

urlNWW31 = "https://data.nodc.noaa.gov/thredds/fileServer/ncep/nww3/"
urlNWW32= "glo_30m/multi_1.glo_30m.hs."

#iterate year and month
ww3data = []
for dataset in ww3data:
    dlWW3data = str(downloadfolder + r"\nww3.t00z." + formatlocal + r".grib.grib2")
    outWW3 = open(dlWW3data, 'wb')

#dlWW3data = str(downloadfolder + r"\multi_2.glo_30m.t00z." +formatutc+ r".grib.grib2")
dlWW3data = str(downloadfolder + r"\nww3.t00z." +formatlocal+ r".grib.grib2")
outWW3 = open(dlWW3data, 'wb')

print ("Model Date (UTC)")
#print (formatutc)
print (formatlocal)

arcpy.AddMessage("Data Date")
#arcpy.AddMessage(formatutc)
arcpy.AddMessage(formatlocal)

#Combine Strings to form URL
#dlWW3 = str(urlNWW31 + formatutc + urlNWW32)

dlWW3 = str(urlNWW31 + formatlocal + urlNWW32)
print (dlWW3)
arcpy.AddMessage(dlWW3)

#urllib.request.urlretrieve(dlWW3,dlWW3data)

requests.get(dlWW3,dlWW3data)
arcpy.AddMessage("Retrieved Data from source")

