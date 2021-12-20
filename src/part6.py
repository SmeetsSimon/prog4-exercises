def find_problematic_scores(scores):
    """Geef het aantal punten minder dan 5 terug."""
    count = 0
    for i in scores:
        if i < 5:
            count += 1
    return count


def count_ice_cream_flavors(ice_creams):
    """Geef een dictionary terug met voor iedere smaak het aantal ijsjes

    De volgende smaken zijn voorzien: vanille, chocolade, banaan, aardbei
    """
    smaken = {
        "vanille": 0,
        "chocolade": 0,
        "banaan": 0,
        "aardbei": 0,
    }
    for i in ice_creams:
        smaken[i] += 1
    return smaken


def count_words(text):
    """Return het aantal woorden in de tekst"""
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.lower()
    aantal = 0

    for i in text.split():
        aantal += 1
    return aantal


def count_word_frequency(text):
    """Return een dictionary met voor ieder woord het aantal keren dat het voorkomt
    Voor deze versie worden hoofdletters en kleine letters als verschillend beschouwd.

    Dus, voor de tekst "hello hello world World", krijg je de dictionary:
    {
        "hello": 2,
        "world": 1,
        "World": 1,
    }
    """
    dic = {}
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    for i in text.split():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


def count_word_frequency_nocase(text):
    """Return een dictionary met voor ieder woord het aantal keren dat het voorkomt
    Voor deze versie worden hoofdletters en kleine letters als hetzelfde beschouwd.

    Dus, voor de tekst "hello hello world World", krijg je de dictionary:
    {
        "hello": 2,
        "world": 2,
    }
    """
    dic = {}
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.lower()
    for i in text.split():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic