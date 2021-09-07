import pytest

from .part4 import *


def test_addressbook_search():
    addressbook = [
        {"name": "Jan Peters", "address": "Dorpsstraat 11"},
        {"name": "Piet Dirkx", "address": "Kerkstraat 32"},
        {"name": "Klaas Gadeyne", "address": "Groenstraat 44"},
    ]
    assert addressbook_search(addressbook, "Jan Peters") == "Dorpsstraat 11"


def test_addressbook_search_not_found():
    addressbook = [
        {"name": "Jan Peters", "address": "Dorpsstraat 11"},
        {"name": "Piet Dirkx", "address": "Kerkstraat 32"},
        {"name": "Klaas Gadeyne", "address": "Groenstraat 44"},
    ]
    assert addressbook_search(addressbook, "Jan Leenders") == None
