import pytest
from Triangle import *
from Square import *


def test_triangle_creation_negative():

    with pytest.raises(ValueError):
        Triangle(10, 20, 10)


def test_triangle_creation_positive():

    assert Triangle(10, 19, 10)


def test_triangle_perimetr_calc():

    abc = Triangle(20, 20, 5)
    assert abc.perimetr == 45


def test_triangle_area_calc():

    abc = Triangle(20, 20, 5)
    assert abc.area == 49.607837082461074


def test_triangle_add_area_func():

    square = Square(10)
    triangle = Triangle(10, 10, 10)
    assert triangle.add_area(square) == 143.30127018922192
