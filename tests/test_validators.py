from validators import username_valido


def test_username_valido():
    assert username_valido("paulomatheuz")


def test_username_com_hifen_no_inicio():
    assert not username_valido("-github")


def test_username_com_caractere_invalido():
    assert not username_valido("git@hub")

def test_username_dois_hifens():
    assert not username_valido("git--hub")

def test_username_com_39_caractere():
    assert username_valido("a" * 39)

def test_username_com_mais_de_39_caractere():
    assert not username_valido("a" * 40)

def test_username_vazio():
    assert not username_valido("")