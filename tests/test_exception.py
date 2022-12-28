import pytest


def lucas_function(x):
    if x == 0:
        raise ValueError("The number can not be 0")
    else:
        pass


def test_lucas():
    with pytest.raises(ValueError):
        lucas_function(0)


def test_lucas_2():
    assert lucas_function(20) == None