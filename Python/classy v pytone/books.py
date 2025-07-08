class Books:
    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
    def __str__(self):
        return (f"Автор: {self.author} Название: {self.name} Цена: {self.price}")
books = []
books[0].author
for i in range(5):
    author = input("Введите автора книги ")
    name = input("Введите название книги ")
    price = input("Введите цену книги ")
    books.append(Books(author, name, price))
for i in range(len(books)):
    t1 = str(books[i]).split(' ')
    print(t1)
    for j in range(i, len(books)):
        t2 = str(books[j]).split(' ')
        print(t2)
        if (t1[-1] > t2[-1]):
            temp_arr = ' '.join(t2)
            books[j] = ' '.join(t1)
            books[i] = temp_arr
            print(books[i], books[j])
for book in books:
    print(str(book))