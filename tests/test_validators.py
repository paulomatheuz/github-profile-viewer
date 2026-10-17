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


def test_username_com_hifen_no_final():
    assert not username_valido("github-")


def test_username_com_espaco():
    assert not username_valido("git hub")


def test_username_com_acento():
    assert not username_valido("usuário")


def test_username_com_underscore():
    assert not username_valido("git_hub")


def test_username_com_caractere_nao_ascii():
    assert not username_valido("ｇithub")


def test_username_com_letras_maiusculas():
    assert username_valido("GitHub")


def test_username_com_numeros():
    assert username_valido("github123")


def test_username_com_hifen_no_meio():
    assert username_valido("git-hub")


def test_username_com_um_caractere():
    assert username_valido("a")
