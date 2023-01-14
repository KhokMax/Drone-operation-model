from datetime import datetime, timedelta

class Dron():

    def __init__(self, id):
        """Initializes the cargo and sets its starting position."""
        self.id = id
        self.charge_percentage = 100
        self.charge_speed = 1
        self.max_weight = 5500

    def charge_dron(self):
        self.charge_percentage = 100

    def update_percentage(self, num):
        self.charge_percentage -= num



class Base():
    def __init__(self):
        """Initializes the cargo and sets its starting position."""
        self.x = 0
        self.y = 0