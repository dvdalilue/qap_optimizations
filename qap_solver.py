#!/usr/bin/python2

import sys
import os.path
import random
import numpy as np

from solution import Solution
import input_processor as Processor

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        sys.exit('Bad arguments')
    
    if os.path.isfile(sys.argv[1]):
        file = open(sys.argv[1],'r')
    else:
        sys.exit('Not a file')

    (n, distances, flows) = Processor.processInput(file)

    solutions = map(lambda (x,y,z): Solution(x,y,z), [(n, distances, flows)] * 100)

    options = xrange(0,n)
    secure_random = random.SystemRandom()

    aux_sol_cost = None

    for i in xrange(1,100):
        for _ in xrange(1, int(1.27 * n)):
            city_1 = random.choice(options)
            city_2 = random.choice(options)

            aux_sol_cost = solutions[i].cost

            solutions[i].exchangeFacilities(city_1, city_2)

            if aux_sol_cost < solutions[i].cost:
                solutions[i].exchangeFacilities(city_1, city_2)

        print solutions[i].cost

if __name__ == "__main__":
    main()