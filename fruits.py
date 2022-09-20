# fruits.py()

# initial fruits
my_fruits = ['Apple','Banana','Pear']
print("My favorite fruits are " + str(my_fruits))

# adds fruit to list without storing to its own variable
my_fruits.append(input("\nEnter your fruit: ")) # usually oranges
print("My favorite fruits are " + str(my_fruits))

# inserts fruit to list at index 0 without storing to its own variable
my_fruits.insert(0, input("\nEnter a fruit to insert to beginning: "))
print("My favorite fruits are " + str(my_fruits))

# removes fruit from list without storing to its own variable
my_fruits.remove(input("\nEnter a fruit to remove: "))
print("My favorite fruits are " + str(my_fruits))

# removes fruit from list based on index number without storing to its own variable
my_fruits.pop(int(input("\nEnter a fruit index (number) to remove: ")))
print("My favorite fruits are " + str(my_fruits))

# Reverses order of fruits
my_fruits.reverse()
print("\nMy favorite fruits are " + str(my_fruits))

#prints length of my_fruits
print("There are", len(my_fruits), "fruits on my list")