class Decision_model():
    """
        This is super easy and stupid
    """
    def __init__(self):
        pass

    def enter(self, time):
        return time == 60*12 or time == 60*18

    def exit(self, time):
        return time == 60*8 or time == 60*14

    def inner_call(self, time, floor):
        return floor if floor > 2 else -1

    def outer_call(self, time, floor):
        return floor if floor > 2 else -1