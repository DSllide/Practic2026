import math

v0 = float(input("Введіть початкову швидкість (м/с): "))
angle = float(input("Введіть кут вильоту (градуси): "))

g = 9.81
angle_rad = math.radians(angle)

t_flight = (2 * v0 * math.sin(angle_rad)) / g
h_max = (v0 ** 2 * math.sin(angle_rad) ** 2) / (2 * g)

print("Максимальна висота польоту:", h_max)
print("Висота снаряда по секундах:")

t = 0
while t <= t_flight:
    h = v0 * t * math.sin(angle_rad) - (g * t ** 2) / 2
    if h < 0:
        h = 0
    print("t =", t, "c | h =", round(h, 2), "м")
    t += 1
