def do_undo(undo_list, redo_list, lista):
    """
    functia retine lista inaite de a fii apelata o functionalitate
    :param undo_list: lista de rezervari inaintea apelarii unei functionalitati
    :param redo_list: lista de rezervari dupa aplicarea unei functionalitati
    :param lista: lista curenta
    :return: last_undo: lista noua
    """
    if undo_list:
        last_undo = undo_list.pop()
        redo_list.append(lista)
        return last_undo
    return None


def do_redo(undo_list, redo_list, lista):
    """
    functia returneaza lista inaitea apelarii undo-ului
    :param undo_list: lista de rezervari inaintea apelarii unei functionalitati
    :param redo_list: lista de rezervari dupa aplicarea unei functionalitati
    :param lista: lista curenta
    :return: last_redo: lista noua
    """
    if redo_list:
        last_redo = redo_list.pop()
        undo_list.append(lista)
        return last_redo
    return None
