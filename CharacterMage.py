import random

class Fighter2:
    """
    Create character Mage. Name,Health, Attack, Defense, etc.
    """
    def __init__(self, name, health, attack, defense, attribute_value=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.attribute_value = attribute_value
    """
    If character is still alive/ >0 return character health.
    """
    def still_alive(self):
        return self.health > 0
    """
    If character takes damage show health after defence/after being hit.
    """
    def take_damage(self, damage):
        damage_after_defense = max(0, damage - self.defense)
        self.health -= damage_after_defense
