from tkinter import Button, Entry, Tk, N, W, S, E
from operation import get_input, backspace, clear, cal
import tkinter.font as tkFont
from PIL import Image, ImageTk
from functools import partial
import os


def show():
    root = Tk()
    root.title("Calculator --XCMYZ")
    root.resizable(0, 0)

    button_bg = '#FFFFFF'
    button_active_bg = '#C6C6C6'

    entry_font = tkFont.Font(size=30)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0,
               columnspan=4,
               sticky=N+W+S+E,
               ipadx=5, ipady=7,
               padx=3, pady=5)

    myButton = partial(Button, root,
                       bg=button_bg,
                       activebackground=button_active_bg)

    im0 = Image.open(os.path.join("img", "0.png"))
    ph0 = ImageTk.PhotoImage(im0)

    im1 = Image.open(os.path.join("img", "1.png"))
    ph1 = ImageTk.PhotoImage(im1)

    im2 = Image.open(os.path.join("img", "2.png"))
    ph2 = ImageTk.PhotoImage(im2)

    im3 = Image.open(os.path.join("img", "3.png"))
    ph3 = ImageTk.PhotoImage(im3)

    im4 = Image.open(os.path.join("img", "4.png"))
    ph4 = ImageTk.PhotoImage(im4)

    im5 = Image.open(os.path.join("img", "5.png"))
    ph5 = ImageTk.PhotoImage(im5)

    im6 = Image.open(os.path.join("img", "6.png"))
    ph6 = ImageTk.PhotoImage(im6)

    im7 = Image.open(os.path.join("img", "7.png"))
    ph7 = ImageTk.PhotoImage(im7)

    im8 = Image.open(os.path.join("img", "8.png"))
    ph8 = ImageTk.PhotoImage(im8)

    im9 = Image.open(os.path.join("img", "9.png"))
    ph9 = ImageTk.PhotoImage(im9)

    button0 = myButton(image=ph0,
                       command=lambda: get_input(entry, '0'))
    button0.grid(row=4, column=1,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button1 = myButton(image=ph1,
                       command=lambda: get_input(entry, '1'))
    button1.grid(row=3, column=0,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button2 = myButton(image=ph2,
                       command=lambda: get_input(entry, '2'))
    button2.grid(row=3, column=1,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button3 = myButton(image=ph3,
                       command=lambda: get_input(entry, '3'))
    button3.grid(row=3, column=2,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button4 = myButton(image=ph4,
                       command=lambda: get_input(entry, '4'))
    button4.grid(row=2, column=0,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button5 = myButton(image=ph5,
                       command=lambda: get_input(entry, '5'))
    button5.grid(row=2, column=1,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button6 = myButton(image=ph6,
                       command=lambda: get_input(entry, '6'))
    button6.grid(row=2, column=2,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button7 = myButton(image=ph7,
                       command=lambda: get_input(entry, '7'))
    button7.grid(row=1, column=0,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button8 = myButton(image=ph8,
                       command=lambda: get_input(entry, '8'))
    button8.grid(row=1, column=1,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button9 = myButton(image=ph9,
                       command=lambda: get_input(entry, '9'))
    button9.grid(row=1, column=2,
                 ipadx=5, ipady=7,
                 padx=3, pady=5,
                 sticky=N+W+S+E)

    button_bg = '#D0D0D0'
    button_active_bg = '#666666'

    myButton = partial(Button, root,
                       bg=button_bg,
                       activebackground=button_active_bg)

    imadd = Image.open(os.path.join("img", "add.png"))
    phadd = ImageTk.PhotoImage(imadd)

    buttonadd = myButton(image=phadd,
                         command=lambda: get_input(entry, '+'))
    buttonadd.grid(row=2, column=3, ipadx=5, ipady=7,
                   padx=3, pady=5, sticky=N+W+S+E)

    imsub = Image.open(os.path.join("img", "sub.png"))
    phsub = ImageTk.PhotoImage(imsub)

    buttonsub = myButton(image=phsub,
                         command=lambda: get_input(entry, '-'))
    buttonsub.grid(row=3, column=3, ipadx=5, ipady=7,
                   padx=3, pady=5, sticky=N+W+S+E)

    immul = Image.open(os.path.join("img", "mul.png"))
    phmul = ImageTk.PhotoImage(immul)

    buttonmul = myButton(image=phmul,
                         command=lambda: get_input(entry, '*'))
    buttonmul.grid(row=4, column=2, ipadx=5, ipady=7,
                   padx=3, pady=5, sticky=N+W+S+E)

    imdiv = Image.open(os.path.join("img", "div.png"))
    phdiv = ImageTk.PhotoImage(imdiv)

    buttondiv = myButton(image=phdiv,
                         command=lambda: get_input(entry, '/'))
    buttondiv.grid(row=4, column=3, ipadx=5, ipady=7,
                   padx=3, pady=5, sticky=N+W+S+E)

    impoint = Image.open(os.path.join("img", "point.png"))
    phpoint = ImageTk.PhotoImage(impoint)

    buttonpoint = myButton(image=phpoint,
                           command=lambda: get_input(entry, '.'))
    buttonpoint.grid(row=4, column=0, ipadx=5, ipady=7,
                     padx=3, pady=5, sticky=N+W+S+E)

    imdelete = Image.open(os.path.join("img", "delete.png"))
    phdelete = ImageTk.PhotoImage(imdelete)

    buttondelete = Button(root, image=phdelete,
                          bg=button_bg,
                          activebackground=button_active_bg,
                          command=lambda: backspace(entry))
    buttondelete.grid(row=1, column=3, ipadx=5, ipady=7,
                      padx=3, pady=5, sticky=N+W+S+E)

    imlbra = Image.open(os.path.join("img", "lbra.png"))
    phlbra = ImageTk.PhotoImage(imlbra)

    buttonlbra = Button(root, image=phlbra,
                        bg=button_bg,
                        activebackground=button_active_bg,
                        command=lambda: get_input(entry, '('))
    buttonlbra.grid(row=5, column=0, ipadx=5, ipady=7,
                    padx=3, pady=5, sticky=N+S+E+W)

    imrbra = Image.open(os.path.join("img", "rbra.png"))
    phrbra = ImageTk.PhotoImage(imrbra)

    buttonrbra = Button(root, image=phrbra,
                        bg=button_bg,
                        activebackground=button_active_bg,
                        command=lambda: get_input(entry, ')'))
    buttonrbra.grid(row=5, column=1, ipadx=5, ipady=7,
                    padx=3, pady=5, sticky=N+S+E+W)

    imequal = Image.open(os.path.join("img", "equal.png"))
    phequal = ImageTk.PhotoImage(imequal)

    buttonequal = Button(root, image=phequal,
                         bg=button_bg,
                         activebackground=button_active_bg,
                         command=lambda: cal(entry))
    buttonequal.grid(row=5, column=2, columnspan=2,
                     ipadx=5, ipady=7,
                     padx=3, pady=5,
                     sticky=N+S+E+W)

    root.mainloop()
