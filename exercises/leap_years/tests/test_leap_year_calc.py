from lib.leap_year_calc import leap_year_calc

def test_leap_year_calc_returns_true_for_400_divisible():
    assert leap_year_calc(2000) == True

def test_leap_year_calc_returns_false_for_non_400_divisible():
    assert leap_year_calc(1970) == False

def test_leap_year_calc_returns_false_for_non_400_and_100_divisible():
    assert leap_year_calc(1300) == False

def test_leap_year_calc_returns_true_for_divisible_by_4_not_100():
    assert leap_year_calc(2004) == True
    assert leap_year_calc(2008) == True

def test_leap_year_calc_false_for_years_not_divisible_by_4():
    assert leap_year_calc(2009) == False
    assert leap_year_calc(2010) == False
    assert leap_year_calc(2011) == False