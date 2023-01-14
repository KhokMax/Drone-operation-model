import random
from math import sqrt

class Cargo():

    def __init__(self, id):
        """Initializes the cargo and sets its starting position."""
        self.id = id
        self.x = random.randint(-25, 25)
        self.y = random.randint(-25, 25)
        self.weight = random.randint(1, 2000)
        self.profit = sqrt((self.x ** 2) + (self.y)**2)

