import createodd

def test_odd():
    assert createodd.genodd(4) == [1, 3]
    assert createodd.genodd(0) == []
    assert len(createodd.genodd(100)) == 50