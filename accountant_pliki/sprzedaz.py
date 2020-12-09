import sys
from acc import odczyt_z_pliku, sprzedaz, zapis_do_pliku

sciezka = sys.argv[1]   # "3/in.txt"
(odczyt_danych, rejestr, magazyn, stan_konta) = odczyt_z_pliku(sciezka)

linia = "sprzedaz"
id_prod = sys.argv[2]
cena_prod = int(sys.argv[3])
ile_prod = int(sys.argv[4])
(stan_konta, magazyn, rejestr) = sprzedaz(
linia, id_prod, cena_prod, ile_prod, stan_konta, magazyn, rejestr
)
zapis_do_pliku(sciezka, rejestr)
for x in rejestr:
    print(x) # pisać do pliku przez - fd write
    print("stop")