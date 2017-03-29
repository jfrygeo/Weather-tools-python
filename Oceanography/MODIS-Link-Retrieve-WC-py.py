#-------------------------------------------------------------------------------
# Name:        MODIS-Link-Retrieve
# Purpose:     Retrieve latest NetCDF chlorophyll file from NASA MODIS - Different URLS than other script in this Repo
#
# Author:      JFry
#
# Created:     12/10/2015
# Edited:      11/30/2016
# Copyright:   (c) john6807 2016
# Licence:  Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
#-------------------------------------------------------------------------------

import datetime, time, sys, os

scriptPath = sys.path[0]

# local folder where wanting to download data
downloadfolder = sys.path[0] + "\\Scratch\\MODIS\\"

##Base Urls where data resides
baseurl = "http://coastwatch.pfeg.noaa.gov/erddap/files/"

sstmid = "erdMWsstd1day/"
chlmid = "erdMWchla1day/"

producturlChl = "_chla.nc"
producturlSST = "_sstd.nc"


#Calculate local time of yesterday - depending on where you are, the data may not yet be available for the current day
yesterdaytime = str(datetime.datetime.now()- datetime.timedelta(2))
print (yesterdaytime)

#Today's date
#todaytime = str(datetime.datetime.now())
#print (todaytime)

formattime = time.strftime('%Y%j',time.strptime(yesterdaytime,"%Y-%m-%d %H:%M:%S.%f"))
print (formattime)

##format string request
downloadlocationChl = str(os.path.join(downloadfolder) + "MW" + formattime + "_" + formattime + producturlChl)
downloadlocationSST = str(os.path.join(downloadfolder) + "MW" + formattime + "_" + formattime + producturlSST)

print ("Chlorophyll Location " + downloadlocationChl)
print ("SST Location " + downloadlocationSST)

#Format string request for Cholorphyll
dlMODISdataChl = str(baseurl + chlmid + "MW" + formattime + "_" + formattime +  producturlChl)
print ("Downloading Chl " + dlMODISdataChl)

#Format string request for Sea Surface Temperature
dlMODISdataSST= str(baseurl + sstmid + "MW" + formattime + "_" + formattime + producturlSST)

print ("Downloading SST " + dlMODISdataSST)

if sys.version_info[0]== 3:
    import urllib.request
    #What Python
    sysver = sys.version
    print (sysver)
    urllib.request.urlretrieve(dlMODISdataChl, downloadlocationChl)
    urllib.request.urlretrieve(dlMODISdataSST, downloadlocationSST)

    print ("Downloaded MODIS Data")

else:
    if sys.version_info[0]== 2:
        import urllib
        sysver = sys.version
        print (sysver)
        urllib.urlretrieve(dlMODISdataChl, downloadlocationChl)
        urllib.urlretrieve(dlMODISdataSST, downloadlocationSST)

        print ("Downloaded MODIS Data")


