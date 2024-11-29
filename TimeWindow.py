import datetime as dt

import State
class TimeWindow:

    def __init__(self, rows, timestamp, timestep):
        self.index = 0
        self.rows = rows
        self.timestep = timestep
        self.data = []
        for i in range(self.rows):
            self.data.append(State.State(timestamp))
            timestamp = timestamp + timestep

    def get(self, row):
        return self.data[(self.index + row) % self.rows]
    
    def getRows(self):
        return self.rows
    
    def getTimestep(self):
        return self.timestep
    
    # row is relational, starting from index
    def put(self, row, value):
        self.data[(self.index+row)%self.rows] = value

    def move(self):
        self.data[self.index] = State.State(self.get(-1).timestamp + self.timestep)
        self.index = self.index + 1
        if self.index == self.rows :
            self.index = 0
            