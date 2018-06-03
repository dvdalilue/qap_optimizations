import math
import random

from helper_functions import randomOptions

LOCAL_SEARCH_COEFFICIENT = 5.27
ANNEALING_TEMPERATURE_FACTOR = 1000

def eager_search(sln, iterations_coeff=LOCAL_SEARCH_COEFFICIENT):
    crnt_it = 0.0
    max_it_f = iterations_coeff * sln.n

    while crnt_it < max_it_f:
        crnt_it += 1.0
        mutation_factor = crnt_it / max_it_f
        aux_sln = sln.copy()

        for i in xrange(0, int(math.ceil(mutation_factor * sln.n))):
            aux_sln.randomize()

            if aux_sln.cost < sln.cost:
                sln.permutation = aux_sln.permutation
                sln.flows = aux_sln.flows
                sln.cost = aux_sln.cost
                crnt_it = 0
                break

        del aux_sln

    return sln

def annealing(sln):
    t_max = math.floor(sln.n * ANNEALING_TEMPERATURE_FACTOR)
    t = t_max
    s_cost = sln.cost

    while t > 0.0:
        aux_sln = sln.copy()
        aux_sln.randomize(int(aux_sln.n * (t / t_max)))

        # search(aux_sln, 0.8)

        diff_cost = sln.cost - aux_sln.cost

        if diff_cost > 0 or \
           math.exp(float(diff_cost) / t) > random.uniform(0,1):
            sln.permutation = aux_sln.permutation
            sln.flows = aux_sln.flows
            sln.cost = aux_sln.cost

        del aux_sln
        t = math.floor(0.73 * t)

    return sln

def search(sln, iterations_coeff=LOCAL_SEARCH_COEFFICIENT):
    for _ in xrange(0, int(iterations_coeff * sln.n)):
        cities = randomOptions(sln.n, k=2)
        aux_cost = sln.cost

        sln.exchangeFacilities(cities[0], cities[1])

        if aux_cost < sln.cost:
            sln.exchangeFacilities(cities[0], cities[1])

    return sln