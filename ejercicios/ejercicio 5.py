import numpy as np
import random

# Función de fitness
def fitness(position, matrix):
    row, col = position
    return matrix[row][col]

# Función de mutación
def mutate(position, matrix):
    row, col = position
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if random.random() < 0.5:  # Mutación en fila
        new_row = random.randint(0, num_rows - 1)
        return (new_row, col)
    else:  # Mutación en columna
        new_col = random.randint(0, num_cols - 1)
        return (row, new_col)

# Función de cruzamiento
def crossover(parent1, parent2):
    row1, col1 = parent1
    row2, col2 = parent2
    return (row1, col2)

# Algoritmo genético
def genetic_algorithm(matrix, population_size, generations):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Inicializar población aleatoria de posiciones
    population = [(random.randint(0, num_rows - 1), random.randint(0, num_cols - 1)) for _ in range(population_size)]

    for _ in range(generations):
        # Calcular valores de fitness para cada individuo en la población
        fitness_scores = [fitness(position, matrix) for position in population]

        # Seleccionar a los padres basados en sus valores de fitness
        parents = [population[i] for i in np.argsort(fitness_scores)[-2:]]

        # Generar nueva población a través de cruzamiento y mutación
        new_population = [crossover(parents[0], parents[1])]

        for _ in range(population_size - 1):
            mutated_child = mutate(random.choice(parents), matrix)
            new_population.append(mutated_child)

        population = new_population

    # Encontrar el individuo con el mejor valor de fitness (posición del máximo)
    best_position = max(population, key=lambda position: fitness(position, matrix))
    return best_position

# Ejemplo de uso
matrix = [
    [3, 8, 2],
    [10, 5, 9],
    [4, 7, 1]
]
population_size = 10
generations = 50

best_position = genetic_algorithm(matrix, population_size, generations)
print("Matriz:")
for row in matrix:
    print(row)
print("La posición del número máximo es:", best_position)
print("El número máximo es:", matrix[best_position[0]][best_position[1]])
