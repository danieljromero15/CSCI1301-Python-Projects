# product_inventory.py

# Daniel Romero
# CSCI 1301-HY8, Fall 2022
# Dr. Abi Salimi

product_list = []
price_list = []

for x in range(0,4):
    tempProductInfo = input("Name of product " + str(x+1) + ": ")
    tempProductPrice = input("Price of the product: ")
    # I would use a switch statement but I'm worried about zybooks's ability to handle it
    print(tempProductInfo)
    print(tempProductPrice)