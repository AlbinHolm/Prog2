input = input("ARRRRG!!! Vad vill du säga på rövarspråket? \n -> ")
letters = "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"
ord = ""

for x in input:
    if x in letters:
        ord = ord+x+"o"+x
    else:
        ord = ord+x

print(ord)
