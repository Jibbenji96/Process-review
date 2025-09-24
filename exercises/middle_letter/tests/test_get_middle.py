from lib.get_middle import get_middle

def test_get_middle_test():
    assert get_middle("test") == 'es'


def test_get_middle_testing():
    assert get_middle("testing") == 't'


def test_get_middle_middle():
    get_middle("middle") == 'dd'


def test_get_middle_A():
    get_middle("A") == 'A'


def test_get_middle_of():
    get_middle("of") == 'of'
