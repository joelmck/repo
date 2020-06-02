s = {10, 20, 30, 10, "XYZ"}
print(s)
print(type(s))

# set does not allow duplicates, it will just ignore them
# set does not guarantee an order, so you cannot slice or index, it will throw error

s.update([88,99])
print(s)

s.remove(30)
print(s)

f = frozenset(s)  # frozen sets cannot be updated and attributes cannot be remvoed, it will throw errors


