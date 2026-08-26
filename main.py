username = input("Digite um usuario do GitHub: ").strip()

def username_valido(username):
    if len(username) < 3:
        return False
    else:
        return True

user = username_valido(username)
if user:
	print("Username recebido: " + username)
else:
	print("Username invalido")