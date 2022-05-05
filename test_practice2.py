import sys
import pytest 


@pytest.mark.smoke
def test_login():
    print("Login done")


@pytest.mark.regression
def test_addProduct():
    print("add product")

@pytest.mark.skip
def test_xyz():
    print("Skipped")

@pytest.mark.skipif(sys.version_info<(3,9),reason="Python version not supported")
def test_abc():
    print("abc")

@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_checkout():
    print("Failed")

@pytest.mark.parametrize("username,password",[("abc","123"),("def","123"),("xyz","0000")])
def test_login(username,password):
    print(username,password)
