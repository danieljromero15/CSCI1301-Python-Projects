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
    " to the end of the inventory"]

    #asks for name and price of product
    tempProductInfo = input("Name of product " + str(x+1) + productInputEnding[x] +": ")
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
        print(error)
        exit()
    
    #might need to add another if else for this
    print("\nInventory after the " + numSuffix(x+1) + " product is added" + productInputEndingInventory[x] +":")
    print(product_list, price_list)
    print()
