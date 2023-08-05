import random

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def avoid_collision(self, other):
        if self.x == other.x and self.y == other.y:
            # Handle collision
            self.move(random.choice([-1, 1]), random.choice([-1, 1]))

# Crear algunas entidades
num_entities = 5
entities = [Entity(random.randint(0, 10), random.randint(0, 10)) for _ in range(num_entities)]

# Simular el movimiento y aprendizaje social
num_steps = 20
for step in range(num_steps):
    print(f"Step {step}:")
    for entity in entities:
        print(f"Entity at ({entity.x}, {entity.y})")
        entity.move(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))
        for other in entities:
            if entity != other:
                entity.avoid_collision(other)
    print("------------------")
