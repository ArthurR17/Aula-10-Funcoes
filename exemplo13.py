

def func():
    local_variable = 5
    print(local_variable) # Isso imprimirá "5" porque local_variable é uma variável local


func()

# Temtar acessar local_variable fora da função resultará em um erro:
# print(local_variable) # Isso geraria um erro NameError, pois local_variable não está definido globalmente