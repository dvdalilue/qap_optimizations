import math
import random

LOCAL_SEARCH_COEFFICIENT = 5.27

def eager_search(sln, iterations_coeff=LOCAL_SEARCH_COEFFICIENT):
    options = xrange(0, sln.n)
    a_random = random.SystemRandom()

    current_ite = 0
    max_ite_f = iterations_coeff * sln.n
    max_ite_i = int(max_ite_f)

    while current_ite < max_ite_i:
        current_ite += 1
        mutation_factor = float(current_ite) / max_ite_f

        aux_sln = sln.copy()

        for _ in xrange(0, int(math.ceil(mutation_factor * sln.n))):
            city_1 = a_random.choice(options)
            city_2 = a_random.choice(options)

            aux_sln.exchangeFacilities(city_1, city_2)

            if aux_sln.cost < sln.cost:
                sln.permutation = aux_sln.permutation
                sln.flows = aux_sln.flows
                sln.cost = aux_sln.cost
                current_ite = 0
                break

        del aux_sln

def search(sln, iterations_coeff=LOCAL_SEARCH_COEFFICIENT):
    options = xrange(0,sln.n)
    a_random = random.SystemRandom()
    
    for _ in xrange(0, int(iterations_coeff * sln.n)):
        city_1 = a_random.choice(options)
        city_2 = a_random.choice(options)

        aux_sol_cost = sln.cost

        sln.exchangeFacilities(city_1, city_2)

        if aux_sol_cost < sln.cost:
            sln.exchangeFacilities(city_1, city_2)