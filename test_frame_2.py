import pytest


class TestCase(object):
    def setup_class(self):
        print("\n setup_class 所有用例执行之前")

    def teardown_class(self):
        print("\n teardown_class 所有用例执行之后")

    #def setup_method(self):
    #    print("\n setup_method 每个用例执行之前")

    #def teardown_method(self):
    #    print("\n teardown_method 每个用例执行后执行")

    def setup(self):
        print("\n setup  每个用例执行之前")

    def teardown(self):
        print("\n teardown 每个用例结束后")

    def test_three(self):
        print("执行第一条用例")

    def test_four(self):
        print("执行第二条用例")


if __name__ == "__main__":
    pytest.main(["-s", "test_frame_2.py"])
