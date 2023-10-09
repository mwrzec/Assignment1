import random
from CharacterSpartan import Fighter1
from CharacterMage import Fighter2

# ANSI escape codes for text colors
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

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
        player = Fighter1(name="Spartan", health=100, attack=15, defense=5, attribute_value=0)
        enemy = Fighter2(name="Enemy", health=100, attack=6, defense=0, attribute_value=random.randint(1, 10))

    elif select == "2" or select.lower() == "mage":
        player = Fighter2(name="Mage", health=70, attack=80, defense=3, attribute_value=0)
        enemy = Fighter1(name="Enemy", health=100, attack=15, defense=1, attribute_value=random.randint(1, 10))

    else:
        print(RED + "Invalid Character Chosen. Try again." + RESET)
        return None

    return player, enemy

def roll_dice(num_dice, dice_range):
    return sum(random.randint(dice_range[0], dice_range[1]) for _ in range(num_dice))

def determine_outcome(roll_value, attribute_value):
    if 2 <= roll_value <= 3:
        return "Critical Loss"
    elif 4 <= roll_value <= 7:
        return "Loss"
    elif 8 <= roll_value <= 10:
        return "Win"
    elif 11 <= roll_value <= 12:
        return "Critical Win"

def main():
    print(GREEN + "*******************************" + RESET)
    print(GREEN + "   Welcome to Dungeon Warfare!" + RESET)
    print(GREEN + "*******************************" + RESET)
    print("\nIn this game, your goal is to complete all levels and defeat all enemies to recover the treasure.")

    player, enemy = select_character()
    if player is None:
        return

    total_levels = 3
    levels_won = 0
    levels_lost = 0

    while levels_won < total_levels:
        level = levels_won + 1
        enemy_name = f"Enemy {level}"
        enemy = Fighter2(name=enemy_name, health=100, attack=6 + level, defense=0, attribute_value=random.randint(1, 10))
        print(GREEN + "*******************************" + RESET)
        print(GREEN + f"Level {level} - Battle against {enemy_name}!" + RESET)
        print(GREEN + "*******************************" + RESET)

        defending = False

        while player.still_alive() and enemy.still_alive():
            print("\nPlayer Health =", player.health)
            print(BLUE + f"{enemy_name} Health =", str(enemy.health) + RESET)
            print("\nOptions:")
            print("1. Attack")
            print("2. Defend")
            print("3. Quit")
            select = input("\nEnter your choice: ")

            if select == "1":
                player_roll = roll_dice(2, (2, 12))
                enemy_attribute_value = enemy.attribute_value
                outcome = determine_outcome(player_roll, enemy_attribute_value)

                if outcome == "Critical Loss":
                    player.attribute_value -= 1
                elif outcome == "Critical Win":
                    player.attribute_value += 1

                player_damage = max(0, player_roll - enemy.defense)
                print(f"\n{player.name} attacks {enemy.name} for {player_damage} damage!")
                enemy.take_damage(player_damage)

                if enemy.still_alive():
                    enemy_roll = roll_dice(2, (2, 12))
                    counter_damage = max(0, enemy_roll - player.defense)
                    print(f"{enemy.name} counter-attacks {player.name} for {counter_damage} damage!")
                    player.take_damage(counter_damage)

                defending = False

            elif select == "2":
                print(f"\nYou chose to defend.")
                enemy_self_damage = random.randint(0, 5)
                print(f"{enemy.name} did {enemy_self_damage} damage to themselves while you defended.")
                enemy.health -= enemy_self_damage
                defending = True

            elif select == "3":
                print(RED + "\nYou have quit the game." + RESET)
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
