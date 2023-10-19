num = int(input("Digite um número inteiro positivo: "))


def fatorial(num):
    count = 1
    i = 1
    while i <= num:
        count = count * i
        i += 1
    print(f"O fatorial de {num} é {count}")


fatorial(num)
