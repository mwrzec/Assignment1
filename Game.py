import random
from CharacterSpartan import Fighter1
from CharacterMage import Fighter2

# ANSI escape codes for text colors
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"
"""
Select your character, Spartan or Mage. Depending on chosen character input user/enemy stats.
"""
def select_character():
    print("\nChoose your Character:")
    print("1. Spartan (Easy Difficulty)")
    print("   - High Health and Defense")
    print("   - Moderate Attack")
    print("2. Mage (Hard Difficulty)")
    print("   - Low Health and Defense")
    print("   - High Magical Attack")
    select = input("\nEnter your choice: ")

    if select == "1" or select.lower() == "spartan":
        player = Fighter1(name="Spartan", hlth=100, attack=15, defense=5, attr_val=0)
        enemy = Fighter2(name="Enemy", hlth=100, attack=6, defense=0, attr_val=random.randint(1, 10))

    elif select == "2" or select.lower() == "mage":
        player = Fighter2(name="Mage", hlth=70, attack=80, defense=3, attr_val=0)
        enemy = Fighter1(name="Enemy", hlth=100, attack=15, defense=1, attr_val=random.randint(1, 10))

    else:
        print(RED + "Invalid Character Chosen. Try again." + RESET)
        return None

    return player, enemy
"""
Roll random 2 sided dice.
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
"""
Intro to the game, levels, battle options, pop ups, info, etc.
"""
def main():
    print(GREEN + "\n\n\n*******************************" + RESET)
    print(GREEN + "   Welcome to Dungeon Brawl!" + RESET)
    print(GREEN + "*******************************" + RESET)
    print("\nIn this game, your goal is to fight for your life using strategic attacks/defence moves.\n Complete all levels and defeat all 3 enemies to recover the treasure.\nPick your characters wisely as some may be more challenging than others! Good Luck!")

    player, enemy = select_character()
    if player is None:
        return

    total_levels = 3
    levels_won = 0
    levels_lost = 0

    while levels_won < total_levels:
        level = levels_won + 1
        enemy_name = f"Enemy {level}"
        enemy = Fighter2(name=enemy_name, hlth=100, attack=6 + level, defense=0, attr_val=random.randint(1, 10))
        print(GREEN + "*******************************" + RESET)
        print(GREEN + f"Level {level} - Battle against {enemy_name}!" + RESET)
        print(GREEN + "*******************************" + RESET)

        defending = False

        while player.still_alive() and enemy.still_alive():
            print("\nPlayer Health =", player.hlth)
            print(BLUE + f"{enemy_name} Health =", str(enemy.hlth) + RESET)
            print("\nOptions:")
            print("1. Attack!")
            print("2. Defend")
            print("3. Quit")
            select = input("\nEnter your choice: ")

            if select == "1":
                player_roll = roll_dice(2, (2, 12))
                enemy_attr_val = enemy.attr_val
                otcm = determine_otcm(player_roll, enemy_attr_val)

                if otcm == "Critical Loss":
                    player.attr_val -= 1
                elif otcm == "Critical Win":
                    player.attr_val += 1

                player_dmg = max(0, player_roll - enemy.defense)
                print(f"\n{player.name} attacks {enemy.name} for {player_dmg} damage!")
                enemy.take_dmg(player_dmg)

                if enemy.still_alive():
                    enemy_roll = roll_dice(2, (2, 12))
                    counter_dmg = max(0, enemy_roll - player.defense)
                    print(f"{enemy.name} counter-attacks {player.name} for {counter_dmg} damage!")
                    player.take_dmg(counter_dmg)

                defending = False

            elif select == "2":
                print(f"\nYou chose to defend yourself against the enemy.")
                enemy_self_dmg = random.randint(0, 5)
                print(f"{enemy.name} did {enemy_self_dmg} damage to themselves while you defended.")
                enemy.hlth -= enemy_self_dmg
                defending = True

            elif select == "3":
                print(RED + "\nYou have quit the game. Enemy wins." + RESET)
                return

            else:
                print(RED + "\nInvalid Selection. Try again." + RESET)

        if player.still_alive():
            print(GREEN + f"\nCongratulations, You've Defeated {enemy_name}" + RESET)
            levels_won += 1
        else:
            print(RED + "\nYou've lost the battle." + RESET)
            levels_lost += 1
            break

    if levels_won == 3:
        print(GREEN + f"\nYou've completed {levels_won} levels and found the treasure!" + RESET)

    else: 
        print(GREEN + f"You've completed {levels_won} level(s), however failed the mission.")

if __name__ == "__main__":
    main()
