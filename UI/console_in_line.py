from Domain.rezervare import creeaza_rezervare, to_string
from Logic.CRUD import add_rezervare, delete_rezervare


def print_menu_in_line():
    print("Utilizati comenzile: ")
    print("    - add + valorile adecvate pentru a adauga o rezervare noua")
    print("    - delete + id-ul rezervarii care urmeaza sa fie stearsa")
    print("    - showall pentru a afisa toate rezervarile")
    print("    - exit pentru a iesi din aplicatie")
    print(" ! Toate comenzile trebuie sa fie apelate pe o singura linie, separate prin ';' , ")
    print("iar campurile prin ',' ! FARA ALTI SEPARATORI! ")


def add(id, nume, clasa, pret, checkin, lista):
    '''
    adauga o rezervare in lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: string
    :param checkin: string
    :param lista : lista de rezervari
    :return: o lista care contine atat elemente vechi, cat si rezervarea noua
    '''
    try:
        rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, checkin)
        lista = add_rezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare:", ve)
    return lista


def delete(id, lista):
    '''
    sterge o rezervare dupa ID-ul dat dintr-o lista
    :param id: string: id-ul rezervarii care se va sterge
    :param lista: lista de rezervari
    :return: o lista de rezervari fara rezervarea stearsa
    '''
    lista = delete_rezervare(id, lista)
    return lista


def showall(lista):
    '''
    afiseaza lista
    '''
    for rezervare in lista:
        print(to_string(rezervare))


def run_console_in_line(lista):
    should_run = True
    while should_run:
        print_menu_in_line()
        comanda = input ("Introduceti lista de comenzi: ")
        comenzi = comanda.split(";")
        for fiecare_comanda in comenzi:
            sir_optiune = fiecare_comanda.split(",")
            if sir_optiune[0] == "add":
                lista = add(sir_optiune[1],sir_optiune[2],sir_optiune[3],sir_optiune[4], sir_optiune[5], lista)
            elif sir_optiune[0] == "delete":
                lista = delete(sir_optiune[1], lista)
            elif sir_optiune[0] == "showall":
                showall(lista)
            elif sir_optiune[0] == "exit":
                should_run = False
            else:
                print("Ati introdus o comanda gresita! REINCERCATI")



