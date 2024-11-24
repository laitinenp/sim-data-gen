import json

class TimeWindow:

    def __init__(self, rows, cols):
        self.index = 0
        self.rows = rows
        self.cols = cols
        self.data = [[0]*cols]*rows

    def get(self, row, col):
        return self.data[row][col]
    
    # row is relational, starting from index
    def put(self, row, col, value):
        self.data[(self.index+row)%self.rows][col] = value

    def move(self):
        self.index = self.index + 1
        if self.index == self.rows :
            self.index = 0
        # clear the data under the new, current index
        for i in range(self.cols):
            self.data[self.index][i] = None
