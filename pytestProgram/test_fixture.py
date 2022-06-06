import pytest

@pytest.fixture
def setup():
    print("Get driver")
    print("Maximize window")
    yield      ## devide before activity
    print("print title")
    print("close window")


def test_1(setup):
    print("Get facebook.com or open url")


def test_2(setup):
    print("Get amazon.com or open url")


def test_3(setup):
    print("Get Gmail.com or open url")
