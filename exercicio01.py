senha = input("Digite uma senha: ")


def valida_senha(senha):
    if len(senha) < 8:
        print("Senha inválida. A senha deve ter pelo menos 8 caracteres")
        return False
    elif (senha.islower()):
        print("Senha inválida. A senha deve ter pelo menos uma letra maiúscula")
        return False
    elif (senha.isupper()):
        print("Senha inválida. A senha deve ter pelo menos uma letra minúscula")
        return False
    elif (senha.isalnum()):
        print("Senha inválida. A senha deve ter pelo menos um número")
        return False
    else:
        print("Senha válida!")
        return True


valida_senha(senha)