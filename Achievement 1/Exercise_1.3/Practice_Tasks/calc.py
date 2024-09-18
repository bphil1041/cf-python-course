# User inputs
first_value = float(input("Enter the first value: "))
second_value = float(input("Enter the second value: "))
operator = input("Enter the operator (+ or -): ")

# Perform the calculation based on the operator
if operator == '+':
    result = first_value + second_value
    print(f"The result of {first_value} + {second_value} is: {result}")
elif operator == '-':
    result = first_value - second_value
    print(f"The result of {first_value} - {second_value} is: {result}")
else:
    print("Unknown operator")
