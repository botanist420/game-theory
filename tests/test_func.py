def add_numbers(x: int, y: int):
    return x + y


def test_1():
    assert 7 == add_numbers(3, 4)


def test_2():
    assert 10 == add_numbers(5, 5)
    
def test_add_num():
    assert 18 == add_numbers(14, 4)
