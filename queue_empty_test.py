import main

def test_queue():
    dmv = main.GanoLine()
    dmv.push(1)
    dmv.pop()
    assert dmv.people == []