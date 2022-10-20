from Square import *
from Rectangle import *


def test_rectangle_perimetr_calc():
    abc = Square(35)
    assert abc.perimetr == 140


def test_rectangle_area_calc():
    abc = Square(100)
    assert abc.area == 10000


def test_rectangle_add_area_func():
    square = Square(10)
    rectangle = Rectangle(10, 20)
    assert square.add_area(rectangle) == 300
