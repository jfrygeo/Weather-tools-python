# Retrieve Sea Ice Data
Retrieves a daily ice coverage kml from the National Ice Center. Use this layer to run geospatial analyses with ArcGIS desktop (ArcMap or ArcGISPro).

**This script does the following:**
- Downloads Arctic ice coverage and marginal ice zone kml from http://www.natice.noaa.gov/pub/special/google_kml/arctic.kmz
- Downloads Antarctic ice coverage and marginal ice zone kml from http://www.natice.noaa.gov/pub/special/google_kml/antarctic.kmz
- Uses Arcpy KMLToLayer_conversion tool to convert from kml to Esri Feature Class in a Geodatabase

Use this with ArcMap or ArcGIS Pro as a script to obtain data. Script will work with Python 2.7 or Python 3.4

![Ice Layer](https://ago-item-storage.s3.amazonaws.com/c4b423e843d24e139739f429d5f2fcb3/ArcticICE.PNG?AWSAccessKeyId=AKIAJS2Y2E72HYCOE7BA&Expires=1424388102&Signature=VUmdMjO0bjhJILDN%2FGx5H7%2F9E7A%3D "Ice Layer")
