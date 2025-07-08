import random

x = int(input())
z = str()

def weak(z, x):
    if (z == ''):
        z = z + str(random.randint(0, 1))
    elif (x == 0):
        return z
    elif (z[-1] == '1'):
        z+='0'
    elif (z[-1] == '0'):
        z+='1'
    return weak(z, x-1)
      
print(weak(z, x))