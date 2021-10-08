import numpy as np

from HQueens.HQueens import HQueens


class Evolutionary:
    def __init__(self, pop_size=10, population=None):

        if population is None:
            # gera a população localmente
            self.pop_size = pop_size
            self.population = np.random.randint(1, 9, size=[pop_size, 8])
        else:
            self.population = np.array(population)
            self.pop_size = self.population.shape[0]

    def getFitness(self, population=None):

        if population is None:
            population = self.population

        fitness = []
        for p in population:
            game = HQueens(board=p)
            fitness.append(game.get_attack())

        fitness = np.array(fitness)
        fitness_normalized = fitness / np.sum(fitness)

        return np.array(fitness_normalized)

    def getParents(self):
        parent1ID = np.random.choice(list(range(0, self.pop_size)),
                                     1, p=self.get_fitness())
        parent2ID = np.random.choice(list(range(0, self.pop_size)),
                                     1, p=self.get_fitness())
        self.parents = []
        self.parents.append(self.population[parent_1_id][0])
        self.parents.append(self.population[parent_2_id][0])