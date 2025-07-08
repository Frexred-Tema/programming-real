a = int(input("Введите: число "))
b = int(input("Введите: степень "))
abc = a
def stepa(a, b, abc):
    if (b == 1 and abc!=0):
        return(abc)
    elif (b == 0):
        return 1
    else:
        abc = abc * a
        return stepa(a, b-1, abc)
print(stepa(a, b, abc))
