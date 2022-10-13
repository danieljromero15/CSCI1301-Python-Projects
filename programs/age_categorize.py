# 10/13/2022

age = int(input("Enter an age: "))

if 0 < age <= 12:
    print(age,"is Youth")
elif age < 20:
    print(age,"is Teen")
elif age >= 25:
    print(age,"is Adult")
else:
    print(age,"is invalid")