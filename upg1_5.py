import math
from sympy import limit, oo

#Leibniz approximation
x=0
namnare=3
tal=1

while x < 10000:
    tal = tal - (1/namnare)
    namnare = namnare + 2
    tal = tal + (1/namnare)
    namnare = namnare + 2
    x += 1

#print(tal * 4)


#Eulers konstant 1
def euler1(tal):
    x = 0
    svar = ""
    while x < 1000:
        svar = limit((1 + (1/tal)**tal), oo)
        tal += 1
        x += 1
    print(svar)
euler1(1)


tal = 1
pp = limit(x, oo, 1+(1/x)**x)
print(pp)



