stack = []
falsetrue = []
def temirlan(x):

    xr = len(x)//2

    cvop=[]
    cvcl=[]

    caop=[]
    cacl=[]

    figop=[]
    figcl=[]

    for i in x:
        if (i == '('):
            caop.append(True)
            stack.append(i)
        elif (i == ')'):
            cacl.append(False)
            stack.pop()
        if (i == '{'):
            stack.append(i)
            figop.append(True)
        elif (i == '}'):
            figcl.append(False)
            stack.pop()
        if (i == '['):
            cvop.append(True)
            stack.append(i)
        elif (i == ']'):
            cvcl.append(False)
            stack.pop()
    true = 0
    print(cacl, cvcl, figcl)
    for j in range(len(cvop)):
        if (len(cvop)!=len(cvcl)):
            return('all false')
        elif (cvop[j] == True and cvcl[j] == False):
            true+=1
        else:
            return False
    for b in range(len(caop)):
        if (len(caop)!=len(cacl)):
            return('all false')
        elif (caop[b] == True and cacl[b] == False):
            true+=1
        else:
            return False
    for a in range(len(figop)):
        if (len(figop)!=len(figcl)):
            return('all false')
        elif (figop[a] == True and figcl[a] == False):
            true+=1
        else:
            return False
    if (xr == true):
        return "all True"
        
print(temirlan('(((({[[]]}))))'))