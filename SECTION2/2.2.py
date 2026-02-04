class Student:
    def __init__(self, name, group, average_score):
        self.name = name
        self.group = group
        self.average_score = average_score

    def show_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Група: {self.group}")
        print(f"Середній бал: {self.average_score}")
        print("-" * 30)


student1 = Student("Олександр", "CS-101", 4.5)
student2 = Student("Софія", "CS-102", 4.8)
student3 = Student("Іван", "CS-101", 4.2)

student1.show_info()
student2.show_info()
student3.show_info()
