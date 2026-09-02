import requests


def hifen_nas_bordas(username):
    if username == "":
        return False

    if username[0] == "-" or username[-1] == "-":
        return True
    else:
        return False


def tem_caractere_invalido(username):
    for caractere in username:
        if not caractere.isascii() or (
            not caractere.isalnum() and caractere != "-"
        ):
            return True

    return False


def username_valido(username):
    if (
        username == ""
        or len(username) > 39
        or hifen_nas_bordas(username)
        or "--" in username
        or tem_caractere_invalido(username)
    ):
        return False
    else:
        return True


def buscar_usuario(username):
    url = "https://api.github.com/users/" + username
    resposta = requests.get(url, timeout=10)

    return resposta


username = input("Digite um usuario do GitHub: ").strip()

user = username_valido(username)

if user:
    try:
        resposta = buscar_usuario(username)

        if resposta.status_code == 200:
            dados = resposta.json()

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

        elif resposta.status_code == 404:
            print("Usuário não encontrado")

        else:
            print("Erro ao buscar usuário:", resposta.status_code)

    except requests.exceptions.RequestException as erro:
        print("Erro de conexão")
        print("Detalhes:", erro)

else:
    print("Username invalido")