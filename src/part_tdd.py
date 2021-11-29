# Schrijf voor onderstaande oefeningen eerst de testen in test_part_tdd.py
# Implementeer ze vervolgens in dit bestand.

# Oefening 1
# ==========
# Schrijf een functie palindroom, die controlleert of een bepaalde string
# een palindroom is.
# > palindroom("lol")
# True
def palindroom(x):
    if x == x[::-1]:
        return True
    else:
        return False

# Oefening 2
# ==========
# Schrijf een functie anagram, die controlleert of een twee gegeven woorden
# anagrammen zijn van elkaar.
# > anagram("lol", "lot")
# False
# > anagram("tol", "lot")
# True
def anagram(x, y):
    if (sorted(x) == sorted(y)):
        return True
    else: 
        return False

# Oefening 3
# ==========
# Schrijf een functie leeftijd, die gegeven een datum, je leeftijd in jaren
# teruggeeft:
# > leeftijd(1976, 12, 20)
# 44
# > leeftijd(1976, 2, 10)
# 45
# 
# Tip: Gebruik de datetime module:
# datetime.date.now() geeft de huidige datum
# datetime.date.date(year=2021, month=1, day=1) stelt 1 januari voor
# Je kan data van elkaar aftrekken.
from datetime import date

def leeftijd(j, m, d):
    today = date.today()
    x = date(year=j, month=m, day=d)
    age = today - x
    return age.total_seconds() // (60*60*24*365)
     