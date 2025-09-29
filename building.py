import numpy as np
from elevator import *
from individual import *
from decision import *

class Building():
    """
        This class is dedicated to the representation of a building.
        In the init building it place an individual to each apartment 
    """

    def __init__(self, number_of_floor, apartment_per_floor, decision_model):
        self.number_of_floor = number_of_floor
        self.apartment_per_floor = apartment_per_floor
        self.elev = Elevator(number_of_floor)
        self.time = 0 
        self.step = 5
        self.init_building(decision_model)
    
    def init_building(self, decision_model : Decision_model):
        """
            For now it is fixed that each apartment has just 1 people inside. 
        """
        self.floors = []
        for floor in range (self.number_of_floor):
            apartment = []
            for j in range (self.apartment_per_floor):
                apartment.append(Individual(floor, decision_model))
            self.floors.append(apartment)

    def update(self):
        """
            self.clock += 5 min -> on this side the time is just in minute 
            for each individual, individual.call(time) 
            if the call is not -1, call the elevator 
        """
        self.time += self.step
        self.time = self.time%(60*24) # one day limit
        for apartment in self.floors:
            for individual in apartment:
                floor_call = individual.call(self.time)
                if floor_call != -1:
                    self.elev.call(floor_call)
    
    def simulate(self, number_of_days):
        for i in range (number_of_days):
            for k in range(60*24//self.step):
                self.update()
    
if __name__ == "__main__":
    
    decisioner = Decision_model()
    building = Building(6, 2, decisioner)
    building.simulate(7)
    print(building.elev.get_history())