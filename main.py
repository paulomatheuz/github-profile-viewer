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


username = input("Digite um usuario do GitHub: ").strip()

user = username_valido(username)

if user:
    print("Username recebido: " + username)
else:
    print("Username invalido")