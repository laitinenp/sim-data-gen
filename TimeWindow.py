import datetime as dt

import State
class TimeWindow:

    def __init__(self, rows, timestamp, timestep):
        self.index = 0
        self.rows = rows
        self.timestep = timestep
        self.timestamp = timestamp
        self.data = [State.State(timestamp) for i in range(rows)]

    def get(self, row):
        return self.data[row]
    
    def getRows(self):
        return self.rows
    
    # row is relational, starting from index
    def put(self, row, value):
        self.data[(self.index+row)%self.rows] = value

    def move(self):
        self.data[self.index] = State.State(self.timestamp + self.timestep)
        self.timestamp = self.timestamp + self.timestep
        self.index = self.index + 1
        if self.index == self.rows :
            self.index = 0
            