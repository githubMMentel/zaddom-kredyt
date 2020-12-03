import sys

class Wychowawca:
    def __init__(self, imie_nazwisko): #wiele klas
        self.imie_nazwisko = imie_nazwisko
        self.klasa_numer = ""

    def wydruk(self):
        print("{} jest wychowawcą klasy {}.".format(
            self.imie_nazwisko, self.klasa_numer
        ))

    def pobranie(self, klasy_slownik):
        self.klasa_numer = input()


class Nauczyciel:
    def __init__(self, imie_nazwisko): #wiele klas
        self.imie_nazwisko = imie_nazwisko
        #self.przedmiot = []
        self.przedmiot = ""
        self.klasy = []

    def wydruk(self):
        print("{} jest nauczycielem przedmiotu {} w klasie {}.".format(
            self.imie_nazwisko, self.przedmiot, self.klasy
        ))

    def pobranie(self, klasy_slownik):
        #x = input()
        #self.przedmiot.appedn(x)
        self.przedmiot = input()
        klasa_numer = input()
        while klasa_numer:
            if klasa_numer in klasy_slownik:
                klasa_obiekt = klasy_slownik[klasa_numer]
            else:
                klasa_obiekt = Clasroom(klasa_numer)
                klasy[klasa_numer] = klasa_obiekt
            self.klasy.append(klasa_obiekt)
            klasa_obiekt.nauczyciele.append(self)
            klasa_numer = input()


class Uczen:
    def __init__(self, imie_nazwisko): #jedna klasa
        self.imie_nazwisko = imie_nazwisko
        self.klasa_numer = ""

    def wydruk(self):
        print("{} jest uczniem klasy {}.".format(
            self.imie_nazwisko, self.klasa_numer
        ))

    def pobranie(self, klasy):
        self.klasa_numer = input()

class Clasroom:
    def __init__(self, klasa_numer):
        self.klasa_numer = klasa_numer
        self.wychowawca = None
        self.nauczyciele = []
        self.uczniowie = []


klasy_slownik = dict()
#wychowawcy = list()
#nauczyciele = list()
#uczniowie = list()
osoby = dict()
#klasa_numer = list()

while True:
#    print("Nowy użytkownik")
#    print("Podaj funkcję, a następnie imię i nazwisko")
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









#if sys.argv in osoby.items([klasa_numer]):

#osoby["Adam Mickiewicz"].wydruk()
print(osoby["Adam Mickiewicz"].__dict__)
print(klasy_slownik["1a"].__dict__)
#osoby.wydruk(:)

'''
for osoba in osoby:
    osoba.wydruk()
    
for wychowawca in wychowawcy:
    wychowawca.wydruk()

for nauczyciel in nauczyciele:
    nauczyciel.wydruk()

#print(uczniowie)
#print(wychowawcy)
#print(nauczyciele)
'''


'''
while true:
    print("Podaj kolejno: funkcję, nazwisko, imię")
    print("Aby zakończyć, wpisz \"koniec\"")
    funkcja = input()
    if funkcja == uczen:
        imie_nazwisko = input()
        #print("Podaj klasę")
        klasa_numer = input()
        if imie_nazwisko not in uczniowie:
            uczen = 
            uczniowie.append(imie_nazwisko)
            # no ale co z klasą?
        else:
            break
    if funkcja == nauczyciel:





do argv
if sys.argv in klasy:
    #wypisz wychowawcę
    #wypisz uczniów w klasie
    
elif sys.argv in wychowawcy:
    #wypisz uczniów wychowawcy

elif sys.argv in nauczyciele:
    #wypisz klasy, które uczy
    #wypisz wychowawców klas, które uczy

elif sys.argv in uczniowie:
    #wypisz lekcje, które ma
    #wypisz nauczycieli tych lekcji

else:
    print("Błędne dane")
    break
'''
