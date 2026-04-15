from Population import Population
from Individual import Individual
from Operations import Selections, CrossMethods
import random

class GeneticAlgorithm:
    def __init__(self, config):
        self.config = config
        self.pop = Population(
            config['pop_size'], config['n_vars'], config['bits_per_var'],
            config['range_min'], config['range_max']
        )
        self.history = []

    def run(self):
        for epoch in range(self.config['epochs']):
            self.pop.evaluate_all()

            self.pop.individuals.sort(key=lambda x: x.fitness)

            best_fitness = self.pop.individuals[0].fitness
            self.history.append(best_fitness)
            print(f"Epoch {epoch}: Best Fitness = {best_fitness}")

            new_individuals = []

            elite_count = self.config.get('elite_count', 1)
            new_individuals.extend(self.pop.individuals[:elite_count])

            while len(new_individuals) < self.config['pop_size']:
                # Wybór rodziców (Selekcja)
                p1 = self._select_parent()
                p2 = self._select_parent()

                # Krzyżowanie (Crossover)
                if random.random() < self.config['prob_cross']:
                    # Wybieramy metodę krzyżowania z CrossMethods na podstawie config
                    c1_gen, c2_gen = self._apply_crossover(p1.genome, p2.genome)
                else:
                    # Jeśli nie ma krzyżowania, dzieci są kopiami rodziców
                    c1_gen, c2_gen = p1.genome[:], p2.genome[:]

                # Mutacja i Inwersja dla każdego dziecka
                for genome in [c1_gen, c2_gen]:
                    if len(new_individuals) < self.config['pop_size']:
                        # Mutacja
                        if random.random() < self.config['prob_mut']:
                            genome = self._apply_mutation(genome)

                        # Inwersja
                        if random.random() < self.config['prob_inv']:
                            genome = CrossMethods.inversion(genome)

                        # Tworzenie nowego obiektu dziecka z nowym genomem
                        child = Individual(
                            self.config['n_vars'], self.config['bits_per_var'],
                            self.config['range_min'], self.config['range_max']
                        )
                        child.genome = genome
                        new_individuals.append(child)

            # Nadpisanie starej populacji nową
            self.pop.individuals = new_individuals
            self.pop.evaluate_all()
            self.pop.individuals.sort(key=lambda x: x.fitness)
            best_overall = self.pop.individuals[0]
        return self.history, best_overall

    def _select_parent(self):
        """Pomocnicza metoda do wyboru rodzica na podstawie metody z config."""
        method = self.config['selection_method']
        if method == "Tournament":
            return Selections.select_tournament(self.pop.individuals, self.config['tournament_size'])
        elif method == "Roulette":
            return Selections.select_roulette(self.pop.individuals)
        else:  # Domyślnie 'Best'
            return Selections.select_best(self.pop.individuals, 1)[0]

    def _apply_crossover(self, g1, g2):
        """Pomocnicza metoda do wyboru typu krzyżowania."""
        method = self.config['crossover_method']
        if method == "Two-Point":
            return CrossMethods.crossover_two_points(g1, g2)
        elif method == "Uniform":
            return CrossMethods.crossover_uniform(g1, g2)
        return CrossMethods.crossover_single_point(g1, g2)

    def _apply_mutation(self, gen):
        """Pomocnicza metoda do wyboru typu mutacji."""
        method = self.config['mutation_method']
        if method == "Two-Point":
            return CrossMethods.mutate_two_points(gen)
        elif method == "Edge":
            return CrossMethods.mutate_edge(gen)
        return CrossMethods.mutate_one_point(gen)