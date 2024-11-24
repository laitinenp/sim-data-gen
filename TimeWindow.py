

class TimeWindow:

    def __init__(self, rows, cols):
        data = [[0]*cols]*rows

    def get(self, row, col):
        return data[row][col]
    

