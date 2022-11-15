# Title: Driving Costs
# Student name: Daniel Romero  
# Class: CSCI 1301 – Section HY8
# Professor: Dr. Abi Salimi
# Purpose: Asks a user for the number of cars to process, along with each mpg, price of gas, and number of driven miles. Then, computes the gas price of driving the car.

if __name__ == '__main__':
    # For example, when the function is called with the arguments (20.0, 3.1599, 50.0), it returns 7.89975 to the calling program
    def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
        gallons = miles_driven / miles_per_gallon
        return gallons * dollars_per_gallon
    

    # not gonna lie to you, i completely forgot python, an object oriented programming language, had objects
    # been a while since I really used the language I guess
    class Car:
        def __init__(self):
            self.miles_per_gallon = 0
            self.dollars_per_gallon = 0
            self.miles_driven = 0

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
        car = Car()

        car.miles_per_gallon = float(input("Enter miles per gallon: "))
        car.dollars_per_gallon = float(input("Enter Dollar amount per gallon: "))
        car.miles_driven = float(input("Enter the number of miles the car was driven: "))

        print()

        print(f"Miles per gallon: {car.miles_per_gallon:.2f}")
        print(f"Dollars per gallon: ${car.dollars_per_gallon:.2f}")
        print(f"Miles driven: {car.miles_driven:.2f}")

        print()

        print(f'Driving cost: ${car.driving_cost():.2f}')

        print()

    print("\nEnjoy your moments!")