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
    exit_schedule = [60*8, 60*14]
    enter_schedule = [60*12, 60*18]
    floor_threshold = 2
    number_of_floors = 6
    apartment_per_floor = 3
    # -- Object initialiazing --
    decisioner = Simple_deterministic_model(exit_schedule= exit_schedule, enter_schedule=enter_schedule, floor_threshold=floor_threshold)
    building = Building(number_of_floors, apartment_per_floor, decisioner)
    # -- Simulation --
    number_of_days = 7
    building.simulate(number_of_days)
    # -- Retrieve empiric probability distribution --
    print(building.elev.get_history())