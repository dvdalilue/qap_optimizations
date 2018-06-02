import random

LOCAL_SEARCH_COEFFICIENT = 1.27

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