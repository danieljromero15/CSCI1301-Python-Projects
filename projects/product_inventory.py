# product_inventory.py

# Daniel Romero
# CSCI 1301-HY8, Fall 2022
# Dr. Abi Salimi

product_list = []
price_list = []

#function to change 1 to 1st, 2 to 2nd, 3 to 3rd, and so on
#only properly works for 1-5, which is all that is needed for this program
def numSuffix(num):
    #num = number // 10**n % 10 #taken from stackoverflow
    #print(num) #commented because it was for debug for above line
    if(num == 1):
        return str(num) + "st"
    elif(num == 2):
        return str(num) + "nd"
    elif(num == 3):
        return str(num) + "rd"
    else:
        return str(num) + "th"

for x in range(0,5):

    #wrote these lists so I didn't have to resort to a massive if else
    productInputEnding = ["",
    " to add to the end", 
    " to add after the 1st product",
    " to insert in position 3 of inventory",
    " to add to the end of the inventory"]
    productInputEndingInventory = [" to it",
    " to the end",
    " after the 1st product",
    " to position 3",
    " to the end of inventory"]

    #asks for name and price of product
    tempProductInfo = input("Name of product " + str(x+1) + productInputEnding[x] + ": ")
    tempProductPrice = float(input("Price of the product: "))
    #print(tempProductInfo)
    #print(tempProductPrice)

    # I would use a switch statement but I'm worried about zybooks's ability to handle it
    if(x < 2 or x > 3):
        # Add to the end of the list
        product_list.append(tempProductInfo)
        price_list.append(tempProductPrice)
    elif(x >= 2 or x <= 3):
        # After the 1st product, so index 1
        # number 4 follows the same rule
        product_list.insert(x-1, tempProductInfo)
        price_list.insert(x-1, tempProductPrice)
    else:
        print("Error")
        exit()
    
    #might need to add another if else for this
    print("\nInventory after the " + numSuffix(x+1) + " product is added" + productInputEndingInventory[x] +":")
    print(product_list, price_list)
    print()

#asks for the percent increase and makes sure it's within the correct bounds
print("By what percentage do you want to increase the product prices? (0-100): ", end='')
percent_increase = -1
while(percent_increase < 0):
    percent_increase = float(input())
    percent_increase = percent_increase * 0.01
    if(not (0 < percent_increase < 1)):
        print("Invalid value, please try again.")
        print(percent_increase)
        percent_increase = -1

# increases each value in price_list
for price in price_list:
    #print(price)
    modPrice = price * (1 + percent_increase)
    price_list[price_list.index(price)] = round(modPrice, 5)

print("\nInventory after all the prices are increased by " + str(int(percent_increase / 0.01)) + " percent:")
print(product_list, price_list)
print()

#removes product from inventory
remIndex = product_list.index(input("Name of the product to remove from inventory: "))
remName = product_list[remIndex]
product_list.remove(product_list[remIndex])
price_list.remove(price_list[remIndex])

print("\nInventory after " + remName + " is removed from the inventory:")
print(product_list, price_list)
print()

#prints average price of inventory
priceAvg = sum(price_list) / len(price_list)
print("The average price of " + str(len(price_list)) + " products is " + str(priceAvg))

#reverses inventory
print()
print("Original inventory:")
print(product_list, price_list)
print()
print("Reversed inventory:")
product_list.reverse()
price_list.reverse()
print(product_list, price_list)

#prints minimum value
minIndex = price_list.index(min(price_list))
print("\nThe least expensive product " + product_list[minIndex] + " costs " + str(price_list[minIndex]) + " Dollars.")
print("\n")

print("Products and respective prices side by side:")
print("Product \tPrice")
print("------- \t-----")
for product in product_list:
    print(product + " \t\t " + str(price_list[product_list.index(product)]))

print("\nHave a nice day!")