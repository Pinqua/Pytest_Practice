import pytest


@pytest.fixture
def setup():
    print("Start")
    yield 
    print("Close")

def test_1(setup):
    print("Test1")
    print("Test1")

def test_2(setup):
    print("Test2")
    print("Test2")