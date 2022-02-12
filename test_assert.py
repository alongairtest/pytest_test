import pytest


def myfunc():
    raise ValueError("40013")


def test_match():
    with pytest.raises(ValueError) as excinfo:
        myfunc()
    assert "40013" in str(excinfo.value), "错误"


class Foo(object):
    def __init__(self, val):
        self.val = val

    #def __eq__(self, other):
    #    return self.val == other.val

    def __repr__(self):
        return repr(self.val)


def test_foo_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
