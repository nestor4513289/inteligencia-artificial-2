import random

# Parámetros del algoritmo genético
target_string = "HELLO WORLD"
population_size = 20
mutation_rate = 0.1
num_generations = 10

# Función para crear un individuo aleatorio
def create_individual():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ') for _ in range(len(target_string)))

# Función para evaluar la aptitud de un individuo
def fitness(individual):
    return sum(1 for i, j in zip(individual, target_string) if i == j)

# Función para seleccionar individuos para la reproducción
def select_parents(population):
    return sorted(population, key=lambda ind: -fitness(ind))[:2]

# Función para cruzar dos padres y producir descendencia
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(target_string) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Función para aplicar mutaciones a un individuo
def mutate(individual):
    mutated = [c if random.random() > mutation_rate else random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ') for c in individual]
    return ''.join(mutated)

# Generar la población inicial
population = [create_individual() for _ in range(population_size)]

# Ejecutar el algoritmo genético a lo largo de varias generaciones
for generation in range(num_generations):
    new_population = []

    for _ in range(population_size // 2):
        parent1, parent2 = select_parents(population)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])

    population = new_population

    # Encontrar el mejor individuo de esta generación
    best_individual = max(population, key=fitness)
    best_fitness = fitness(best_individual)

    print(f"Generación {generation + 1}: {best_individual} (Aptitud: {best_fitness}/{len(target_string)})")

    # Si se encuentra la cadena objetivo, detener el algoritmo
    if best_fitness == len(target_string):
        print("¡Cadena objetivo encontrada!")
        break
