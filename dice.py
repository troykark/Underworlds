import random
import statistics
def statarray(): 
    roll = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    roll.remove(min(roll))
    return sum(roll)

def rollDice(rolls,dice): 
    output = 0
    for roll in list(range(rolls)):
        output += random.randint(1,dice)
    return output
def attackRoll(advantage):
        if advantage == 1: 
            return max([random.randint(1,20),random.randint(1,20)])
        elif advantage == -1 : 
            return min([random.randint(1,20),random.randint(1,20)])    
        else: 
            return random.randint(1,20)


def testrolls():
    test = []
    for i in list(range(10000)):
        test.append(statarray())
    print(statistics.mean(test))
    
testrolls() 
