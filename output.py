import tkinter

def generate(data):
    # init tk
    root = tkinter.Tk()
    root.title("Blocks Required")

    # set canvas dimensions
    canvas_width = 150
    canvas_height = (len(data) + 1) * 20

    # create canvas
    myCanvas = tkinter.Canvas(root, bg="white", height= canvas_height, width=canvas_width)

    myCanvas.create_text(10, 5, text="Block",anchor="nw")
    myCanvas.create_text(canvas_width - 5, 5, text="Quantity",anchor="ne")
    myCanvas.create_line(0, 23, canvas_width, 23)
    
    y = 27
    for block in data:
        myCanvas.create_text(10, y, text=block, anchor="nw")
        myCanvas.create_text(120, y, text=data[block], anchor="nw")
        y += 20

    # add to window and show
    root.wm_attributes('-toolwindow', 'True')
    myCanvas.pack()
    root.mainloop()
