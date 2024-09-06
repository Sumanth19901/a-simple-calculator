import tkinter as tk
from tkinter import END, ttk

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

    operators = ["+", "-", "*", "/"]
    for i, op in enumerate(operators):
        button = ttk.Button(button_frame, text=op, width=5)
        button.grid(row=i, column=3, padx=5, pady=5)
        buttons.append(button)

    equal_button = ttk.Button(button_frame, text="=", width=11)
    equal_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    buttons.append(equal_button)

    clear_button = ttk.Button(button_frame, text="Clear", width=11)
    clear_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
    buttons.append(clear_button)

    return buttons

def create_gui(root):
    entry = create_entry_frame(root)
    buttons = create_button_frame(root)

    def button_click(number):
        current = entry.get()
        entry.delete(0, END) # type: ignore
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

    for button in buttons:
        if button.cget("text").isdigit():
            button.config(command=lambda btn=button: button_click(int(btn.cget("text"))))
        elif button.cget("text") in ["+", "-", "*", "/"]:
            button.config(command=lambda btn=button: button_click(btn.cget("text")))
        elif button.cget("text") == "=":
            button.config(command=button_equal)
        elif button.cget("text") == "Clear":
            button.config(command=button_clear)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("250x300")

create_gui(root)

root.mainloop()