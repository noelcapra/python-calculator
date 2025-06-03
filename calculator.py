def add(x, y):
   print(x + y)

def subtract(x, y):
    print(x - y)

def divide(x, y):
    print(x / y)

def multiply(x, y):
    print(x * y)

def want_continue():
    while True:
        userinput = input("Do you wish to continue? (yes/no)").lower()
        if userinput == "yes" or userinput == "y":
            return True
        elif userinput == "no" or userinput == "n":
            return False
        else:
            print("Please answer with yes or no")

def calculator():
    numbers = ["1", "2", "3", "4", "5"]
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. End")
        answer = input("Please select what you want to do")
        num1 = int(input("Enter your first number"))
        num2 = int(input("Enter your second number"))
        if answer in numbers:
            if answer == "1":
                add(num1, num2)
            elif answer == "2":
                subtract(num1, num2)
            elif answer == "3":
                divide(num1, num2)
            elif answer == "4":
                multiply(num1, num2)
            elif answer == "5":
                break
            else:
                print("Enter a valid number")

            if not want_continue():
                print("Goodbye!")
                break




calculator()