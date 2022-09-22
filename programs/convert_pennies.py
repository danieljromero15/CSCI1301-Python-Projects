# convert_pennies.py

# Daniel Romero
# CSCI 1301-HY8, Fall 2022

#input pennies
penniesLeft = int(input('Enter the amount of pennies to convert: '))
print()

print(penniesLeft , "pennies is equal to\n")

# split money into dollars, quarters, dimes, nickels, and pennies
dollars = penniesLeft // 100
penniesLeft = penniesLeft % 100

quarters = penniesLeft // 25
penniesLeft = penniesLeft % 25

dimes = penniesLeft // 10
penniesLeft = penniesLeft % 10

nickels = penniesLeft // 5
penniesLeft = penniesLeft % 5

#redundant as I can just use penniesLeft
#pennies = penniesLeft // 1

# print total
print(dollars , "one dollar bills")
print(quarters , "quarters")
print(dimes , "dimes")
print(nickels , "nickels")
print(penniesLeft , "pennies")

#print( (dollars * 100) + (quarters * 25) + (dimes * 10) + (nickels * 5) + (penniesLeft) )

print("\nHave a nice day!")