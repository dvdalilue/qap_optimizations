import numpy as np
from helper_functions import swapRows, swapColumns, randomOptions

class Solution:
    def __init__(self, n, ds, fs):
        self.n = n
        self.permutation = np.array(xrange(1,n+1))
        self.distances = np.array(ds)
        self.flows = np.array(fs)
        self._cost = None

    def cityCosts(self, a, b):
        city_costs = 0

        for i in xrange(0, self.n):
            if i != a:
                city_costs += self.distances[a][i] * self.flows[a][i]
            if i != b:
                city_costs += self.distances[b][i] * self.flows[b][i]

        city_costs -= self.distances[a][b] * self.flows[a][b]

        return city_costs

    def exchangeFacilities(self, a, b):
        old_city_costs = self.cityCosts(a, b)
        old_cost = self.cost

        swapColumns(self.permutation, a, b)
        swapRows(self.flows, a, b)
        swapColumns(self.flows, a, b)

        new_city_costs = self.cityCosts(a, b)
        self._cost = old_cost + new_city_costs - old_city_costs

    def randomize(self, k=1):
        for i in xrange(0, k):
            cities = randomOptions(self.n, k=2)
            self.exchangeFacilities(cities[0], cities[1])

        return self

    def new_cost(self):
        cost_acc = 0

        for i in xrange(0, self.n):
            for j in xrange(i+1, self.n):
                cost_acc += self.distances[i][j] * self.flows[i][j]

        return cost_acc

    def copy(self):
        aux = Solution(self.n, self.distances, self.flows.copy())
        aux._cost = self.cost
        aux.permutation = self.permutation.copy()

        return aux

    @property
    def cost(self):
        if self._cost:
            return self._cost

        self._cost = self.new_cost()

        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @cost.deleter
    def cost(self):
        del self._cost