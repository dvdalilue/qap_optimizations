import random
import operator
import local_search as local
from solution import Solution

def crossover(parent_1, parent_2):
    a_random = random.SystemRandom()

    n = parent_1.n # == parent_2.n
    d = parent_1.distances # == parent_2.distances

    offspring_1 = Solution(n, d, parent_1.flows.copy())
    offspring_2 = Solution(n, d, parent_2.flows.copy())

    random_parents_facilities = [[],[]]

    # n_unequal = 0

    for i in xrange(0, n):
        for j in xrange(i+1, n):
            if offspring_1.flows[i][j] != offspring_2.flows[i][j]:
                # n_unequal += 1
                random_parents_facilities[0].append(offspring_1.flows[i][j])
                random_parents_facilities[1].append(offspring_2.flows[i][j])

    # matrix_size = float(n * n)
    # equivalence_ratio = (matrix_size - float(n_unequal)) / matrix_size

    random_parents_facilities[0] = random.sample(
                                    random_parents_facilities[0],
                                    len(random_parents_facilities[0]))
    random_parents_facilities[1] = random.sample(
                                    random_parents_facilities[1],
                                    len(random_parents_facilities[1]))

    for i in xrange(0, n):
        for j in xrange(i+1, n):
            if offspring_1.flows[i][j] != offspring_2.flows[i][j]:
                # Assign random facilities to offspring 1
                aux_pop = random_parents_facilities[0].pop()
                offspring_1.flows[i][j] = aux_pop
                offspring_1.flows[j][i] = aux_pop
                # Assign random facilities to offspring 2
                aux_pop = random_parents_facilities[1].pop()
                offspring_2.flows[i][j] = aux_pop
                offspring_2.flows[j][i] = aux_pop

    return (offspring_1, offspring_2)

def genetic(parents, generations):
    n = len(parents)

    for i in xrange(0, n):
        local.search(parents[i], iterations_coeff=1.0)

    gen_number = 0

    while gen_number < generations:
        new_generation = []

        for i in xrange(0, n-1):
            (of1, of2) = crossover(parents[i],parents[i+1])

            new_generation.append(of1)
            new_generation.append(of2)

        map(local.search, new_generation)

        new_generation.sort(key=operator.attrgetter('cost'))

        parents = new_generation[:n]
        gen_number += 1

    return parents