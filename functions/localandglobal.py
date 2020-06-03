x = 123


def display():
    x = 456
    print(x)
    print(globals()['x'])


print(x)  # prints the global x
z = display
z()
z()
z()
