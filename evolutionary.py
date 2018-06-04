import random
import operator

import local_search as local
from solution import Solution

a_random = random.SystemRandom()

def crossover(parent_1, parent_2):
    n = parent_1.n # == parent_2.n

    offspring_1 = parent_1.copy()
    offspring_2 = parent_2.copy()

    unequal_facilities = [[],[]]

    for i in xrange(0, n):
        if offspring_1.permutation[i] != offspring_2.permutation[i]:
            unequal_facilities[0].append(i)
            unequal_facilities[1].append(i)

    n_unequal = len(unequal_facilities[0]) # == len(unequal_facilities[1])

    unequal_facilities[0] = a_random.sample(unequal_facilities[0], n_unequal)
    unequal_facilities[1] = a_random.sample(unequal_facilities[1], n_unequal)

    for i in xrange(0, n_unequal-1, 2):
        # Assign random facilities to offspring 1
        offspring_1.exchangeFacilities(
            unequal_facilities[0][i],
            unequal_facilities[0][i+1])
        # Assign random facilities to offspring 2
        offspring_2.exchangeFacilities(
            unequal_facilities[1][i],
            unequal_facilities[1][i+1])

    return (offspring_1, offspring_2)

def crossover_mutant(parent_1, parent_2):
    n = parent_1.n # == parent_2.n

    offspring_1 = parent_1.copy()
    offspring_2 = parent_2.copy()
    mutant = parent_1.copy()

    unequal_facilities = [[],[],[]]

    for i in xrange(0, n):
        if offspring_1.permutation[i] != offspring_2.permutation[i]:
            unequal_facilities[0].append(i)
            unequal_facilities[1].append(i)

    n_unequal = len(unequal_facilities[0]) # == len(unequal_facilities[1])

    unequal_facilities[0] = a_random.sample(unequal_facilities[0], n_unequal)
    unequal_facilities[1] = a_random.sample(unequal_facilities[1], n_unequal)
    unequal_facilities[2] = a_random.sample(unequal_facilities[1], n_unequal)

    for i in xrange(0, n_unequal-1, 2):
        # Assign random facilities to offspring 1
        offspring_1.exchangeFacilities(
            unequal_facilities[0][i],
            unequal_facilities[0][i+1])
        # Assign random facilities to offspring 2
        offspring_2.exchangeFacilities(
            unequal_facilities[1][i],
            unequal_facilities[1][i+1])
        # Assign random facilities to mutant
        mutant.exchangeFacilities(
            unequal_facilities[2][i],
            unequal_facilities[2][i+1])

    return (offspring_1, offspring_2, mutant)

def genetic(parents, generations, local_s):
    n = len(parents)

    gen_number = 0

    while gen_number < generations:
        new_generation = []

        for i in xrange(0, n-1):
            (of1, of2, mut) = crossover_mutant(parents[i],parents[i+1])

            new_generation.append(of1)
            new_generation.append(of2)
            new_generation.append(mut)

        map(local_s, new_generation)

        new_generation.sort(key=operator.attrgetter('cost'))

        parents = a_random.sample(new_generation[:n], n)
        gen_number += 1

    return parents