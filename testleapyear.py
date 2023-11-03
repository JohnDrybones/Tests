import pytest
from Leapyear import isLeapYear

@pytest.mark.parametrize("year, expected", [
    (2004, True),
    (2020, True),
    (2024, True),
])
def test_leap_year_div_by_4_not_div_by_100(year, expected):
    assert isLeapYear(year) == expected

@pytest.mark.parametrize("year, expected", [
    (1600, True),
    (2000, True),
    (2400, True),
])
def test_leap_year_div_by_400(year, expected):
    assert isLeapYear(year) == expected

@pytest.mark.parametrize("year", [2021, 2022, 2023])
def test_not_leap_year_not_div_by_4(year):
    assert isLeapYear(year) == False

@pytest.mark.parametrize("year", [1700, 1800, 1900, 2100])
def test_not_leap_year_div_by_100_not_div_by_400(year):
    assert isLeapYear(year) == False

if __name__ == "__main__":
    pytest.main()
