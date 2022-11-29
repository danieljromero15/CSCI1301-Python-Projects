# Title: car_speeds_class_random.py
# Student name: Daniel Romero
# Class: CSCI 1301 – Section HY8
# Professor: Dr. Abi Salimi
# Purpose: Track the speeds of different cars using classes and objects. The car speeds will be generated randomly.

import random

# not random but okay
random.seed(10)

#def class car with id and topSpeed
class Car:
    def __init__(self, id, topSpeed):
        self.id = id
        self.topSpeed = topSpeed

    def displayinfo(self):
        return f'{self.id} has a top speed of {self.topSpeed} miles per hour.'

#func to create cars, returns a list
def create_cars(num_cars, startID, min_speed, max_speed):
    cars = []
    for i in range(0, num_cars):
        car = Car((startID + i), random.randint(min_speed, max_speed))
        cars.append(car)
    return cars

#input for number of cars
n = int(input("Enter the number of cars: "))
ID = int(input("Enter the starting car ID: "))
min = int(input("Enter the minimum speed of the cars: "))
max = int(input("Enter the maximum speed of the cars: "))

# init variables for later
speedTotal = 0
topSpeed = 0

# create two lists, one for all cars and one for the top speeds (currently empty)
cars_list = create_cars(n, ID, min, max)
top_speed_cars = []

print()
print("Created cars are:")
# for all cars, print info, add to totalspeed for avg calculation, and grabs max value
for car in cars_list:
    print(car.displayinfo())
    speedTotal += car.topSpeed
    if car.topSpeed >= topSpeed:
        topSpeed = car.topSpeed #could do this another way but im already parsing the entire list so whatever

#needs to be after other loop because def topSpeed var
for car in cars_list:
    if car.topSpeed == topSpeed:
        top_speed_cars.append(car)

print()

#avg speed
cars_list_length = len(cars_list)
#for car in cars_list:
#    speedTotal += car.topSpeed

avgSpeed = speedTotal / cars_list_length
print(f'Average speed of all the cars: {avgSpeed}')

print()

#prints top speed based on previously calculated
print(f'The highest speed is {topSpeed}')
print('The following cars have the above speed:')
for car in top_speed_cars:
    print(f'Car {car.id}')

print()

print("All the existing cars are:")

print()

#prints all cars in a table
print('ID\tTop Speed\n----\t---------')
for car in cars_list:
    print(f'{car.id}\t{car.topSpeed}')

print('\nHave a nice day!')