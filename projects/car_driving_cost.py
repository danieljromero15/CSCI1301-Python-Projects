# Title: Driving Costs
# Student name: Daniel Romero  
# Class: CSCI 1301 – Section HY8
# Professor: Dr. Abi Salimi
# Purpose: Asks a user for the number of cars to process, along with each mpg, price of gas, and number of driven miles. Then, computes the gas price of driving the car.

# I have a few long comments, might help to turn on word wrap if you want to read them

# For example, when the function is called with the arguments (20.0, 3.1599, 50.0), it returns 7.89975 to the calling program
# putting this inside __main__ gave me the error "cannot import name 'driving_cost' from 'car_driving_cost'"
# makes sense as it's presumably trying to call car_driving_cost.driving_cost() or something along those lines
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon

if __name__ == '__main__':
    # not gonna lie to you, i completely forgot python, an object oriented programming language, had objects
    # been a while since I really used the language I guess
    # didn't need to put a class here but I thought it would be a fun experiment, plus it doesn't affect the program itself all that much
    class Car:
        def __init__(self):
            self.miles_per_gallon = 0
            self.dollars_per_gallon = 0
            self.miles_driven = 0

        # having driving_cost as a function of the car itself made more sense to me than to have it seperate, since each car has its own driving cost and that's not dependent on any external factors.
        # Plus, all the parameters the function would otherwise use are already variables of the class, meaning I don't have to have any parameters for this except self
        # However, zybooks forces me to have the driving_cost function outside of __name__=='__main__', which makes sense when it's looking for the specific function but somewhat annoying
        # Actually come to think of it, it would make sense in real life to have the dollars per gallon as a parameter, since the price isn't dependent on the car itself but rather the price of gasoline. However, since we're inputting a new gas price on each variable loop anyways, it makes sense to have this rather than the alternative
        def driving_cost(self):
            return (self.miles_driven / self.miles_per_gallon) * self.dollars_per_gallon

    #car1 = Car()
    #car1.miles_per_gallon = 20.0
    #car1.dollars_per_gallon = 3.1599
    #car1.miles_driven = 50

    #print(f'{car1.driving_cost():.2f}')

    carNum = int(input("Enter the number of cars: "))
    
    # thinking of adding the cars to a list so the info is stored, might try that next though it'll have no impact on the program expectations
    #carList = []
    
    for i in range(carNum):
        print("for car", (i+1))
        car = Car() # currently makes a new 'Car' object on each loop and overwrites the previous 'Car' object stored to var 'car'. The intention of this is to append each object to a list or something similar, but this function is currently not implemented since the zybooks assignment doesn't require it.

        # inputs
        car.miles_per_gallon = float(input("Enter miles per gallon: "))
        car.dollars_per_gallon = float(input("Enter Dollar amount per gallon: "))
        car.miles_driven = float(input("Enter the number of miles the car was driven: "))

        print()

        # prints formatted values
        print(f"Miles per gallon: {car.miles_per_gallon:.2f}")
        print(f"Dollars per gallon: ${car.dollars_per_gallon:.2f}")
        print(f"Miles driven: {car.miles_driven:.2f}")

        print()

        # look! it's so small! doesn't need any parameters! yay!
        print(f'Driving cost: ${car.driving_cost():.2f}')

        print()

    print("\nEnjoy your moments!")