import datetime
name = "US058GMET-GR1mdl.0058_0240_02400F0RL1998073100_0007_008500-000000air_temp"


    #Parse input filename into interger components to formulate date run
def getDate(name):
    year = int(name[36:40])
    month = int(name[40:42])
    day = int(name[42:44])
    hour = int(name[44:46])

    #Parse the Tau value of the filename
    tau_hours = int(name[27:30])
    tau_minutes = int(name[30:32])

    #Format the date of the model run by adding Tau
    thedate =datetime.datetime(year,month,day,hour,0,0,0)
    print ("the date of the model run is :", thedate)
    print ("the tau hours is:", tau_hours)
    print ("the tau minutes:",tau_minutes)

    forecast_valid_time = thedate + datetime.timedelta(hours=tau_hours,minutes=tau_minutes)

    print ("the valid forecast time is:"+ str(forecast_valid_time))
    return forecast_valid_time
getDate(name)


