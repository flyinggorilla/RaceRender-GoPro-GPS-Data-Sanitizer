import csv
import math
from datetime import datetime, timedelta

MAX_SPEED = 10.0 ## 15.433 m/s = 30kts
MAX_DISTANCE = 0.000010
SKIP_SECONDS = 60 ## skip seconds at the beginning with bogus coordinates

MIN_LATITUDE = 47.82
MAX_LATITUDE = 47.96 
MIN_LONGITUDE = 13.5 
MAX_LONGITUDE = 13.6 

csvtargetfile = open('target.csv', 'w', newline='')

with open('source.csv', newline='') as csvsourcefile:
    gpsdatareader = csv.reader(csvsourcefile)
    line = 0
    errors = 0

    prevlatitude = None
    prevlongitude = None
    prevaltitude = None
    prevspeed = None

    starttime = None

    for row in gpsdatareader:
        line += 1
        if (len(row) < 5):
            continue

        time = row[0]

        if (time == "Time"):
            print("Header row found")
            writer = csv.writer(csvtargetfile)
            writer.writerow(row)
            continue

        try:
            time = datetime.fromtimestamp(float(time))
            latitude = float(row[1])
            longitude = float(row[2])
            altitude = float(row[3])
            speed = float(row[4])

            if (starttime == None):
                starttime = time
                print("starttime: {}".format(starttime))
            else:
                #print(abs(starttime - time))
                if abs(starttime - time) < timedelta(seconds=SKIP_SECONDS):
                    #print("Skipping row at beginning")
                    continue

                #if abs(starttime - time) > timedelta(minutes=55, seconds=2):
                #    print("****************** {}: {} abs({:.8f})".format(line, row, distance))
                #    quit()
                    


            if (latitude < MIN_LATITUDE or latitude > MAX_LATITUDE or longitude < MIN_LONGITUDE or longitude > MAX_LONGITUDE or speed > MAX_SPEED or speed < 0.0):
                print("Outside Attersee or speed to high {}: {}".format(line, row))
                errors += 1
                prevlatitude = None
                continue

            if (prevaltitude != None):
                distance = math.sqrt((prevlatitude - latitude)**2 + (prevlongitude - longitude)**2)
                if (distance > MAX_DISTANCE):
                    print("What a jump! {}: {} abs({:.8f})".format(line, row, distance))
                    errors += 1
                    prevlatitude = None
                    continue

            writer.writerow(row)

        finally:
            prevlatitude = latitude
            prevlongitude = longitude
            prevaltitude = altitude
            prevspeed = speed


    print("Errors found: {}".format(errors))

