
import sys
tryb = sys.argv[1]


#zmienne początkowe
id_prod = tuple(
    "prod_1", "cena_1",
    "prod_2", "cena_2",
    "prod_3", "cena_3",
    "prod_4", "cena_4",
)
saldo = 0
id_prod = 0
ile_prod = 0
cena_prod = 0


if saldo:
    print("Podaj kwotę")
    saldo = int(input())
    print("Komentarz")
    komentarz = str(input())




if zakup:


if sprzedaz:
    print("Podaj identyfikator produktu:")
    id_prod = input(str())
    print("Podaj cenę produktu:")
    cena_prod = input(int())
    print("Podaj ilośc produktów:")
    ile_prod = input(int())

    saldo = saldo + (cena_prod * ile_prod)
else:
    print("Nieprawidłowe dane. Koniec.")


