#Designing a simpl Calculator
def add(x, y):  #adds two numbers
    return x + y
def subtract(x, y):  #subtracts two numbers
    return x - y
def multiply(x, y):  #multiplies two numbers
    return x * y
def divide(x, y):  #divides two numbers
    return x / y

def modulo(x, y):  #returns remainder
    return x % y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulo")

while True:
    # take input from the user
    choice = input("Enter Operator( '+' , '-' , '*' , '/' , '%' ): ")

    # check if choice is one of the four options
    if choice in ('+', '-', '*', '/', '%'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '%':
            print(num1, "%", num2, "=", modulo(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")