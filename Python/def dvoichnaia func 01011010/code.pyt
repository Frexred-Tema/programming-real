import random
x = int(input())
abc = str()
def randomizer(x, abc):
    if (x != 0):
        a = random.randint(0, 1)
        abc += str(a)
        return randomizer(x-1, abc)
    else:
        return abc
print(randomizer(x, abc))