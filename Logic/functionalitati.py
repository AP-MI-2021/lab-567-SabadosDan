from Domain.rezervare import get_nume, get_clasa, creeaza_rezervare, get_id, get_pret, get_checkin


def trecerea_la_o_clasa_superioara(nume, lista):
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
    return lista_noua


def ieftinire(procentaj, lista):
    '''
    Scade pretul rezervarilor care au checkin ul facut, cu un anumit procentaj
    :param procentaj: float
    :param lista:lista de rezervari
    :return: lista_noua: lista modificata de rezervari
    '''
    if float(procentaj) < 0 :
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
    return lista_noua



