# Title: car_speeds_class_random.py
# Student name: Daniel Romero
# Class: CSCI 1301 – Section HY8
# Professor: Dr. Abi Salimi
# Purpose: Track the speeds of different cars using classes and objects. The car speeds will be generated randomly.

from random import randint
class Car:
    def __init__(self, id, topSpeed):
        self.id = id
        self.topSpeed = topSpeed

    def displayinfo(self):
        return f'{self.id} has a top speed of {self.topSpeed} miles per hour.'

def create_cars(num_cars, startID, min_speed, max_speed):
    cars = []
    for i in range(0, num_cars):
        car = Car((startID + i), randint(min_speed, max_speed))
        cars.append(car)
    return cars

#input for number of cars
n = input("Enter the number of cars: ")
ID = input("Enter the starting car ID: ")
min = input("Enter the minimum speed of the cars: ")
max = input("Enter the maximum speed of the cars: ")

cars_list = create_cars(n, ID, min, max)

print("Created cars are:")
for car in cars_list:
    car.displayinfo()