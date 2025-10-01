from source.building import *
from source.decision import * 

if __name__ == '__main__':
    """
        This is the entry point for the building simulator.

        Future update:
            - terminal line input
            - different types of building initializer
            - different types of decisioners

        Quick usage: 
            py main.py
    """
    # -- Parameters setting --
    exit_schedule = [60*8]
    enter_schedule = [60*12]
    floor_threshold = 5
    number_of_floors = 7
    apartment_per_floor = 2
    # -- Object initialiazing --
    decisioner = Simple_deterministic_model(enter_schedule=enter_schedule, exit_schedule= exit_schedule, floor_threshold=floor_threshold)
    decisioner = Simple_probabilistic_logistic_model(enter_schedule=enter_schedule, exit_schedule= exit_schedule, floor_threshold=floor_threshold)
    building = Building(number_of_floors, apartment_per_floor, decisioner)
    # -- Simulation --
    number_of_days = 30
    building.simulate(number_of_days)
    # -- Retrieve empiric probability distribution --
    print(building.elev.get_history())
    building.elev.plot()