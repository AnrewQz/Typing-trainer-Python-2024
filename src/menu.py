import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, window):
        super().__init__(window, width=1000, height=600, bg="grey")
        self.button = tk.Button(text="Начать", width=10, height=3, bg="red").pack(anchor="center")
