from Domain.rezervare import creeaza_rezervare, get_id, get_checkin, get_nume, get_clasa, get_pret


def test_rezervare():
    rezervare =  creeaza_rezervare("1", "Pop Maria", "economy plus", 199.5, "da")

    assert get_id(rezervare) == "1"
    assert get_nume(rezervare) == "Pop Maria"
    assert get_clasa(rezervare) == "economy plus"
    assert get_pret(rezervare) == 199.5
    assert get_checkin(rezervare) == "da"