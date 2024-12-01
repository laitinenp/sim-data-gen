import csv
import json
import datetime

class State:

    def __init__(self, timestamp):

        self.timestamp = timestamp
        # TODO: Initialize all state data
        self.bays = ['0'] * 10

        # etc. all the simulation parameters for time/timestamp

        # TODO: add your all fieldnames here for managing the writing to a csv file:
        self.fieldnames = ['timestamp', 'bay1', 'bay2', 'bay3', 'bay4', 'bay5', 'bay6', 'bay7', 'bay8', 'bay9', 'bay10']
        # NOTE: these names have to match with self object attribute names

    def writeHeadingToCsvFile( self, filename ):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()

    def writeLineToCsvFile( self, filename ):
        with open(filename, 'a', newline='') as csvfile:
            # TODO: write all the model attributes needed
            print(self.timestamp.isoformat(), file=csvfile, end=', ')
            for bay in self.bays:
                print(bay, file=csvfile, end=', ')
            print("", file=csvfile, end='\n')

