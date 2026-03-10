from random import randint

def generate_target(lower_limit=17, upper_limit=29):
    return randint(lower_limit, upper_limit)

if __name__ == "__main__":
    target_number = generate_target()
    print("Welcome to the Dice Game!")
    print(f"Your target is to reach exactly {target_number} points.")
    print("You can roll the dice as many times as you like, but if you go over or under the target by 5, you lose!")
    print(f'Target_number: {target_number}')

def roll_dice(): 
    return randint(1, 6)

