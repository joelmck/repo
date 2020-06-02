dict1 = {1:"Joel", 2:"Steph", 3:"Freya"}
print(dict1)

print(dict1.items())

k=dict1.keys()
for i in k:
    print(i)

v=dict1.values()
for i in v:
    print(i)

print(dict1[2])

del(dict1[2])
print(dict1)

