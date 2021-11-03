from Domain.rezervare import to_string
from Logic.CRUD import add_rezervare, delete_rezervare, modify_rezervare
from Logic.functionalitati import trecerea_la_o_clasa_superioara, ieftinire


def print_menu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervalorilor facute pe un nume introdus la o clasa superioara")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("a. Afisare rezervari ")
    print("x. Iesire ")


def ui_add_rezervare(lista):
    try:
        id = input("Introduceti ID-ul: ")
        nume = input("Introduceti numele: ")
        clasa = input("Introduceti clasa: ")
        pret = input("Introduceti pretul: ")
        checkin_facut = input("Ati facut checkin-ul? Raspunde cu da/nu: ")
        return add_rezervare(id, nume, clasa, pret, checkin_facut, lista)
    except ValueError as ve:
        print("Eroare:", ve)
    return lista

def ui_delete_rezervare(lista):
    try:
        id = input("Introduceti ID-ul rezervarii pe care doriti sa o stergeti: ")
        return delete_rezervare(id, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista

def ui_modify_rezervare(lista):
    try:
        id = input("Introduceti ID-ul rezervarii pe care doriti sa o modificati: ")
        nume = input("Introduceti noul nume: ")
        clasa = input("Introduceti noua clasa: ")
        pret = input("Introduceti noul pret: ")
        checkin_facut = input("Introduceti noua stare a checkin-ului: ")
        return modify_rezervare(id, nume, clasa, pret, checkin_facut, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista

def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def ui_trecerea_la_o_clasa_superioara(lista):
    nume = input("Introudceti numele pentru care se vor aplica schimbarile: ")
    return trecerea_la_o_clasa_superioara(nume, lista)


def ui_ieftinire(lista):
    try:
        procentaj = float(input ("Introduceti procentajul :"))
        return ieftinire(procentaj, lista)
    except ValueError as ve:
        print("Eroare:", ve)
    return lista
def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = ui_add_rezervare(lista)
        elif optiune == "2":
            lista = ui_delete_rezervare(lista)
        elif optiune == "3":
            lista = ui_modify_rezervare(lista)
        elif optiune == "4":
            lista = ui_trecerea_la_o_clasa_superioara(lista)
        elif optiune == "5":
            lista = ui_ieftinire(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiunea nu exista! Reincercati: ")
