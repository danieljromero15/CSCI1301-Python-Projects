# input_and_output_values.py
# Daniel Romero
# CSCI1301-HY8, Fall 2022
# Input a sequence of numbers and display them after adding 3 to each number

list = input("Please enter a sequence of numbers seperated by spaces: ")
print(list)
list = list.split()
list = [int(n) for n in list]
print(list)

modList = [n+3 for n in list]
print(modList)