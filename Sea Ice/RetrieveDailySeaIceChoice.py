#-------------------------------------------------------------------------------
# Name:  Extract Kml to Feature Class
# Purpose: Polls a website for a kmz file and converts that to a layer
# In this example, we are getting ice data from a kml from the National Ice Center
# Use the retrieved kml to further GIS analyses.

# Author:      John Fry
#              Esri Defense Team
# Created:     03/01/2014
# Copyright:   (c) john6807 2014
# Licence:     <your licence>
# Updated 2/17/15 for providing choice to work with Python 2.7 and 3.4
#-------------------------------------------------------------------------------

#Modules
import  os , sys, arcpy

# Prepare Environment
arcpy.env.overwriteOutput = True
arcpy.env.addOutputsToMap = False

# Prepare folders
scriptPath = sys.path[0]
downloadfolder = str(os.path.join(scriptPath) + r"\scratch\NIC")
dlAntarctic = str(downloadfolder + r"\DailyAntarcticIce.kmz")
dlArctic = str(downloadfolder + r"\DailyArcticIce.kmz")
filegdb = "Scratch.gdb"

outAntarctic = open(dlAntarctic, 'wb')
outArctic = open(dlArctic,'wb')

#Determining if using Python 2.7 or Python 3.4

if sys.version_info[0]== 3:
    import urllib.request

    # What Python?
    sysver = sys.version
    arcpy.AddMessage(sysver)

    # Url where KML/KMZ resides
    urlAntarctic = urllib.request.urlretrieve("http://www.natice.noaa.gov/pub/special/google_kml/antarctic.kmz",dlAntarctic)
    urlArctic = urllib.request.urlretrieve("http://www.natice.noaa.gov/pub/special/google_kml/arctic.kmz",dlArctic)
    arcpy.AddMessage("Retrieving Data from source")


else:
    if sys.version_info[0]== 2:
        import urllib

        # What Python?
        sysver = sys.version
        arcpy.AddMessage(sysver)
        print (sysver)

        # Url where KML/KMZ resides
        urllib.urlretrieve("http://www.natice.noaa.gov/pub/special/google_kml/antarctic.kmz", dlAntarctic)
        urllib.urlretrieve("http://www.natice.noaa.gov/pub/special/google_kml/arctic.kmz", dlArctic)
        print("Retrieving Data from source")
        arcpy.AddMessage("Retrieving Data from source")



# Convert from kmz/kml to feature layer
outantacrticfc = arcpy.KMLToLayer_conversion(dlAntarctic,downloadfolder)
outacrticfc = arcpy.KMLToLayer_conversion(dlArctic,downloadfolder)

##If you want to run this script in an ArcGIS Desktop model, uncomment these two lines and define two
## output parameters in the script. The outputs will be feature class.

#arcpy.SetParameter(0,outantacrticfc)
#arcpy.SetParameter(1,outacrticfc)


outAntarctic.close()
outArctic.close()

arcpy.AddMessage("Retrieved Ice Data")



