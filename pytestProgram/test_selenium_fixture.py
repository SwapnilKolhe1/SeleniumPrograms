import pytest
from selenium import webdriver


driver = None

@pytest.fixture
def setup():
    global driver    ##global=> To access it outside function as well in other functions
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield      ## devide before activity
    print("print title")
    print("close window")


def test_1(setup):
    driver.get("https://www.facebook.com")
    print("Perform test")


def test_2(setup):
    driver.get("https://www.amazon.in")
    print("Perform test")


def test_3(setup):
    driver.get("https://accounts.google.com")
    print("Perform test")
