# Python program to demonstrate
# main() function
import json
import random
import datetime
import TimeWindow

config = json.load(open('config.json'))
print(config)
window = TimeWindow.TimeWindow(
    config['rows'],
    datetime.datetime(2025, 1, 1),      # start from
    datetime.timedelta(minutes=15))     # timestep 15 minutes

# Defining main function
def main():

    # write csv heading line
    window.get(0).writeHeadingToCsvFile('data.csv')

    for i in range(config['numberOfSimulationSteps']):
        # TODO - The simulation operations here
        state = window.get(0)
        state.consumption = 100 * random.random()

        # simulation step finished, print the line
        state.writeLineToCsvFile('data.csv')

        # and then proceed to the next step
        window.move()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()