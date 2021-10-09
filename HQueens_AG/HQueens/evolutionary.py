import numpy as np

from HQueens.HQueens import HQueens


class Evolutionary:
    def __init__(self, population_size=10, population=None):

        self._parents = []

        if population is None:
            # gera a população localmente
            self.population_size = population_size
            self.population = np.random.randint(1, 9, size=[population_size, 8])
        else:
            self.population = np.array(population)
            self.population_size = self.population.shape[0]

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

        parent1_index = np.random.choice(list(range(0, self.population_size)), 1, p=self.getFitness())
        parent2_index = np.random.choice(list(range(0, self.population_size)), 1, p=self.getFitness())

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
        # Mutation process
        if np.random.rand() <= mutation:
            position = np.ramdom.randint(child.size)
            value = np.random.randint(1, 9, size=1)[0]
            child[position] = value

        return child

    def seolve(self, maximum_generations=2000, separation=None, mutation=0.1):
        generation = 0
        number_attack = 0

        while number_attack < 28 and generation < maximum_generations:
            new_generation = []  # store the new children

            # generating the new children
            for _ in range(self.population_size):
                # Carry out the crossing
                child = self.crossing(separation=separation, mutation=mutation)
                new_generation.append(child)
            new_generation = np.array(new_generation)

            # Adding the new generation to the previous population
            new_population = np.concatenate((new_generation, self.population))

            # Excluding the worst individuals from the population
            local_fitness = self.getFitness(new_population)
            worst_index = np.argmin(local_fitness)
            new_population = np.delete(new_population, worst_index, 0)

            # populating the global population
            self.population = new_population

            # Defining stop criteria
            best_index = np.argmax(self.getFitness())
            game_solved = HQueens(board=self.population[best_index])
            number_attack = game_solved.get_attack()  # first stop criterion
            generation += 1  # second stop criterion
            print(f'Número de gerações: {generation}\nNumero de pares não atacados: {number_attack}')

        return game_solved
