#number_list[10,15,20]
number_list = []
for i in range(10, 150 + 1, 5):
    number_list.append(i)

print(f'{number_list=}')

increase_num = int(input("Enter a number to increase by: "))

#my brain hurts today
number_list_new = []
for num in number_list:
    num += increase_num
    number_list_new.append(num)

print(f'{number_list_new=}')