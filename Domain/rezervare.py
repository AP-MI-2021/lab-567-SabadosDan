def creeaza_rezervare(id, nume, clasa, pret, checkin_facut):
    '''
    creeaza un dictionar ce reprezinta o rezervare a unei companii aeriene
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :return: un dictionar ce contine o rezervare
    '''
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin_facut": checkin_facut
    }


def get_id(rezervare):
    '''
    da id-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: id-ul rezervarii
    '''
    return rezervare["id"]


def get_nume(rezervare):
    '''
    da numele unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: numele rezervarii
    '''
    return rezervare["nume"]


def get_clasa(rezervare):
    '''
    da clasa unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: clasa rezervarii
    '''
    return rezervare["clasa"]


def get_pret(rezervare):
    '''
    da pretul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: pretul rezervarii
    '''
    return rezervare["pret"]


def get_checkin(rezervare):
    '''
    da checkin-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: checkin-ul rezervarii
    '''
    return rezervare["checkin_facut"]


def to_string(rezervare):
    return "ID: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin facut: {}  ".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )