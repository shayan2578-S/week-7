from random import randint

def generate_target(lower_limit=17, upper_limit=29):
    return randint(lower_limit, upper_limit)

if __name__ == "__main__":
    target_number = generate_target()
    print("Welcome to the Dice Game!")
    print(f"Your target is to reach exactly {target_number} points.")
    print("You can roll the dice as many times as you like, but if you go over or under the target by 3, you lose!")
    print(f'Target_number: {target_number}')

from random import randint

from random import randint

def roll_dice():
    """Returns a random number between 1 and 6."""
    return randint(1, 6)

print("Welcome to the Dice Roller!")
print("Press Enter to roll the dice or type 'q' to quit.\n")

total = 0   
roll_number = 1 

while True:
    user_input = input(f"Roll {roll_number}: Press Enter to roll, or 'q' to quit: ")

    if user_input.lower() == 'q':
        break

    roll = roll_dice()
    total += roll

    print(f"       You rolled a {roll}! (Running total: {total})\n   Roll again?")

    roll_number += 1

print(f"\nFinal total after {roll_number - 1} rolls: {total}")


if total == target_number:
    print("Congratulations! You've hit the target LAD!")
  
elif total < target_number - 3:
    print("You've gone too low LAD! Better luck next time.")
 
elif total > target_number + 3:
    print("You've gone too high LAD! Better luck next time.")

print(((total)), "-- thanks for playing the game!")
