import sys

    #zmienne początkowe
stan_konta = 0
id_prod = 0
ile_prod = 0
cena_prod = 0
stan_mag = 0
rejestr = list()
magazyn = dict()

    #import danych argv
#for index, elem in enumerate(sys.argv):
#    print("{}: {}".format(index, elem))
print("")
    #import danych wejściowych
while True:
    linia = input()
    if linia != "stop":
            # akcja
        if linia == "saldo":
            kwota = int(input())
            koment = input()
            rejestr.append("{}\n{}\n{}".format(linia, kwota, koment))
            stan_konta += kwota # przesunięcie z nad rejestr.append pod kątem przeglądu

        elif linia == "zakup":
            id_prod = input()
            cena_prod = int(input())
            ile_prod = int(input())
            rejestr.append("{}\n{}\n{}\n{}".format(
                linia, id_prod, cena_prod, ile_prod)
            )
            stan_konta = stan_konta - (cena_prod * ile_prod)
            if id_prod not in magazyn:
                magazyn[id_prod] = ile_prod
            else:
                magazyn[id_prod] += ile_prod

        elif linia == "sprzedaz":
            id_prod = input()
            cena_prod = int(input())
            ile_prod = int(input())
            rejestr.append("{}\n{}\n{}\n{}".format(
                linia, id_prod, cena_prod, ile_prod)
            )
#            stan_konta = stan_konta + (cena_prod * ile_prod) # poprawka, bo się będzie naliczać mimo braku na stanie
            if id_prod not in magazyn:
                magazyn[id_prod] = ile_prod
                stan_konta = stan_konta + (cena_prod * ile_prod)
                print("Błąd - brak na magazynie")
                break
            elif ile_prod <= magazyn[id_prod]:
                magazyn[id_prod] -= ile_prod
                stan_konta = stan_konta + (cena_prod * ile_prod)
            else:
                print("Błąd - za mało na magazynie")
                break
    else:
        break
else:
    print("Nieprawidłowe dane. Koniec.")

if sys.argv[1] == "zakup": # kat.2
    id_prod = sys.argv[2]
    cena_prod = int(sys.argv[3])
    ile_prod = int(sys.argv[4])
    rejestr.append("{}\n{}\n{}\n{}".format(
        sys.argv[1], id_prod, cena_prod, ile_prod)
    )
    stan_konta = stan_konta - (cena_prod * ile_prod)
#    print(magazyn)
    if id_prod not in magazyn:
        magazyn[id_prod] = ile_prod
    else:
        magazyn[id_prod] += ile_prod
    for x in rejestr:
        print(x)
    print("stop")

if sys.argv[1] == "magazyn": # kat. 4
    for id_prod in sys.argv[2:]:
        if id_prod in magazyn:
            print("{}: {}".format(id_prod, magazyn[id_prod]))
        else:
            print("{}: {}".format(id_prod, 0))

if sys.argv[1] == "sprzedaz": # kat. 3
    id_prod = sys.argv[2]
    cena_prod = int(sys.argv[3])
    ile_prod = int(sys.argv[4])
    rejestr.append("{}\n{}\n{}\n{}".format(
        sys.argv[1], id_prod, cena_prod, ile_prod)
    )
#    stan_konta = stan_konta + (cena_prod * ile_prod)
    if id_prod not in magazyn:
        magazyn[id_prod] = ile_prod
        print("Błąd - brak na magazynie")
#        break #-- break outside the loop - tylko dla pętli for i while
    elif ile_prod <= magazyn[id_prod]:
        stan_konta = stan_konta + (cena_prod * ile_prod)
        magazyn[id_prod] -= ile_prod
    else:
        print("Błąd - za mało na magazynie")
        print("Sprzedaż z argv niezrealizowana")
#        break
    for x in rejestr:
        print(x)
        print("stop")

if sys.argv[1] == "saldo": # kat. 1
#    for stan_konta in rejestr:
#        print("{}".format(stan_konta))
    print("{} saldo końcowe".format(stan_konta))

if sys.argv[1] == "konto": # kat.5
    print("{} saldo końcowe".format(stan_konta))

if sys.argv[1] == "przeglad": # kat. 6
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    for linia in range(2):
        print(rejestr[linia])
#        print("{} - {} - {}".format(strip(linia), strip(stan_konta), strip(koment)))
print("")
print("---")

#print(rejestr)
#print(stan_konta)

#print(magazyn)
#print(magazyn[id_prod], [ile_prod])
#for id_prod in magazyn:
#    print("{} {}".format(id_prod, ile_prod))


#a = sys.argv[1] # akcja   saldo   zakup   sprzedaz    magazyn  konto   przeglad
#b = sys.argv[2] # id_prod         jetson  jetson      jetson           0
#c = sys.argv[3] # cena_prod       40000   50000       raspberry        1
#d = sys.argv[4] # ile_prod        5       4           arduino
