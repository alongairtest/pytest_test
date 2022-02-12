import pytest


# 模块中的方法
def setup_module():
    print("\n setup_module:整个.py里只执行一次")


def teardown_module():
    print("\n teardown_module:整个.py执行一次")


# 函数级别

def setup_function():
    print("\n set_function 执行每条用例前执行")


def teardown_function():
    print("\n teardown_function 每条用例执行完成后执行")


def test_one():
    print("执行测试用例 one")


def test_two():
    print("执行测试用例 two")


def f():
    raise SystemExit(1)


def test_f():
    with pytest.raises(SystemExit):
        f()


if __name__ == "__main__":
    pytest.main(["-s", "test_frame_1.py"])
