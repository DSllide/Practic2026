def calculate(num1, num2, op):
    try:
        n1 = float(num1)
        n2 = float(num2)
        if op == "+":
            return n1 + n2
        elif op == "-":
            return n1 - n2
        elif op == "*":
            return n1 * n2
        elif op == "/":
            if n2 == 0:
                return "Помилка: ділення на нуль"
            return n1 / n2
        else:
            return "Невідома операція"
    except ValueError:
        return "Помилка: введіть числа"
