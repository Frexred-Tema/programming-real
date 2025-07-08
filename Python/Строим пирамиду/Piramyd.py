x=int(input())
p = x
spl = 0
for z in range(1, x+1):
    if (z==1):
        print(' ' * p,'*'*z)
        spl+=1
        p-=1
    else:
        print(' ' * p,'*'*(z+spl))
        spl+=1
        p-=1