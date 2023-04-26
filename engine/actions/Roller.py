import random


def roll_dice(times, size, modifier):
    result = 0
    for i in range(times):
        result += random.randint(1, size)
    return result + modifier
