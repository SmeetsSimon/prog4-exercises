

def maak_persoonsinformatie_dict(naam, leeftijd, gewicht, lengte, oogkleur):
    """Geef een dictionary terug met alle gegevens die als parameters aan
    de functie meegegeven werden.

    Bijvoorbeeld:
    >>> maak_persoonsinformatie_dict("Jan", 32, 79, 167, "blauw")
    {'naam': 'Jan', 'leeftijd': 32, 'gewicht': 79, 'lengte': 167, 'oogkleur': 'blauw'}
    """
    geg = {
        "naam" : naam,
        "leeftijd" : leeftijd, 
        "gewicht" : gewicht,
        "lengte" : lengte, 
        "oogkleur" : oogkleur 

    }
    return geg


def tel_autos(lijst_autos):
    """Gegeven een lijst met automerken, geef je een dictionary terug met
    voor ieder automerk het aantal keer dat dit merk in de lijst voorkomt.

    Bijvoorbeeld:
    >>> tel_autos(["bmw", "audi", "audi", "ford", "bmw"])
    {'peugeot': 0, 'ford': 1, 'bmw': 2, 'audi': 2, 'nissan': 0}
    """
    lijst_peugeot = 0
    lijst_ford = 0
    lijst_bmw = 0
    lijst_audi = 0
    lijst_nissan = 0

    for i in lijst_autos:
        if "peugeot"in i["merk"]:
            lijst_peugeot += 1
        if "ford"in i["merk"]:
            lijst_ford += 1
        if "bmw"in i["merk"]:
            lijst_bmw += 1
        if "audi"in i["merk"]:
            lijst_audi += 1
        if "nissan"in i["merk"]:
            lijst_nissan += 1   

    dict = {
        "peugeot" : lijst_peugeot,
        "ford" : lijst_ford,
        "bmw" : lijst_bmw,
        "audi" : lijst_audi,
        "nissan" : lijst_nissan,
    }  

    return dict  



def leeftijden_acteurs(acteurs):
    """Gegeven een lijst van lijsten met informatie over acteurs,
    geef je een lijst van leeftijden van acteurs terug.

    Bijvoorbeeld:
    >>> leeftijden_acteurs([["Will Smith", 53], ["Tom Hanks", 65]])
    [53, 65]
    """
    lijst = []
    for actuer in acteurs:
        lijst.append(actuer[1])
    return lijst


def lengtes_acteurs(acteurs):
    """Gegeven een lijst van dictionaries met informatie over acteurs,
    geef je een lijst van lengtes van acteurs terug.

    Bijvoorbeeld:
    >>> lengtes_acteurs([{"naam": "Jennifer Lawrence", "leeftijd": 31, "lengte": 175}])
    [175]
    """
    lijst = []
    for acteur in acteurs:
        lijst.append(acteur["lengte"])
    return lijst
