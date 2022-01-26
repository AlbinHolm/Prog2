from tkinter import *
import random

root = Tk()
canv = Canvas(root, height=400, width=400, bg="blue")
canv.pack()
img2 = PhotoImage(file = "media/duck.png")

img = PhotoImage(file = "media/crosshairs.png")
id = canv.create_image(200, 150, image=img)
movespeed = 10
score = 0

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
    # print("Debug: Updated pos")

# Picks a new random pos for target
def updateRandPos():
    global randPosX
    global randPosY
    randPosX = random.randint(17, 377)
    randPosY = random.randint(8, 210)
    # print("Debug: Updated randpos")

# Moves target to updated pos
def updateTarget():
    updateRandPos()
    canv.move(target, randPosX + 5, randPosY + 15)
    # print("Debug: Updated target")


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
    global score

    updatePos()
    
    if (abs(x_pos - randPosX) <= 15):
        xHit = True
    if (abs(y_pos - randPosY) <= 15):
        yHit = True

    if (xHit == True & yHit == True):
        shot = canv.create_oval(0, 10, 5, 15, fill="red")
        canv.move(shot, x_pos, y_pos)
        
        print("hit")
        updateTarget()
        score += 1 
        
        
    else:
        print("miss")

    xHit = False
    yHit = False

def debug(e):
    global x_pos
    global y_pos
    global randPosX
    global randPosY

    updatePos()
    print(x_pos, y_pos)
    print(randPosX, randPosY)



canv.bind_all("<Left>", move_left)
canv.bind_all("<Right>", move_right)
canv.bind_all("<Up>", move_up)
canv.bind_all("<Down>", move_down)
canv.bind_all("<space>", shoot)
canv.bind_all("<8>", debug) 

root.mainloop()






# Fixa anka spawnar utanför canvas
# Update anka och ta bort