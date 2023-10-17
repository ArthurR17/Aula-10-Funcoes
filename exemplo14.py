global_variable = 10


def func():
    global global_variable
    global_variable = 20


func()
print(global_variable) # Isso imprimirá "20" porque global_variable foi alterada globalmente