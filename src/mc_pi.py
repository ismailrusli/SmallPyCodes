"""
Monte Carlo method to calculate pi.
"""

import random
import math
import matplotlib.pyplot as plt

def mc_pi(iteration):
    pointX, pointY = [],[]
    countpi = 0.0
    for i in range(iteration):
        v = (randomized(),randomized())		
        if distance(v,(0,0)) <= 0.5:
            countpi += 1.0
    return (countpi/iteration)*4
	
def randomized():
    return random.random() - 0.5;
	
		
def distance(v1,v2):
    return math.sqrt((v1[0]-v2[0])*(v1[0]-v2[0])+(v1[1]-v2[1])*(v1[1]-v2[1]))		
		

print(mc_pi(1000))
