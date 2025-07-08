import re
x = '0000000000000000001000000000000000000'
counter = 0
def krutoytemirlan(x, counter):
    x = list(x)
    z = ''
    for i in range(len(x)):
        if (i != 0 and i != len(x)-1):
            if (str(x[i-1] + x[i] + x[i+1]) == "111"):
                z+='0'
            if (str(x[i-1] + x[i] + x[i+1]) == "110"):
                z+='1'
            if (str(x[i-1] + x[i] + x[i+1]) == "101"):
                z+='0'
            if (str(x[i-1] + x[i] + x[i+1]) == "100"):
                z+='1'
            if (str(x[i-1] + x[i] + x[i+1]) == "011"):
                z+='1'
            if (str(x[i-1] + x[i] + x[i+1]) == "010"):
                z+='0'
            if (str(x[i-1] + x[i] + x[i+1]) == "001"):
                z+='1'
            if (str(x[i-1] + x[i] + x[i+1]) == "000"):
                z+='0'
        elif (i == 0):
            if (str('0' + x[i] + x[i+1]) == "111"):
                z+='0'
            if (str('0' + x[i] + x[i+1]) == "110"):
                z+='1'
            if (str('0' + x[i] + x[i+1]) == "101"):
                z+='0'
            if (str('0' + x[i] + x[i+1]) == "100"):
                z+='1'
            if (str('0' + x[i] + x[i+1]) == "011"):
                z+='1'
            if (str('0' + x[i] + x[i+1]) == "010"):
                z+='0'
            if (str('0' + x[i] + x[i+1]) == "001"):
                z+='1'
            if (str('0' + x[i] + x[i+1]) == "000"):
                z+='0'
        elif (i == len(x)-1):
            if (str(x[i-1] + x[i] + '0') == "111"):
                z+='0'
            if (str(x[i-1] + x[i] + '0') == "110"):
                z+='1'
            if (str(x[i-1] + x[i] + '0') == "101"):
                z+='0'
            if (str(x[i-1] + x[i] + '0') == "100"):
                z+='1'
            if (str(x[i-1] + x[i] + '0') == "011"):
                z+='1'
            if (str(x[i-1] + x[i] + '0') == "010"):
                z+='0'
            if (str(x[i-1] + x[i] + '0') == "001"):
                z+='1'
            if (str(x[i-1] + x[i] + '0') == "000"):
                z+='0'
    print(z)
    pere = []
    for i in range(len(z)):
        if (z[i] == '1'):
            pere.append('█')
        else:
            pere.append('_')
    pereo = ' '.join(pere)
    if (counter <= 30):
        counter+=1
        return krutoytemirlan(z, counter)
print(krutoytemirlan(x, 0))