import math


binaryNum = int(input("Type in a binary number (no spaces): "))

# adds each number to a list
binaryList = []
for x in str(binaryNum):
    binaryList.append(int(x))

print(binaryList)

# stores length of list
binaryListLength = len(binaryList)

#print(binaryListLength)

# takes each value and adds them to decimalNum
decimalNum = 0
for i in range(0,binaryListLength):
    decimalNum += int(binaryList[i] * math.pow(2, binaryListLength - i - 1))

print(decimalNum)