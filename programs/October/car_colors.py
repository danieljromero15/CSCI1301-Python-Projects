# enter color of each car and store the color on a list called car_colors
# if the observer enters a color which is already on the list mention it's a duplicate and ignore it
# when the user enters 'stop' display list of observed colors

print("Please enter the color of each car: ")

color = []
userIn = ''
while userIn != 'stop':
    userIn = input()
    if userIn in color:
        print("duplicate color\n")
    else:
        color.append(userIn)

# color.pop removes the 'stop' from the list
color.pop()
print(color)