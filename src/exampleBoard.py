from tkinter import *

class TextExampleScreen(Frame):
    def  __init__(self, window, text):
        super().__init__(window)
        self.example_text = Label(self, text=text,
                                 bg='#DEC09B',
                                 relief = RAISED,
                                 anchor='nw',
                                 justify='left',
                                 padx=5,
                                 pady=5,
                                 bd=10,
                                 font="Ariel, 15", wraplength=650)
        self.example_text.place(relx=0, rely=0, relwidth=1, relheight=1)



