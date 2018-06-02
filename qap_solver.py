#!/usr/bin/python2

import sys
import random
import os.path
import operator
import numpy as np

from solution import Solution
import evolutionary as evo
# import local_search as local
import input_processor as processor

GENERATIONS = 8

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        sys.exit('Bad arguments')
    
    if os.path.isfile(sys.argv[1]):
        file = open(sys.argv[1],'r')
    else:
        sys.exit('Not a file')

    (n, distances, flows) = processor.processInput(file)

    solutions = map(lambda (x,y,z): Solution(x,y,z), [(n, distances, flows)] * GENERATIONS)

    # solutions = [Solution(n, distances, flows),Solution(n, distances, flows)]
    
    # solution = Solution(n, distances, flows)

    #####################################
    # solution.exchangeFacilities(0,11) #
    # solution.exchangeFacilities(1,6)  #
    # solution.exchangeFacilities(2,8)  #
    # solution.exchangeFacilities(3,8)  #
    # solution.exchangeFacilities(4,8)  #
    # solution.exchangeFacilities(5,7)  #
    # solution.exchangeFacilities(6,10) #
    # solution.exchangeFacilities(7,11) #
    # solution.exchangeFacilities(9,11) #
    # solution.exchangeFacilities(10,11)#
    #####################################
    # print solution.cost # Optimal nug #
    # print solution.permutation        #
    #####################################

    solutions = evo.genetic(solutions, generations=GENERATIONS)

    print(min(solutions,key=operator.attrgetter('cost')).cost)

if __name__ == "__main__":
    main()