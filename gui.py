from tkinter import *

gui = Tk()
height = "1200"
width = "1500"
gui.geometry(width + "x" + height)

canvas = Canvas(gui, height = 1200, width = 1500)
title = Label(canvas, text = "Connect 4 Online game")
player1Info = Label(canvas, text = "Player 1")
player2Info = Label(canvas, text = "Player 2")
title.config(font = ("Courier", 40))
player2Info.config(font = ("Courier", 40))
player1Info.config(font = ("Courier", 40))
title.place(relx = 0.3)
player2Info.place(relx = 0.8)
player1Info.place(relx = 0.1)

def create_grid(event=None):
    w = 1100
    h = 1100
    marginX = 350
    marginY = 450
    canvas.delete('grid_line')  
    for i in range(100, w, 100):
        canvas.create_line([(marginX, i), (h, i)], tag='grid_line') 
    for i in range(marginY, h,  100):
        canvas.create_line([(i, 100), (i, h)], tag='grid_line') 

canvas.pack(fill=BOTH, expand=True)
canvas.bind('<Configure>', create_grid)
gui.mainloop()

