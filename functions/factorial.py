def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result


print(factorial(3))  # 3 + 2 + 1

# maximum recursion depth is 997
for i in range(0, 90):
    print(factorial(i))

