from random import randint


def roll_dice(): 
    return randint(1, 6)

for _ in range(10):
    print(roll_dice())