import random

class Fighter1:
    """
    Create character Spartan, Health, Name, Attack, Defense, etc.
    """
    def __init__(self, name, hlth, attack, defense, attr_val=0):
        self.name = name
        self.hlth = hlth
        self.attack = attack
        self.defense = defense
        self.attr_val = attr_val
    """
    If character is still alive, return character health.
    """
    def still_alive(self):
        return self.hlth > 0
    """
    If character takes damage return character health after defence/hit.
    """
    def take_dmg(self, dmg):
        dmg_after_defense = max(0, dmg - self.defense)
        self.hlth -= dmg_after_defense
    """
    If player attacks enemy return damage, attack sucess/fail, etc.
    """
    def attack_player(self, enemy, player_roll, enemy_attr_val):
        if player_roll <= enemy_attr_val:
            dmg = 0  # Player's attack failed due to enemy's attr
            print(f"\n{self.name}'s attack failed!")
        else:
            dmg = random.randint(1, self.attack)  # Player's successful attack

        if dmg > 0:
            print(f"\n{self.name} attacks {enemy.name} for {dmg} damage!")
            enemy.take_dmg(dmg)
   