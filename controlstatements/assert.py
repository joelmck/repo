"""
x = int(input("Enter a number greater than 10"))
assert x > 10, "Wrong number entered"
print("You entered", x)
"""

"""
Assignment:
enter a number
display  numbers up to that number
skip multiples of 10
stop if number is >100
while, continue, break
"""

"""
x = int(input("Provide number: "))
y = 0
while y <= x:
    y += 1
    if y % 10 == 0:
        continue
    elif y > 101:
        break
    else:
        print(y)
"""

n = int(input("Provide number: "))
primeFlag = True
i = 1
while i < n-1:
    i += 1
    if n % i == 0:
        primeFlag = False
    else:
        continue
if primeFlag:
    print("Prime")
else:
    print("Not prime")
