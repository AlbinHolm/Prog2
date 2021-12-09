from tkinter import *

letters = "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"
ord = ""

# Main
root = Tk()

lbl1 = Label(root)
lbl1["text"] = "Skriv något du vill översätta till rövarspråk:"
lbl1.pack()

entryText = Entry(root)
entryText.pack()

button = Button(root, text ="Översätt!")

def click_handler(self):
    global ord, letters
    for x in entryText.get():
        if x in letters:
            ord = ord+x+"o"+x
        else:
            ord = ord+x 
    lbl2["text"] = "Översättning: " + ord

button.bind("<Button-1>", click_handler)
button.pack()

lbl2 = Label(root)
lbl2.pack()

root.mainloop()
