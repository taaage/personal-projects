# Calculator with two inputs
# Written by: Tigge y un poco Oliver
############################

while True:
    print("Enter a number, Enter an operator (+, -, /, *) and Enter another number")
    
    input1 = input("First number: ")
    math_function = input("Math input: ")
    input2 = input("Second number: ")

    if math_function == '+':
        result = float(input1) + float(input2)
        print(input1, "+", input2, "=", result)
    elif math_function == '-':
        result = float(input1) - float(input2)
        print(input1, "-", input2, "=", result)
    elif math_function == '/':
        result = float(input1) / float(input2)
        print(input1, "/", input2, "=", result)
    elif math_function == '*':
        result = float(input1) * float(input2)
        print(input1, "*", input2, "=", result)
    else:
        result = "Not a valid operator"

    # check if user wants another calculation
    # break the while loop if answer is no

    next_calculation = input("Let's do another calculation? (yes/no): ")

    if next_calculation == "yes":
        print("New calculation")

    elif next_calculation == "no":
          break
    else:
        print("Invalid choice")
