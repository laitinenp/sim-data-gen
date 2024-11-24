import json

class TimeWindow:

    def __init__(self, rows, cols):
        self.data = [[0]*cols]*rows
        self.index = 0
        self.config = json.load(open('config.json'))

    def get(self, row, col):
        return self.data[row][col]
    
    # row is relational, starting from index
    def put(self, row, col, value):
        self.data[(self.index+row)%self.config.rows][col] = value

    def move():
        self.index = self.index + 1
        if self.index == self.config.rows :
            self.index = 0
