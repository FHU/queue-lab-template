import main

def test_queue():
    dmv = main.GanoLine()
    dmv.push(1)
    dmv.push(2)
    dmv.push(3)
    dmv.pop()
    assert dmv.people == [2,3]