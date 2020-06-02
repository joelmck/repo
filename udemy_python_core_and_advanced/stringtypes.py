s = "Awesome string"
print(s)

s1 = """You are
the creator 
of your destiny"""
print(s1)

print(s[0])

print(s*2)

print(len(s1))

# slicing string
print(s[0:5])  # prints the first 5 characters
print(s[1:])  # prints all characters from the after the first character
print(s[:3])  # prints the first characters before the fourth (0, 1, 2 = "Awe")
print(s[-3:-1])  # prints the 3rd last character to BEFORE the last character (second last)

# step value slicing
print(s[0:9:2])  # steps every two values
print(s[::-1])  # reverses the string

# strip spaces from string
print(s.strip())
print(s.lstrip())  # left side strip
print(s.rstrip())  # right side strip

# find string within string
print(s.find("Awe", 0, len(s)))

# counts number of "A"s in "Awesome string"
print(s.count("A"))

# replace string
print(s.replace("Awesome", "Super"))

# change casing
print(s.upper())
print(s.lower())
print(s.title())

# assignment
a = 10
b = 20.54
c = True
d = "I am the best"
answers = [a, b, c, d]
for i in answers:
    print("answer = {} and it's a {}".format(i, type(i)))


print(d.find("best"))

# assignment 2
"""define list of countries
add country at end
remove by index
add a country in the middle
do something similar using a set type
"""

countries = ["Australia", "New Zealand"]
countries.append("Papua New Guinea")
del(countries[1])
countries.insert(1, "Samoa")
print(countries)
s = set(countries)
s.remove("Samoa")
s.update(["Tonga"])
print(s)