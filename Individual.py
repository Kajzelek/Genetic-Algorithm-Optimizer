import random

from fitness_function import styblinski_tang


class Individual:
    def __init__(self, n_vars, bits_per_var, range_min, range_max):
        self.n_vars = n_vars
        self.bits_per_var = bits_per_var
        self.genome = [random.randint(0,1) for _ in range(n_vars * bits_per_var)]
        self.fitness = None
        self.range_min = range_min
        self.range_max = range_max

    def decode_bits(self, binary_array, a, b, m):
        #zamiana na liczbe dziesiatna z binarki
        binary_str = "".join(map(str, binary_array))
        decimal_value = int(binary_str, 2)
        #skalowanie do przedzialu
        x = a + decimal_value * (b - a) / (2 ** m - 1)
        return x

    def decode(self):
        """Dekoduje cały genom do listy wartości zmiennych"""
        decoded_vars = []
        for i in range(self.n_vars):
            start = i * self.bits_per_var
            end = start + self.bits_per_var
            bits = self.genome[start:end]
            decoded_vars.append(self.decode_bits(bits, self.range_min, self.range_max, self.bits_per_var))
        return decoded_vars



    def evaluate(self):
        decoded_vars = []
        for i in range(self.n_vars):
            start = i * self.bits_per_var
            end = start + self.bits_per_var
            bits = self.genome[start:end]
            decoded_vars.append(self.decode_bits(bits, self.range_min, self.range_max, self.bits_per_var))
        self.fitness = styblinski_tang(decoded_vars)
        return self.fitness
