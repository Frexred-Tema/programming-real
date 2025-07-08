x = '21+3*2-'

def axe(x):
    chto=0
    x = list(x)
    while len(x) != 0:
        if len(x) != 1:
            if x[2] == '+':
                chto = ("{}".format(int(x[0]) + int(x[1])))
                for i in range(3):
                    x.pop(0)
                x = [chto] + x
            elif x[2] == '-':
                chto = ("{}".format(int(x[0]) - int(x[1])))
                for i in range(3):
                    x.pop(0)
                x = [chto] + x
            elif x[2] == '*':
                chto = ("{}".format(int(x[0]) * int(x[1])))
                for i in range(3):
                    x.pop(0) 
                x = [chto] + x
            elif x[2] == '/':
                chto = ("{}".format(int(x[0]) / int(x[1])))
                for i in range(3):
                    x.pop(0)
                x = [chto] + x
        else:
            return chto

print(axe(x))