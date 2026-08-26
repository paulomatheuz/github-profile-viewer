username = input("Digite um usuario do GitHub: ")

def username_valido(username):
	if username == "":
		return False
	else:
		return True

user = username_valido(username)
if user:
	print("Username recebido: " + username)
else:
	print("Username invalido")