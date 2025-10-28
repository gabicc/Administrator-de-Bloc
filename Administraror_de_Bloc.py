from datetime import datetime
import os

class Cheltuiala:
    def __init__(self, apartament, tip, pret, data_aparitie):
        self.apartament = apartament
        self.tip = tip
        self.pret = pret
        self.data_aparitie = data_aparitie

    def get_name(self):
        return self.name

payments = []
old_payments = []

if os.path.exists("Payments.txt"):
    with open("Payments.txt", "r") as f:
        for payment in f:
            items = payment.strip().split("|")
            payments.append(Cheltuiala(int(items[0]), items[1], int(items[2]), datetime.strptime(items[3], "%Y-%m-%d")))

def afis_choices():
    print("\n1. Adaugă cheltuială pentru un apartament")
    print("2. Modifică cheltuială")
    print("3. Șterge toate cheltuielile de la un apartament")
    print("4. Șterge cheltuielile de la apartamente consecutive "
          "(Ex. se dau două numere de apartament 2 și 5 și se șterg toate cheltuielile de la apartamentele 1,2,3,4 și 5)")
    print("5. Șterge cheltuielile de un anumit tip de la toate apartamentele")
    print("6. Tipărește toate apartamentele care au cheltuieli mai mari decât o sumă dată")
    print("7. Tipărește cheltuielile de un anumit tip de la toate apartamentele")
    print("8. Tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o sumă (se dă suma și ziua)")
    print("9. Tipărește suma totală pentru un tip de cheltuială")
    print("10. Tipărește toate apartamentele sortate după un tip de cheltuială")
    print("11. Tipărește totalul de cheltuieli pentru un apartament dat")
    print("12. Elimină toate cheltuielile de un anumit tip")
    print("13. Elimină toate cheltuielile mai mici decât o sumă dată")
    print("14. Reface ultima operație (lista de cheltuieli revine la ce exista înainte de ultima operație care a modificat lista).")
    print("15. Lista totala de cheltuieli")
    print("0. Iesi din aplicatie")
    print("Alege numarul corespunzator unei operatii de mai sus: ")

def add_cheltuiala():
    apartam = int(input("Nr apartament: "))
    newtip = input("Tip(apa/gaz/etc): ")
    newpret = int(input("Pret: "))
    date_string = input("Data aparitie: ")
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    payments.append(Cheltuiala(apartam, newtip, newpret, date_object))

def show_cheltuieli():
    for payment in payments:
        print(f"Nr apartament: {payment.apartament}  Tip: {payment.tip}  Pret: {payment.pret}  Data aparitie: {payment.data_aparitie.strftime('%Y-%m-%d')}")

def sum_total():
    sume = {}
    for p in payments:
        if sume.get(p.apartament) is None:
            sume[p.apartament] = p.pret
        else:
            sume[p.apartament] += p.pret
    return sume

def cheltuieli_inainte_data_suma(suma, date):
    for p in payments:
        if p.data_aparitie < date and p.pret > suma:
            print(f"Nr apartament: {p.apartament}  Tip: {p.tip}  Pret: {p.pret}  Data aparitie: {p.data_aparitie.strftime('%Y-%m-%d')}")

def save_to_file():
    with open("Payments.txt", "w") as f:
        for p in payments:
            strtime = p.data_aparitie.strftime("%Y-%m-%d")
            f.write(f"{p.apartament}|{p.tip}|{p.pret}|{strtime}\n")

def modifica_cheltuiala():
    app = int(input("Apartament: "))
    tip = input("Tip: ")
    pret = int(input("Pret: "))
    date_string = input("Data aparitie: ")
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    for p in payments:
        if p.apartament == app and p.tip == tip and p.data_aparitie == date_object:
            p.pret = pret

def cheltuieli_same_tip(a):
    for p in payments:
        if p.tip.lower() == a:
            print(f"Nr apartament: {p.apartament}  Tip: {p.tip}  Pret: {p.pret}  Data aparitie: {p.data_aparitie.strftime('%Y-%m-%d')}")

def delete_chel_app(nr_app):
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

def delete_tip_chel(tipp):
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

def elim_tip_chel(tip):
    tip = tip.lower()
    new_payments = []
    for p in payments:
        if p.tip.lower() != tip:
            new_payments.append(p)
    for p in new_payments:
        print(f"Nr apartament: {p.apartament}  Tip: {p.tip}  Pret: {p.pret}  Data aparitie: {p.data_aparitie.strftime('%Y-%m-%d')}")

def elim_chel_sum_mai_mic(suma):
    new_payments = []
    for p in payments:
        if p.pret >= suma:
            new_payments.append(p)
    for p in new_payments:
        print(f"Nr apartament: {p.apartament}  Tip: {p.tip}  Pret: {p.pret}  Data aparitie: {p.data_aparitie.strftime('%Y-%m-%d')}")

def copy_payments():
    old_payments.clear()
    for p in payments:
        old_payments.append(p)

copy_payments()

while True:
    afis_choices()
    choice = int(input())
    match choice:
        case 1:
            copy_payments()
            add_cheltuiala()
        case 2:
            copy_payments()
            modifica_cheltuiala()
        case 3:
            copy_payments()
            nr_app = int(input("Nr apartament: "))
            delete_chel_app(nr_app)
            with open("Payments.txt", "r") as f:
                for p in f:
                    print(p.strip())
        case 4:
            copy_payments()
            inceput = int(input("Apartament inceput: "))
            sfarsit = int(input("Apartament sfarsit: "))
            for i in range(inceput, sfarsit + 1):
                delete_chel_app(i)
            with open("Payments.txt", "r") as f:
                for p in f:
                    print(p.strip())
        case 5:
            copy_payments()
            tip_chel = input("Tip cheltuiala: ")
            delete_tip_chel(tip_chel)
            with open("Payments.txt", "r") as f:
                for p in f:
                    print(p.strip())
        case 6:
            suma_limita = int(input("Suma data: "))
            cheltuieli_totale = sum_total()
            for k, v in cheltuieli_totale.items():
                if v > suma_limita:
                    print(k)
        case 7:
            tip_cheltuiala = input("Tip cheltuiala: ")
            a = tip_cheltuiala.lower()
            cheltuieli_same_tip(a)
        case 8:
            suma = int(input("Suma: "))
            date_string = input("Date: ")
            date_format = "%Y-%m-%d"
            date_object = datetime.strptime(date_string, date_format)
            cheltuieli_inainte_data_suma(suma, date_object)
        case 9:
            tip_cheltuiala = input("Tip cheltuiala: ")
            sum_chel_tip = sum_tip_chel(tip_cheltuiala)
            print(f"Suma totala la cheltuielile pt {tip_cheltuiala} este {sum_chel_tip}")
        case 10:
            tip_chel = input("Tip cheltuiala: ")
            tip_chel = tip_chel.lower()
            afis_tip_chel(tip_chel)
        case 11:
            nr_app = int(input("Nr apartament: "))
            sum_apartament = sum_chel_app(nr_app)
            print(f"Suma totala pt toate cheltuielile din apartamentul {nr_app} este {sum_apartament}")
        case 12:
            tip_chel = input("Tip cheltuiala: ")
            elim_tip_chel(tip_chel)
        case 13:
            suma = int(input("Suma: "))
            elim_chel_sum_mai_mic(suma)
        case 14:
            print("Undo")
            payments.clear()
            for p in old_payments:
                payments.append(p)
        case 15:
            show_cheltuieli()
        case 0:
            break
        case _:
            print("Aceasta instructiune nu exista")

    save_to_file()

    # 1) Cerintele: 1, 2
    # 2) Cerintele: 3, 4, 5
    # 3) Cerintele: 6, 7, 8
    # 4) Cerintele: 9, 10, 11
    # 5) Cerintele: 12, 13
    # 6) Cerinta: 14

    """
    Exemplu de conținut pentru Payments.txt:

    1|apa|100|2023-08-13
    1|gaz|120|2025-06-30
    2|apa|120|2025-06-14
    3|telefon|300|2025-07-05
    4|gaz|130|2025-06-14
    5|apa|150|2025-07-31
    6|televizor|300|2025-07-31
    1|televizor|731|2025-07-31
    """
