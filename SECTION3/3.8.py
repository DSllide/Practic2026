import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

class DrawingApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Графіка")
        self.window.geometry("650x500")

        self.current_color = "black"
        self.draw_mode = tk.StringVar(value="line")
        self.start_x = None
        self.start_y = None
        self.temp_shape = None

        control_frame = tk.Frame(self.window)
        control_frame.pack(pady=5)

        tk.Radiobutton(control_frame, text="Лінія", variable=self.draw_mode, value="line").pack(side="left", padx=5)
        tk.Radiobutton(control_frame, text="Коло", variable=self.draw_mode, value="circle").pack(side="left", padx=5)
        tk.Button(control_frame, text="Вибрати колір", command=self.choose_color).pack(side="left", padx=5)
        tk.Button(control_frame, text="Очистити", command=self.clear_canvas).pack(side="left", padx=5)
        tk.Button(control_frame, text="Зберегти", command=self.save_canvas).pack(side="left", padx=5)

        self.canvas = tk.Canvas(self.window, width=600, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_preview)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def choose_color(self):
        color = colorchooser.askcolor(title="Виберіть колір")[1]
        if color:
            self.current_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".ps",
                                                 filetypes=[("PostScript files", "*.ps"), ("Всі файли", "*.*")])
        if file_path:
            self.canvas.postscript(file=file_path)
            messagebox.showinfo("Збережено", f"Зображення збережено у {file_path}")

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.temp_shape = None

    def draw_preview(self, event):
        if self.temp_shape:
            self.canvas.delete(self.temp_shape)
        if self.draw_mode.get() == "line":
            self.temp_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                                      fill=self.current_color, width=2)
        elif self.draw_mode.get() == "circle":
            self.temp_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y,
                                                      outline=self.current_color, width=2)

    def end_draw(self, event):
        if self.temp_shape:
            self.canvas.delete(self.temp_shape)
        if self.draw_mode.get() == "line":
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                    fill=self.current_color, width=2)
        elif self.draw_mode.get() == "circle":
            self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y,
                                    outline=self.current_color, width=2)
        self.temp_shape = None

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = DrawingApp()
    app.run()
