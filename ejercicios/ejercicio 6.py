import random

class Entity:
    def __init__(self, id):
        self.id = id
        self.position = (random.uniform(0, 10), random.uniform(0, 10))
        self.food_found = []

    def move(self):
        self.position = (random.uniform(0, 10), random.uniform(0, 10))

    def forage(self):
        if random.random() < 0.5:
            self.food_found.append(self.position)

    def share_information(self, other):
        if random.random() < 0.7:
            shared_food = set(self.food_found) & set(other.food_found)
            self.food_found.extend(shared_food)
            other.food_found.extend(shared_food)

def simulate(entities, num_steps):
    for _ in range(num_steps):
        for entity in entities:
            entity.move()
            entity.forage()

        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                entities[i].share_information(entities[j])

        print(f"Step {_+1}:")
        for entity in entities:
            print(f"Entity {entity.id} - Position: {entity.position}, Food found: {entity.food_found}")
        print("="*30)

if __name__ == "__main__":
    num_entities = 5
    num_steps = 10
    entities = [Entity(id) for id in range(num_entities)]

    simulate(entities, num_steps)
