from Rectangle import *


class Square(Rectangle):

    def __init__(self, side_1):
        self.name = Square
        self.side_1 = side_1

    @property
    def side_2(self):
        return self.side_1
