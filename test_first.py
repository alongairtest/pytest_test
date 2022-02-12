import pytest


def test_1():
    print("这是第一个方法")


def test_2():
    print('这是第二个方法')


if __name__ == "__main__":
    pytest.main(['-s', "test_first.py"])
