from tkinter import *
import random

root = Tk()
canv = Canvas(root, height=400, width=400, bg="blue")
canv.pack()
img2 = PhotoImage(file = "media/duck.png")

img = PhotoImage(file = "media/crosshairs.png")
id = canv.create_image(200, 150, image=img)
movespeed = 10

x_pos = 0
y_pos = 0

randPosX = 0
randPosY = 0

xHit = False
yHit = False



def updatePos():
    global x_pos
    global y_pos
    x_pos = (canv.coords(id)[0] - 3)
    y_pos = (canv.coords(id)[1] - 12)

def updateRandPos():
    global randPosX
    global randPosY
    randPosX = random.randint(-43, 377)
    randPosY = random.randint(18, 318)

def updateTarget():
    canv.delete(target)
    updateRandPos()
    return canv.create_image(randPosX + 5, randPosY + 15, image=img2)


updateRandPos()
target = canv.create_image(randPosX + 5, randPosY + 15, image=img2)


def move_left(e):
    if canv.coords(id)[0] >= 0:
        canv.move(id, -(movespeed), 0)

def move_right(e):
    if canv.coords(id)[0] < 400:
        canv.move(id, movespeed, 0)

def move_up(e):
    if canv.coords(id)[1] >= 0:
        canv.move(id, 0, -(movespeed))
    
def move_down(e):
    if canv.coords(id)[1] < 400:
        canv.move(id, 0, movespeed)

def shoot(e):
    global xHit
    global yHit

    updatePos()
    
    if (abs(x_pos - randPosX) <= 15):
        xHit = True
    if (abs(y_pos - randPosY) <= 15):
        yHit = True

    if (xHit == True & yHit == True):
        shot = canv.create_oval(0, 10, 5, 15, fill="red")
        canv.move(shot, x_pos, y_pos)
        print("hit")
        target = updateTarget()
        
        
    else:
        print("miss")

    xHit = False
    yHit = False

def debug(e):
    updateRandPos()
    print("debug")







canv.bind_all("<Left>", move_left)
canv.bind_all("<Right>", move_right)
canv.bind_all("<Up>", move_up)
canv.bind_all("<Down>", move_down)
canv.bind_all("<space>", shoot)
canv.bind_all("<k>", debug)

root.mainloop()






# Fixa anka spawnar utanför canvas
# Update anka och ta bort