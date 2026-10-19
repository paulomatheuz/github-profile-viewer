import importlib
from unittest.mock import Mock

import pytest
import requests

import main


def test_importar_main_nao_executa_consulta(monkeypatch, capsys):
    entrada = Mock(side_effect=AssertionError("Não deve solicitar entrada"))
    consulta = Mock(side_effect=AssertionError("Não deve consultar a API"))
    monkeypatch.setattr("builtins.input", entrada)
    monkeypatch.setattr("github_client.buscar_usuario", consulta)

    importlib.reload(main)

    entrada.assert_not_called()
    consulta.assert_not_called()
    assert capsys.readouterr().out == ""


def test_main_exibe_perfil(monkeypatch, capsys):
    resposta = Mock(status_code=200)
    resposta.json.return_value = {
        "login": "paulomatheuz",
        "name": "Paulo",
        "bio": "Estudante",
        "public_repos": 7,
        "followers": 11,
    }
    consulta = Mock(return_value=resposta)
    monkeypatch.setattr("builtins.input", lambda mensagem: " paulomatheuz ")
    monkeypatch.setattr(main, "buscar_usuario", consulta)

    main.main()

    consulta.assert_called_once_with("paulomatheuz")
    assert capsys.readouterr().out == (
        "Usuário: paulomatheuz\n"
        "Nome: Paulo\n"
        "Biografia: Estudante\n"
        "Repositórios públicos: 7\n"
        "Seguidores: 11\n"
    )


def test_main_rejeita_username_invalido(monkeypatch, capsys):
    consulta = Mock()
    monkeypatch.setattr("builtins.input", lambda mensagem: "git@hub")
    monkeypatch.setattr(main, "buscar_usuario", consulta)

    main.main()

    consulta.assert_not_called()
    assert capsys.readouterr().out == "Username inválido\n"


@pytest.mark.parametrize(
    "status, mensagem",
    [
        (404, "Usuário não encontrado\n"),
        (500, "Erro ao buscar usuário: 500\n"),
    ],
)
def test_main_trata_erro_http(monkeypatch, capsys, status, mensagem):
    resposta = Mock(status_code=status)
    monkeypatch.setattr("builtins.input", lambda mensagem: "paulomatheuz")
    monkeypatch.setattr(main, "buscar_usuario", Mock(return_value=resposta))

    main.main()

    resposta.json.assert_not_called()
    assert capsys.readouterr().out == mensagem


@pytest.mark.parametrize(
    "erro, mensagem",
    [
        (requests.exceptions.ConnectionError, "Erro de conexão. Tente novamente.\n"),
        (requests.exceptions.Timeout, "A consulta demorou demais. Tente novamente.\n"),
    ],
)
def test_main_trata_falha_na_consulta(monkeypatch, capsys, erro, mensagem):
    monkeypatch.setattr("builtins.input", lambda mensagem: "paulomatheuz")
    monkeypatch.setattr(main, "buscar_usuario", Mock(side_effect=erro))

    main.main()

    assert capsys.readouterr().out == mensagem
