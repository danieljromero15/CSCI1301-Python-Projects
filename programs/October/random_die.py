import random

max = int(input("Enter a max amount of times to roll the die: "))

for i in range(0,max):
    print(random.randint(1,6))