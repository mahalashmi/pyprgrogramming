import checklistsame

def test_listsame():
    assert checklistsame.AreSame([], []) == True
    assert checklistsame.AreSame([1], [1]) == True
    assert checklistsame.AreSame([1], [2]) == False
    assert checklistsame.AreSame([1, 2], [1]) == False