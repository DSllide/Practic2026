number = int(input("Введіть ціле число: "))

is_negative = number < 0
number = abs(number)

result = ""

if number == 0:
    result = "0"
else:
    while number > 0:
        digit = number % 10
        result = chr(ord('0') + digit) + result
        number //= 10

if is_negative:
    result = "-" + result

print("Рядкове представлення числа:", result)
