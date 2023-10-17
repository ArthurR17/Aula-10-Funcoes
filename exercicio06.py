print("-" * 150)
print("%50s Purple Moon" % " ")
print("-" * 150)
print("%1sCÓDIGO" % " ", "%10sPRODUTO" % " ", "%20sMercado Nárnia" % " ", "%18sMercadoSouthTown" % " ", "%15sMercado Ashura" % " ")
print("-" * 150)
print("%1s100" % " ", "%10sUvas (kg)" % " ", "%23sR$ 350,00" % " ", "%23sR$ 450,00" % " ", "%23sR$ 250,00" % " ")
print("%1s101" % " ", "%10sBarris de carvalho (un)" % " ", "%9sR$ 1.500,00" % " ", "%21sR$ 1250,00" % " ", "%22sR$ 1000,00" % " ")
print("%1s102" % " ", "%10sLeveduras (kg)" % " ", "%18sR$ 429,90" % " ", "%23sR$ 400,00" % " ", "%23sR$ 350,00" % " ")
print("%1s103" % " ", "%10sProdutos Químicos (kg)" % " ", "%10sR$ 345,00" % " ", "%23sR$ 621,00" % " ", "%23sR$ 752,00" % " ")
print("-" * 150)

uva = [350, 450, 250]
barris = [1500, 1250, 1000]
leveduras = [429.90, 400, 350]
produtos_quimicos = [345, 621, 752]

total1 = uva[0] * 32 + barris[0] * 3 + leveduras[0] * 150 + produtos_quimicos[0] * 100
total2 = uva[1] * 32 + barris[1] * 3 + leveduras[1] * 150 + produtos_quimicos[1] * 100
total3 = uva[2] * 32 + barris[2] * 3 + leveduras[2] * 150 + produtos_quimicos[2] * 100

print("Sua receita: ")
print("32kg de uvas")
print("3 barris de carvalho")
print("150kg de Ls")
print("100kg de Produtos Químicos")
print("-" * 40)

print("Preço total da receita em cada mercado: ")
print("-" * 40)

print("Mercado Nárnia: ")
print(f"Uvas: ${uva[0] * 32:.2f}")
print(f"Barris de carvalho: ${barris[0] * 3:.2f}")
print(f"Leveduras: ${leveduras[0] * 150:.2f}")
print(f"Produtos Químicos: ${produtos_quimicos[0] * 100:.2f}")
print(f"Total: R${total1:.2f}")

print("-" * 40)

print("Mercado SouthTown: ")
print(f"Uvas: ${uva[1] * 32:.2f}")
print(f"Barris de carvalho: ${barris[1] * 3:.2f}")
print(f"Leveduras: ${leveduras[1] * 150:.2f}")
print(f"Produtos Químicos: ${produtos_quimicos[1] * 100:.2f}")
print(f"Total: R${total2:.2f}")

print("-" * 40)

print("Mercado Ashura: ")
print(f"Uvas: ${uva[2] * 32:.2f}")
print(f"Barris de carvalho: ${barris[2] * 3:.2f}")
print(f"Leveduras: ${leveduras[2] * 150:.2f}")
print(f"Produtos Químicos: ${produtos_quimicos[2] * 100:.2f}")
print(f"Total: R${total3:.2f}")



