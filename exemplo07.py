l = [10, 20, 25, 30]
def soma(l):
    total = 0
    for e in l:
        total += e
    return total


def media(l):
    return soma(l) / len(l)


print(media(l))