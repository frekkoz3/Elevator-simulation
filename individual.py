from decision import *

class Individual():
    """
        This class is dedicated to the representation of a simple individual.
        An external decision model is passed to the individual. 
        For now there are few input for the decision model (time and living floor) but there's a plenty
        of space for experimentation (eg age).
    """

    def __init__(self, living_floor, decision_model : Decision_model):
        self.living_floor = living_floor
        self.decision_model = decision_model
        self.inside = True
        self.outside = False
        
    def call(self, time):
        """
            This function return if an individual want to exit or enter the building based on the time.
            If an individual want to take an action (enter or exit) the self.decision_model.action(time)
            will return True, False otherwise.
            If an individual want to call the elevator the self.decision_model.call(time, living_floor)
            will return the floor number (0 or living floor) if decided to call the elevator, -1 otherwise.
        """
        action = self.decision_model.enter(time) if self.outside else self.decision_model.exit(time)
        # Update state
        if action and self.outside:
            self.inside = True
            self.outside = False
        if action and self.inside:
            self.inside = False
            self.outside = True
        if action:
            call = self.decision_model.outer_call(time, self.living_floor) if self.outside else self.decision_model.inner_call(time, self.living_floor)
        else:
            call = -1
        return call
    
    def get_state(self):
        return self.inside, self.outside    
    
    

        