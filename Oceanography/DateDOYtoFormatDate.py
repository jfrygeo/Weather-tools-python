#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: Convert a string with Day of year to date "%m/%d/%Y %H:%M:%S"
#
# Author:      john6807
#
# Created:     12/10/2015
# Copyright:   (c) john6807 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import datetime, time
Name = "A20150702015090.L3m_MO_CHL_chlor_a_4km.nc:chlor_a"
print Name[1:8]

#newtime(Name)
def newtime(Name):
  ydoy = Name[1:8]
  formattime = time.strftime("%m/%d/%Y %H:%M:%S",time.strptime(ydoy,"%Y%j"))
  print (formattime)
newtime(Name)
