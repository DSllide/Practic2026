import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    global current_file
    if text_edit.edit_modified():
        if not ask_save_changes():
            return
    text_edit.delete(1.0, tk.END)
    current_file = None
    window.title("Блокнот - Новий файл")
    text_edit.edit_modified(False)

def open_file():
    global current_file
    if text_edit.edit_modified():
        if not ask_save_changes():
            return
    file_path = filedialog.askopenfilename(filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text_edit.delete(1.0, tk.END)
            text_edit.insert(tk.END, f.read())
        current_file = file_path
        window.title(f"Блокнот - {current_file}")
        text_edit.edit_modified(False)

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text_edit.get(1.0, tk.END))
    else:
        save_as_file()
    text_edit.edit_modified(False)

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_edit.get(1.0, tk.END))
        current_file = file_path
        window.title(f"Блокнот - {current_file}")
        text_edit.edit_modified(False)

def exit_app():
    if text_edit.edit_modified():
        if not ask_save_changes():
            return
    window.destroy()

def ask_save_changes():
    answer = messagebox.askyesnocancel("Попередження", "Зберегти зміни перед виходом?")
    if answer:
        save_file()
        return True
    elif answer is False:
        return True
    else:  
        return False

window = tk.Tk()
window.title("Блокнот - Новий файл")
window.geometry("600x400")

current_file = None


menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новий", command=new_file)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_command(label="Зберегти як...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=exit_app)


text_edit = tk.Text(window, wrap="word")
text_edit.pack(expand=1, fill="both")
text_edit.edit_modified(False)

window.protocol("WM_DELETE_WINDOW", exit_app)
window.mainloop()
