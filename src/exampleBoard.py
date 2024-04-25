import tkinter as tk


class TextExampleScreen(tk.Frame):
    def __init__(self, window, text):
        super().__init__(window)
        self.example_text = tk.Label(self, text=text,
                                     bg='#DEC09B',
                                     relief=tk.RAISED,
                                     anchor='nw',
                                     justify='left',
                                     padx=5,
                                     pady=5,
                                     bd=10,
                                     font="Ariel, 15", wraplength=650)
        self.example_text.place(relx=0, rely=0, relwidth=1, relheight=1)
