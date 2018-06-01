#!/usr/bin/python2

import sys
import os.path

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

    solution = Solution(n, distances, flows)
    
    print solution.flows

    solution.exchangeFacilities(0,1)

    print solution.flows

if __name__ == "__main__":
    main()