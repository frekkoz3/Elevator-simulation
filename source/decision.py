class Decision_model():
    """
        This is super easy and stupid
    """
    def __init__(self):
        pass

    def enter(self, time):
        pass
        return time == 60*12 or time == 60*18

    def exit(self, time):
        pass
        return time == 60*8 or time == 60*14

    def inner_call(self, time, floor):
        pass
        return floor if floor > 2 else -1

    def outer_call(self, time, floor):
        pass
        return floor if floor > 2 else -1
    
class Simple_deterministic_model(Decision_model):
    """
        This deterministic decision model just follow an enter and exit schedule.
    """

    def __init__(self, enter_schedule : list, exit_schedule : list, floor_threshold : int):
        super().__init__()
        self.enter_schedule = enter_schedule
        self.exit_schedule = exit_schedule
        self.floor_threshold = floor_threshold
        
    def enter(self, time):
        return time in self.enter_schedule
    
    def exit(self, time):
        return time in self.exit_schedule
    
    def inner_call(self, time, floor):
        """
            It just check if the floor is or not over the threshold.
            Return True if the floor is over the threshold, False otherwise.
        """
        return floor > self.floor_threshold
    
    def outer_call(self, time, floor):
        """
            It just check if the floor is or not over the threshold.
            Return True if the floor is over the threshold, False otherwise.
        """
        return floor > self.floor_threshold
        