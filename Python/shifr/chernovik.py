letters = [['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']]
pswd = list(input('Введите пароль: '))
key = list(input('Введите ключ: '))
for i in range(len(pswd)):
    if (len(pswd) == len(key)):
        continue
    else:
        key+=key[i]
for j in range(len(letters[0])):
    if (j < len(letters)):
        letters.append(letters[-1])
        clown = list(letters[-1].pop(0))
        letters[-1] = letters[-1] + clown
del letters[-1]
del letters[-1]
cl = []
pss = []
truler = False
letters.insert(0,['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'])
for word in range(len(pswd)):
    truler = False
    for n in range(len(letters[0])): 
        if (pswd[word] == letters[0][n]): 
            for key_i in range(len(key)): 
                for key_j in range(len(letters[0])):
                    if (truler == True):
                        continue
                    elif (key[key_i] == letters[0][key_j]):
                        pss.append(letters[key_j][n]) 
                        cl.append(n)
                        truler = True
k = ''.join(pss)
print(k)