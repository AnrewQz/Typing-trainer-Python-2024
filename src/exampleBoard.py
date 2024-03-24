import tkinter as tk
import textGenerator as textG


class ExampleBoard(tk.Frame):
    def __init__(self, window, text):
        super().__init__(window, width=700, height=300, bg="#E9967A")
        l_text = tk.Label(self, text=text, wraplength="700", bg="#F08080", fg="white", font="Arial 14")
        l_text.pack(fill = tk.X)
