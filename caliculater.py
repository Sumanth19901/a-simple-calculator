import tkinter as tk
from tkinter import END, ttk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_entry_frame(root):
    entry_frame = ttk.Frame(root)
    entry_frame.pack(fill="x", padx=10, pady=10)

    entry = ttk.Entry(entry_frame, width=35)
    entry.pack(fill="x")

    return entry

def create_button_frame(root):
    button_frame = ttk.Frame(root)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)

    buttons = []
    for i in range(10):
        button = ttk.Button(button_frame, text=str(i), width=5)
        button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        buttons.append(button)

    operators = ["+", "-", "*", "/", "^", "sin", "cos", "tan", "(", ")"]
    for i, op in enumerate(operators):
        button = ttk.Button(button_frame, text=op, width=5)
        button.grid(row=i // 2, column=3 + i % 2, padx=5, pady=5)
        buttons.append(button)

    equal_button = ttk.Button(button_frame, text="=", width=11)
    equal_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    buttons.append(equal_button)

    clear_button = ttk.Button(button_frame, text="Clear", width=11)
    clear_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
    buttons.append(clear_button)

    graph_button = ttk.Button(button_frame, text="Graph", width=11)
    graph_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    buttons.append(graph_button)

    return buttons

def create_gui(root):
    entry = create_entry_frame(root)
    buttons = create_button_frame(root)

    def button_click(number):
        current = entry.get()
        entry.delete(0, END) 
        entry.insert(0, str(current) + str(number))

    def button_clear():
        entry.delete(0, END)

    def button_equal():
        try:
            result = str(eval(entry.get()))
            entry.delete(0, END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(0, "Error")

    def button_graph():
        try:
            x = np.linspace(-10, 10, 400)
            y = eval(entry.get())
            plt.plot(x, y)
            plt.show()
        except Exception as e:
            entry.delete(0, END)
            entry.insert(0, "Error")

    for button in buttons:
        if button.cget("text").isdigit():
            button.config(command=lambda btn=button: button_click(int(btn.cget("text"))))
        elif button.cget("text") in ["+", "-", "*", "/", "^", "sin", "cos", "tan", "(", ")"]:
            button.config(command=lambda btn=button: button_click(btn.cget("text")))
        elif button.cget("text") == "=":
            button.config(command=button_equal)
        elif button.cget("text") == "Clear":
            button.config(command=button_clear)
        elif button.cget("text") == "Graph":
            button.config(command=button_graph)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width * 0.8)
    window_height = int(screen_height * 0.8)
    root.geometry(f"{window_width}x{window_height}")

root = tk.Tk()
root.title("Simple Calculator with 3D Graphics")

create_gui(root)

root.mainloop()