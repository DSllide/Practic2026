import math

a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

if a == 0:
    print("Це не квадратне рівняння")
else:
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Рівняння має два корені:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("Рівняння має один корінь:")
        print("x =", x)
    else:
        print("Рівняння не має дійсних коренів")
