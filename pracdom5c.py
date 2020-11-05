# program na pisany na bazie kodu Roberta Górzyńskiego

# zmienne początkowe
liczba_paczek = 0
obecna = 0
max_pustych = -1
max_paczka = -1
suma_pustych = 0
suma_pustych_e = 0
suma_obecna = 0

# początek
print("Podaj wagi produktów do pakowania w przedziale 1-10 kg:")

# warunek główny
while True:

# warunek wagi produktu
    waga = int(input())
    if waga == 0:
        print("Koniec ładowania.")
        break
    if waga < 1:
        print("Błąd. Produkt za lekki.")
        continue
    if waga > 10:
        print("Błąd. Produkt za ciężki.")
        continue

# liczymy wagę w paczce
    obecna += waga
    if obecna <= 20: # poprawione z parametru: waga
        continue
    obecna -= waga
    suma_obecna += obecna
    print("W obecnej paczce jest {} kg.".format(obecna))
    if max_pustych < 20 - obecna:
        max_pustych = 20 - obecna
        max_paczka = liczba_paczek
        suma_pustych += max_pustych
    obecna = waga
    suma_pustych = max_pustych
    liczba_paczek += 1
    print("Obecna paczka nr {}".format(liczba_paczek))
    print("Niedopakowano {} kg.".format(max_pustych))
    print("")
    print("Do nowej paczki przenosimy {} kg.".format(obecna))

# warunek ostatniej paczki
if obecna:
    liczba_paczek += 1
    print("W obecnej paczce jest {} kg.".format(obecna))
    print("Obecna paczka nr {}".format(liczba_paczek))
    print("Niedopakowano {} kg.".format(20 - obecna))
    if max_pustych < 20 - obecna:
        max_pustych = 20 - obecna
        max_paczka = liczba_paczek
        suma_obecna += obecna
        suma_pustych = suma_pustych + (20 - obecna)
suma_pustych_e = suma_pustych # no za cholerę nie chce działać

# wydruk podsumowania
print("")
print("Liczba wysłanych paczek {}.".format(liczba_paczek))
print("Liczba wysłanych kilogramów {}.".format(suma_obecna))
#print("Suma niedopakowanych kilogramów {}.".format(suma_pustych_e))
print("Suma niedopakowanych kilogramów {}.".format((liczba_paczek) * 20 - suma_obecna))
#print("Najbardziej niedopakowana paczka nr {}. Brakowało w niej {} kg.".format(
#    ?, ?)) - no nie, bo nie umiem
