# calculator

#prints menu
def menu():
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
        return userChoiceInt
    else:
        print("Invalid choice. Please try again.")
        print()
        return 0
    

#performs math operations based on selection
def mathematics(x,y, operation):
    if operation == 1:
        return x + y
    elif operation == 2:
        return x - y
    elif operation == 3:
        return x * y
    elif operation == 4:
        return x / y

userSelect = 0

#var names are a bit confusing rn, sorry!
while userSelect != 5:
    userSelect = menu()
    #print(operation)
    if userSelect != 5:
        #number input
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))

        print(f'Result: {mathematics(num1, num2, userSelect)}')
        print()