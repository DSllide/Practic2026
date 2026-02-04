import pandas as pd


df = pd.read_csv("students.csv")

subjects = ["subject1", "subject2", "subject3", "subject4", "subject5"]

print("Середній бал кожного студента:")


df["average"] = df[subjects].mean(axis=1)

for index, row in df.iterrows():
    print(f"{row['name']} {row['surname']} - {round(row['average'], 2)}")

print("\nСередній бал групи з кожної дисципліни:")


subject_averages = df[subjects].mean()

for i, avg in enumerate(subject_averages, start=1):
    print(f"Дисципліна {i}: {round(avg, 2)}")
