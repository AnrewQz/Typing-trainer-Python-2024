from tkinter import *

class ResultsScreen(Frame):
    def  __init__(self, window):
        super().__init__(window)
        with open("results.txt", "r") as results:
            list_text = results.readlines()
            amount_of_line = len(list_text)
            self.results_screen = Canvas(self, scrollregion=(0, 0, 20*amount_of_line, 20*amount_of_line),
                                 bg='#9BDEC0',
                                 width=665, height=400,
                                 relief=RAISED,
                                 bd=5)
            self.results_screen.pack()
            self.scrollbar = Scrollbar(self, orient=VERTICAL)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.scrollbar.config(command=self.results_screen.yview)
            str_text = ""
            for i in range(amount_of_line):
                str_text+=list_text[i]
            self.results_screen.create_text(8, 8, text=str_text, anchor='nw', justify='left', font="Ariel 12")
            self.scrollbar["command"]=self.results_screen.yview
            self.results_screen.config(yscrollcommand=self.scrollbar.set)
            self.results_screen.pack(side=LEFT, expand=True, fill=BOTH)
