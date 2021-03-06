import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename


def Exit():
    answer = tkinter.messagebox.askokcancel("Are You Sure?", "If You Not Saved Your Data It May be lost")
    if(answer):
        print("Exit")
        quit()

def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Unnamed.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def Open():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def newFile():
    global file
    root.title("Unnamed - Notepad")
    file = None
    TextArea.delete(1.0, END)

def Grey():
    TextArea.config(bg='grey', fg='white')
    #print("Dark Mode")

def Light():
    TextArea.config(bg='White')
    #print("Light Mode")

def Lightsalmon():
    TextArea.config(bg='#FFA07A', fg='black')
    #print("Light Mode")
def Orange():
    TextArea.config(bg='#FFA500', fg='black')
    #print("Light Mode")
def Khaki():
    TextArea.config(bg='#F0E68C', fg="black")
    #print("Light Mode")
def Blue():
    TextArea.config(bg='#AFEEEE', fg='black')
def Georgia():
    TextArea.config(font=("Georgia", 16, "bold"))
def Informal_Roman():
    TextArea.config(font=("Informal Roman", 16))
def Latin():
    TextArea.config(font=("Latin", 16))

root = Tk()
root.geometry("400x400")

menu1 = Menu(root)
root.config(menu=menu1)
menu1.add_command(label="Open", command=Open)
menu1.add_command(label="Save", command=Save)
FontSubMenu = Menu(menu1)
menu1.add_cascade(label="format", menu=FontSubMenu)
FontSubMenu.add_command(label="Georgia", command=Georgia)
FontSubMenu.add_command(label="Informal Roman", command=Informal_Roman)
FontSubMenu.add_command(label="Latin", command=Latin)
menu1.add_command(label="New", command=newFile)
submenu = Menu(menu1)
menu1.add_cascade(label="Theme", menu=submenu)
submenu.add_command(label="Grey", command=Grey)
submenu.add_command(label="Light", command=Light)
submenu.add_command(label="Lightsalmon", command=Lightsalmon)
submenu.add_command(label="Orange", command=Orange)
submenu.add_command(label="Khaki", command=Khaki)
submenu.add_command(label="Blue", command=Blue)
menu1.add_command(label="Exit", command=Exit)

TextArea = Text(root, font="Arial 16")
file = None
TextArea.pack(expand=True, fill=BOTH)

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand = Scroll.set)


footer = Label(root, text="Text Editor", relief=SUNKEN, bd=1, anchor=W)
footer.pack(side=BOTTOM, fill=X)
root.mainloop()
