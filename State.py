import csv
import json
import datetime

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
class State:

    def __init__(self, timestamp):

        self.timestamp = timestamp
        # Initialize all state data
        self.consumption = 0
        # etc. all the parameters

        # TODO: add your all fieldnames here for managing the writing to a csv file:
        self.fieldnames = ['timestamp', 'consumption']
        # NOTE: these names have to match with self object attribute names

    def writeHeadingToCsvFile( self, filename ):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()

    def writeLineToCsvFile( self, filename ):
        with open(filename, 'a', newline='') as csvfile:
            # TODO: solve how to print object's different field types, dates, etc.
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames, extrasaction='ignore')
            writer.writerow(self.__dict__)
