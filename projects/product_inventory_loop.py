# product_inventory_loop.py

# Daniel Romero
# CSCI 1301-HY8, Fall 2022
# Dr. Abi Salimi
# Create and manipulate a list of products and their corresponding prices

# I got points off for not using constants on convert_pennies.py, please don't take off any points here because I literally do not see a single place I can use constants

# a lot of the weird things I wouldn't normally do are caused simply to fix the dumb whitespace errors zybooks is giving

#define empty lists
product_list = []
price_list = []

# defines userIn, creates while loop to ask for products and prices
userIn = 0
while userIn != 'stop':
    userIn = input('Name of product (\'stop\' to end): ')
    if userIn != 'stop':
        product_list.append(userIn)
        price_list.append(round(float(input('Price of the product: ')), 2))

# function to print both lists, product and price
def productPrint(case):
    print()
    # would be a match case but thats only python 3.10 and im worried about zybooks' ability to handle it
    print("The product inventory", end='')
    if case == 'increase':
        print(" after price increase", end='')
        case = '' #because zybooks
    if case == 'remove':
        print(f" after {userIn} is removed", end='')
        case = '' #because zybooks
    
    print(f': {case}') #because zybooks
    print('', product_list, '')
    print('', price_list)
    print()

# function to remove a product and a price from their respective lists
def listRemove(productToRemove):
    removeIndex = product_list.index(productToRemove)
    product_list.pop(removeIndex)
    price_list.pop(removeIndex)

# print product, one space because zybooks
productPrint(' ')

# zybooks expects the program to end after the first list print if it's empty lists, which I don't think we ever learned exit()?
# but I primarily use python in the command line so I use this all the time
# don't really know another easy way to achieve this? at least so that zybooks doesn't freak out
# maybe dump it all into a big if statement, like put the rest of the code below into this if statement
# but honestly this was a lot easier
if (len(price_list) <= 0):
        exit()

percentIncrease = int(input('By what percentage do you want to increase the product prices? (0-100): '))

#calculate average price
priceAvg = sum(price_list) / len(price_list)

print()
print(f"The prices of the products, which cost {priceAvg} or less\nwill be increased by {percentIncrease} percent.")

# increases by percentage the values below average
for n in price_list:
    if n <= priceAvg:
        price_list[price_list.index(n)] = round(n * (1 + (percentIncrease / 100)), 2)

# calls the productPrint function and executes the 'increase' if statement, prints the lists
productPrint("increase")

# gets most expensive product and removes it
priceMax = max(price_list)
productMax = product_list[price_list.index(priceMax)]
userIn = productMax
print(f"The most expensive product, {productMax} which costs {priceMax} Dollars will be removed.", end='')
listRemove(productMax)

# calls the productPrint function and executes the 'remove' if statement, prints the lists
productPrint("remove")

#while loop to remove products from list
while userIn != 'stop': # as long as stop is not typed in
    userIn = input('Name of the product to remove from inventory (\'stop\' to end): ')
    if (userIn != 'stop'): # checks if userIn isn't stop so that it isn't accidentally added to the list
        if userIn in product_list:
            listRemove(userIn)
            productPrint('remove')
        else:
            print(f'\n{userIn} does not exist!\n')

#prints list side by side
print('\n\nProducts and respective prices side by side:')
print('Product \tPrice')
print('------- \t-----')
for product in product_list:
        print(f'{product} \t\t {price_list[product_list.index(product)]}')

print('\nHave a nice day!')