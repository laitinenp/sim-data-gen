# Python program to demonstrate
# main() function
import json
import TimeWindow

config = json.load(open('config.json'))
window = TimeWindow(config.rows, config.cols)

# Defining main function
def main():
    for i in range(config.rows):
        window.move()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()