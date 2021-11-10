from Domain.rezervare import to_string
from Logic.CRUD import add_rezervare, delete_rezervare, modify_rezervare
from Logic.functionalitati import trecerea_la_o_clasa_superioara, ieftinire, pret_maxim, lista_ordonata_dupa_pret, \
    suma_pe_fiecare_nume
from Logic.undo_and_redo import do_undo, do_redo


def print_menu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervalorilor facute pe un nume introdus la o clasa superioara")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("6. Determinarea pretului maxim pentru fiecare clasa")
    print("7. Afisarea rezervarilor ordonate descrescator dupa pretul acestora")
    print("8. Afisarea sumelor preturilor pentru fiecare nume")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare rezervari ")
    print("x. Iesire ")


def ui_add_rezervare(lista, undo_list, redo_list):
    try:
        id = input("Introduceti ID-ul: ")
        nume = input("Introduceti numele: ")
        clasa = input("Introduceti clasa: ")
        pret = input("Introduceti pretul: ")
        checkin_facut = input("Ati facut checkin-ul? Raspunde cu da/nu: ")
        lista = add_rezervare(id, nume, clasa, pret, checkin_facut, lista, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare:", ve)
    return lista

def ui_delete_rezervare(lista, undo_list, redo_list):
    try:
        id = input("Introduceti ID-ul rezervarii pe care doriti sa o stergeti: ")
        lista = delete_rezervare(id, lista, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista

def ui_modify_rezervare(lista, undo_list, redo_list):
    try:
        id = input("Introduceti ID-ul rezervarii pe care doriti sa o modificati: ")
        nume = input("Introduceti noul nume: ")
        clasa = input("Introduceti noua clasa: ")
        pret = input("Introduceti noul pret: ")
        checkin_facut = input("Introduceti noua stare a checkin-ului: ")
        lista = modify_rezervare(id, nume, clasa, pret, checkin_facut, lista, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista

def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def ui_trecerea_la_o_clasa_superioara(lista, undo_list, redo_list):
    nume = input("Introudceti numele pentru care se vor aplica schimbarile: ")
    return trecerea_la_o_clasa_superioara(nume, lista, undo_list, redo_list)


def ui_ieftinire(lista, undo_list, redo_list):
    try:
        procentaj = float(input("Introduceti procentajul :"))
        lista = ieftinire(procentaj, lista, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare:", ve)
    return lista


def ui_pret_maxim(lista):
    rezultat = pret_maxim(lista)
    for clasa in rezultat:
        print("Clasa {} are ca pret maxim valoarea : {}".format(clasa, rezultat[clasa]))


def ui_lista_ordonata_dupa_pret(lista):
    rezultat = lista_ordonata_dupa_pret(lista)
    print(rezultat)


def ui_suma_pe_fiecare_nume(lista):
    rezultat = suma_pe_fiecare_nume(lista)
    for nume in rezultat:
        print("Rezervarile facute pe numele {}"
              " au suma totala in valoare de {}".format(nume,rezultat[nume]))


def ui_undo(lista,undo_list, redo_list):
    print()
    undo_rezultat = do_undo(undo_list, redo_list, lista)
    if undo_rezultat is not None:
        print("Operatiunea a fost efectuata cu succes !")
        return undo_rezultat
    return lista


def ui_redo(lista, undo_list , redo_list):
    print()
    redo_result = do_redo(undo_list, redo_list, lista)
    if redo_result is not None:
        print("Operatiunea a fost efectuata cu succes !")
        return redo_result
    return lista


def run_menu(lista, undo_list, redo_list):
    while True:
        print_menu()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = ui_add_rezervare(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_delete_rezervare(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modify_rezervare(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_trecerea_la_o_clasa_superioara(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = ui_ieftinire(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_pret_maxim(lista)
        elif optiune == "7":
            ui_lista_ordonata_dupa_pret(lista)
        elif optiune == "8":
            ui_suma_pe_fiecare_nume(lista)
        elif optiune == "u":
            lista = ui_undo(lista, undo_list, redo_list)
        elif optiune == "r":
            lista = ui_redo(lista, undo_list, redo_list)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiunea nu exista! Reincercati: ")
