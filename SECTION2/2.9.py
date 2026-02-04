from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def info(self):
        pass

class Book(Item):
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def info(self):
        return f"Книга: {self.__title} Автор: {self.__author}"

    def get_title(self):
        return self.__title

class Magazine(Item):
    def __init__(self, title, issue):
        self.__title = title
        self.__issue = issue

    def info(self):
        return f"Журнал: {self.__title} Номер: {self.__issue}"

class Reader:
    def __init__(self, name):
        self.name = name
        self.__borrowed_items = []

    def borrow(self, item):
        self.__borrowed_items.append(item)
        print(f"{self.name} взяв {item.info()}")

    def return_item(self, item):
        if item in self.__borrowed_items:
            self.__borrowed_items.remove(item)
            print(f"{self.name} повернув {item.info()}")
        else:
            print(f"{self.name} не мав цієї книги/журналу")

    def list_borrowed(self):
        print(f"{self.name} має:")
        for i in self.__borrowed_items:
            print("-", i.info())

book1 = Book("Війна і мир", "Толстой")
book2 = Book("1984", "Орвелл")
mag1 = Magazine("Наука і життя", 5)

reader1 = Reader("Олександр")
reader2 = Reader("Марія")

reader1.borrow(book1)
reader1.borrow(mag1)
reader2.borrow(book2)

reader1.list_borrowed()
reader2.list_borrowed()

reader1.return_item(mag1)
reader1.list_borrowed()
