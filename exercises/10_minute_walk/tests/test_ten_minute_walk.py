from lib.ten_minute_walk import ten_minute_walk

def test_ten_minute_walk_one():
    assert ten_minute_walk(['w', 's', 'e', 'e', 'n', 'n', 'e', 's', 'w', 'w']) == True


def test_ten_minute_walk_two():
    assert ten_minute_walk(['w', 's', 'e', 'n', 'n', 'e', 's', 'w', 'w', 'w']) == False


def test_ten_minute_walk_three():
    assert ten_minute_walk(['w', 's', 'e', 's', 's', 'e', 's', 'w', 'n', 'n']) == False


def test_ten_minute_walk_four():
    assert ten_minute_walk(['w', 's']) == False


def test_ten_minute_walk_five():
    assert ten_minute_walk(['n', 'e', 's', 'w', 'n', 'e', 's', 'w', 'n', 's']) == True