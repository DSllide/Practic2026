class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand          # марка авто
        self.year = year            # рік випуску
        self.mileage = mileage      # пробіг у км

    def drive(self, km):

        if km > 0:
            self.mileage += km
        else:
            print("Кількість кілометрів повинна бути додатньою!")

    def info(self):

        print(f"Марка: {self.brand}")
        print(f"Рік випуску: {self.year}")
        print(f"Пробіг: {self.mileage} км")
        print("-" * 30)

    def __str__(self):

        return f"{self.brand} ({self.year}) - Пробіг: {self.mileage} км"



car1 = Car("Toyota", 2015, 50000)
car2 = Car("Honda", 2018, 30000)


car1.info()
car2.info()


car1.drive(150)
print(car1)

car2.drive(200)
print(car2)
