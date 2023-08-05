import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area_of_a_circle(self):
        return math.pi * self.radius ** 2


