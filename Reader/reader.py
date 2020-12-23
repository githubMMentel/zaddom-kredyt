# reader.py <src> <dst> <change1> <change2> ... <changeN>
# Y,X,wartosc" Y to wiersz do zmodyfikowania (liczony od 0, X to kolumna (liczona od 0)

import csv
from sys import argv

# import re


def odczyt():
    sciezka = argv[1]
    zawartosc_pliku = list()
    # sciezka = "addresses.csv"
    fp = open(sciezka)
    reader = csv.reader(fp)
    for line in reader:
        zawartosc_pliku.append(line)
    fp.close()
    return zawartosc_pliku


def zapis(kontakty):
    sciezka2 = argv[2]
    # sciezka2 = "addresses2.csv" # do zakomentowania po uruchomieniu linii 19
    fp = open(sciezka2, "w", newline="")
    writer = csv.writer(fp)
    writer.writerows(kontakty)
    """
    for line in kontakty:
        writer.writerow(kontakty)       # Zapytać Roberta, czy dobrze rozwiązana pętla

#    writer.writerow(["a", "b", "c"])
    """


def modyfikacja(kontakty, lista_zmian):
    for zmiana in lista_zmian:
        zmiana_lista = zmiana.split(",")  # [Y X wartość] lista
        kontakty[int(zmiana_lista[0])][int(zmiana_lista[1])] = zmiana_lista[2]
    return kontakty


kontakty = odczyt()  # lista, której elementy również są listami
kontakty = modyfikacja(kontakty, argv[3:])
print(kontakty)
zapis(kontakty)

# doczytać z pakietu csv o writerows
