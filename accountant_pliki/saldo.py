import sys
from acc import odczyt_z_pliku, saldo, zapis_do_pliku

sciezka = sys.argv[1]     # "3/in.txt"
(odczyt_danych, rejestr, magazyn, stan_konta) = odczyt_z_pliku(sciezka)

kwota = int(sys.argv[2])
koment = sys.argv[3]
linia = "saldo"
(stan_konta, rejestr) = saldo(linia, kwota, koment, rejestr, stan_konta)
zapis_do_pliku(sciezka, rejestr)
print("{} saldo końcowe".format(stan_konta))