w_log = input('Введите логин: ')
w_pswd = input('Введите пароль: ')
class Thing:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
    def __str__(self):
        return f"{self.name:<15}{self.price:<6}{self.rating:<3}"
assortiment = []
t1 = []
t1.append(Thing('Coca-Cola', '1$', '3.2'))
t1.append(Thing('Fanta', '1$', '5'))
t1.append(Thing('Sprite', '0.7$', '4.7'))
t1.append(Thing('Pepsi', '0.8$', '3.9'))
assortiment.append(t1)

t1 = []
t1.append(Thing('Яблоко', '1.5$', '5'))
t1.append(Thing('Груша', '1$', '3.9'))
t1.append(Thing('Банан', '2.5$', '5'))
t1.append(Thing('Персик', '1.8$', '4.9'))
assortiment.append(t1)

class Category:
    def __init__(self, name, things):
        self.name = name
        self.things = things
    def __str__(self):
        return f"{self.name}", self.things
towary = []
towary.append(Category('Напитки', assortiment[0]))
towary.append(Category('Фрукты', assortiment[1]))

class Basket:
    def __init__(self, bought):
        self.bought = bought
    def __str__(self):
        return f"{self.bought}"
korzina = []
korzina.append(Basket(assortiment[0][2]))
korzina.append(Basket(assortiment[1][2]))
korzina.append(Basket(assortiment[1][3]))

class User:
    def __init__(self, login, password, basket):
        self.login = login
        self.password = password
        self.basket = basket
    def __str__(self):
        return str(f"{self.login} купил(а) {self.basket}")
for i in range(len(assortiment)):
    for j in range(len(assortiment[i])):
        print(str(assortiment[i][j]))
users = []
users.append(User(w_log, w_pswd, korzina))
print(users[0])
