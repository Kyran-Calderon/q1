class Hero:
    def __init__(self, name, health):
        self.name = name
        print("Our Hero's name is", {name})
        self.health = health
        print({name}, "has", {health}, "health")
        
    def damage(self, amount):
        self.health -= amount
        print({self.name}, "has taken", {amount}, "amount of damage")
        
arthur = Hero("Arthur", 300)
morgana = Hero("Morgana", 500)
print(arthur.name, arthur.health)
print(morgana.name, morgana.health)
arthur.damage(10)
print(arthur.name, arthur.health)
print(morgana.name, morgana.health)
