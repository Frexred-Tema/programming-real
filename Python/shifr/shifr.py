password = list(str(input('Введите желаемый пароль: ')))
key = int(input('Введите ключ: '))
secret_code = []
letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ',
            'Ы', 'Ь', 'Э', 'Ю', 'Я']
for i in range(len(password)):
    for j in range(len(letters)):
        if (password[i] == letters[j]):
            secret_code.append(letters[(j + key)%36])
print("Ваш зашифрованный пароль:", secret_code)