import pytest
import clashgap as cg

clash = cg.Clash(["ham", "spam"])
def test_gap():
    assert clash.gap() == [['h', 'sp'], 'am']

def test_repr():
    assert clash.__repr__() == "[['h', 'sp'], 'am']"

