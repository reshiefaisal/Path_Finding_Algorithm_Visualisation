from tkinter import *
from tkinter import ttk


# initialisation of the basic window of tkinter as black
root = Tk()
root.title("Path-Finding Algorithm Visualisation.")
root.maxsize(900, 900)
root.config(bg='black')
# Variables and function

selected_agm = []  # variable for auto generated menu (agm)
selected_alg = []  # variable for the chosen algorithm
WIDTH = 900
ROWS = 30


def scale_action(event):
    if auto_generate_menu.get() == 'Random':
        wallScale.configure(state='normal')
    else:
        wallScale.configure(state='disable')

# creating a basic structure for user interface

ui_frame = Frame(root, width=900, height=100, bg='grey')
ui_frame.grid(row=0, column=0, padx=10, pady=5)

# creating the canvas and grid structure

canvas = Canvas(root, width=900, height=480, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# building the components of the user interface
# row 0
auto_generate_menu = ttk.Combobox(ui_frame, textvariable=selected_agm, values=['Random', 'Circular', 'Carved'])
auto_generate_menu.grid(row=0, column=0, padx=2, pady=2, sticky=W)
auto_generate_menu.current(0)
auto_generate_menu.bind("<<ComboboxSelected>>", scale_action)

wallScale = Scale(ui_frame, from_=10, to=50, resolution=1, orient=HORIZONTAL, label='Wall Density', length=200)
wallScale.grid(row=0, column=1, padx=2, pady=2, sticky=W)
Button(ui_frame, text='Build Maze', bg='pale green').grid(row=0, column=2, padx=2, pady=2)

algMenu = ttk.Combobox(ui_frame, textvariable=selected_alg,
                       values=['A* Algorithm', 'Breadth_first search', 'Depth_first Search'])
algMenu.grid(row=0, column=3, padx=2, pady=2)
algMenu.current(0)

speedScale = Scale(ui_frame, from_=0.05, to=3.0, digits=2, resolution=0.1, orient=HORIZONTAL, label='Speed', length=160)
speedScale.grid(row=0, column=4, padx=2, pady=2)
Button(ui_frame, text='Start Search', bg='light salmon').grid(row=0, column=5, padx=2, pady=2)
Button(ui_frame, text="Reset", bg='White').grid(row=0, column=6, padx=2, pady=2)

# run the tkinter instance
root.mainloop()
