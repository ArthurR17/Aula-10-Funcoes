signo = []

while len(signo) < 12:
    signo.append(input("Informe o nome do signo: "))


def verificar_signo(signo):
    numero_signo = input("Informe o número do signo: ")
    if numero_signo == "0":
        print(signo[0])
    elif numero_signo == "1":
        print(signo[1])
    elif numero_signo == "2":
        print(signo[2])
    elif numero_signo == "3":
        print(signo[3])
    elif numero_signo == "4":
        print(signo[4])
    elif numero_signo == "5":
        print(signo[5])
    elif numero_signo == "6":
        print(signo[6])
    elif numero_signo == "7":
        print(signo[7])
    elif numero_signo == "8":
        print(signo[8])
    elif numero_signo == "9":
        print(signo[9])
    elif numero_signo == "10":
        print(signo[10])
    elif numero_signo == "11":
        print(signo[11])
    else:
        print("Número inválido")

verificar_signo(signo)