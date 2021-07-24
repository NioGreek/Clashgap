import clashgap as cg

def test_list_has():
    arr = [1, 2]
    assert cg._gap.list_has(arr, 1) == True
    assert cg._gap.list_has(arr, 2) == False

def test_collision():
    assert cg._gap.collision("spam", "ham") == (2, 1)

def test_gap():
    assert cg.gap(["spam", "ham"]) == [['sp', 'h'], 'am']

