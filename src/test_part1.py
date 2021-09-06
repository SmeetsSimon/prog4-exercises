import pytest
from .part1 import *


def test_add():
    assert add(4, 5) == 9


def test_add_0():
    assert add(5, -5) == 0


def test_kwadraat():
    assert kwadraat(4) == 16


def test_kwadraat_5():
    assert kwadraat(5) == 25


def test_oppervlakte_kubus_4():
    assert oppervlakte_kubus(4) == 16 * 6


def test_oppervlakte_kubus_5():
    assert oppervlakte_kubus(5) == 25 * 6


def test_seconds_in_days():
    """Test het aantal seconden in 1 dag"""
    assert seconds_in_days() == 3600 * 24


def test_seconds_in_1_days():
    assert seconds_in_days(1) == 3600 * 24


def test_seconds_in_2_days():
    assert seconds_in_days(2) == 3600 * 24 * 2


def test_seconds_in_1_week():
    assert seconds_in_weeks(1) == 3600 * 24 * 7


def test_seconds_in_2_weeks():
    assert seconds_in_weeks(2) == 3600 * 24 * 14


def test_seconds_in_1_year():
    assert seconds_in_years(1) == 3600 * 24 * 7 * 52


def test_seconds_in_17_year():
    assert seconds_in_years(17) == 3600 * 24 * 7 * 52 * 17


def test_seconds_remaining_in_life_male():
    assert seconds_remaining_in_life(44) == 3600 * 24 * 7 * 52 * (80 - 44)


def test_seconds_remaining_in_life_female():
    seconden_in_dag = 3600 * 24
    seconden_in_jaar = seconden_in_dag * 7 * 52
    verwachtte_levensduur = 84  # verwachtte levensduur vrouwen in Belgie
    leeftijd = 44
    overgebleven_levensduur = verwachtte_levensduur - leeftijd
    overgebleven_levensduur_in_s = overgebleven_levensduur * seconden_in_jaar
    assert seconds_remaining_in_life(44, is_female=True) == overgebleven_levensduur_in_s


def test_postcode_dilsen():
    v = postcodes()
    assert v["3650"] == "Dilsen-Stokkem"


def test_postcode_leuven():
    v = postcodes()
    assert v["3000"] == "Leuven"


def test_oneven_getallen_0():
    result = oneven_getallen(0)
    assert result == []


def test_oneven_getallen_1():
    result = oneven_getallen(1)
    assert result == [1]


def test_oneven_getallen():
    result = oneven_getallen(4)
    assert result == [1, 3, 5, 7]


def test_oneven_getallen_6():
    result = oneven_getallen(6)
    assert result == [1, 3, 5, 7, 9, 11]
