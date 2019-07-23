import random
def statarray(): 
    roll = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    roll.remove(min(roll))
    return sum(roll)