def test_1():
    y=18
    x=20
    assert x==y 

def test_2():
    name="Selenium"
    title="Selenium is for web development"
    assert name in title

def test_3():
    name="Jenkins"
    title="Jenkins is CI server"
    assert name is title,"Title does not match"

