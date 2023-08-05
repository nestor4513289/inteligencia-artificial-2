import random

# Parámetros del algoritmo genético
POPULATION_SIZE = 10
NUM_GENERATIONS = 5
MUTATION_RATE = 0.1

# Función de aptitud (fitness)
def fitness(individual, number_list):
    total = sum(number_list[i] for i, bit in enumerate(individual) if bit == 1)
    return total

# Inicialización de la población
def initialize_population(length):
    return [[random.randint(0, 1) for _ in range(length)] for _ in range(POPULATION_SIZE)]

# Operador de cruzamiento (crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Operador de mutación
def mutate(individual):
    mutated_individual = individual[:]
    for i in range(len(mutated_individual)):
        if random.random() < MUTATION_RATE:
            mutated_individual[i] = 1 - mutated_individual[i]
    return mutated_individual

# Algoritmo genético
def genetic_algorithm(number_list):
    population = initialize_population(len(number_list))
    
    for generation in range(NUM_GENERATIONS):
        # Evaluar la aptitud de la población
        fitness_scores = [fitness(individual, number_list) for individual in population]
        best_index = fitness_scores.index(max(fitness_scores))
        best_individual = population[best_index]
        
        print(f"Generación {generation}: Mejor valor = {max(fitness_scores)}")
        
        new_population = [best_individual]
        
        # Operador de selección y cruzamiento
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1, child2 = crossover(parent1, parent2)
            
            # Operador de mutación
            child1 = mutate(child1)
            child2 = mutate(child2)
            
            new_population.append(child1)
            new_population.append(child2)
        
        population = new_population
    
    return max(fitness_scores)

# Lista de números de ejemplo
number_list = [3, 8, 4, 5, 6, 2, 9, 7]

# Resolver el problema usando el algoritmo genético
max_value = genetic_algorithm(number_list)
print(f"El máximo valor encontrado es: {max_value}")
