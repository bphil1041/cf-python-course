# The function gets defined here, arguments
# value1 and value2 are set up to accept values.
def adder(value1, value2):
    result = value1 + value2
    print("The added result is " + str(result))


# The main code starts here. We'll take the user's inputs now.
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Calling adder() which prints the result
adder(a, b)
