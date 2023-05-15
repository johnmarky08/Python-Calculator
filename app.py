# REMADE BY JOHN MARKY A. NATIVIDAD
"""PYTHON CALCULATOR"""
from tkinter import Tk, Label, Button, PhotoImage
from ast import literal_eval

root = Tk()

icon = PhotoImage("logo.ico")
root.iconbitmap(False, icon)

root.title("Python Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161B")

EQUATION = ""


def show(value):
    """SHOWS A VALUE"""
    global EQUATION  # pylint: disable=W0603
    EQUATION += value
    label_result.config(text=EQUATION)


def clear():
    """CLEARS ALL VALUES"""
    global EQUATION  # pylint: disable=W0603
    EQUATION = ""
    label_result.config(text=EQUATION)


def calculate():
    """CALCULATES ALL VALUES"""
    global EQUATION  # pylint: disable=W0603
    result = ""
    if EQUATION != "":
        try:
            result = literal_eval(EQUATION)
        except:  # pylint: disable=W0702
            result = "Syntax Error!"
            EQUATION = ""
    label_result.config(text=result)


def clearone():
    """CLEARS ONE VALUE FROM THE END"""
    global EQUATION  # pylint: disable=W0603
    if EQUATION != "":
        EQUATION = [*EQUATION].pop()
        EQUATION = "".join(EQUATION)
    label_result.config(text=EQUATION)


label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#3697F5", command=clear()).place(x=10, y=100)
Button(root, text="<", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#3697F5", command=clearone()).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("%")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("*")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("-")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("+")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("0")).place(x=10, y=500)

Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("/")).place(x=430, y=400)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2A2D36", command=lambda: show(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#FE9037", command=calculate()).place(x=430, y=500)

root.mainloop()
