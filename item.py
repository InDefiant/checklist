import random
random.randint(0, 11)

r = random.randint(0, 11)+random.randint(0, 11)
if r > 21:
    r = 21
print(r)
n = "hit"
while n == "hit":
    print("would you like to be hit or stay")
    n = input()
    if n == "hit":
        r += random.randint(0, 11)
    if r > 21:
        print("you lose")
        n = "fail"
    print(r)


r2 = random.randint(0, 11)+random.randint(0, 11)
if r2 < 10:
    r2 += random.randint(0, 11)
if r2 > 21:
    r2 = 21
if n != "fail":
    if r > r2:
        print("you win")
    else:
        print("you lose")
    print("your opponent had")
    print(r2)