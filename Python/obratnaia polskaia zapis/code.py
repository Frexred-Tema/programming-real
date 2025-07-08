x = str(input())

def rpw(x):

    integers = []
    operations = []
    concl = []

    for i in range(len(x)):

        if (x[i] == '('):
            concl.append(x[i])

        elif (x[i] == ')'):
            for j in range(len(concl)):
                if (concl[0] != '('):
                    concl.append(concl[0])
                    del concl[0]

        elif (type(x[i]) is int):
            integers.append(int(x[i]))
        
        elif (x[i] in ['+', '-', '/', '*']):
            operations.append(x[i])

        whiler_1 = 0
        whiler_2 = 0

        while (whiler_1 != len(integers) and whiler_2 != len(operations)):

            if (concl == []):
                concl.append(int(integers[whiler_1]))
                concl.append(int(integers[whiler_1+1]))
                whiler_1+=2
            
            elif (type(concl[-1]) is int):
                for n in operations:
                    if (operations[n] == '*' or operations[n] == '/'):
                        concl.append(operations[n])
                        whiler_2+=1
                    else:
                        continue

                for u in operations:
                    if (operations[u] == '-' or operations[u] == '+'):
                        concl.append(operations[u])
                        whiler_2+=1
                    else:
                        continue
            
            if (type(concl[-1]) is str):
                    concl.append(int(integers[whiler_1]))
                    whiler_1+=1

    return concl

print(rpw(x))