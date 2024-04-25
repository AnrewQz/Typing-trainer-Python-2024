import tkinter as tk


class ResultsScreen(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        with open("results.txt", "r") as results:
            list_text = results.readlines()
            amount_of_line = len(list_text)
            self.results_screen = tk.Canvas(self, scrollregion=(0, 0, 20 * amount_of_line, 20 * amount_of_line),
                                            bg='#9BDEC0',
                                            width=665, height=400,
                                            relief=tk.RAISED,
                                            bd=5)
            self.results_screen.pack()
            self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.scrollbar.config(command=self.results_screen.yview)
            str_text = ""
            for i in range(amount_of_line):
                str_text += list_text[i]
            self.results_screen.create_text(8, 8, text=str_text, anchor='nw', justify='left', font="Ariel 12")
            self.scrollbar["command"] = self.results_screen.yview
            self.results_screen.config(yscrollcommand=self.scrollbar.set)
            self.results_screen.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
