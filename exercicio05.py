num = int(input("Digite um número: "))
print("Escolha uma das opções: ")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
opcao = input("Sua opção: ")
def converter(num):
    if opcao == "1":
        num = bin(num)
        print(num)
    elif opcao == "2":
        num = oct(num)
        print(num)
    elif opcao == "3":
        num = hex(num)
        print(num)
    else:
        print("Opção inválida")

converter(num)