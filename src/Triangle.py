from math import sqrt
from Figure import *


class Triangle(Figure):

    def __init__(self, side_1, side_2, side_3):
        self.name = Triangle
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        if self.area <= 0:
            raise ValueError("Unable to create triangle!")

    @property
    def perimetr(self):
        return self.side_1 + self.side_2 + self.side_3

    @property
    def area(self):
        half_perim = self.perimetr / 2
        return sqrt(half_perim * (half_perim - self.side_1) * (half_perim - self.side_2) * (half_perim - self.side_3))
