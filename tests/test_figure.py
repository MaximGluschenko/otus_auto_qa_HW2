import pytest
from Circle import *


def test_circle_add_area_func_negative():

    circle = Circle(10)
    num = 100
    with pytest.raises(ValueError):
        circle.add_area(num)
