import pytest
from app.main import get_human_age

def test_should_return_zeros_for_zero_input() -> None:
    assert get_human_age(0, 0) == [0, 0]

def test_should_return_zeros_before_fifteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_should_return_one_human_year_at_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_should_return_one_human_year_before_twenty_four() -> None:
    assert get_human_age(23, 23) == [1, 1]

def test_should_return_two_human_years_at_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_should_return_two_human_years_just_before_next_step() -> None:
    assert get_human_age(27, 27) == [2, 2]

def test_different_ratios_after_twenty_four() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(28, 29) == [3, 3]

def test_large_values_calculation() -> None:
    assert get_human_age(100, 100) == [21, 17]
