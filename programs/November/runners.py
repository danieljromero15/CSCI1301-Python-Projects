from random import randint


class Runner:

    def __init__(self, id, distance=0):
        self.id = id
        self.distance = distance

        # self.distance = randint(10, 30) * 5 #5 is hours, we can make that a variable if we so choose

        self.speed = randint(10, 30)

    def __str__(self):

        return f'Runner {self.id} ran {self.distance} miles'

    def addDistance(self, hour):

        self.distance += self.speed * hour


runnersList = []

for i in range(0, 10):

    runner = Runner(1000 + i)

    # print(runner.distance)

    runnersList.append(runner)


# print(runnersList)


for n in runnersList:
    print(n)


hours = int(input("How many hours long is the race? "))


for runner in runnersList:
    runner.addDistance(hours)
    print(runner)
