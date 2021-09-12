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
    pass


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
    pass


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
    return 100


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
    return None
