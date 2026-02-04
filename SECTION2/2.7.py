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
    print(f"Об'єкт {animal.__class__.__name__} викликає метод sound(): ", end="")
    animal.sound()

print("\nПояснення:")
print("У Python працює пізнє зв'язування (динамічна диспетчеризація).")
print("Це означає, що метод, який викликається на об'єкті, визначається під час виконання програми,")
print("а не під час написання коду. Тому, хоча всі об'єкти належать до базового типу Animal,")
print("для кожного об'єкта виконується саме той метод sound(), який визначений у його класі.")
