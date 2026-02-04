class Animal:
    def sound(self):
        print("Цей звір видає якийсь звук")

class Dog(Animal):
    def sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def sound(self):
        print("Мяу-мяу!")

class Cow(Animal):
    def sound(self):
        print("Му-у-у!")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"{animal.__class__.__name__} видає звук: ", end="")
    animal.sound()
