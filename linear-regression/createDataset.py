import random
import math

DATASET_SIZE = 70

class Set:
    def __init__(self):
        f = open("data.csv", "w")
        f.write("hsize,price\n")
        f.close()

        self.createSet()
    
    def createSet(self):
        f = open("data.csv", "a")

        print('creating dataset')
        for i in range(DATASET_SIZE):
            houseSize = random.uniform(50, 2000)
            price = (90*houseSize)*random.uniform(0.75, 1.5)

            f.write( f'{houseSize:.2f},{price:.2f}\n' )
        print('dataset created')
        f.close()
