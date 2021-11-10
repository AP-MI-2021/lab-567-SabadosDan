from Tests.test_CRUD import test_add_rezervare, test_delete_rezervare, test_modify_rezervare, test_get_by_id
from Tests.test_domain import test_rezervare
from Tests.test_functionalitati import test_trecerea_la_o_clasa_superioara, test_ieftinire, test_pret_maxim, \
    test_lista_ordonata_dupa_pret, test_suma_pe_fiecare_nume
from Tests.test_undo_and_redo import test_undo_redo_lab
from Tests.teste_console_in_line import test_add, test_delete


def run_all_tests():
    test_rezervare()
    test_add_rezervare()
    test_delete_rezervare()
    test_modify_rezervare()
    test_get_by_id()
    test_trecerea_la_o_clasa_superioara()
    test_ieftinire()
    test_add()
    test_delete()
    test_pret_maxim()
    test_lista_ordonata_dupa_pret()
    test_suma_pe_fiecare_nume()
    test_undo_redo_lab()

