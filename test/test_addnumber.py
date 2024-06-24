import addtwonumber

def test_add():
    assert addtwonumber.addtwonumberfn(2, 3) == 5
    assert addtwonumber.addtwonumberfn(0, 0) == 0
    assert addtwonumber.addtwonumberfn(-2, -3) == -5
    assert addtwonumber.addtwonumberfn(2, -3) == -1
    assert addtwonumber.addtwonumberfn(-2, 3) == 1
    assert addtwonumber.addtwonumberfn(1000000000, 3) == 1000000003
    assert addtwonumber.addtwonumberfn(2, 1000000000) == 1000000002
