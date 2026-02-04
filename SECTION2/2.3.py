num_students = int(input("Введіть кількість студентів: "))

students_scores = {}

for _ in range(num_students):
    name = input("\nВведіть ім'я студента: ")
    scores_str = input("Введіть оцінки через пробіл: ")
    scores = list(map(float, scores_str.split()))
    students_scores[name] = scores

average_scores = {}
for name, scores in students_scores.items():
    avg = sum(scores) / len(scores) if scores else 0
    average_scores[name] = avg

all_scores = []
for scores in students_scores.values():
    all_scores.extend(scores)

unique_scores = set(all_scores)


print("\nСередній бал кожного студента:")
for name, avg in average_scores.items():
    print(f"{name}: {avg:.2f}")

print("\nУнікальні оцінки серед усіх студентів:", unique_scores)
print("\nСловник у форматі {ім'я: середній_бал}:")
print(average_scores)
