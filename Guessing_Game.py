import random
typ = input("Type a number: ")
if typ.isdigit():
    typ = int(typ)
    if typ <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number next time")
    quit()
r = random.randint(1, typ)
x = 0
print(r)
while True:
    num = input("Guess a number! ")
    x += 1
    if num.isdigit():
        num = int(num)
    else:
        print("Please type a number next time")
        continue
    if typ == num:
        print("\n \nCongratulations!")
        break
    else:
        print("Bad Luck!")
print("You got in", x, "guesses!")
