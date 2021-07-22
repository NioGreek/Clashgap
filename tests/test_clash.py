import pytest
import clashgap as cg

clash = cg.Clash(["ham", "spam"])
def test_gap():
    assert clash.gap() == [['h', 'sp'], 'am']

def test_repr():
    assert repr(clash) == "[['h', 'sp'], 'am']"

def test_str():
    assert str(clash) == "[['h', 'sp'], 'am']"
