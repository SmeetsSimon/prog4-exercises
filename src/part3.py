# Your exercises should appear in this file.


def list_search(l, value):
    """Return the index of the value in the list"""
    
    return l.index(value)


def phonebook_search(phonebook, search_name):
    """Return het telefoonnummer van de gevraagde persoon

    Als de persoon niet in het telefoonboek staat, geef dan None terug.

    phonebook: een list van lists met hierin naam, telefoonnummer paren
    search_name: de naam van de te zoeken persoon
    """
    for i, j in phonebook:
        if i == search_name:
            return j 
    return None


def phonebook_add(phonebook, name, number):
    """Voeg het telefoonnummer voor 'name' aan de lijst toe.

    Als het koppel name,number al in het telefoonboek zit,
    voeg het dan niet toe, maar toon "data reeds in telefoonboek"
    op het scherm.
    Als de telefoonnummer reeds voor een ander persoon in het telefoonboek
    staat, voeg het dan niet toe, maar toon "ander persoon met deze nummer
    in telefoonboek" op het scherm.
    """
    
    for a, b  in phonebook:
        
        if a == name:
            print("data reds in telefoonboek")
            return

        if b == number:
            print("andere persoon met deze nummer in telefoonboek")

    phonebook.append([name, number])   

    return phonebook

def phonebook_remove(phonebook, name, number):
    """Verwijder het koppel name,number van het telefoonboek.

    Indien het koppel niet voorkomt, print dan
    "persoon niet gevonden in telefoonboek" op het scherm.
    """
    a = phonebook_search(phonebook, name)
    if a != number:
        print("persoon niet gevonden in telefoonboek")
        return
    return phonebook.remove([name, number])
    
    


def phonebook_print(phonebook, search_name):
    """Print de telefoonnummers van de gevraagde persoon

    Als de persoon niet in het telefoonboek staat, toon dan "niets gevonden".

    phonebook: een list van lists met hierin naam, telefoonnummer paren
    search_name: de naam van de te zoeken persoon
    """
    find = False
    for a, b in phonebook:
        if a == search_name:
            print(b)
            find = True 
    if find == False:
        print("niets gevonden")
