from Tests.test_CRUD import test_add_rezervare, test_delete_rezervare, test_modify_rezervare, test_get_by_id
from Tests.test_domain import test_rezervare
from Tests.test_functionalitati import test_trecerea_la_o_clasa_superioara, test_ieftinire
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

