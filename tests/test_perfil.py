import pytest

from main import mostrar_perfil


@pytest.mark.parametrize("valor", [None, "", "   ", "\n\t"])
def test_mostrar_perfil_com_campos_vazios(capsys, valor):
    mostrar_perfil({"name": valor, "bio": valor})

    saida = capsys.readouterr().out
    assert "Nome: Não informado\n" in saida
    assert "Biografia: Não informada\n" in saida


def test_mostrar_perfil_com_campos_ausentes(capsys):
    mostrar_perfil({})

    saida = capsys.readouterr().out
    assert "Nome: Não informado\n" in saida
    assert "Biografia: Não informada\n" in saida


def test_mostrar_perfil_remove_espacos_nas_bordas(capsys):
    mostrar_perfil({"name": " Paulo ", "bio": " Estudante\n"})

    saida = capsys.readouterr().out
    assert "Nome: Paulo\n" in saida
    assert "Biografia: Estudante\n" in saida
