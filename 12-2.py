from tkinter import *
import time
w = 665
h = 665
tk = Tk()
canvas = Canvas(tk, width=w, height=h)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)


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
