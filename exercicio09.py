palindromo = input("Digite um palíndromo: ")


def verificar_palindromo(palindromo):
    if palindromo == palindromo[::-1]:
        print(f"Essa palavra é um palíndromo: {palindromo[::-1]}!")
        return True
    else:
        print("Essa palavra não é um palíndromo!")
        return False

verificar_palindromo(palindromo)
