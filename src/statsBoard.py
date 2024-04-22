from tkinter import *
import time

class StatisticScreen(Frame):
    def  __init__(self, window):
        super().__init__(window)
        self.amount_of_symbols = 0
        self.amount_of_words = 0
        self.amount_of_mistakes = 0
        self.cpm = 0
        self.wpm = 0
        self.starting_time = 0
        self.final_time = 0
        self.current_time = 0
        self.cpm_label = Label(self, text="Amount of symbols per minute: 0",
                                 bg='#9BDEC0',
                                 width=90, height=1,
                                 wraplength=600,
                                 anchor='nw',
                                 justify='center',
                                 padx=5,
                                 pady=5,
                                 relief=RAISED,
                                 bd=10,
                                 font="Ariel, 15")
        self.wpm_label = Label(self, text="Amount of words per minute: 0",
                         bg='#9BDEC0',
                         width=90, height=1,
                         wraplength=600,
                         anchor='nw',
                         justify='center',
                         padx=5,
                         pady=5,
                         relief=RAISED,
                         bd=10,
                         font="Ariel, 15")
        self.mistakes_label = Label(self, text="Amount of mistakes: 0",
                              bg='#9BDEC0',
                              width=90, height=1,
                              wraplength=600,
                              anchor='nw',
                              justify='center',
                              padx=5,
                              pady=5,
                              relief=RAISED,
                              bd=10,
                              font="Ariel, 15")
        text_time = "Time: "
        self.time_label = Label(self,
                                    bg='#9BDEC0', text=text_time,
                                    width=90, height=1,
                                    wraplength=600,
                                    anchor='nw',
                                    justify='center',
                                    padx=5,
                                    pady=5,
                                    relief=RAISED,
                                    bd=10,
                                    font="Ariel, 15")
        self.every_sec()
        self.time_label.place(relx=0, rely=0, relwidth=1, relheight=0.25)
        self.cpm_label.place(relx=0, rely=0.25, relwidth=1, relheight=0.25)
        self.wpm_label.place(relx=0, rely=0.5, relwidth=1, relheight=0.25)
        self.mistakes_label.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

    def every_sec(self):
        if self.final_time!=0:
            return
        if self.starting_time!=0:
            self.time_label['text'] = "Time: " + str((time.time() - self.starting_time)//1)
            self.after(1000, self.every_sec)
        else:
            self.time_label['text'] = "Time: 0.0"
            self.after(1000, self.every_sec)



