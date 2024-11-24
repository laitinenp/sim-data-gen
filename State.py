import csv

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
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames, extrasaction='ignore')
            print(self.__dict__)
            print(type(self.__dict__))
            writer.writerow(self.__dict__)
