from unittest.mock import Mock

import pytest
import requests

from github_client import buscar_usuario


@pytest.mark.parametrize("status", [200, 404, 403, 429, 500])
def test_buscar_usuario_retorna_resposta(monkeypatch, status):
    resposta = Mock(status_code=status)
    consulta = Mock(return_value=resposta)
    monkeypatch.setattr("github_client.requests.get", consulta)

    resultado = buscar_usuario("paulomatheuz")

    assert resultado is resposta
    consulta.assert_called_once_with(
        "https://api.github.com/users/paulomatheuz", timeout=10
    )


@pytest.mark.parametrize(
    "erro", [requests.exceptions.Timeout, requests.exceptions.ConnectionError]
)
def test_buscar_usuario_propaga_falha_de_rede(monkeypatch, erro):
    consulta = Mock(side_effect=erro)
    monkeypatch.setattr("github_client.requests.get", consulta)

    with pytest.raises(erro):
        buscar_usuario("paulomatheuz")

    consulta.assert_called_once()
