import tkinter as tk
from tkinter import *
import tkinter.font as font

root = tk.Tk()
root.title("Calculator by egegl")
frame = Frame(root, borderwidth=5)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)
frame.grid_rowconfigure(5, weight=1)
frame.grid_rowconfigure(6, weight=1)
frame.pack(fill=BOTH, expand=1)
font.nametofont('TkDefaultFont').configure(size=10)


def button_click(button):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(button))


def clear():
    entry.delete(0, END)


def equal():
    try:
        final_expression = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(final_expression))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")


entry = Entry(frame, borderwidth=5)
button_0 = tk.Button(frame, text="0", command=lambda: button_click(0))
button_dot = tk.Button(frame, text=".", command=lambda: button_click("."))
button_clear = tk.Button(frame, text="Clear", command=lambda: clear())
button_1 = tk.Button(frame, text="1", command=lambda: button_click(1))
button_2 = tk.Button(frame, text="2", command=lambda: button_click(2))
button_3 = tk.Button(frame, text="3", command=lambda: button_click(3))
button_4 = tk.Button(frame, text="4", command=lambda: button_click(4))
button_5 = tk.Button(frame, text="5", command=lambda: button_click(5))
button_6 = tk.Button(frame, text="6", command=lambda: button_click(6))
button_7 = tk.Button(frame, text="7", command=lambda: button_click(7))
button_8 = tk.Button(frame, text="8", command=lambda: button_click(8))
button_9 = tk.Button(frame, text="9", command=lambda: button_click(9))
button_add = tk.Button(frame, text="+", command=lambda: button_click(" + "))
button_subtract = tk.Button(frame, text="-", command=lambda: button_click(" - "))
button_equal = tk.Button(frame, text="=", command=equal)
button_multiply = tk.Button(frame, text="x", command=lambda: button_click(" * "))
button_divide = tk.Button(frame, text="÷", command=lambda: button_click(" / "))

entry.grid(row=0, column=0, sticky="nsew", columnspan=3)
button_1.grid(row=1, column=0, sticky="nsew")
button_2.grid(row=1, column=1, sticky="nsew")
button_3.grid(row=1, column=2, sticky="nsew")
button_4.grid(row=2, column=0, sticky="nsew")
button_5.grid(row=2, column=1, sticky="nsew")
button_6.grid(row=2, column=2, sticky="nsew")
button_7.grid(row=3, column=0, sticky="nsew")
button_8.grid(row=3, column=1, sticky="nsew")
button_9.grid(row=3, column=2, sticky="nsew")
button_0.grid(row=4, column=0, sticky="nsew")
button_dot.grid(row=4, column=1, sticky="nsew")
button_clear.grid(row=4, column=2, sticky="nsew")
button_subtract.grid(row=5, column=0, sticky="nsew")
button_add.grid(row=5, column=1, sticky="nsew")
button_equal.grid(row=5, column=2, sticky="nsew", rowspan=2)
button_multiply.grid(row=6, column=0, sticky="nsew")
button_divide.grid(row=6, column=1, sticky="nsew")

root.mainloop()
