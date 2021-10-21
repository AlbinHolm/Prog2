class Djur:
    def __init__(self, name):
        self.name = name

class Fisk(Djur):
    def __init__(self, name, swimming, can_swim):
        super().__init__(name)
        self.swimming = swimming
        self.can_swim = can_swim

class Haj(Djur):
    def __init__(self, name, eat_fisk):
        super().__init__(name)
        self.eat_fisk = eat_fisk
        


fisk1 = Fisk("Abborre", True, True)
fisk2 = Fisk("Lax", False, True)
fisk3 = Fisk("Gädda", True, True)
haj = Haj("Vithaj", "just ate ")

print("---------------------------------------------------------------")
print(f'The fish "{fisk1.name}" can swim: {fisk1.can_swim}, Is currently swimming: {fisk1.swimming}')
print(f'The fish "{fisk2.name}" can swim: {fisk2.can_swim}, Is currently swimming: {fisk2.swimming}')
print(f'The fish "{fisk3.name}" can swim: {fisk3.can_swim}, Is currently swimming: {fisk3.swimming}')
print("---------------------------------------------------------------")
print(f'{haj.name} {haj.eat_fisk} {fisk1.name}!')
print("---------------------------------------------------------------")
