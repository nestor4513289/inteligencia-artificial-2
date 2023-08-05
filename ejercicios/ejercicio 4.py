import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_entities = 30
num_iterations = 200
speed = 0.1
neighborhood_radius = 3.0
formation_distance = 2.0
learning_rate = 0.05

# Crear las posiciones iniciales aleatorias de las entidades
positions = np.random.rand(num_entities, 2) * 20

# Función para calcular la distancia entre dos puntos
def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

# Bucle principal de simulación
for iteration in range(num_iterations):
    plt.clf()
    
    # Dibujar las posiciones actuales de las entidades
    plt.scatter(positions[:, 0], positions[:, 1], color='blue', marker='o')
    plt.title(f"Iteration {iteration}")
    
    # Calcular el centro de masas del enjambre
    center_of_mass = np.mean(positions, axis=0)
    
    # Calcular la dirección hacia el centro de masas
    direction_to_center = center_of_mass - positions
    
    # Actualizar las posiciones de las entidades según la dirección hacia el centro de masas
    positions += direction_to_center * speed
    
    # Actualizar las posiciones basadas en el aprendizaje social
    for i in range(num_entities):
        neighbors = [j for j in range(num_entities) if i != j and distance(positions[i], positions[j]) < neighborhood_radius]
        if neighbors:
            average_neighbor_position = np.mean([positions[n] for n in neighbors], axis=0)
            direction_to_neighbor = average_neighbor_position - positions[i]
            
            # Calcular la diferencia entre la distancia actual y la distancia deseada para mantener la formación
            formation_offset = direction_to_neighbor - (formation_distance * direction_to_neighbor / np.linalg.norm(direction_to_neighbor))
            
            # Actualizar la posición de la entidad según el aprendizaje social
            positions[i] += learning_rate * formation_offset
    
    plt.pause(0.1)

plt.show()
