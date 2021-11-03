from Domain.rezervare import get_clasa, get_pret
from Logic.CRUD import add_rezervare, get_by_id
from Logic.functionalitati import trecerea_la_o_clasa_superioara, ieftinire


def test_trecerea_la_o_clasa_superioara():
    lista = []

    lista = add_rezervare("1", "Pop", "economy", 330, "da", lista)
    lista = add_rezervare("2", "Pop", "economy plus", 330, "da", lista)
    lista = add_rezervare("3", "Mihai", "business", 330, "da", lista)

    lista = trecerea_la_o_clasa_superioara("Pop", lista)

    assert get_clasa(get_by_id("1", lista)) == "economy plus"
    assert get_clasa(get_by_id("2", lista)) == "business"
    assert get_clasa(get_by_id("3", lista)) == "business"


def test_ieftinire():
    lista = []

    lista = add_rezervare("1", "Pop", "economy", 100, "da", lista)
    lista = add_rezervare("2", "Pop", "economy plus", 200, "da", lista)
    lista = add_rezervare("3", "Mihai", "business", 330, "nu", lista)

    lista = ieftinire(10, lista)

    assert get_pret(get_by_id("1", lista)) == 90.0
    assert get_pret(get_by_id("2", lista)) == 180.0
    assert get_pret(get_by_id("3", lista)) == 330

