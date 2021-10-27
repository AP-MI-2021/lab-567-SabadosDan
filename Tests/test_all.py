from Tests.test_CRUD import test_add_rezervare, test_delete_rezervare, test_modify_rezervare
from Tests.test_domain import test_rezervare


def run_all_tests():
    test_rezervare()
    test_add_rezervare()
    test_delete_rezervare()
    test_modify_rezervare()