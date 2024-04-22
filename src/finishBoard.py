from tkinter import *
class FinishBoard(Frame):
    def  __init__(self, window):
        super().__init__(window)
        text = "Сongratulations! On this page, you can see your current results. Use Menu to continue"
        self.final_text = Label(self, text=text,
                                 bg='#EFCFF3',
                                 anchor='nw',
                                 justify='left',
                                 padx=5,
                                 pady=5,
                                 relief=RAISED,
                                 bd=10,
                                 font="Ariel, 20", wraplength=650)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.3)
        self.final_text.place(relx=0, rely=0, relwidth=1, relheight=1)

