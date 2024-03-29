import random
from CharacterSpartan import Fighter1
from CharacterMage import Fighter2

# ANSI escape codes for text colors
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

"""
Select your character from the options listed. Enter your choice, if Selection 1 or 2 chosen stats based off Character.
"""

def select_character():
    print("\nChoose your Character:")
    print("1. Spartan")
    print("   - High Health and Defense")
    print("   - Moderate Attack")
    print("2. Mage")
    print("   - Low Health and Defense")
    print("   - High Magical Attack")
    select = input("\nEnter your choice: ")

    if select == "1" or select.lower() == "spartan":
        player = Fighter1(name="Spartan", hlth=100, attack=15, defense=5)
        enemy = Fighter2(name="Enemy", hlth=100, attack=6, defense=0, attr_val=random.randint(1, 10))

    elif select == "2" or select.lower() == "mage":
        player = Fighter2(name="Mage", hlth=70, attack=50, defense=2)
        enemy = Fighter1(name="Enemy", hlth=100, attack=15, defense=5, attr_val=random.randint(1, 10))

    else:
        print(RED + "Invalid Character Chosen. Try again." + RESET)
        return None

    return player, enemy
"""
Roll random 2 sided dice for attack, defence etc.
"""
def roll_dice(num_dice, dice_range):
    return sum(random.randint(dice_range[0], dice_range[1]) for _ in range(num_dice))

def determine_otcm(roll_val, attr_val):
    if 2 <= roll_val <= 3:
        return "Critical Loss"
    elif 4 <= roll_val <= 7:
        return "Loss"
    elif 8 <= roll_val <= 10:
        return "Win"
    elif 11 <= roll_val <= 12:
        return "Critical Win"

if __name__ == "__main__":
    pass  
