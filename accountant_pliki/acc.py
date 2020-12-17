
def zakup(linia, id_prod, cena_prod, ile_prod, stan_konta, magazyn, rejestr):
    rejestr.append("{}\n{}\n{}\n{}".format(linia, id_prod, cena_prod, ile_prod))
    stan_konta = stan_konta - (cena_prod * ile_prod)
    if id_prod not in magazyn:
        magazyn[id_prod] = ile_prod
    else:
        magazyn[id_prod] += ile_prod
    return (stan_konta, magazyn, rejestr) # nawiasy, bo to tupla

def sprzedaz(linia, id_prod, cena_prod, ile_prod, stan_konta, magazyn, rejestr):
    rejestr.append("{}\n{}\n{}\n{}".format(linia, id_prod, cena_prod, ile_prod))
    stan_konta = stan_konta + (cena_prod * ile_prod)
    if id_prod not in magazyn:
         magazyn[id_prod] = ile_prod
         print("Błąd - brak na magazynie")
    elif ile_prod <= magazyn[id_prod]:
         magazyn[id_prod] -= ile_prod
    else:
         print("Błąd - za mało na magazynie")
    return (stan_konta, magazyn, rejestr)

def saldo(linia, kwota, koment, rejestr, stan_konta):
    rejestr.append("{}\n{}\n{}".format(linia, kwota, koment))
    stan_konta += kwota
    return (stan_konta, rejestr)

def odczyt_z_pliku(sciezka):
    odczyt_danych = list()
    rejestr = list()
    magazyn = dict()
    stan_konta = 0
    fp = open(sciezka)
    while True:
        linia = fp.readline().strip()
        odczyt_danych.append(linia)
        if linia != "stop":
            if linia == "saldo":
                kwota = int(fp.readline().strip())
                koment = fp.readline().strip()
                (stan_konta, rejestr) = saldo(
                linia, kwota, koment, rejestr, stan_konta
                )

            elif linia == "zakup":
                id_prod = fp.readline().strip()
                cena_prod = int(fp.readline().strip())
                ile_prod = int(fp.readline().strip())
                (stan_konta, magazyn, rejestr) = zakup(
                linia, id_prod, cena_prod, ile_prod, stan_konta, magazyn,rejestr
                )

            elif linia == "sprzedaz":
                id_prod = fp.readline().strip()
                cena_prod = int(fp.readline().strip())
                ile_prod = int(fp.readline().strip())
                (stan_konta, magazyn, rejestr) = sprzedaz(
                linia, id_prod, cena_prod, ile_prod, stan_konta, magazyn,rejestr
                )
        else:
            break
    else:
        print("Nieprawidłowe dane. Koniec.")
    fp.close()
    return (odczyt_danych, rejestr, magazyn, stan_konta)

def zapis_do_pliku(sciezka, rejestr):
    fp = open(sciezka, "w")
    for linia in rejestr:
        # fp.write(linia + "\n") # spróbuj zrobić zapis z formatem
        fp.write("{}\n".format(linia)) # spróbowałem - pokazać Robertowi - ok
    fp.write("stop")
    fp.close()
