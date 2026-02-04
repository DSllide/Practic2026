import tkinter as tk
from logic import calculate

class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Модульний калькулятор")
        self.window.geometry("300x200")

        tk.Label(self.window, text="Число 1:").pack(pady=5)
        self.entry1 = tk.Entry(self.window)
        self.entry1.pack(pady=5)

        tk.Label(self.window, text="Число 2:").pack(pady=5)
        self.entry2 = tk.Entry(self.window)
        self.entry2.pack(pady=5)

        frame = tk.Frame(self.window)
        frame.pack(pady=10)

        tk.Button(frame, text="+", width=5, command=lambda: self.show_result("+")).pack(side="left", padx=5)
        tk.Button(frame, text="-", width=5, command=lambda: self.show_result("-")).pack(side="left", padx=5)
        tk.Button(frame, text="*", width=5, command=lambda: self.show_result("*")).pack(side="left", padx=5)
        tk.Button(frame, text="/", width=5, command=lambda: self.show_result("/")).pack(side="left", padx=5)

        self.result_label = tk.Label(self.window, text="Результат: ")
        self.result_label.pack(pady=10)

    def show_result(self, op):
        num1 = self.entry1.get()
        num2 = self.entry2.get()
        result = calculate(num1, num2, op)
        self.result_label.config(text=f"Результат: {result}")

    def run(self):
        self.window.mainloop()
