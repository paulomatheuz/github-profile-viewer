import requests

from github_client import buscar_usuario
from validators import username_valido


def mostrar_perfil(dados):
    nome = dados.get("name") or "Não informado"

    bio = dados.get("bio")

    if bio:
        bio = bio.strip()
    else:
        bio = "Não informada"

    print("Usuário:", dados.get("login"))
    print("Nome:", nome)
    print("Biografia:", bio)
    print("Repositórios públicos:", dados.get("public_repos"))
    print("Seguidores:", dados.get("followers"))


username = input("Digite um usuário do GitHub: ").strip()

user = username_valido(username)

if user:
    try:
        resposta = buscar_usuario(username)

        if resposta.status_code == 200:
            dados = resposta.json()
            mostrar_perfil(dados)

        elif resposta.status_code == 404:
            print("Usuário não encontrado")

        else:
            print("Erro ao buscar usuário:", resposta.status_code)

    except requests.exceptions.RequestException:
        print("Erro de conexão. Tente novamente.")

else:
    print("Username inválido")