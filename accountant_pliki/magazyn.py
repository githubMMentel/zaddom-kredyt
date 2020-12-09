import sys
from acc import odczyt_z_pliku # magazyn (po przecinku, jeśli ma być)

sciezka = sys.argv[1]    # "3/in.txt"
(odczyt_danych, rejestr, magazyn, stan_konta) = odczyt_z_pliku(sciezka)

linia = "magazyn"
for id_prod in sys.argv[2:]:
    if id_prod in magazyn:
        print("{}: {}".format(id_prod, magazyn[id_prod]))
    else:
        print("{}: {} i nigdy nie było".format(id_prod, 0))
#fp.close()
