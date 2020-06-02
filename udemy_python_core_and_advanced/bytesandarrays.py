lst = [20, 30, 40, 234]
print(type(lst))
b = bytes(lst)
print(type(b))

# cannot index bytes type

b1 = bytearray(lst)
print(type(b1))
b1[2] = 33
print(b1)