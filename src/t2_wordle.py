import datetime
import random
import re

from rich import print


def choose_word(words):
    """Een functie die een willekeurig woord uit een lijst kiest"""
    return random.choice(words)
    




def lines_to_words(lines):
    """Een functie die de newlines uit een lijst strings verwijdert"""
    lijst = []
    for i in lines:
         lijst.append(i.strip())
    return lijst


def process_words(woorden, length):
    """Een functie die gegeven een lijst woorden de bruikbare woorden filtert
    
    De bruikbare woorden zijn:
    - woorden van de juiste lengte
    - woorden zonder: koppeltekens, spaties, hoofdletters, punten, quotes
    """
    lijst = []
    for woord in woorden:
        if len(woord) != length:
            continue
        if '-' in woord:
            continue
        if ' ' in woord:
            continue
        if '.' in woord:
            continue
        if '"' in woord:
            continue
        if woord.isupper():
            continue
        if woord.istitle():
            continue
        lijst.append(woord)
    return lijst 

        
        


def combine_letters_of_words(word1, word2):
    """Een functie die gegeven twee woorden een lijst van tuppels geeft.
    
    Bijvoorbeeld:
    >>> combine_letters_of_words("ab", "12")
    [('a', '1'), ('b', '2')]

    Gebruik hiervoor de zip-functie die je in de standaard bibliotheek
    van Python vindt.
    """
    woorden = zip(word1, word2)
    lijst = list(woorden)
    return lijst




def print_letter_volledig_juist(a):
    """Geef een string terug die de letter 'a' in het groen weer zou geven bij gebruik van Rich"""
    result = (f"[green]{a}[/green]")
    return result 




def print_letter_bijna_juist(a):
    """Geef een string terug die de letter 'a' in het geel weer zou geven bij gebruik van Rich"""
    result = (f"[yellow]{a}[/yellow]")
    return result


def print_letter_fout(a):
    """Geef een string terug die de letter 'a' in het rood weer zou geven bij gebruik van Rich"""
    result = (f"[red]{a}[/red]")
    return result

def print_letter(a, b, secret_word):
    """Geef een string terug die de letter 'a' in kleur weergeeft bij gebruik van Rich
    
    Als de letters overeenkomen, in het groen.
    Als de letters niet overeenkomen, maar letter 'a' komt voor in het
    geheime woord, dan in het geel.
    Als letter 'a' helemaal niet voorkomt in het woord, dan in het rood.

    Dus, bijvoorbeeld:
    >>> print_letter("u", "u", "mus")
    '[green]u[/green]'
    >>> print_letter("s", "u", "mus")
    '[yellow]s[/yellow]'
    >>> print_letter("o", "u", "mus")
    '[red]o[/red]'
    """
    if a == b :
        return (f"[green]{a}[/green]")

    elif a in secret_word:
        return (f"[yellow]{a}[/yellow]")
    if a != b:
        return (f"[red]{a}[/red]")

     






if __name__ == "__main__":

    # lees de woordlijst in
    filename = "wordlist.txt"
    f = ...

    lines = ...

    # gebruik lines_to_words en
    # process_words om een lijst met
    # woorden van lengte 5 te verkrijgen
    words = ...
    words = ...

    # kies een willekeurig woord mbv choose_word
    secret_word = ...

    counter = 1
    while counter < 6:
        # vraag de gebruiker om een gok te wagen
        w = input("?")

        # als de gebruiker "stop" ingeeft beeindig het programma dan
        # gebruik hiervoor het break statement
        # if ...

        # als het woord geen 5 letters lang is, sla dit woord dan over
        # gebruik hiervoor het continue statement
        # if ...

        # controlleer of het woord correct is, en druk het woord in kleur
        # op het scherm af gebruik makend van combine_letters_of_words en
        # print_letter
        # for a, b in ...
        #     letter = ...
        #     print(letter, end="")
        # print()
        # counter += 1

        # als het woord correct geraden werd
        # toon dan een overwinningsboodschap
        # if ...

    # toon hoeveel pogingen nodig waren om het woord juist te raden
    ...

