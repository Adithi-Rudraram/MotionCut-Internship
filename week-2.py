import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.hp = 100

    def display_status(self):
        print(f"\nPlayer: {self.name}")
        print(f"Health: {self.hp}")
        print("Inventory:", ', '.join(self.inventory))

def introduction():
    print("Welcome to the Epic Adventure Game!")
    time.sleep(1)
    print("You, a brave adventurer, set out on a quest to save the kingdom.")
    time.sleep(1)
    print("The land is filled with magical creatures, hidden treasures, and ancient mysteries.")
    time.sleep(1)

def make_choice(choices):
    print("\nChoose your action:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def explore_forest(player):
    print("\nYou venture into the enchanted forest.")
    time.sleep(1)

    # Random event
    if random.choice([True, False]):
        print("You encounter a friendly creature who offers guidance.")
        choices = ["Follow the creature", "Continue on your own"]
        user_choice = make_choice(choices)

        if user_choice == 1:
            print("\nThe creature leads you to a hidden clearing with a healing spring.")
            player.hp += 20
            print("You feel refreshed and gain additional health!")
        else:
            print("\nYou decide to continue on your own.")
    else:
        print("You face a group of hostile goblins!")
        combat(player)

def explore_mountains(player):
    print("\nYou climb the treacherous mountains.")
    time.sleep(1)

    # Random event
    if random.choice([True, False]):
        print("You discover a hidden cave.")
        choices = ["Enter the cave", "Bypass the cave"]
        user_choice = make_choice(choices)

        if user_choice == 1:
            print("\nInside the cave, you find a mystical portal.")
            print("Do you step through the portal?")
            choices = ["Step through the portal", "Stay in the cave"]
            user_choice = make_choice(choices)

            if user_choice == 1:
                print("\nCongratulations! You find yourself in a magical realm and gain a new ability.")
                player.inventory.append("Enchanted Ability")
            else:
                print("\nYou decide to stay in the cave.")
        else:
            print("\nYou bypass the cave and continue your journey.")
    else:
        print("You encounter a group of mountain trolls!")
        combat(player)

def combat(player):
    print("Combat initiated!")
    time.sleep(1)

    # Random outcome in combat
    if random.choice([True, False]):
        print("You defeat the enemies and find a treasure chest.")
        player.inventory.append("Treasure Chest")
    else:
        print("The enemies overwhelm you, and you lose some health.")
        player.hp -= 20

def main():
    introduction()
    player_name = input("\nEnter your character's name: ")
    while True:
        player = Player(player_name)

        # Chapter One
        print(f"\n{player.name}, you stand at the edge of the mystical forest.")
        time.sleep(1)
        print("What will you do?")
        
        choices = ["Explore the forest", "Head to the mountains"]
        user_choice = make_choice(choices)

        if user_choice == 1:
            explore_forest(player)
        else:
            explore_mountains(player)

        # Display player status and ending
        player.display_status()

        if "Enchanted Ability" in player.inventory:
            print("Congratulations! You've gained a special ability and completed your quest.")
        elif "Treasure Chest" in player.inventory:
            print("You've found a treasure chest, but your quest continues.")
        else:
            print("Unfortunately, your journey comes to an end. Better luck next time!")

        play_again = input("\nDo you want to start a new quest? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
