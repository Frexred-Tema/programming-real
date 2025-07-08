fn = int(input('Введите первое число: '))
sn = int(input('Введите второе число: '))
fm = ''
sm = ''
while (fn != 0):
    fm = str(fn % 2) + fm
    fn = fn // 2
while (sn != 0):
    sm = str(sn % 2) + sm
    sn = sn//2
while (len(fm) != 16):
    fm = "0" + fm
    sm = "0" + sm
un = sm + fm
un = list(un)
um = []
for i in range(len(un)):
    um.insert(0, un[i])
vyvod = 0
for j in range(len(un)):
    vyvod = vyvod + (int(um[j]) * 2**j)
print(vyvod)