import random

dices = {
    1: (

        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",

    ),

    2: (

        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",

    ),

    3: (

        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",

    ),

    4: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    5: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    6: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",

    )

}


def print_dice(dice_value):
    dice_art = "\n".join(dices[dice_value])
    print(dice_art)


def roll_dice():
    return random.randint(1, 6)


def display_menu():
    print("Hello! What would you like to do?")
    print("a) Roll 1 dice")
    print("b) Roll 2 dices")
    print("c) Roll n dices")
    print("d) Exit")

def main_loop():
    while True:
        display_menu()
        try:
            choice = input("Write a, b, c, or d: ").strip().lower()
            if choice not in ['a', 'b', 'c', 'd']:
                raise ValueError("Invalid choice")

            if choice == "a":
                rolled_dice = roll_dice()
                print_dice(rolled_dice)
                print(f"\n You rolled: {rolled_dice}")

            elif choice == "b":
                print("\n First Dice: \n")
                rolled_dice_1 = roll_dice()
                print_dice(rolled_dice_1)
                print(f"\n You rolled: {rolled_dice_1}")
                print(f"\n Second dice: \n")
                rolled_dice_2 = roll_dice()
                print_dice(rolled_dice_2)
                print(f"\n You rolled: {rolled_dice_2}")
                print(f"\n Sum of rolls = {rolled_dice_1+rolled_dice_2} \n")

            elif choice == "c":
                n = int(input("\nHow many dice would you like to roll: "))
                rolled_dice_array = []
                for i in range(n):
                    rolled_dice = roll_dice()
                    print(f"Dice {i+1}:")
                    print_dice(rolled_dice)
                    rolled_dice_array.append(rolled_dice)
                print(f"your rolls are: {rolled_dice_array}")
                print(f"\n Sum of rolls = {sum(rolled_dice_array)}")
            elif choice == "d":
                print("Thanks for playing!")
                break
        except ValueError as e:
            print(f"Error: {e}. Please enter valid values.\n")


main_loop()