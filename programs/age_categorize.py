# 10/13/2022

#age = int(input("Enter an age: "))
age = 0

def agePrint():
    if 0 < age <= 12:
        print(age,"is Youth")
    elif 13 <= age < 20:
        print(age,"is Teen")
    elif age >= 25:
        print(age,"is Adult")
    else:
        print(age,"is invalid")

while age < 30:
    agePrint()
    age += 1