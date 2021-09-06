# Your exercises should appear in this file.


def add(x, y):
    resultaat = x + y
    return resultaat 


def kwadraat(x):
    
    """Return het kwadraat van x"""
    
    
    resultaat = x * x
    return resultaat 
    


def oppervlakte_kubus(z):
    """Return de oppervlakte van een kubus met zijde z"""
    resultaat = z*z*6

    return resultaat

    


def seconds_in_days(days=1):
    """Geef het aantal seconden in het opgegeven aantal dagen

    Als er geen parameter doorgegeven wordt, geef dan het aantal
    seconden in 1 dag terug.
    """
    seconden = days * 86400

    return seconden


def seconds_in_weeks(weeks):
    """Return het aantal seconden in 'week' weken."""
    seconden = weeks * 604800
    return seconden


def seconds_in_years(years):
    """Return het aantal seconden in 'years' jaren.

    Veronderstel dat ieder jaar uit exact 52 weken bestaat.
    """
    eenjaar = 52 * 604800
    seconden = eenjaar * years 
    return seconden


def seconds_remaining_in_life(age, is_female=False):
    """Return het aantal seconden dat overblijft in je leven.

    Ga uit van een maximale levensduur van 80 jaren voor mannen,
    en 84 jaren voor vrouwen.
    """
    if is_female == False:
        jaren = 80 - age
        result = seconds_in_years(jaren)
        return result
    else:
        jaren = 84 - age
        result = seconds_in_years(jaren)
        return result
    


def postcodes():
    """Return een dictionary met postcodes"""
    result = {
        "3650": "Dilsen-Stokkem",
        "3000": "Leuven",
    }
    return result


def oneven_getallen(x):
    """Return een lijst met de eerste 'x' oneven getallen."""
    lijst = []
    som = 0
    if x == 0:
        return []
    for i in range(1, 10000000, 2):
        lijst.append(i)
        som = som + 1
        if som == x:
            break
    return lijst 
    