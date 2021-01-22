# reader.py <src> <dst> <change1> <change2> ... <changeN>
# Y,X,wartosc" Y to wiersz do zmodyfikowania (liczony od 0, X to kolumna (liczona od 0)

import csv
import json
import pickle
from sys import argv

class FileHandler:

    def modyfikacja(self, lista_zmian):
        for zmiana in lista_zmian:
            zmiana_lista = zmiana.split(",")  # [Y X wartość] lista
            self.zawartosc_pliku[int(zmiana_lista[0])][int(zmiana_lista[1])] \
                = zmiana_lista[2]

    def importuj(self, obj):
        self.zawartosc_pliku = obj.zawartosc_pliku



class FileCSV(FileHandler):

    def odczyt(self, sciezka_o):
        self.zawartosc_pliku = list()
        fp = open(sciezka_o)
        reader = csv.reader(fp)
        for line in reader:
            self.zawartosc_pliku.append(line)
        fp.close()

    def zapis(self, sciezka_z):
        fp = open(sciezka_z, "w", newline="")
        writer = csv.writer(fp)
        writer.writerows(self.zawartosc_pliku)


class FileJSON(FileHandler):

    def odczyt(self, sciezka_o):
        self.zawartosc_pliku = list()
        fp = open(sciezka_o)
        zawartosc_tekst = fp.read()
        self.zawartosc_pliku = json.loads(zawartosc_tekst)
        # for line in reader:
        #    self.zawartosc_pliku.append(line)          # alternatywa dla 39
        fp.close()

    def zapis(self, sciezka_z):     # zrobić jak def odczyt - dumps
        fp = open(sciezka_z, "w", newline="")
        zawartosc_tekst = json.dumps(self.zawartosc_pliku)        # ???
        fp.write(zawartosc_tekst)
        fp.close()


class FilePICKLE(FileHandler):

    def odczyt(self, sciezka_o):
        self.zawartosc_pliku = list()
        fp = open(sciezka_o)
        zawartosc_tekst = fp.read()
        self.zawartosc_pliku = pickle.loads(zawartosc_tekst)
        # self.zawartosc_pliku = pickle.loads(str(zawartosc_tekst))
        fp.close()
        # program nie radzi sobie z odczytem danych pickle, proste rozwiązanie
        # z linii 63 nie pomoogło, ale w zapisie w linii 71 już tak.

    def zapis(self, sciezka_z):     # zrobić jak def odczyt - dumps
        fp = open(sciezka_z, "w", newline="")
        zawartosc_tekst = pickle.dumps(self.zawartosc_pliku)
        fp.write(str(zawartosc_tekst))
        fp.close()

# Pickle ma te same metody jak JSON loads i dumps
# todo
    # Zrobić modyfikację pliku np. z csv do json
    # porównanie ostanich 4 znaków z argv[1]
    # zrobić rozbicie przez split, lub bibl os.path

ext = argv[1].split(".")[-1]
if ext == "csv":
    plik_odczyt = FileCSV()
if ext == "json":
    plik_odczyt = FileJSON()
if ext == "pickle":
    plik_odczyt = FilePICKLE()

ext = argv[2].split(".")[-1]
if ext == "csv":
    plik_zapis = FileCSV()
if ext == "json":
    plik_zapis = FileJSON()
if ext == "pickle":
    plik_zapis = FilePICKLE()


# plik_csv = FileCSV()
plik_odczyt.odczyt(argv[1])
plik_odczyt.modyfikacja(argv[3:])
plik_zapis.importuj(plik_odczyt)
plik_zapis.zapis(argv[2])
