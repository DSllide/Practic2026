def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Введіть число для обчислення факторіала: "))

result = factorial(number)

if result is None:
    print("Факторіал від’ємного числа не визначений")
else:
    print("Факторіал числа", number, "=", result)
