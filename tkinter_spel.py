from tkinter import *
root = Tk()
canv = Canvas(root, height=300, width=400, bg="blue")
canv.pack()
img = PhotoImage(file = "media/crosshairs.png")
id = canv.create_image(200, 150, image=img)
# id = canv.create_oval(0, 100, 50, 150)
movespeed = 30

x_pos = 0
y_pos = 0

def updatePos():
    global x_pos
    global y_pos
    x_pos = (canv.coords(id)[0] - 3)
    y_pos = (canv.coords(id)[1] - 12)


def move_left(e):
    if canv.coords(id)[0] >= -10:
        canv.move(id, -(movespeed), 0)
def move_right(e):
    if canv.coords(id)[0] < 365:
        canv.move(id, movespeed, 0)
def move_up(e):
    if canv.coords(id)[1] >= 60:
        canv.move(id, 0, -(movespeed))
def move_down(e):
    if canv.coords(id)[1] < 320:
        canv.move(id, 0, movespeed)
def shoot(e):
    updatePos()
    print(x_pos, y_pos)
    shot = canv.create_oval(0, 10, 5, 15, fill="red")
    canv.move(shot, x_pos, y_pos)

canv.bind_all("<Left>", move_left)
canv.bind_all("<Right>", move_right)
canv.bind_all("<Up>", move_up)
canv.bind_all("<Down>", move_down)
canv.bind_all("<space>", shoot)

root.mainloop()
