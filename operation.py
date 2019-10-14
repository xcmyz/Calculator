from tkinter import NORMAL, END
from module import get_output


def get_input(entry, argu):
    entry.config(state=NORMAL)
    entry.insert(END, argu)
    entry.icursor(len(entry.get()))
    entry.xview(len(entry.get()))


def backspace(entry):
    entry.config(state=NORMAL)
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.config(state=NORMAL)
    entry.delete(0, END)


def cal(entry):
    input = entry.get()
    output = str(get_output(input))
    print(output)
    output = str(eval(input.strip()))

    clear(entry)
    entry.insert(END, output)
