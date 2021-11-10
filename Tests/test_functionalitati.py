from Domain.rezervare import get_clasa, get_pret, get_id
from Logic.CRUD import add_rezervare, get_by_id
from Logic.functionalitati import trecerea_la_o_clasa_superioara, ieftinire, pret_maxim, lista_ordonata_dupa_pret, \
    suma_pe_fiecare_nume


def test_trecerea_la_o_clasa_superioara():
    lista = []

    lista = add_rezervare("1", "Pop", "economy", 330, "da", lista, [], [])
    lista = add_rezervare("2", "Pop", "economy plus", 330, "da", lista, [], [])
    lista = add_rezervare("3", "Mihai", "business", 330, "da", lista, [], [])

    lista = trecerea_la_o_clasa_superioara("Pop", lista, [], [])

    assert get_clasa(get_by_id("1", lista)) == "economy plus"
    assert get_clasa(get_by_id("2", lista)) == "business"
    assert get_clasa(get_by_id("3", lista)) == "business"


def test_ieftinire():
    lista = []

    lista = add_rezervare("1", "Pop", "economy", 100, "da", lista, [], [])
    lista = add_rezervare("2", "Pop", "economy plus", 200, "da", lista, [], [])
    lista = add_rezervare("3", "Mihai", "business", 330, "nu", lista, [], [])

    lista = ieftinire(10, lista, [], [])

    assert get_pret(get_by_id("1", lista)) == 90.0
    assert get_pret(get_by_id("2", lista)) == 180.0
    assert get_pret(get_by_id("3", lista)) == 330


def test_pret_maxim():
    lista = []

    lista = add_rezervare("1", "Pop", "economy", 100, "da", lista, [], [])
    lista = add_rezervare("2", "Pop", "economy plus", 400, "da", lista, [], [])
    lista = add_rezervare("3", "Mihai", "business", 330, "nu", lista, [], [])
    lista = add_rezervare("4", "Tibi", "economy", 90, "da", lista, [], [])

    rezultat = pret_maxim(lista)

    assert len(rezultat) == 3
    assert rezultat["economy"] == 100
    assert rezultat["economy plus"] == 400
    assert rezultat["business"] == 330


def test_lista_ordonata_dupa_pret():
    lista = []

    lista = add_rezervare("1", "Pop", "economy", 100, "da", lista, [], [])
    lista = add_rezervare("2", "Pop", "economy plus", 300, "da", lista, [], [])
    lista = add_rezervare("3", "Mihai", "business", 400, "nu", lista, [], [])
    lista = add_rezervare("4", "Tibi", "economy", 90, "da", lista, [], [])


    rezultat = lista_ordonata_dupa_pret(lista)

    assert get_id(rezultat[0]) == "3"
    assert get_id(rezultat[1]) == "2"
    assert get_id(rezultat[2]) == "1"
    assert get_id(rezultat[3]) == "4"


def test_suma_pe_fiecare_nume():
    lista = []

    lista = add_rezervare("1", "Pop", "economy", 100, "da", lista, [], [])
    lista = add_rezervare("2", "Pop", "economy plus", 250, "da", lista, [], [])
    lista = add_rezervare("3", "Mihai", "business", 400, "nu", lista, [], [])
    lista = add_rezervare("4", "Tibi", "economy", 90, "da", lista, [], [])

    rezultat = suma_pe_fiecare_nume(lista)

    assert len(rezultat) == 3
    assert rezultat["Pop"] == 350
    assert rezultat["Mihai"] == 400
    assert rezultat["Tibi"] == 90

