from pro2 import maxnumber

def test_maxnumber():
    assert maxnumber(10, 20, 30) == 30
    assert maxnumber(-10, -20, -5) == -5
    assert maxnumber(0, 0, 0) == 0
    assert maxnumber(1.5, 2.5, 0.5) == 2.5
