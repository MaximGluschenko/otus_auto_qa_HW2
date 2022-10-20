from Rectangle import *
from Circle import *


def test_rectangle_perimetr_calc():
    abc = Rectangle(10, 20)
    assert abc.perimetr == 60


def test_rectangle_area_calc():
    abc = Rectangle(10, 20)
    assert abc.area == 200


def test_rectangle_add_area_func():
    circle = Circle(10)
    rectangle = Rectangle(10, 100)
    assert rectangle.add_area(circle) == 1314.1592653589794
