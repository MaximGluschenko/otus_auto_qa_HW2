from Circle import *
from Triangle import *


def test_circle_perimetr_calc():
    abc = Circle(10)
    assert abc.perimetr == 62.83185307179586


def test_circle_area_calc():
    abc = Circle(10)
    assert abc.area == 314.1592653589793


def test_circle_add_area_func():
    circle = Circle(10)
    triangle = Triangle(10, 10, 10)
    assert circle.add_area(triangle) == 357.4605355482013
