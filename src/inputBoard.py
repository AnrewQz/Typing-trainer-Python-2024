import checker
import tkinter as tk


class InputBoard(tk.Frame):
    def __init__(self, window, generated_text, stat):
        super().__init__(window)
        self.master = window
        self.typed_text_screen = tk.Text(self, bg='#BFE2F1', relief=tk.RAISED, width=90, height=8, padx=5, pady=5,
                                         bd=10, font="Ariel, 15", wrap="word")
        self.typed_text_screen.bind("<Key>", self.key_press)
        self.number_of_typed_screen = 0
        self.generated_text = generated_text
        self.typed_text_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.stat = stat

    def key_press(self, event):
        if (event.char != "Shift") and checker.check(self.number_of_typed_screen, event.char, self.generated_text,
                                                     self.stat, self.master) == True:
            self.number_of_typed_screen += 1
        else:
            return "break"
