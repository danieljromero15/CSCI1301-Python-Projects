from random import randint

class Runner:
    def __init__(self, id, distance=0):
        self.id = id
        self.distance = randint(10, 30) * 5

    def __str__(self):
        return f'Runner {self.id} ran {self.distance} miles'

runnersList = []
for i in range(0, 10):
    runner = Runner(1000 + i)
    #print(runner.distance)
    runnersList.append(runner)

#print(runnersList)

for n in runnersList:
    print(n)