import tkinter as tk

def greet():
    label.config(text="Вітаю, користувач!")

def clear():
    label.config(text="")

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("Програма з кнопками")
window.geometry("400x200")

label = tk.Label(window, text="", font=("Arial", 16))
label.pack(pady=20)

frame = tk.Frame(window)
frame.pack(pady=10)

greet_button = tk.Button(frame, text="Привітати", command=greet, width=10)
greet_button.pack(side="left", padx=5)

clear_button = tk.Button(frame, text="Очистити", command=clear, width=10)
clear_button.pack(side="left", padx=5)

exit_button = tk.Button(frame, text="Вийти", command=exit_app, width=10)
exit_button.pack(side="left", padx=5)

window.mainloop()
