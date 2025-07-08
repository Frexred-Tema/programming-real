import csv
class Flakes:
    def __init__(self, length):
        self.length = length
    def __str__(self):
        return f'Размер {self.length}'
box_of_flakes = []
with open("iris.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        if (row[0] != 'sepal.length'):
            length = row[0]
            box_of_flakes.append(Flakes(length))
for i in range(len(box_of_flakes)):
    for j in range(i, len(box_of_flakes)):
        if box_of_flakes[i].length < box_of_flakes[j].length:
            temporary = box_of_flakes[j]
            box_of_flakes[j] = box_of_flakes[i]
            box_of_flakes[i] = temporary
for sheet in box_of_flakes:
    print(str(sheet))