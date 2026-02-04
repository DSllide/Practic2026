import math

def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    return math.pi * radius ** 2

print("Процедурний підхід:")
w = float(input("Введіть ширину прямокутника: "))
h = float(input("Введіть висоту прямокутника: "))
r = float(input("Введіть радіус кола: "))

print("Площа прямокутника:", rectangle_area(w, h))
print("Площа кола:", circle_area(r))


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

print("\nОб'єктно-орієнтований підхід:")
rect = Rectangle(w, h)
circle = Circle(r)

print("Площа прямокутника:", rect.area())
print("Площа кола:", circle.area())
