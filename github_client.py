import requests

def buscar_usuario(username):
    url = "https://api.github.com/users/" + username
    resposta = requests.get(url, timeout=10)
    return resposta