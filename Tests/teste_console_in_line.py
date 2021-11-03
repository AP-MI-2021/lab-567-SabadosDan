from Logic.CRUD import get_by_id
from UI.console_in_line import add, delete


def test_add():
    lista = []
    lista = add("1", "Pop Maria", "economy plus", 199.5, "da", lista)
    lista = add("2", "Antal Marius", "economy", 150, "da", lista)

    assert get_by_id("1", lista) == ["1", "Pop Maria", "economy plus", 199.5, "da"]
    assert get_by_id("2", lista) == ["2", "Antal Marius", "economy", 150, "da"]
    assert get_by_id("3", lista) is None


def test_delete():
    lista = []
    lista = add("1", "Pop Maria", "economy plus", 199.5, "da", lista)
    lista = add("2", "Antal Marius", "economy", 150, "da", lista)

    lista = delete("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

    lista = delete("2", lista)

    assert len(lista) == 0
    assert get_by_id("2", lista) is None