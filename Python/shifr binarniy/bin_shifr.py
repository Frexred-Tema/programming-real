word = str(input())
word = word.upper()
word = list(word.replace(' ', ''))
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
temp = []
mw = []
for i in range(len(word)):
    for j in range(len(alp)):
        if (word[i] == alp[j]):
            temp.append(j)
print(mw)
while len(temp) != 0:
    tem = []
    for sep in range(5):
        if len(temp) != 0:
            tem.append(temp[0])
            del temp[0]
        else:
            tem.append(0)
    mw.append(tem)
print(mw)
total = []
for n in range(len(mw)):
    t = mw[n][4] << 5
    t = t | mw[n][3]
    t = t << 5
    t = t | mw[n][2]
    t = t << 5
    t = t | mw[n][1]
    t = t << 5
    t = t | mw[n][0]
    total.append(t)
print(total)