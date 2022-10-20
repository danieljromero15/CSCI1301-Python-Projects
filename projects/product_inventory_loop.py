product_list = []
price_list = []

userIn = 0
while userIn != 'stop':
    userIn = input('Name of product (\'stop\' to end): ')
    if userIn != 'stop':
        product_list.append(userIn)
        price_list.append(float(input('Price of the product: ')))

def productPrint(case):
    print()
    # would be a match case but thats only python 3.10 and im worried about zybooks' ability to handle it
    print("The product inventory", end='')
    if case == 'increase':
        print(" after price increase", end='')
    if case == 'remove':
        print(f" after {userIn} is removed", end='')
    
    print(':')
    print(product_list)
    print(price_list)
    print()

def listRemove(productToRemove):
    removeIndex = product_list.index(productToRemove)
    product_list.pop(removeIndex)
    price_list.pop(removeIndex)

productPrint(0)

percentIncrease = int(input('By what percentage do you want to increase the product prices? (0-100): '))

priceAvg = sum(price_list) / len(price_list)

print()
print(f"The prices of the products, which cost {priceAvg} or less will be increased by {percentIncrease} percent.")

for n in price_list:
    if n <= priceAvg:
        price_list[price_list.index(n)] = n * (1 + (percentIncrease / 100))

productPrint("increase")

priceMax = max(price_list)
productMax = product_list[price_list.index(priceMax)]
userIn = productMax
print(f"The most expensive product, {productMax} which costs {priceMax} Dollars will be removed.")
listRemove(productMax)

productPrint("remove")

while userIn != 'stop':
    userIn = input('Name of the product to remove from inventory (\'stop\' to end): ')
    if userIn != 'stop':
        listRemove(userIn)
        productPrint('remove')

print('Products and respective prices side by side:')
print('Product\t\tPrice')
print('-------\t\t-----')
for product in product_list:
        print(f'{product}\t\t{price_list[product_list.index(product)]}')


print('\n\nHave a nice day!')