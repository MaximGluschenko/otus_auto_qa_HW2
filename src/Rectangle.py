from Figure import *


class Rectangle(Figure):
    def __init__(self, side_1, side_2):
        self.name = Rectangle
        self.side_1 = side_1
        self.side_2 = side_2

    @property
    def perimetr(self):
        return (self.side_1 + self.side_2)*2

    @property
    def area(self):
        return self.side_1 * self.side_2
