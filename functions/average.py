def average(a=10, b=20):  # assigned default parameters
    print(a)
    print(b)
    return (a+b)/2


result = average(b=30)  # keyword values can be used to change the order of parameters
print(result)

