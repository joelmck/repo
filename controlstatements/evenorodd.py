"""
x = int(input("Enter an integer:"))
if x == 0:
    print(x, "is zero")
elif x % 3 == 0:
    print(x, " is even")
else:
    print(x, " is odd")
"""

""" assignment
<35 in maths, physics, chemistry is a
if fail:
then average and if <=59 C and <=69 B
"""

maths = int(input("Enter grades for maths"))
physics = int(input("Enter grades for physics"))
chemistry = int(input("Enter grades for chemistry"))

grades = [maths, physics, chemistry]
grade_score = sum([maths, physics, chemistry])/3

if min(grades) < 35:
    print("Failed")
else:
    if grade_score <= 59:
        print("C")
    elif grade_score <= 69:
        print("B")
    else:
        print("A")