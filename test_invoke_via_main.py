import pytest
import time


def test_one():
    time.sleep(10)


if __name__ == '__main__':
    pytest.main(["-q", __file__])
    print('返回Exitcode:', ret == pytest.ExitCode.INTERRUPTED)
