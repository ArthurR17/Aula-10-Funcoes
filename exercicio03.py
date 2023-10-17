quantidade = int(input("Digite a quantidade de ingressos: "))

def calcular_valor_total(quantidade):
    preco_ingresso = 120.76
    global total
    total = quantidade * preco_ingresso
    if 5 <= quantidade <= 10:
        if quantidade >= 7:
            desconto = 0.05 * total
            total -= desconto
            return total
    else:
        print("Seus ingressos têm que ser maior que 4 e menor que 10")

calcular_valor_total(quantidade)

print(f"O valor total da compra é de: ${total:.2f}")