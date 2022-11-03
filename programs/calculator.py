# calculator

operation = 0

#prints menu
def menu():
    # sets it so that operation can be changed globally
    global operation
    
    #while operation != 5: #moved to main program because this was kinda dumb
    print("1) Add\n" +
    "2) Subtract\n" +
    "3) Multiply\n" +
    "4) Divide\n" +
    "5) Quit")

    userChoice = input("Please select a choice: ")

    print()
    print(f"Your operation was: {userChoice}")

    try:
        userChoiceInt = int(userChoice)
    except:
        userChoiceInt = 0

    if(1 <= userChoiceInt <= 5):
        operation = userChoiceInt
    else:
        print("Invalid choice. Please try again.")
        print()

#performs math operations based on selection
def mathematics(x,y):
    if operation == 1:
        return x + y
    elif operation == 2:
        return x - y
    elif operation == 3:
        return x * y
    elif operation == 4:
        return x / y

while operation != 5:
    menu()
    #print(operation)
    if operation != 5:
        #number input
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))

        print(f'Result: {mathematics(num1, num2)}')
        print()