import random

numeros = [random.randint(0, 30)]

def gerar_numeros(numeros):
    while len(numeros) < 15:
        numeros.append(random.randint(0, 30))


gerar_numeros(numeros)

print(f"Você tem a seguinte lista de números: {numeros}")
acerto = int(input("Digite o número máximo que está presenta na lista: "))
numero_maximo = max(numeros)

if acerto == numero_maximo:
    print("Parabéns, você pode passar para a próxima fase!")
else:
    print("Você errou, tente novamente")