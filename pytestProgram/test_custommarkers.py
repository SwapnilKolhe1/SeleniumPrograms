import sys

import pytest


@pytest.mark.smoke
def test_1():
    x = 10
    y = 20
    assert x == y   # assert is like comparision if its result is true then test case is passed if false then test case is failed

@pytest.mark.smoke
def test_2():
    x = 20
    y = 20
    assert x == y

@pytest.mark.smoke
def test_t3():
    x = 10
    y = 20
    result = x + y
    assert result == 30


@pytest.mark.smoke
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

@pytest.mark.swapnil
def test_t5():
    x = 30
    y = 20
    result = x + y
    assert result == 50


@pytest.mark.regression
def test_t6():
    x = 30
    y = 20
    result = x * y
    assert result == 600


@pytest.mark.regression
def test_t7():
    x = 30
    y = 2
    result = x / y
    assert result == 15

@pytest.mark.regression
@pytest.mark.smoke
def test_check_in():
    name = "Credence"
    message = "Credence is the best place to learn adn also extended family"
    assert name in message     ##in => like operator or contains function

@pytest.mark.regression
def test_check_is():
    name = "Credence"
    message = "Credence is the best place to learn adn also extended family"
    assert name is message   ## is => equal to