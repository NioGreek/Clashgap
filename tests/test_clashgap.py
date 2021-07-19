import pytest
from clashgap import *

def test_version():
    assert __version__ == '0.1.0'   

class clash:
    def __init__(self):
        clash = clash(["ham", "spam"])
    
    def test_gap(self):
        assert self.clash.gap() == [['h', 'sp'], 'am']

class gap:
    def test_listHas():
        arr = [1, 2]
        assert list_has(arr, 1)
        assert not(list_has(arr, 2))
    
    def test_maxElem():
        arr = ["ham", "spam"]
        assert max_elem(arr) == 1
    
    def test_gap():
        arr = ["ham", "spam"]
        assert gap(arr) == [['h', 'sp'], 'am']

