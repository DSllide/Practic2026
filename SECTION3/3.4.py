import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Помилка", "Ділення на нуль неможливе!")
                return
            result = num1 / num2
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числа!")

window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x200")

tk.Label(window, text="Число 1:").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack(pady=5)

tk.Label(window, text="Число 2:").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Button(frame, text="+", width=5, command=lambda: calculate("+")).pack(side="left", padx=5)
tk.Button(frame, text="-", width=5, command=lambda: calculate("-")).pack(side="left", padx=5)
tk.Button(frame, text="*", width=5, command=lambda: calculate("*")).pack(side="left", padx=5)
tk.Button(frame, text="/", width=5, command=lambda: calculate("/")).pack(side="left", padx=5)

result_label = tk.Label(window, text="Результат: ")
result_label.pack(pady=10)

window.mainloop()
