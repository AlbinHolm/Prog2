from tkinter import *
import random

root = Tk()
canv = Canvas(root, height=400, width=400, bg="blue")

score = Label(canv)
score.place(x = 10, y = 10)
score["text"] = "Score: 0"
scoreint = 0

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


# Updates pos for crosshairs
def updatePos():
    global x_pos
    global y_pos
    x_pos = (canv.coords(id)[0] - 3)
    y_pos = (canv.coords(id)[1] - 12)


# Picks a new random pos for target
def updateRandPos():
    global randPosX
    global randPosY
    randPosX = random.randint(-50, 50)
    randPosY = random.randint(-50, 50)


# Moves target to updated pos
def updateTarget():
    updateRandPos()
    canv.move(target, randPosX, randPosY)

    # If target moves out of screen
    if canv.coords(target)[0] > 300:
        canv.move(target, -100, 0)

    if canv.coords(target)[0] < 10:
        canv.move(target, 100, 0)
    
    if canv.coords(target)[1] > 300:
        canv.move(target, 0, -100)
            
    if canv.coords(target)[1] < 10:
        canv.move(target, 0, 100)



updateRandPos()
target = canv.create_image(200, 200, image=img2)


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
    global score
    global scoreint

    updatePos()
    
    if (abs(x_pos - canv.coords(target)[0]) <= 15):
        xHit = True
    if (abs(y_pos - canv.coords(target)[1]) <= 15):
        yHit = True

    if (xHit == True & yHit == True):
        shot = canv.create_oval(0, 10, 5, 15, fill="red")
        canv.move(shot, x_pos, y_pos)

        scoreint += 1
        score["text"] = "Score: " + str(scoreint)
    
        updateTarget()

    else:
        scoreint -= 1
        score["text"] = "Score: " + str(scoreint)

    xHit = False
    yHit = False


def debug(e):
    pass



canv.bind_all("<Left>", move_left)
canv.bind_all("<Right>", move_right)
canv.bind_all("<Up>", move_up)
canv.bind_all("<Down>", move_down)
canv.bind_all("<space>", shoot)
canv.bind_all("<8>", debug) 

root.mainloop()