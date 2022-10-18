# Input a day of the week from Sunday to Saturday. 
# Determine if that day is a work-day or a weekend.
# Repeat the process until the user enters “stop”

#days_list=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#if automating add day as parameter
def days_func():
    days_list=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    #comment this if automated
    day = input("Please enter a day of the week, such as \"Sunday\" or \"Monday\": ")

    if day in days_list:
        #print("Yay")
        index = days_list.index(day)
        if index == 0 or index == 6:
            print(day, "is on the weekend")
        else:
            print(day, "is a weekday")
    else:
        #print("Nay")
        print(day, "is an invalid entry")
'''
for d in days_list:
    days_func(d)

days_func("no")
days_func("bad")
'''

days_func()