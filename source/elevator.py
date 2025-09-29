class Elevator():
    """
        This class is dedicated to the representation of a simple elevator. 
        It can be call from the outside and from the inside. 
        It tracks every floor it has been. 
        If it has been called from the same floor where it is, no floor will be tracked.
    """

    def __init__(self, number_of_floor):
        self.floor = 0
        self.number_of_floor = number_of_floor
        self.history = { i : 0 for i in range (number_of_floor)}

    def double_call(self, floors : tuple):
        for f in floors:
            self.call(f)
    
    def call(self, floor):
        if floor < 0 or floor > self.number_of_floor:
            return 
        print(f"Elevator at the floor {self.floor}. Called from the floor {floor}.")
        if self.floor == floor:
            return 
        self.floor = floor
        self.history[floor] += 1
    
    def get_history(self):
        return self.history
    

    