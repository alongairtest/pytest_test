import pytest
import textwrap
from math import sqrt


# 勾股定理 求斜边值 sqrt表示求平方根
def magnitude(x, y):
    return sqrt(x * y + y * y)


def test_mag():
    assert magnitude(3, 4) == 5


def test_simple_match():
    assert abs(0.1 + 0.3) < 0.00001


def get_long_class_description(class_name):
    assert class_name == "warrior"
    return textwrap.dedent("A seasda dceitn of")


def test_warrior_class_description():
    desc = get_long_class_description("warrior")
    assert (
            desc == textwrap.dedent('A seasda dceitn of')
    ), '不相同'
