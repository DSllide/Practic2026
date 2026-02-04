students = [
    {
        "name": "Ілья",
        "surname": "Петренко",
        "grades": [80, 75, 90, 85, 88]
    },
    {
        "name": "Оксана",
        "surname": "Коваль",
        "grades": [90, 92, 85, 87, 91]
    },
    {
        "name": "Андрій",
        "surname": "Мельник",
        "grades": [70, 78, 82, 80, 76]
    }
]

subjects_count = 5

print("Середній бал кожного студента:")
for student in students:
    average = sum(student["grades"]) / subjects_count
    print(
        student["name"],
        student["surname"],
        "-",
        round(average, 2)
    )

print("\nСередній бал групи з кожної дисципліни:")

for i in range(subjects_count):
    subject_sum = 0
    for student in students:
        subject_sum += student["grades"][i]
    subject_average = subject_sum / len(students)
    print("Дисципліна", i + 1, ":", round(subject_average, 2))
