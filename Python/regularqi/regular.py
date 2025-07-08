import re
x = str('+996'+input('Введите свой номер: 000 000 000:'))
x = x.replace(' ','')
x = x.replace('-','')
def ckecker(x):
    if len(x) != 13:
        print("Неверно")
        break
    if (re.fullmatch(r'\+99670[0-9]\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+996755\d{3}\d{3}', x)):0
        return 'Верно'
    if (re.fullmatch(r'\+99650[0-9]\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+99655[0-9]\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+99677[0-9]\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+99622[0-8]\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+996880\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+996888\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+996990\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+996995\d{3}\d{3}', x)):
        return 'Верно'
    if (re.fullmatch(r'\+99699[7-9]\d{3}\d{3}', x)):
        return 'Верно'
    else:
        return 'Номер неправльный'
        
print(ckecker(x))