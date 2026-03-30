import random

def select_best(population, count):
    sorted_pop = sorted(population, key=lambda ind: ind.fitness)
    return sorted_pop[:count]

def select_tournament(population, tournament_size):
    participants = random.sample(population, tournament_size)
    winner = min(participants, key=lambda ind: ind.fitness)
    return winner

def select_roulette(population):
    total_fitness = sum(1.0 / (ind.fitness + 1e-10) for ind in population)
    pick = random.uniform(0, total_fitness)

    current = 0
    for ind in population:
        current += 1.0 / (ind.fitness + 1e-10)
        if current > pick:
            return ind
    return population[0]