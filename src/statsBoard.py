import tkinter as tk

class StatsBoard(tk.Frame):
    def __init__(self, window):
        super().__init__(window, width = 300, height = 600, bg = "#DC143C")
        self.number_of_missclicks = 0
        self.number_written_symbols = 0

    def percent_of_missclicks(self):
        return round(self.number_of_missclicks / self.number_written_symbols * 100)