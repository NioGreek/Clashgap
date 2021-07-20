import pytest
import clashgap as cg

def test_listHas():
    arr = [1, 2]
    assert cg.Gap._list_has(arr, 1) == True
    assert cg.Gap._list_has(arr, 2) == False

def test_maxElem():
    arr = ["spam", "ham"]
    assert cg.Gap._max_elem(arr) == "spam"

def test_gap():
    arr = ["spam", "ham"]
    assert cg.gap(arr) == [['sp', 'h'], 'am']

