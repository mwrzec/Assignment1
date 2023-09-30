import random

class Fighter:
    def __innit__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def still_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self, enemy):
        damage = random.randint(1,self.attack) #use dice based attack
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.damage_taken(damage)