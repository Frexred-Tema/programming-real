z = 2
while z <= 9:
    for x in range(1, 10):
        print("%d * %d = %d: первый вид" % (z, x, z*x))
    z+=1
    print(' ')
a = 2
while a <= 9:
    for x in range(1, 10):
        print("{} * {} = {}: второй вид".format(a, x, a*x))
    a+=1
    print(' ')
z = 2
while z <= 9:
    for x in range(1, 10):
        print(f"{z} * {x} = {z*x}: третий вид",)
    z+=1
    print(' ')