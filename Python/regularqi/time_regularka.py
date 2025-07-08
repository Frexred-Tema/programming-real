import re
x = str(input('введите время через / - . : '))
def ckecker(x):
    if (re.fullmatch(r'[0-2][0-4].[0-5][0-9].[0-5][0-9]', x)):
        return 'Верно'
    if (re.fullmatch(r'[0-1][0-9].[0-5][0-9].[0-5][0-9]', x)):
        return 'Верно'
    if (re.fullmatch(r'[0-2][0-4]-[0-5][0-9]-[0-5][0-9]', x)):
        return 'Верно'
    if (re.fullmatch(r'[0-1][0-9]-[0-5][0-9]-[0-5][0-9]', x)):
        return 'Верно'
    if (re.fullmatch(r'[0-2][0-4]/[0-5][0-9]/[0-5][0-9]', x)):
        return 'Верно'
    if (re.fullmatch(r'[0-1][0-9]/[0-5][0-9]/[0-5][0-9]', x)):
        return 'Верно'
    else:
        return 'Неверно'
print(ckecker(x))