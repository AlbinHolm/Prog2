#Additionsfunktion
def addition(*val):
    summa = 0
    for arg in val:
        summa = summa + arg
    return summa

def caller(func,val):
    return func(*val)


print(caller(addition, (7, 4, 7, 2)))

#Funktion för uppgift "Sojamjölk"
def food(s, vegan=False):
    if vegan:
        print("Sojamjölk")
    else:
        print("Mjölk")


food("Mjölk", False)
food("Mjölk", True)