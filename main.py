# Python program to demonstrate
# main() function
import json
import random
import datetime
import TimeWindow

PROB_CAR = 0.15
PROB_TRUC = 0.05
CHARGE_TIMESTEP_CAR = 3
CHARGE_TIMESTEP_TRUCK = 4

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
        state = window.get(0)

        # TODO - The simulation operations here
        carArrives = (random.random() < PROB_CAR)
        if carArrives:
            for i in range(10):
                # is bay nr. i free for charging
                if state.bays[i] == '0':
                    # book also the following timesteps for charging
                    for t in range(CHARGE_TIMESTEP_CAR):
                        window.get(t).bays[i] = 'C'
                    break

        truckArrives = (random.random() < PROB_TRUC)
        if truckArrives:
            for i in range(10):
                # is bay nr. i free for charging
                if state.bays[i] == '0':
                    # book also the following timesteps for charging
                    for t in range(CHARGE_TIMESTEP_TRUCK):
                        window.get(t).bays[i] = 'T'
                    break

        # simulation step finished, print the line
        state.writeLineToCsvFile('data.csv')

        # and then proceed to the next step
        window.move()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()