from Domain.rezervare import creeaza_rezervare, get_id


def add_rezervare(id, nume, clasa, pret, checkin_facut, lista):
    '''
    adauga o rezervare in lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :param lista : lista de rezervari
    :return: o lista care contine atat elemente vechi, cat si rezervarea noua
    '''
    if get_by_id(id, lista) is not None:
        raise ValueError("ID-ul introdus exista deja!")
    if int(id) < 0:
        raise ValueError("ID-ul introdus nu este corect ca si format!")
    if clasa != "economy" and clasa != "economy plus" and clasa != "business":
        raise ValueError("Clasa introdusa nu exista! Alegeti dintre economy, economy plus sau business)")
    rezervare = creeaza_rezervare(id, nume, clasa, float(pret), checkin_facut)
    return lista + [rezervare]


def get_by_id(id, lista):
    '''
    gaseste o rezervare dupa ID intr-o lista
    :param id: string
    :param lista: lista de rezervari
    :return: rezervarea cu ID-ul cerut sau None, daca aceasta nu exista
    '''
    for rezervare in lista:
        if get_id(rezervare) == id:
            return rezervare
    return None


def delete_rezervare(id, lista):
    '''
    sterge o rezervare dupa ID-ul dat dintr-o lista
    :param id: string: id-ul rezervarii care se va sterge
    :param lista: lista de rezervari
    :return: o lista de rezervari fara rezervarea stearsa
    '''
    if get_by_id(id ,lista) is None:
        raise ValueError("Nu exista o rezervare cu ID-ul dat! ")
    return [rezervare for rezervare in lista if get_id(rezervare) != id]


def modify_rezervare(id, nume, clasa, pret, checkin_facut, lista):
    '''
    modifica o rezervare dupa ID-ul dat
    :param id: id-ul rezervarii
    :param nume: numele rezervarii
    :param clasa: clasa rezervarii
    :param pret: pretul rezervarii
    :param checkin_facut: checkin-ul rezervarii
    :param lista: lista de rezervari
    :return: lista modificata
    '''
    if get_by_id(id ,lista) is None:
        raise ValueError("Nu exista o rezervare cu ID-ul dat! ")
    lista_noua = []
    for rezervare in lista:
        if get_id(rezervare) == id:
            rezervare_noua = creeaza_rezervare(id,nume,clasa,pret,checkin_facut)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua
