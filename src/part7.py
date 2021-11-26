def write_rick_and_morty(filename):
    """Schrijf de tekst "Rick and Morty" naar het tekstbestand met naam filename"""
    bestand = open(filename, "wt")
    bestand.write("Rick and Morty")
    return bestand


def write_numbers(filename):
    """Schrijf de getallen van 0 tot en met 99 in het bestand met naam filename.

    Schrijf ieder getal op een aparte regel.

    Bijvoorbeeld:
    0
    1
    2
    ...
    99
    """
    bestand = open(filename, "wt")
    for i in range(100):
        bestand.write(f"{i}\n")
    return bestand


def write_numbers_and_squares(filename):
    """Schrijf de getallen gevolgd door de kwadraten naar het bestand filename.

    Schrijf ieder getal en kwadraat ervan gescheiden door een komma op een aparte regel.

    Bijvoorbeeld:
    0,0
    1,1
    2,4
    3,9
    4,16
    ...
    """
    bestand = open(filename, "wt")
    for i in range(100):
        bestand.write(f"{i},{i**2}\n")
    return bestand


def sum_numbers_from_file(filename):
    """Geef de som terug van alle getallen in bestand met naam filename

    De getallen staan allen op aparte regels.

    Bijvoorbeeld, een bestand getallen.txt met inhoud:
    100
    20
    8

    Zou bij oproep read_numbers('getallen.txt') 128 teruggeven, dus:
    >> v = read_numbers('getallen.txt')
    >> print(v) # toont 128
    """
    bestand = open(filename, "rt")
    v = bestand.readlines()
    som = 0
    for i in v:
        try:
            i = int(i)
        except ValueError:
            continue
        som+= int(i)
    bestand.close()
    return som


def sum_two_columns_of_numbers_from_file(filename):
    """Geef twee sommen terug van de twee kolommen in bestand met naam filename

    De getallen van alle kolommen staan allen op aparte regels. De kolommen
    zijn gescheiden door komma's.

    Bijvoorbeeld, een bestand getallen.txt met inhoud:
    12,99
    8,1
    7,4

    Heeft twee kolommen, de som van de getallen van kolom 1 is 27, de som
    van de getallen in kolom 2 is 104.

    >> v = sum_two_columns_of_numbers_from_file('getallen.txt')
    >> print(v) # toont (27, 104)
    """
    bestand = open(filename, "rt")
    v = bestand.readlines()
    som1 = 0
    som2 = 0
    for i in v:
        a, b = i.split(",")
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            continue
        som1 += a 
        som2 += b
    bestand.close()
    return som1, som2


def count_words_from_file(filename):
    """Geef het aantal woorden terug in bestand met naam filename"""
    n = 0
    with open(filename, "rt") as f:
        lines = f.readlines()
        for l in lines:
            words = l.split()
            n += len(words)
    return n


def count_word_frequency_from_file(filename):
    """Geef een dictionary terug met per woord het aantal keer dat het woord voorkomt

    Bijvoorbeeld voor een bestand met inhoud:
    Ik drink veel koffie en veel bruiswater. En veel koffie. En ook koffie.

    {
        "ik": 1,
        "en": 3,
        "koffie": 3,
        "drink": 1,
        "veel": 3,
        ...
    }

    Tips:
    - maak alle woorden lowercase
    - verwijder alle leestekens, zeker ",.?"
    - verwijder de newlines '\\n' mbv de method strip()
    """
    freq = {}
    with open(filename, "rt") as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            l = l.lower()
            l = l.replace(",", " ").replace("?", " ").replace(".", " ")
            words = l.split()
            for w in words:
                if w in freq:
                    freq[w] += 1
                else:
                    freq[w] = 1
    return freq
