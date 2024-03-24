import tkinter as tk
import checker


class InputBoard(tk.Frame):
    def __init__(self, window, chckr: checker.Checker):
        super().__init__(window, width=700, height=300, bg="#E9967A")
        self.users_input = tk.Text(self, width=700, height=300, wrap="word", bg="#B22222", fg="white", font="Arial 14")
        self.users_input.pack(fill = tk.X)
        self.users_input.bind("<Key>", chckr.is_correct)
