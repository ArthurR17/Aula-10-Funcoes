a = 20 # Variável global - fora da funções
def funcao():
    a = 10 # Variável local - Dentro da função
    print(a)

funcao() # Imprimirá o valor de 'a' local
print(a) # Imprimirá o valor de 'a' global