import csv
import json
import datetime

CSV_DELIMITER = ";"

class State:

    def __init__(self, timestamp):

        self.timestamp = timestamp
        # TODO: Initialize all state data
        self.bays = ['0'] * 10

        # etc. all the simulation parameters for time/timestamp

        # TODO: add your all fieldnames here for managing the writing to a csv file:
        self.fieldnames = ['timestamp', 'season', 'timeofday', 'weekday', 'bay1', 'bay2', 'bay3', 'bay4', 'bay5', 'bay6', 'bay7', 'bay8', 'bay9', 'bay10']
        # NOTE: these names have to match with self object attribute names

    def writeHeadingToCsvFile( self, filename ):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames, delimiter=CSV_DELIMITER)
            writer.writeheader()

    def writeLineToCsvFile( self, filename ):
        with open(filename, 'a', newline='') as csvfile:
            # TODO: write all the model attributes needed
            print(self.timestamp.isoformat(), file=csvfile, end=CSV_DELIMITER)
            print( self.getSeason(), file=csvfile, end=CSV_DELIMITER)
            print( self.getTimeOfDay(), file=csvfile, end=CSV_DELIMITER)
            print( self.getWeekday(), file=csvfile, end=CSV_DELIMITER)
            for bay in self.bays:
                print(bay, file=csvfile, end=CSV_DELIMITER)
            print("", file=csvfile, end='\n')

    def getSeason(self):
        if self.timestamp.month == 12 or self.timestamp.month == 1 or self.timestamp.month == 2:
            return 'winter'
        if self.timestamp.month == 3 or self.timestamp.month == 4 or self.timestamp.month == 5:
            return 'spring'
        if self.timestamp.month == 6 or self.timestamp.month == 7 or self.timestamp.month == 8:
            return 'summer'
        return 'autumn'

    def getTimeOfDay(self):
        hour = self.timestamp.hour
        if  hour < 6 or hour >= 22:
            return 'nighttime'
        else:
            return 'dayteime'
        
    def getWeekday(self):
        day = self.timestamp.weekday()
        return 'weekday' if day <= 5 else 'weekend'
