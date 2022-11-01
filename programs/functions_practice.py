# who cares im not submitting this
#tbh i think the normal math functions are an easier way to explain this
#start them out easy with numbers yk
#also the example he has on the board is basically just an overcomplicated print statement lol

def average(list):
    #print(list)
    avg = sum(list) / len(list)
    return avg

'''
def average(x,y,z):
    avg = (x + y + z) / 3
    return avg
'''

a = []
userIn = 0
while userIn != 'stop':
    userIn = int(userIn)
    a.append(userIn)
    if userIn != 'stop':
        userIn = input("Add number to list to find avg (type stop to stop): ")
        #print(userIn)
a.pop(0) #here because 0 would always be 0

print(average(a))