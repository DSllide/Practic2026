import tkinter as tk
from tkinter import StringVar, IntVar

def save_info():
    name_val = name_entry.get()
    gender_val = gender_var.get()
    agree_val = "Погодився" if agree_var.get() else "Не погодився"
    info_label.config(text=f"Ім'я: {name_val}\nСтать: {gender_val}\nУмови: {agree_val}")

window = tk.Tk()
window.title("Анкета користувача")
window.geometry("400x250")

tk.Label(window, text="Ім'я:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Стать:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
gender_var = StringVar(value="Чоловіча")
tk.Radiobutton(window, text="Чоловіча", variable=gender_var, value="Чоловіча").grid(row=1, column=1, sticky="w")
tk.Radiobutton(window, text="Жіноча", variable=gender_var, value="Жіноча").grid(row=1, column=1, sticky="e")

agree_var = IntVar()
tk.Checkbutton(window, text="Погоджуюсь із умовами", variable=agree_var).grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(window, text="Зберегти", command=save_info).grid(row=3, column=0, columnspan=2, pady=10)

info_label = tk.Label(window, text="", justify="left", anchor="w")
info_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

window.mainloop()
