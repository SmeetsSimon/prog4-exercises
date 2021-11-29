
from unittest.mock import mock_open, patch

from .part_tdd import *


# Schrijf hier testen voor je oefeningen.
# Begin iedere testfunctie met naam "test_" gevolgd door de
# naam van de functie die je gaat testen, gevold door 
# een naam die aangeeft wat je gaat testen.
# 
# B.v.
# Om een functie "kwadraat" te testen, kan je als eerste test
# een functie met naam "test_kwadraat_2" die test dat het
# kwadraat van 2 4 is.

def test_palindroom():
    x = "lol"
    result = palindroom(x)
    assert result == True

def test_palindroom_2():
    x = "haas"
    result = palindroom(x)
    assert result == False


def test_anagram():
    x = "tol"
    y = "lot"
    result = anagram(x, y)
    assert result == True

def test_anagram_2():
    x = "pot"
    y = "zat"
    result = anagram(x, y)
    assert result == False

def test_leeftijd():
    j = 2004
    m = 8
    d = 5
    result = leeftijd(j, m, d)
    assert result == 17

def test_leeftijd2():
    j = 2000
    m = 10
    d = 1
    result = leeftijd(j, m, d)
    assert result == 21