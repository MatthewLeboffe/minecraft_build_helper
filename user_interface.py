from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox

import block_finder

window = Tk()

window.columnconfigure([0, 1, 2, 3], pad=20)
window.rowconfigure([0, 1, 2, 3, 4, 5], pad=5)

ttk.Label(text="Upload World File:").grid(column= 0,row= 0)
world = ttk.Entry(width=25)
world.grid(column= 1, row= 0, columnspan= 2)


def open_file():
   filepath = filedialog.askdirectory(title="Open a Text File")
   world.insert(0, filepath)
   

worldSelect = Button(text="Select File", command=open_file).grid(column= 3, row= 0)


ttk.Label(text="Enter Coordinates").grid(column=2, row=1)

ttk.Label(text="x").grid(column=1, row=2)
ttk.Label(text="y").grid(column=2, row=2)
ttk.Label(text="z").grid(column=3, row=2)


ttk.Label(text="(x1, y1, z1)").grid(column=0, row=3)
ttk.Label(text="(x2, y2, z2)").grid(column=0, row=4)

x1 = ttk.Entry(width=5, justify="center")
x1.grid(column=1, row=3)
x2 = ttk.Entry(width=5, justify="center")
x2.grid(column=1, row=4)

y1 = ttk.Entry(width=5, justify="center")
y1.grid(column=2, row=3)
y2 = ttk.Entry(width=5, justify="center")
y2.grid(column=2, row=4)

z1 = ttk.Entry(width=5, justify="center")
z1.grid(column=3, row=3)
z2 = ttk.Entry(width=5, justify="center")
z2.grid(column=3, row=4)

def populate():
    x1.insert(0, -192)
    y1.insert(0, 4)
    z1.insert(0, 63)
    x2.insert(0, -194)
    y2.insert(0, 4)
    z2.insert(0, 65)
    world.insert(0, "C:/Users/Matth/OneDrive/Desktop/LegoProject/test")

populate()
def myClick():
    usercoords = [x1.get(), y1.get(), z1.get(), x2.get(), y2.get(), z2.get()]
    coords = ["x1", "y1", "z1", "x2", "y2", "z2"]
    for i in range(len(usercoords)):
        try:
            usercoords[i] = int(usercoords[i])
        except:
            tkinter.messagebox.showinfo("Error", coords[i] + " is not a whole number")
            break
    
    x = block_finder.createList(world.get(), usercoords[:3], usercoords[3:])
    print(x)
    for block in x:
        print(block, x[block])

sub = ttk.Button(text="Create List", command=myClick).grid(column=2, row=5)


window.mainloop()