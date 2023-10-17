# Para criar uma função em Python usamos o comando 'def':
# Função para calcular metros quadrados de um terreno:

def calcularM2(comprimeto, largura):
    return comprimeto * largura

area = calcularM2(12, 20)
if area > 200:
    print(f"Terreno possui mais de 200 m2: {area}")