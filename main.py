from Tests.test_all import run_all_tests
from UI.console import run_menu
from UI.console_in_line import run_console_in_line


def meniuri():
    print("  1. Meniul vechi")
    print("  2. Meniul tip console in line")
    print("  x. Iesire")

def main():
    run_all_tests()
    lista = []
    undo_list = []
    redo_list = []
    while True:
        meniuri()
        optiune_meniu = input(" Alegeti meniul: ")
        if optiune_meniu == "1":
            run_menu(lista, undo_list, redo_list)
        elif optiune_meniu == "2":
            run_console_in_line(lista)
        elif optiune_meniu == "x":
            break
        else:
            print("Ati introdus o valoare gresita! REINCERCATI: ")

if __name__ == '__main__':
    main()