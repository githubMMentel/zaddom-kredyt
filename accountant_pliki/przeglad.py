import sys
from acc import odczyt_z_pliku

sciezka = sys.argv[1]    # "3/in.txt"
(odczyt_danych, rejestr, magazyn, stan_konta) = odczyt_z_pliku(sciezka)

linia = "przeglad"
a = int(sys.argv[2])
b = int(sys.argv[3])
for linia in range(a,b+1):
    print(rejestr[linia])

