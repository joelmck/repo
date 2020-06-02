lst = [10, 20, "Bharath", -10, 30.5]
print(lst)
print(lst[3])
print(lst[3:5])  # slice
print(lst*4)  # repetition
print(len(lst))  # length of list, number of elements in list

lst.append(40)  # append to list
lst.remove("Bharath")  # remove item from list
del(lst[0])
print(lst)

print(max(lst))  # largest element
print(min(lst))  # smallest element
lst.sort()  # rearranges list
print(lst)
lst.sort(reverse=True)  # rearranges in reverse
print(lst)

lst.insert(3, 99)  # insert new element in position 3
print(lst)

lst.clear()  # remove all list elements
print(lst)
