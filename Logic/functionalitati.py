from Domain.rezervare import get_nume, get_clasa, creeaza_rezervare, get_id, get_pret, get_checkin


def trecerea_la_o_clasa_superioara(nume, lista, undo_list, redo_list):
    '''
    Schimba clasa rezervarilor introduse pe numele citit in clasa superioara
    :param nume:str: numele asupra caruia se aplica modificarile
    :param lista: lista de rezervari
    :return: lista_noua: lista modificata de rezervari
    '''
    lista_noua = []
    for rezervare in lista:
        if nume == get_nume(rezervare):
            if get_clasa(rezervare) == "economy":
                rezervare_noua = creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    "economy plus",
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                lista_noua.append(rezervare_noua)
            elif get_clasa(rezervare) == "economy plus":
                rezervare_noua = creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    "business",
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                lista_noua.append(rezervare_noua)
            else:
                rezervare_noua = creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    get_clasa(rezervare),
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    undo_list.append(lista)
    redo_list.clear()
    return lista_noua


def ieftinire(procentaj, lista, undo_list, redo_list):
    '''
    Scade pretul rezervarilor care au checkin ul facut, cu un anumit procentaj
    :param procentaj: float
    :param lista:lista de rezervari
    :return: lista_noua: lista modificata de rezervari
    '''
    if float(procentaj) < 0:
        raise ValueError("Valorea procentajului nu este corecta din punct de vedere al formatului")
    lista_noua = []
    for rezervare in lista:
        if get_checkin(rezervare) == "da":
            rezervare_noua = creeaza_rezervare(
                get_id(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                get_pret(rezervare) - (procentaj / 100 * get_pret(rezervare)),
                get_checkin(rezervare)
            )
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    undo_list.append(lista)
    redo_list.clear()
    return lista_noua


def pret_maxim(lista):
    '''
    Returneaza pretul maxim specific fiecarei clase
    :param lista: lista de rezervari
    :return: rezultat: dictionar
    '''
    rezultat = {}
    for rezervare in lista:
        clasa = get_clasa(rezervare)
        if clasa in rezultat:
            if get_pret(rezervare) > rezultat[clasa]:
                rezultat[clasa] = get_pret(rezervare)
        else:
            rezultat[clasa] = get_pret(rezervare)
    return rezultat


def lista_ordonata_dupa_pret(lista):
    '''
    Returneaza lista ordonata descrescator dupa pret.
    :param lista: lista de rezervari
    :return: lista sortata
    '''
    return sorted(lista, key = get_pret, reverse = True)


def suma_pe_fiecare_nume(lista):
    '''
    Returneaza suma rezervarilor pe fiecare nume
    :param lista: lista de rezervari
    :return: rezultat: dictionar
    '''
    rezultat = {}
    for rezervare in lista:
        nume = get_nume(rezervare)
        pret = get_pret(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat


