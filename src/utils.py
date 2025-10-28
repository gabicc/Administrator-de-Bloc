
from datetime import datetime

from cheltuiala import Cheltuiala


#payments = []
#old_payments = []

def add_cheltuiala(payments):
    apartam = int(input("Nr apartament: "))
    newtip = input("Tip(apa/gaz/etc): ")
    newpret = int(input("Pret: "))
    date_string = input("Data aparitie: ")
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    payments.append(Cheltuiala(apartam, newtip, newpret, date_object))

def show_cheltuieli(payments):
    for payment in payments:
        print(f"Nr apartament: {payment.apartament}  Tip: {payment.tip}  Pret: {payment.pret}  Data aparitie: {payment.data_aparitie.strftime('%Y-%m-%d')}")

def sum_total(payments):
    sume = {}
    for p in payments:
        if sume.get(p.apartament) is None:
            sume[p.apartament] = p.pret
        else:
            sume[p.apartament] += p.pret
    return sume

def cheltuieli_inainte_data_suma(payments, suma, date):
    for p in payments:
        if p.data_aparitie < date and p.pret > suma:
            print(f"Nr apartament: {p.apartament}  Tip: {p.tip}  Pret: {p.pret}  Data aparitie: {p.data_aparitie.strftime('%Y-%m-%d')}")

def save_to_file(payments):
    with open("Payments.txt", "w") as f:
        for p in payments:
            strtime = p.data_aparitie.strftime("%Y-%m-%d")
            f.write(f"{p.apartament}|{p.tip}|{p.pret}|{strtime}\n")

def modifica_cheltuiala(payments):
    app = int(input("Apartament: "))
    tip = input("Tip: ")
    pret = int(input("Pret: "))
    date_string = input("Data aparitie: ")
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    for i, p in enumerate(payments):
        if p.apartament == app and p.tip == tip and p.data_aparitie == date_object:
            #p.pret = pret
            payments.remove(p)
            payments.insert(i, Cheltuiala(p.apartament, p.tip, pret, p.data_aparitie))

def cheltuieli_same_tip(payments, a):
    for p in payments:
        if p.tip.lower() == a:
            print(f"Nr apartament: {p.apartament}  Tip: {p.tip}  Pret: {p.pret}  Data aparitie: {p.data_aparitie.strftime('%Y-%m-%d')}")

def delete_chel_app(payments, nr_app):
    with open("Payments.txt", "r") as f:
        lines = f.readlines()
    with open("Payments.txt", "w") as f:
        for payment in lines:
            items = payment.strip().split("|")
            if int(items[0]) != nr_app:
                f.write(payment)
    payments.clear()
    with open("Payments.txt", "r") as f:
        for payment in f:
            items = payment.strip().split("|")
            payments.append(Cheltuiala(int(items[0]), items[1], int(items[2]), datetime.strptime(items[3], "%Y-%m-%d")))

def delete_tip_chel(payments, tipp):
    with open("Payments.txt", "r") as f:
        lines = f.readlines()
    with open("Payments.txt", "w") as f:
        for payment in lines:
            items = payment.strip().split("|")
            if items[1] != tipp:
                f.write(payment)
    payments.clear()
    with open("Payments.txt", "r") as f:
        for payment in f:
            items = payment.strip().split("|")
            payments.append(Cheltuiala(int(items[0]), items[1], int(items[2]), datetime.strptime(items[3], "%Y-%m-%d")))

def sum_tip_chel(tipp):
    total = 0
    with open("Payments.txt", "r") as f:
        for payment in f:
            items = payment.strip().split("|")
            if items[1] == tipp:
                total += int(items[2])
    return total

def sum_chel_app(nr_app):
    total = 0
    with open("Payments.txt", "r") as f:
        for payment in f:
            items = payment.strip().split("|")
            if int(items[0]) == nr_app:
                total += int(items[2])
    return total

def afis_tip_chel(tip_chel):
    with open("Payments.txt", "r") as f:
        for payment in f:
            items = payment.strip().split("|")
            if items[1] == tip_chel:
                print(payment)

def elim_tip_chel(payments, tip):
    tip = tip.lower()
    new_payments = []
    for p in payments:
        if p.tip.lower() != tip:
            new_payments.append(p)
    for p in new_payments:
        print(f"Nr apartament: {p.apartament}  Tip: {p.tip}  Pret: {p.pret}  Data aparitie: {p.data_aparitie.strftime('%Y-%m-%d')}")

def elim_chel_sum_mai_mic(payments, suma):
    new_payments = []
    for p in payments:
        if p.pret >= suma:
            new_payments.append(p)
    for p in new_payments:
        print(f"Nr apartament: {p.apartament}  Tip: {p.tip}  Pret: {p.pret}  Data aparitie: {p.data_aparitie.strftime('%Y-%m-%d')}")

def copy_payments(payments, old_payments):
    old_payments.clear()
    for p in payments:
        old_payments.append(p)