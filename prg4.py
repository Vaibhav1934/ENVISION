a = 3
b = 4

c = 0
i = 1

while i <= 20:
    if a*2 + b*2 == i*2:
        c = i
    i += 1

if c == 0:
    print("No Pythagorean triple found.")
else:
    print("The length of the hypotenuse is")
