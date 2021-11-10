from Logic.CRUD import add_rezervare
from Logic.undo_and_redo import do_undo, do_redo


def test_undo_redo_lab():
    lista = []
    undo_list = []
    redo_list = []
    lista = add_rezervare("1", "nume1", "economy plus", 100, "da", lista, undo_list, redo_list)
    lista = add_rezervare("2", "nume2", "economy plus", 200, "da", lista, undo_list, redo_list)
    lista = add_rezervare("3", "nume3", "economy plus", 300, "da", lista, undo_list, redo_list)
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["2", "nume2", "economy plus", 200, "da"],
                     ["3", "nume3", "economy plus", 300, "da"]]
    lista = do_undo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["2", "nume2", "economy plus", 200, "da"]]
    lista = do_undo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"]]
    lista = do_undo(undo_list, redo_list, lista)
    assert len(lista) == 0
    lista = add_rezervare("1", "nume1", "economy plus", 100, "da", lista, undo_list, redo_list)
    lista = add_rezervare("2", "nume2", "economy plus", 200, "da", lista, undo_list, redo_list)
    lista = add_rezervare("3", "nume3", "economy plus", 300, "da", lista, undo_list, redo_list)
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["2", "nume2", "economy plus", 200, "da"],
                     ["3", "nume3", "economy plus", 300, "da"]]
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["2", "nume2", "economy plus", 200, "da"],
                     ["3", "nume3", "economy plus", 300, "da"]]
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["2", "nume2", "economy plus", 200, "da"]]
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"]]
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["2", "nume2", "economy plus", 200, "da"]]
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["2", "nume2", "economy plus", 200, "da"],
                     ["3", "nume3", "economy plus", 300, "da"]]
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["2", "nume2", "economy plus", 200, "da"]]
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista == [["1", "nume1", "economy plus", 100, "da"]]
    lista = add_rezervare("4", "nume4", "economy plus", 400, "da", lista, undo_list, redo_list)
    assert len(lista) == 2
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["4", "nume4", "economy plus", 400, "da"]]
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert len(lista) == 2
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["4", "nume4", "economy plus", 400, "da"]]
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert len(lista) == 1
    assert lista == [["1", "nume1", "economy plus", 100, "da"]]
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert len(lista) == 0
    assert lista == []
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert len(lista) == 1
    assert lista == [["1", "nume1", "economy plus", 100, "da"]]
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert len(lista) == 2
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["4", "nume4", "economy plus", 400, "da"]]
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert len(lista) == 2
    assert lista == [["1", "nume1", "economy plus", 100, "da"],
                     ["4", "nume4", "economy plus", 400, "da"]]









