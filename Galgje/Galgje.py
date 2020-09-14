'''
goede letters lege variabele

lijst met geheime woorden maken
eers het gehijmen woordt uit de lijst van gehijmen woorden kiezen

maak de galg(aantalfouten) -> functie

0
=========

1
 |/
 |
 |
 |
 |
=========

2
 _______
 |/
 |
 |
 |
 |
=========
3

_______
 |/   |
 |
 |
 |
 |
=========
4

_______
 |/   |
 |    @
 |
 |
 |
=========
5

_______
 |/   |
 |    @
 |   -+-
 |   /\
 |
=========

herhaal steeds:
    teken de galg
    (teken lijntjes)
    letter = vraag om het eerste leter

    als letter in het woord:   (if letter in woord: )
        boodschap printen
        letter toevoegen aan goed geraden letters
    zo niet:
        zet de leter in de lijst van de fouten leters

    als het hele woord geraden is:
        zeg dan dat het goed is en laat dit zien:

        !!! Goed !!!
        stop het spel  (break)
    als het fout is zeg dan:

    ••• fout •••

    als hij dit laat zien:

    _______
     |/   |
     |    @
     |   -+-
     |   /\
     |
    =========

    zeg:

    ••• fout •••

'''
import random

woord = ["hallo", "fijn", "apen","jij","ons","uil","kat","vis"]

geheim_woord = random.choice(woord)


def galg (aantal_fout):
    if aantal_fout == 0:
        return '''========='''
    if aantal_fout == 1:
        return '''|/
 |
 |
 |
 |
========='''
    if aantal_fout == 2:
        return '''_______
 |/
 |
 |
 |
 |
========='''
    if aantal_fout == 3:
        return '''_______
 |/   |
 |
 |
 |
 |
========='''
    if aantal_fout == 4:
        return '''_______
 |/   |
 |    @
 |
 |
 |
========='''
    if aantal_fout == 5:
        return '''_______
 |/   |
 |    @
 |   -+-
 |   /\\
 |
========='''

aantal_fout = 0
aantal_goed = 0
geraaden_letter = ""

while True:

    # letters = list(geheim_woord)
    # legeLetters = ['- '] * len(letters)
    # samengesteld = ''.join(letters)
    # legeLetters[2] = letters[2]

    het_woord = ""
    for letter in geheim_woord:
        if letter in geraaden_letter:
            het_woord += letter
        else:
            het_woord += "_ "

    if het_woord == geheim_woord:
        print("••• goed •••")
        print(" ")
        print("letters goed " + str(aantal_goed))
        print("letters fout " + str(aantal_fout))
        break

    print(het_woord)
    letter = input("schijf je letter: ")

    #print(geheim_woord)

    if not letter.isalpha():
        print ("doe alleen maar letters in AUB")
        aantal_fout = aantal_fout + 1
    elif letter in geheim_woord:
        print(letter)
        aantal_goed = aantal_goed + 1
        print(galg(aantal_fout))
        geraaden_letter += letter
    else:
        print(letter)
        aantal_fout = aantal_fout + 1
        print(galg(aantal_fout))

    if aantal_fout == 5:
        print(galg(aantal_fout))
        print("•••fout•••")
        print (" ")
        print("letters goed " + str(aantal_goed))
        print("letters fout " + str(aantal_fout))
        print(str(geheim_woord))
        break





