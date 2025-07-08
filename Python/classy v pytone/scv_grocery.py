import csv
class Products:
    def __init__(self, name, mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weigth, cups, rating):
        self.name = name 
        self.mfr = mfr 
        self.type = type 
        self.calories = calories 
        self.protein = protein 
        self.fat = fat 
        self.sodium = sodium 
        self.fiber = fiber 
        self.carbo  = carbo 
        self.sugars  = sugars 
        self.potass  = potass 
        self.vitamins  = vitamins 
        self.shelf = shelf
        self.weigth = weigth
        self.cups = cups
        self.rating = rating
    def __str__(self):
        return f'{self.name:^25}|{self.mfr:^25}|{self.type:^25}|{self.calories:^25}|{self.protein:^25}|{self.fat:^25}|{self.sodium:^25}|{self.fiber:^25}|{self.carbo:^25}|{self.sugars:^25}|{self.potass:^25}|{self.vitamins:^25}|{self.shelf:^25}|{self.weigth:^25}|{self.cups:^15}|{self.rating:^15}'
product_list = []
with open("cereal.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for food in reader_variable:
        if (food[0] == 'name'):
            print(str(food))
        else:
            name = food[0]
            mfr = food[1]
            type = food[2]
            calories = food[3]
            protein = food[4]
            fat = food[5]
            sodium = food[6]
            fiber = food[7]
            carbo = food[8]
            sugars = food[9]
            potass = food[10]
            vitamins = food[11]
            shelf = food[12]
            weigth = food[13]
            cups = food[14]
            rating = food[15]
            product_list.append(Products(name, mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weigth, cups, rating))
for i in range(len(product_list)):
    for j in range(i, len(product_list)):
        if (int(product_list[i].protein) - int(product_list[i].sugars) < int(product_list[j].protein) - int(product_list[j].sugars)):
            t = product_list[j]
            product_list[j] = product_list[i]
            product_list[i] = t
dta = 1
for n in product_list:
    print(str(f"{dta} Продукт по полезности {n.name:^35} потому что он содержит {n.sugars:>3} Сахара | {n.protein:<3} Белка"))
    dta+=1