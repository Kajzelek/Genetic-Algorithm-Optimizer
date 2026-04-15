import random


#KRZYŻOWANIA
def crossover_single_point(parent1_gen, parent2_gen):
    size = len(parent1_gen)
    point = random.randint(1, size - 1)
    child1 = parent1_gen[:point] + parent2_gen[point:]
    child2 = parent2_gen[:point] + parent1_gen[point:]
    return child1, child2

def crossover_two_points(parent1_gen, parent2_gen):
    size = len(parent1_gen)
    p1 = random.randint(1, size -2)
    p2 = random.randint(p1+1,size-1)
    child1 = parent1_gen[:p1] + parent2_gen[p1:p2] + parent1_gen[p2:]
    child2 = parent2_gen[:p1] + parent1_gen[p1:p2] + parent2_gen[p2:]
    return child1, child2

def crossover_uniform(parent1_gen, parent2_gen):
    size = len(parent1_gen)
    child1 = []
    child2 = []
    for i in range(size):
        if random.random() < 0.5:
            child1.append(parent1_gen[i])
            child2.append(parent2_gen[i])
        else:
            child1.append(parent2_gen[i])
            child2.append(parent1_gen[i])
    return child1, child2


#MUTACJE

def mutate_one_point(genome):
    genome = genome[:]  # Kopia, aby nie modyfikować oryginału
    point = random.randint(0, len(genome) - 1)
    genome[point] = 1 - genome[point]
    return genome


def mutate_two_points(genome):
    genome = genome[:]  # Kopia, aby nie modyfikować oryginału
    size = len(genome)
    if size < 2:
        return mutate_one_point(genome)

    p1 = random.randint(0, size - 1)
    p2 = random.randint(0, size - 1)

    genome[p1] = 1 - genome[p1]
    genome[p2] = 1 - genome[p2]

    return genome

def mutate_edge(genome):
    genome = genome[:]  # Kopia, aby nie modyfikować oryginału
    genome[-1] = 1 - genome[-1]
    return genome

def inversion(genome):
    genome = genome[:]  # Kopia, aby nie modyfikować oryginału
    if len(genome) < 2: return genome
    p1 = random.randint(0, len(genome) - 2)
    p2 = random.randint(p1 + 1, len(genome) - 1)
    genome[p1:p2] = genome[p1:p2][::-1]
    return genome