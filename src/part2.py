from math import pi, sqrt

# Your exercises should appear in this file.


def oppervlakte_kegel(r, h):
    # Zoek via Google naar "area cone"
    # l = vierkantswortel(r^2 + h^2)
    # A = π * r * l + π * r^2
    l = sqrt(r**2 + h**2)
    A = pi * r * l + pi * r**2
    return A


def last_element(l):
    """Return het laatste element uit een lijst"""
 
    b = l[-1]
    return b  


def sum_of_list(l):
    """Return de som van alle elementen uit een lijst"""
    b = sum(l)
    return b


def average_of_list(l):
    """Return het gemiddelde van alle elementen uit een lijst"""
    result = sum(l) / len(l)
    return result


def min_max_of_list(l):
    """Return het minimum en het maximum van de elementen uit een lijst"""
    minimum = min(l)
    maximum = max(l)
    return minimum, maximum


def squared_list(l):
    """Return een nieuwe lijst met de kwadraten van de elementen uit de gegeven lijst

    squared_list([2,3]) == [4, 9]
    """
    result = [i**2 for i in l]
    return result 
    


def differences_list(l1, l2):
    a = []
    for i in zip(l1, l2):
        a.append(i[0]-i[1])
    return a


def replace_takis_mr_issaris(text):
    result = text.replace("Takis", "Mr. Issaris")
    return result 
