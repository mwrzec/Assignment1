import random
from Character1 import Fighter
from Character2 import Fighter

def select_character():
    print("Choose your Character: ")
    print("1. Spartan ")
    print("2. Mage ")
    selection = input("Enter your choice: ")

    if selection == 1 or "Spartan":
        return Fighter("Spartan, 100, 6") #Modify Stats
    elif selection == 2 or "Mage":
        return Fighter("Mage", 100, 6)#Modify Stats
    else:
        print("Invalid Character Chosen. Try again.")

def main():
    player = select_character()
    enemy = Fighter("Enemy", 100, 6) #modify stats

    print("Welcome to Combat! ")
    while player.still_alive() and enemy.still_alive():
        print("n\Player Health = ")
        print("n\Enemy Health = ")
        print("n\Options: ")
        print("1. Attack")
        print("2. Quit")
        selection = input ("Enter what you want to do: ")

        if selection == 1 or "Attack":
            player.attack(enemy)
            if enemy.still_alive():
                enemy.attack(player)
        elif selection == 2 or "Quit":
            print("You have quit the game")
            break
        else:
            print("Invalid Selection, try again.")

        if player.stil_alive():
            print("Congratulations, You've Defeated the Enemy!")

        else:
            print("Youve, lost the battle.")
    if __name__ == "__main__":
        main()
