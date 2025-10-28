
from help import afis_choices
from utils import *
from datetime import datetime
import os
from cheltuiala import Cheltuiala

payments = []
old_payments = []

if os.path.exists("Payments.txt"):
    with open("Payments.txt", "r") as f:
        for payment in f:
            items = payment.strip().split("|")
            payments.append(Cheltuiala(int(items[0]), items[1], int(items[2]), datetime.strptime(items[3], "%Y-%m-%d")))

copy_payments(payments, old_payments)

while True:
    afis_choices()
    choice = int(input())
    match choice:
        case 1:
            copy_payments(payments, old_payments)
            add_cheltuiala(payments)
        case 2:
            copy_payments(payments, old_payments)
            modifica_cheltuiala(payments)
        case 3:
            copy_payments(payments, old_payments)
            nr_app = int(input("Nr apartament: "))
            delete_chel_app(payments, nr_app)
            with open("Payments.txt", "r") as f:
                for p in f:
                    print(p.strip())
        case 4:
            copy_payments(payments, old_payments)
            inceput = int(input("Apartament inceput: "))
            sfarsit = int(input("Apartament sfarsit: "))
            for i in range(inceput, sfarsit + 1):
                delete_chel_app(payments, i)
            with open("Payments.txt", "r") as f:
                for p in f:
                    print(p.strip())
        case 5:
            copy_payments(payments, old_payments)
            tip_chel = input("Tip cheltuiala: ")
            delete_tip_chel(payments, tip_chel)
            with open("Payments.txt", "r") as f:
                for p in f:
                    print(p.strip())
        case 6:
            suma_limita = int(input("Suma data: "))
            cheltuieli_totale = sum_total(payments)
            for k, v in cheltuieli_totale.items():
                if v > suma_limita:
                    print(k)
        case 7:
            tip_cheltuiala = input("Tip cheltuiala: ")
            a = tip_cheltuiala.lower()
            cheltuieli_same_tip(payments, a)
        case 8:
            suma = int(input("Suma: "))
            date_string = input("Date: ")
            date_format = "%Y-%m-%d"
            date_object = datetime.strptime(date_string, date_format)
            cheltuieli_inainte_data_suma(payments, suma, date_object)
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
            elim_tip_chel(payments, tip_chel)
        case 13:
            suma = int(input("Suma: "))
            elim_chel_sum_mai_mic(payments, suma)
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
    1|televizor|731|2025-07-30
    """
