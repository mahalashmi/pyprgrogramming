import displaycharlist



def test_charcount():
    assert displaycharlist.charcount([]) == {}
    assert displaycharlist.charcount(['a']) == {'a':1}
    assert displaycharlist.charcount(['a','b','c']) == {'a':1, 'b':1, 'c':1}
    assert displaycharlist.charcount(['a', 'a', 'a']) == {'a':3}
    assert displaycharlist.charcount(['a','b','c', 'a','b', 'a',]) == {'a':3, 'b':2, 'c':1 }