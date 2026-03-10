from random import randint


def roll_dice(): 
    return randint(1, 6)

def main():
    target = randint(17, 29)
    print("Welcome to the Dice Game!")
    print(f"Your target number is: {target}")
    total = 0
    while True:
        user_input = input("Press Enter to roll the dice or type 'stop' to finish: ").strip().lower()
        if user_input == 'stop':
            break
       
