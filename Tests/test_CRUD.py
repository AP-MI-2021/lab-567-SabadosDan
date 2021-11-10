from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import add_rezervare, get_by_id, delete_rezervare, modify_rezervare


def test_add_rezervare():
    lista = []
    lista = add_rezervare("1", "Pop Maria", "economy plus", 199.5, "da", lista, [], [])
    assert len(lista) == 1
    assert get_id(get_by_id("1",lista)) == "1"
    assert get_nume(get_by_id("1",lista)) == "Pop Maria"
    assert get_clasa(get_by_id("1",lista)) == "economy plus"
    assert get_pret(get_by_id("1",lista)) == 199.5
    assert get_checkin(get_by_id("1",lista)) == "da"


def test_get_by_id():
    lista = []
    lista = add_rezervare("1", "Pop Maria", "economy plus", 199.5, "da", lista, [], [])
    lista = add_rezervare("2", "Antal Marius", "economy", 150, "da", lista, [], [])

    assert get_by_id("1", lista) == ["1", "Pop Maria", "economy plus", 199.5, "da"]
    assert get_by_id("2", lista) == ["2", "Antal Marius", "economy", 150, "da"]
    assert get_by_id("3", lista) is None

def test_delete_rezervare():
    lista = []
    lista = add_rezervare("1", "Pop Maria", "economy plus", 199.5, "da", lista, [], [])
    lista = add_rezervare("2", "Antal Marius", "economy", 150, "da", lista, [], [])

    lista = delete_rezervare("1", lista, [], [])

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

    lista = delete_rezervare("2", lista, [], [])

    assert len(lista) == 0
    assert get_by_id("2", lista) is None


def test_modify_rezervare():
    lista = []
    lista = add_rezervare("1", "Pop Maria", "economy plus", 199.5, "da", lista, [], [])
    lista = add_rezervare("2", "Antal Marius", "economy", 150, "da", lista, [], [])

    lista = modify_rezervare("1", "Ioan Simon", "economy plus", 200, "nu", lista, [], [])

    modified_rezervare = get_by_id("1", lista)
    assert get_id(modified_rezervare) == "1"
    assert get_nume(modified_rezervare) == "Ioan Simon"
    assert get_clasa(modified_rezervare) == "economy plus"
    assert get_pret(modified_rezervare) == 200
    assert get_checkin(modified_rezervare) == "nu"

    nemodified_rezervare = get_by_id("2", lista)
    assert get_id(nemodified_rezervare) == "2"
    assert get_nume(nemodified_rezervare) == "Antal Marius"
    assert get_clasa(nemodified_rezervare) == "economy"
    assert get_pret(nemodified_rezervare) == 150
    assert get_checkin(nemodified_rezervare) == "da"

    lista = []
    lista = add_rezervare("1", "Pop Maria", "economy plus", 199.5, "da", lista, [], [])

    lista = modify_rezervare("1", "Antal Marius", "economy", 150, "da", lista, [], [])

    modified_rezervare = get_by_id("1", lista)
    assert get_id(modified_rezervare) == "1"
    assert get_nume(modified_rezervare) == "Antal Marius"
    assert get_clasa(modified_rezervare) == "economy"
    assert get_pret(modified_rezervare) == 150
    assert get_checkin(modified_rezervare) == "da"