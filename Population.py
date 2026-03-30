import random
from Individual import Individual


class Population:
    def __init__(self, size, n_vars, bits_per_var, range_min, range_max):
        self.size = size
        self.n_vars = n_vars
        self.bits_per_var = bits_per_var
        self.range_min = range_min
        self.range_max = range_max

        self.individuals = [
            Individual(n_vars, bits_per_var, range_min, range_max)
            for _ in range(size)
        ]

    def evaluate_all(self):
        for ind in self.individuals:
            ind.evaluate()