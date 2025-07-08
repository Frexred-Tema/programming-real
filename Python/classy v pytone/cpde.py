avatar1 = str(input('Введите свой имя по шаблону Фамилия | Имя | Балл '))
avatar1 = list(avatar1.split(' | '))
avatar2 = str(input('Введите свой имя по шаблону Фамилия | Имя | Балл '))
avatar2 = list(avatar2.split(' | '))
avatar3 = str(input('Введите свой имя по шаблону Фамилия | Имя | Балл '))
avatar3 = list(avatar3.split(' | '))
avatar4 = str(input('Введите свой имя по шаблону Фамилия | Имя | Балл '))
avatar4 = list(avatar4.split(' | '))
avatar5 = str(input('Введите свой имя по шаблону Фамилия | Имя | Балл '))
avatar5 = avatar = list(avatar5.split(' | '))
mass = []
surnames = []
names = []
age = []
mass.append(avatar1)
mass.append(avatar2)
mass.append(avatar3)
mass.append(avatar4)
mass.append(avatar5)
for i in range(len(mass)):
    names.append(mass[i][0])
    surnames.append(mass[i][1])
    age.append(mass[i][2])
for max1 in range(len(age)):
    for max2 in range(len(age)):
        if (age[max1] > age[max2]):
            t1 = age[max1]
            age[max1] = age[max2]
            age[max2] = t1
            t2 = names[max1]
            names[max1] = names[max2]
            names[max2] = t2
            t3 = surnames[max1]
            surnames[max1] = surnames[max2]
            surnames[max2] = t3   
        else:
            continue     
class Student:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.score = ''
    def print(self):
        print(self.surname, self.name, self.score)
for j in range(len(names)):
    s = Student()
    s.name = names[j]
    s.surname = surnames[j]
    s.score = age[j]
    s.print()