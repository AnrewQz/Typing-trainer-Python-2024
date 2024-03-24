import tkinter as tk
import exampleBoard as exampleB
import statsBoard as statsB
import inputBoard as inputB
import menu
import textGenerator as textG
import checker

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Trainer")
        self.geometry("1000x600")
        # self.menu_frame = menu.Menu(self).place(relx = 0, rely = 0)
        self.start_training()

    def start_training(self):
        text = textG.get_text()
        chckr = checker.Checker(text)
        self.example_frame =\
            exampleB.ExampleBoard(self, text).place(relx=0, rely=0, relwidth=0.7, relheight=0.5)
        self.input_frame =\
            inputB.InputBoard(self, chckr).place(relx = 0, rely = 0.5, relwidth = 0.7, relheight = 0.5)
        self.stats_frame =\
            statsB.StatsBoard(self).place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1)
