import tkinter as tk
from tkinter import ttk, colorchooser
import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config():
    config["bg_color"] = main_frame.cget("bg")
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def choose_color():
    color = colorchooser.askcolor(title="Виберіть колір фону")[1]
    if color:
        main_frame.config(bg=color)
        save_config()

window = tk.Tk()
window.title("Програма з вкладками")
window.geometry("500x400")

tab_control = ttk.Notebook(window)

main_tab = ttk.Frame(tab_control)
settings_tab = ttk.Frame(tab_control)
about_tab = ttk.Frame(tab_control)

tab_control.add(main_tab, text="Головна")
tab_control.add(settings_tab, text="Налаштування")
tab_control.add(about_tab, text="Про програму")
tab_control.pack(expand=1, fill="both")


main_frame = tk.Frame(main_tab)
main_frame.pack(expand=1, fill="both", padx=10, pady=10)

tk.Label(main_frame, text="Ім'я:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(main_frame)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(main_frame, text="Вік:").grid(row=1, column=0, sticky="w", pady=5)
age_entry = tk.Entry(main_frame)
age_entry.grid(row=1, column=1, pady=5)

tk.Label(main_frame, text="Ваше місто:").grid(row=2, column=0, sticky="w", pady=5)
city_entry = tk.Entry(main_frame)
city_entry.grid(row=2, column=1, pady=5)


tk.Button(settings_tab, text="Вибрати колір фону", command=choose_color).pack(pady=20)


about_text = "Автор: Володимир\nВерсія: 1.0\nПрограма для демонстрації вкладок"
tk.Label(about_tab, text=about_text, justify="left").pack(padx=10, pady=10)


config = load_config()
if "bg_color" in config:
    main_frame.config(bg=config["bg_color"])

window.mainloop()
