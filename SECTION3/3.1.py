import tkinter as tk

window = tk.Tk()
window.title("Перша програма")
window.geometry("1024x768")

label = tk.Label(window, text="Hello, world!", font=("Arial", 24))
label.pack(expand=True)

close_button = tk.Button(window, text="Закрити", command=window.destroy, font=("Arial", 14))
close_button.pack(pady=20)

window.mainloop()
