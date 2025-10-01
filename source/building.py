from .elevator import *
from .individual import *
from .decision import *
from faker import Faker

class Building():
    """
        This class is dedicated to the representation of a building.
        In the init building it place an individual to each apartment 
    """

    def __init__(self, number_of_floors, apartment_per_floor, decision_model):
        self.number_of_floors = number_of_floors
        self.apartment_per_floor = apartment_per_floor
        self.elev = Elevator(number_of_floors)
        self.time = 0 
        self.step = 5
        self.init_building(decision_model)
    
    def init_building(self, decision_model : Decision_model):
        """
            For now it is fixed that each apartment has just 1 people inside. 
        """
        self.floors = []
        fake = Faker()
        for floor in range (self.number_of_floors):
            apartment = []
            for j in range (self.apartment_per_floor):
                apartment.append(Individual(floor, fake.name(), decision_model))
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
                    self.elev.double_call(floor_call)
    
    def simulate(self, number_of_days):
        for i in range (number_of_days):
            for k in range(60*24//self.step):
                self.update()
    
if __name__ == "__main__":
    
    pass