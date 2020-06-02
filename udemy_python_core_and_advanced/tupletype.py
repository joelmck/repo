tpl = (40)  # if a tpl has a single element, it will read this as an integer in brackets
print(type(tpl))
tpl = (40,)  # tuple
tpl = (40, 50, 40, "XYZ")
print(type(tpl))
print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index("XYZ"))

lst = [67, 34, "XYZ"]
print(type(lst))  # list
tpl1 = tuple(lst)
print(type(tpl1))
print(tpl1)

# once a tuple is created it cannot be modified, unlike a list
