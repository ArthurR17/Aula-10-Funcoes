print("-" * 95)
print("%22s AíSprexx" % " ")
print("-" * 95)
print("%1sCÓDIGO" % " ", "%13sPRODUTO" % " ", "%48sPREÇO (UNIDADE)" % " ")
print("-" * 95)
print("%1s100" % " ", "%10sGarrafa Térmica Vandley 400ml" % " ", "%33s$  50,95" % " ")
print("%1s101" % " ", "%10sFigureArt Luffy G5" % " ", "%44s$  1.567,99" % " ")
print("%1s102" % " ", "%10sNotebook Chucha 666 15”" % " ", "%39s$  2.690,00" % " ")
print("%1s103" % " ", "%10sServidor Topzera 451XXWTop" % " ", "%36s$  18.699,41" % " ")
print("%1s104" % " ", "%10sCapa de Celular Celulose Higiênica Não Corrosível" % " ", "%13s$  0.65" % " ")
print("%1s105" % " ", "%10sSmartphone Samsung Galaxy Note 20 Ultra 5G" % " ", "%20s$  2.700" % " ")
print("%1s106" % " ", "%10sNotebook Gamer Dell G15" % " ", "%39s$  4.700" % " ")
print("-" * 95)

codigo = int(input("Digite o código do produto: "))


def compra(codigo):
    global valor
    valor = 0
    if codigo == 100:
        print("Você pediu uma Garrafa Térmica Vandley 400ml")
        valor = 50.95
        return valor
    elif codigo == 101:
        print("Você pediu uma FigureArt Luffy G5")
        valor = 1567.99
        return valor
    elif codigo == 102:
        print("Você pediu um Notebook Chucha 666 15”")
        valor = 2690.00
        return valor
    elif codigo == 103:
        print("Você pediu um Servidor Topzera 451XXWTop")
        valor = 18699.41
        return valor
    elif codigo == 104:
        print("Você pediu uma Capa de Celular Celulose Higiênica Não Corrosível")
        valor = 0.65
        return valor
    elif codigo == 105:
        print("Você pediu um Smartphone Samsung Galaxy Note 20 Ultra 5G")
        valor = 2700.00
        return valor
    elif codigo == 106:
        print("Você pediu um Notebook Gamer Dell G15")
        valor = 4700.00
        return valor
    elif codigo == 0:
        print("Compra finalizada")
        return True
    else:
        print("Código inválido")
        return False


compra(codigo)
valor_total = valor + (valor * 0.35)


print(f"O valor do produto que você pediu é de: ${valor:.2f}")
print(f"O valor da taxa é de 35%, o valor total do pedido é de: ${valor_total:.2f}")

cupom = input("Digite aqui o cupom de desconto, caso você tenha (Digite 0 caso não tenha): ")

if cupom == "VAMBORA":
    valor_total = valor_total - (valor_total * 0.1)
    print(f"Cupom aplicado com sucesso!, o preço do produto com o desconto é de: ${valor_total:.2f}")

valor_total = valor_total * 5.04

print(f"O valor total do pedido convertido para reais é de: R${valor_total: .2f} ")








