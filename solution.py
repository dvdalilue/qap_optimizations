import numpy as np
from np_functions import *

class Solution:
    def __init__(self, n, ds, fs):
        self.n = n
        self.distances = np.array(ds)
        self.flows = np.array(fs)
        self._cost = None

    def exchangeFacilities(self, a, b):
        swapRows(self.flows, a, b)
        swapColumns(self.flows, a, b)

    @property
    def cost(self):
        if self._cost:
            return self._cost

        cost_acc = 0

        for i in xrange(0,self.n):
            for j in xrange(0,self.n):
                cost_acc += self.distances[i][j] * self.flows[i][j]

        self._cost = cost_acc

        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @cost.deleter
    def cost(self):
        del self._cost