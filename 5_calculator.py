# Calculator with two inputs

############################

print("Enter a number, operator (+, -, /, *) and another number")

input1 = input("First number: ")
math_function = input("Math input: ")
input2 = input("Second number: ")

if math_function == '+':
    result = int(input1) + int(input2)
elif math_function == '-':
    result = int(input1) - int(input2)
elif math_function == '/':
    result = int(input1) / int(input2)
elif math_function == '*':
    result = int(input1) * int(input2)
else:
    result = "Not a valid operator"

print (result)
