import tkinter as tk
from inputBoard import *
from exampleBoard import *
from textGenerator import *
from statsBoard import *
from resultsScreen import *


def start_typing():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    generated_text = generate()
    example_screen = TextExampleScreen(window, generated_text)
    statistic_screen = StatisticScreen(window)
    typed_screen = InputBoard(window, generated_text, statistic_screen)
    example_screen.place(relx=0, rely=0, relwidth=1, relheight=0.3)
    typed_screen.place(relx=0, rely=0.3, relwidth=1, relheight=0.3)
    statistic_screen.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)


def exit_from_typing():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    show_info()


def show_results():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    results_label = ResultsScreen(window)
    results_label.place(relx=0, rely=0, relwidth=1, relheight=0.6)


def create_menu():
    menubar = tk.Menu(window, bg="#BFE2F1", bd=10)
    window.config(menu=menubar)
    settings_menu = tk.Menu(menubar, tearoff=0, bg="#BFE2F1")
    settings_menu.add_command(label="Start typing", command=start_typing)
    settings_menu.add_command(label="Main menu", command=exit_from_typing)
    settings_menu.add_command(label="Results", command=show_results)
    settings_menu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="Menu", menu=settings_menu, font="Arial, 30")


def show_info():
    text_info = tk.Label(window, text="For starting typing, click on the menu and choose proper option",
                         font="Arial, 15", wraplength=200, bg="#BFE2F1", relief=tk.RAISED, bd=10, fg="black")
    text_info.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3, anchor=tk.CENTER)


window = tk.Tk()
window.configure(bg="#DEC09B")
window.title('Keyboard trainer')
window.resizable(False, False)
window.geometry("700x700")
create_menu()
show_info()
window.mainloop()
