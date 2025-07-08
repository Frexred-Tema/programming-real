x = int(input())
abc = 0
def summa(z, abc):
    if (z == 0):
        return abc
    else:
        abc+=z
    return summa(z-1, abc)
print(summa(x, abc))