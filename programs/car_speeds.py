#function that converts two lists into ordered dictionary
def carDict(fcars, fspeeds):
    carSpeeds = {}
    for x in fcars:
        loopVal = fcars.index(x)
        #print(loopVal)
        #print(cars[loopVal])
        #print(speeds[loopVal])
        carSpeeds.update({fcars[loopVal]:fspeeds[loopVal]})

    print("Dictionary: " + str(carSpeeds))

#defines list of cars for now
cars = ["Speedtail", "F1", "F1-LM", "P2", "720S Spider"]
speeds = [250, 240, 225, 217, 212]

'''
car_name = input("Enter the name of the car: ")
car_speed = int(input("Enter the speed of the car: "))
cars.append(car_name)
speeds.append(car_speed)
'''
#combined above into two lines and reduced the number of variables
cars.append(input("Enter the name of the car: "))
speeds.append(int(input("Enter the speed of the car: ")))

#carSpeeds = {}

print("The list of the cars and corresponding speeds is:")
carDict(cars, speeds)
print()
print(cars, speeds)

#calculates average speeds and prints it
avgSpeed = sum(speeds) / len(speeds)
print("Average speed: " + str(avgSpeed))

#finds the index of the highest speed value
highSpeedIndex = speeds.index(max(speeds))
#prints car with highest speed based on index and prints speed based off same index
print("Car with highest speed: " + str(cars[highSpeedIndex]) + ", " + str(speeds[highSpeedIndex]) + "mph")