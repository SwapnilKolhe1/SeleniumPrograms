
def test_1():
    x = 10
    y = 20
    assert x == y   # assert is like comparision if its result is true then test case is passed if false then test case is failed


def test_2():
    x = 20
    y = 20
    assert x == y


def test_t3():
    x = 10
    y = 20
    result = x + y
    assert result == 30


def some_test_t4():             ## invalid test case name # it will be ignored in test execution
    x = 10
    y = 20
    result = x + y
    assert result == 30


def some_test():             ## invalid test case name # it will be ignored in test execution
    x = 10
    y = 20
    result = x + y
    assert result == 30


def test_t5():
    x = 30
    y = 20
    result = x + y
    assert result == 10


def test_t6():
    x = 30
    y = 20
    result = x * y
    assert result == 600


def test_t7():
    x = 30
    y = 2
    result = x / y
    assert result == 15
