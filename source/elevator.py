import matplotlib.pyplot as plt

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
        print(f"Elevator at floor {self.floor}. Requested at floor {floor}.")
        if self.floor == floor:
            return 
        self.floor = floor
        self.history[floor] += 1
    
    def get_history(self):
        return self.history
    
    def plot(self):
        x = list(self.history.keys())
        y = list(self.history.values())

        plt.bar(x, y, width=0.6, color='skyblue', edgecolor='black')

        plt.xlabel("Floor number")
        plt.ylabel("Call")
        plt.title("History Histogram")
        plt.xticks(x)  # show all bins on x-axis
        plt.show()

    

    