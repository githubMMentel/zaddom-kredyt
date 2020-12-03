import sys

class Wychowawca:
    def __init__(self, imie_nazwisko): #wiele klas
        self.imie_nazwisko = imie_nazwisko
        self.klasa_wychowawcy = ""

    def wydruk(self):
        print("{} jest wychowawcą klasy {}.".format(
            self.imie_nazwisko, self.klasa_wychowawcy.klasa_numer
        ))
        print("W klasie ma uczniów:")
        for uczen in self.klasa_wychowawcy.uczniowie:
            print("{}; ".format(uczen.imie_nazwisko), end="")
        print(" ")

    def pobranie(self, klasy_slownik):
        klasa_numer = input()
        if klasa_numer in klasy_slownik:
            klasa_obiekt = klasy_slownik[klasa_numer]
        else:
            klasa_obiekt = Classroom(klasa_numer)
            klasy_slownik[klasa_numer] = klasa_obiekt
        self.klasa_wychowawcy = klasa_obiekt
        klasa_obiekt.wychowawca = self


class Nauczyciel:
    def __init__(self, imie_nazwisko): #wiele klas
        self.imie_nazwisko = imie_nazwisko
        self.przedmiot = ""
        self.klasy = []

    def wydruk(self):
        print("{} jest nauczycielem przedmiotu {} w klasie:".format(
            self.imie_nazwisko, self.przedmiot))
        for nr_k in self.klasy:
            print("- {}, gdzie wychowawcą jest {}".format(
                nr_k.klasa_numer, nr_k.wychowawca.imie_nazwisko
            ))

    def pobranie(self, klasy_slownik):
        self.przedmiot = input()
        klasa_numer = input()
        while klasa_numer:
            if klasa_numer in klasy_slownik:
                klasa_obiekt = klasy_slownik[klasa_numer]
            else:
                klasa_obiekt = Classroom(klasa_numer)
                klasy_slownik[klasa_numer] = klasa_obiekt
            self.klasy.append(klasa_obiekt)
            klasa_obiekt.nauczyciele.append(self)
            klasa_numer = input()


class Uczen:
    def __init__(self, imie_nazwisko): #jedna klasa
        self.imie_nazwisko = imie_nazwisko
        self.klasa_numer = ""

    def wydruk(self):
        print("{} jest uczniem klasy {}. \nMa lekcje:".format(
            self.imie_nazwisko, self.klasa_numer.klasa_numer
        ))
        for nauczyciel in self.klasa_numer.nauczyciele:
            print("- {} z nauczycielem {};".format(
                nauczyciel.przedmiot, nauczyciel.imie_nazwisko
            ))

    def pobranie(self, klasy):
        klasa_numer = input()
        if klasa_numer in klasy_slownik:
            klasa_obiekt = klasy_slownik[klasa_numer]
        else:
            klasa_obiekt = Classroom(klasa_numer)
            klasy_slownik[klasa_numer] = klasa_obiekt
        self.klasa_numer = klasa_obiekt
        klasa_obiekt.uczniowie.append(self)


class Classroom:
    def __init__(self, klasa_numer):
        self.klasa_numer = klasa_numer
        self.wychowawca = ""
        self.nauczyciele = []
        self.uczniowie = []

    def wydruk(self):
        print("Wychowawcą klasy {} jest {}.".format(
            self.klasa_numer, self.wychowawca.imie_nazwisko
        ))
        print("W klasie {} znajdują się uczniowie:".format(self.klasa_numer))
        for uczen in self.uczniowie:
            print(uczen.imie_nazwisko, end="; ")
        print(" ")


osoby = dict()
klasy_slownik = dict()
#wychowawcy = list()
#nauczyciele = list()
#uczniowie = list()
#klasa_numer = list()

while True:
    funkcja = input()
    if not funkcja:
        break
    imie_nazwisko = input()

    if funkcja == "uczen":
        osoba = Uczen(imie_nazwisko)
    elif funkcja == "wychowawca":
        osoba = Wychowawca(imie_nazwisko)
    elif funkcja == "nauczyciel":
        osoba = Nauczyciel(imie_nazwisko)
    osoba.pobranie(klasy_slownik)
    osoby[imie_nazwisko] = osoba

if (sys.argv[1]) in klasy_slownik:
    #print(klasy_slownik[sys.argv[1]].wychowawca.imie_nazwisko)
    klasy_slownik[sys.argv[1]].wydruk()
else:
    dane_os = sys.argv[1] + " " + sys.argv[2]
    osoby[dane_os].wydruk()
