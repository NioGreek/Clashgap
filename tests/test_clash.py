import clashgap as cg

clash = cg.Clash(["spam", "ham"])
def test_gap():
    assert clash.gap() == [['sp', 'h'], 'am']

def test_str():
    assert str(clash) == "[['sp', 'h'], 'am']"

def test_repr():
    assert repr(clash) == "[['sp', 'h'], 'am']"

def test_fill():
    assert clash.fill() == ["spam", "ham"]
