# Here's a function that takes value1 and value2,
# divides value1 by value2 and then prints the result
def divider(value1, value2):
    print(value1 / value2)


# Taking the user's inputs:
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Calling divider() normally
divider(a, b)

# Calling divider() by passing keyword arguments
divider(value1=a, value2=b)
