import random

class Fighter1:
    """
    Create character Spartan, Health, Name, Attack, Defense, etc.
    """
    def __init__(self, name, health, attack, defense, attribute_value=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.attribute_value = attribute_value
    """
    If character is still alive, return character health.
    """
    def still_alive(self):
        return self.health > 0
    """
    If character takes damage return character health after defence/hit.
    """
    def take_damage(self, damage):
        damage_after_defense = max(0, damage - self.defense)
        self.health -= damage_after_defense
    """
    If player attacks enemy return damage, attack sucess/fail, etc.
    """
    def attack_player(self, enemy, player_roll, enemy_attribute_value):
        if player_roll <= enemy_attribute_value:
            damage = 0  # Player's attack failed due to enemy's attribute
            print(f"\n{self.name}'s attack failed!")
        else:
            damage = random.randint(1, self.attack)  # Player's successful attack

        if damage > 0:
            print(f"\n{self.name} attacks {enemy.name} for {damage} damage!")
            enemy.take_damage(damage)
   