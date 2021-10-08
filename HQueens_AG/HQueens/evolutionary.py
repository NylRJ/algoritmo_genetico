import numpy as np

from HQueens.HQueens import HQueens


class Evolutionary:
    def __init__(self, pop_size=10, population=None):

        self._parents = []
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
        parent1_index = np.random.choice(list(range(0, self.pop_size)), 1, p=self.getFitness())
        parent2_index = np.random.choice(list(range(0, self.pop_size)), 1, p=self.getFitness())

        self._parents.append(self.population[parent1_index][0])
        self._parents.append(self.population[parent2_index][0])

        return self._parents

    def crossing(self, parents=None, separation=None, mutation=0.1):
        """
        Making the selection of parents
        :param parents: Parents for the crossing process
        :param separation: Determines the exact cutoff point of part of the chromosome
        :param mutation: Percentage of mutated parents
        :return: returns the son of this cross
        """
        # parent selection
        if parents is None:
            parents = self.getParents()

        child = np.concatenate(parents[0][0:separation], parents[1][separation:parents[1]])

        return child
