def hifen_nas_bordas(username):
    if username == "":
        return False

    if username[0] == "-" or username[-1] == "-":
        return True
    else:
        return False


def username_valido(username):
    if username == "" or len(username) > 39 or hifen_nas_bordas(username) or "--" in username:
        return False
    else:
        return True


username = input("Digite um usuario do GitHub: ").strip()

user = username_valido(username)

if user:
    print("Username recebido: " + username)
else:
    print("Username invalido")