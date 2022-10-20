from math import pi
from Figure import *


class Circle(Figure):

    def __init__(self, radius):
        self.name = Circle
        self.radius = radius

    @property
    def perimetr(self):
        return 2 * pi * self.radius

    @property
    def area(self):
        return pi * self.radius**2
