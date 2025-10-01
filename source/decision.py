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
    
class Simple_probabilistic_logistic_model(Decision_model):
    """
        This is a simple probabilistic logistic model.
        It follows a fixed schedule. 
        To choose wheter to take or not the elevator it uses an exponential distribution.
        It sample from the exponential and if the actual floor is greater than the sample it takes the elevator.
        The exponential distribution has a lambda that ensure a 99% of cumulative probability to take the elevator form a certain floor.
        To solve for the lambda we impose that F(t) = P(X <= t) = 1 - exp(-lambda*t). From that we obtain:
            1. 1 - exp(-lambda*t) = p
            2. exp(-lambda*t) = 1 - p
            3. -lambda*t = ln(1 - p)
            4. lambda = -ln(1 - p)/t
            5. lambda = ln(1/(1-p))/t
        fixing p = 0.999 we obtain lambda = ln(1000)/t
        fixing t = 5 (above the first floor it's almost impossible that someone do not take the elevator) we actually solve for lambda = 1.38155..
    """

    def __init__(self, enter_schedule : list, exit_schedule : list, floor_threshold : int):
        super().__init__()
        self.enter_schedule = enter_schedule
        self.exit_schedule = exit_schedule
        self.floor_threshold = floor_threshold
        self.prob = 0.90
        from math import log
        self.lam = log(1/(1-self.prob))/self.floor_threshold
        self.scale = 1/self.lam
        print(self.scale)
        
    def enter(self, time):
        return time in self.enter_schedule
    
    def exit(self, time):
        return time in self.exit_schedule
    
    def inner_call(self, time, floor):
        """
            Generate a sample from an exponential distribution with the right scale.
            It just check if the floor is or not over the sample.
            Return True if the floor is over the sample, False otherwise.
        """
        import numpy as np
        sample = np.random.exponential(scale=self.scale)
        return floor > sample
    
    def outer_call(self, time, floor):
        """
            Generate a sample from an exponential distribution with the right scale.
            It just check if the floor is or not over the sample.
            Return True if the floor is over the sample, False otherwise.
        """
        import numpy as np
        sample = np.random.exponential(scale=self.scale)
        return floor > sample