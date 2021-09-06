import sys
list = []


class Elev(object):
    def __init__(self, name, age, passed):
        self.name = name
        self.age = age
        self.passed = passed
    # def __str__(self):
    #     return 

    def getName(self):
        print(self.name)
    def setName(self, newName):
        self.name = newName
   
    def getAge(self):
        print(self.age)
    def setAge(self, newAge):
        self.age = newAge
   
    def passedStatus(self):
        print(self.passed)
    def setPass(self, newPass):
        self.passed = newPass




elev1 = Elev('Erik', 17, False)
elev2 = Elev('Lisa', 17, False)
elev3 = Elev('Per', 18, True)
elev4 = Elev('Olle', 17, False)
elev5 = Elev('Julia', 18, True)
elev6 = Elev('Maja', 18, True)

list = [elev1, elev2, elev3, elev4, elev5, elev6]


x = 0
while x != '6':
    print("""
    1. Titta på alla elever \t 2. Visa detaljer för elev
    3. Ändra ålder \t\t\t 4. Ändra status
    5. ------------ \t\t\t 6. Avsluta
    """)
    x = input("Vad vill du göra? ")

# ALTERNATIV 1
    if x == '1':
        print("-----------------------")
        for i in range(len(list)):
            print(f"{i+1}.{list[i].name}")
        print("-----------------------")

# ALTERNATIV 2
    if x == '2':
        status = ""
        print("-----------------------")
        det = int(input(f"Vilken elev vill du se detaljer på? (1-{len(list)}): "))
        if(list[det-1].passed):
            status = "Glad"
        else:
            status = "Ledsen"
        print()
        print(f"{list[det-1].name} - {list[det-1].age} - {status}")
        print("-----------------------")

# ALTERNATIV 3
    if x == '3':
        print("-----------------------")
        y = int(input(f"Vilken elev vill du ändra ålder på? (1-{len(list)}): "))
        age = input(f'Vilken ålder ska "{list[y-1].name}" byta till?  ')
        list[y-1].setAge(age)
        print(f'"{list[y-1].name}" Har uppdaterats.')
        print("-----------------------")


 # ALTERNATIV 4
    if x == '4':
        print("-----------------------")
        z = int(input(f"Vilken elev vill du ändra godkänd status på? (1-{len(list)}): "))
        if(list[z-1].passed):
            list[z-1].setPass(False)
        else:
            list[z-1].setPass(True)
        
        print(f'"{list[z-1].name}" Har uppdaterats.')
        print("-----------------------")

# ALTERNATIV 5
    if x == '5':
        print("-----------------------")
        print("Alternativet är ej implementerat...")
        print("-----------------------")




 # FÖR ALTERNATIV 8
    if x == '6':
        sys.exit(1)