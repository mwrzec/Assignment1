import random

class Fighter2:
    """
    Create character Mage. Name,Health, Attack, Defense, etc.
    """
    def __init__(self, name, hlth, attack, defense, attr_val=0):
        self.name = name
        self.hlth = hlth
        self.attack = attack
        self.defense = defense
        self.attr_val = attr_val
    """
    If character is still alive/ >0 return character health.
    """
    def still_alive(self):
        return self.hlth > 0
    """
    If character takes damage show health after defence/after being hit.
    """
    def take_dmg(self, dmg):
        dmg_after_defense = max(0, dmg - self.defense)
        self.hlth -= dmg_after_defense
