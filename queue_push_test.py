import main

def test_queue():
    dmv = main.GanoLine()
    dmv.push(1)
    dmv.push(2)
    dmv.push(3)
    assert dmv.people == [1,2,3]