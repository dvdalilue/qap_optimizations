#!/usr/bin/python2

import sys
import math
import os.path
import operator

from solution import Solution
import evolutionary as evo
import local_search as local
import input_processor as processor

POPULATION = 10
GENERATIONS = 7

ls = lambda x: local.search(x,43.5)
ils = lambda x: local.eager_search(x, 1)
sa = lambda x: local.annealing(x,1050500)

def timereps(slns, ls):
    from time import time
    start = time()
    slns = evo.genetic(slns,GENERATIONS,ls)
    end = time()
    return (end - start,slns)

def run_ls(n, distances, flows, coeff):
    solution = Solution(n, distances, flows)
    local.search(solution, coeff)
    return solution

def run_sa(n, distances, flows, temp):
    solution = Solution(n, distances, flows)
    local.annealing(solution, temp)
    return solution

def run_ils(n, distances, flows, coeff):
    solution = Solution(n, distances, flows)
    local.eager_search(solution, coeff)
    return solution

def run_evo(n, distances, flows, generations=GENERATIONS):
    print 's1, s2, s3, t1, t2, t3'
    for _ in xrange(0, generations):
        solutions1 = map(lambda x: x.randomize(n),
                        map(
                            lambda (x,y,z): Solution(x,y,z),
                            [(n, distances, flows)] * POPULATION
                            )
                        )
        solutions2 = map(lambda x: x.randomize(n),
                        map(
                            lambda (x,y,z): Solution(x,y,z),
                            [(n, distances, flows)] * POPULATION
                            )
                        )
        solutions3 = map(lambda x: x.randomize(n),
                        map(
                            lambda (x,y,z): Solution(x,y,z),
                            [(n, distances, flows)] * POPULATION
                            )
                        )
        (t1,solutions1) = timereps(solutions1,ls)
        (t2,solutions2) = timereps(solutions2,sa)
        (t3,solutions3) = timereps(solutions3,ils)

        print ("{0},{1},{2},{3},{4},{5}".format(
                min(solutions1,key=operator.attrgetter('cost')).cost,
                min(solutions2,key=operator.attrgetter('cost')).cost,
                min(solutions3,key=operator.attrgetter('cost')).cost,
                t1,t2,t3
            )
        )

def main():
    if len(sys.argv) < 4 or len(sys.argv) > 4:
        sys.exit('Bad arguments')
    
    if os.path.isfile(sys.argv[3]):
        file = open(sys.argv[3],'r')
    else:
        sys.exit('Not a file')

    (n, distances, flows) = processor.processInput(file)

    if sys.argv[1] == 'ls':
        sln = run_ls(n, distances, flows, int(sys.argv[2]))
        print sln.cost
    elif sys.argv[1] == 'sa':
        sln = run_sa(n, distances, flows, int(sys.argv[2]))
        print sln.cost
    elif sys.argv[1] == 'ils':
        sln = run_ils(n, distances, flows, int(sys.argv[2]))
        print sln.cost
    elif sys.argv[1] == 'evo':
        sln = run_evo(n, distances, flows ,int(sys.argv[2]))

if __name__ == "__main__":
    main()