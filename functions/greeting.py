def display(name):
    def message():
        return "Hello "
    result = message() + name
    return result


print(display("Joel"))

# you cannot call message outside of the display function
