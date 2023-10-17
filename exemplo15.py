n = 400


def fatoria(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatoria(n - 1)


print(fatoria(n))