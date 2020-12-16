from tkinter import *
import time
w = 750
h = 950
tk = Tk()
canvas = Canvas(tk, width=w, height=h)
canvas.pack()
my_image = PhotoImage(file='/Users/rohith.nallapothula/Desktop/python.tkinter/Python-Proggraming/Rohith.gif')
canvas.create_image(0,0, anchor=NW, image=my_image)

for x in range(0, 60):
    canvas.move(1,10,0)
    tk.update()
    time.sleep(0.05)
for y in range(0, 60):
    canvas.move(1, 0, 10)
    tk.update()
    time.sleep(0.05)
for z in range(0, 60):
    canvas.move(1, -10, 0)
    tk.update()
    time.sleep(0.05)
for a in range(0, 60):
    canvas.move(1, 0, -10)
    tk.update()
    time.sleep(0.05)
