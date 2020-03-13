import random
from pyeasyga.pyeasyga import GeneticAlgorithm
data = [('orange', 50), ('apple', 35), ('kiwi', 40), ('aaa', 20), ('melon', 10)]
ga = GeneticAlgorithm(data, 40, 50, 0.8, 0.2, True, True)


def create_individual(data):
    individual = []
    for item in data:
        individual.append(random.randint(0, 1))
    return individual


ga.create_individual = create_individual


def crossover(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))
    child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
    child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
    return child_1, child_2


ga.crossover_function = crossover


def mutate(individual):
    mutate_index = random.randrange(len(individual))
    if individual[mutate_index] == 0:
        individual[mutate_index] == 1
    else:
        individual[mutate_index] == 0


ga.mutate_function = mutate


def selection(population):
    return random.choice(population)


ga.selection_function = selection


def fitness(individual, data):
        fitness = 0
        if individual.count(1) == 2:
            for(selected, (fruit, profit)) in zip(individual, data):
                if selected == 1:
                     fitness += profit
        return fitness


ga.fitness_function = fitness

ga.run()
print("the best individual : ", ga.best_individual())

for individual in ga.last_generation():
    print(individual)
