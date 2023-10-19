
palavra = input("Digite uma palavra: ")


def vogais(palavra):
    palavra.count("a")
    print(f"A letra 'a' aparece {palavra.count('a')} vezes")
    palavra.count("e")
    print(f"A letra 'e' aparece {palavra.count('e')} vezes")
    palavra.count("i")
    print(f"A letra 'i' aparece {palavra.count('i')} vezes")
    palavra.count("o")
    print(f"A letra 'o' aparece {palavra.count('o')} vezes")
    palavra.count("u")
    print(f"A letra 'u' aparece {palavra.count('u')} vezes")


def inverter(palavra):
    palavra[::-1]
    print(f"A palavra invertida que você digitou fica: {palavra[::-1]}")


vogais(palavra)
inverter(palavra)
