import sys
from acc import odczyt_z_pliku

sciezka = sys.argv[1]    # "3/in.txt"
(odczyt_danych, rejestr, magazyn, stan_konta) = odczyt_z_pliku(sciezka)

linia = "konto"
print("{} saldo końcowe".format(stan_konta))

#fp = close()
