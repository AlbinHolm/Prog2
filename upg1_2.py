list = []
n = 0
x = 0
s = 0

while n < 1000:
    n += 1
    list.append(int(n/7))

s = (list[-1])

print("------------------------------------------")
print("Dessa tal upp till 1000 är delbara med 7:")
print("------------------------------------------")
while x < s:
    x +=1
    print(x*7)

    
