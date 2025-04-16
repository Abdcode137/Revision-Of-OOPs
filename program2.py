import random

def roll_dice():
    # Simulates rolling a dice
    return random.randint(1, 6)

def main():
    print("🎲 Welcome to the Dice Rolling Simulator 🎲")

    while True:
        user_input = input("Roll the dice? (yes/no): ").lower()

        if user_input == "yes":
            dice_value = roll_dice()
            print(f"You rolled a {dice_value}!")

            # Add a fun message for specific rolls
            if dice_value == 6:
                print("🎉 Lucky! You rolled the highest number!")
            elif dice_value == 1:
                print("😬 Oof! That's the lowest you can go.")
        elif user_input == "no":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Please type 'yes' or 'no'.")

# Run the program
main()
