from engine.actions.Duel import *
from engine.duelist.Duelist import *

# import random
# import matplotlib.pyplot as plt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d1 = Duelist('alice', 6, Attributes([15, 11, 12, 12, 13, 5]), 14, 0, 8)
    d2 = Duelist('bob', 6, Attributes([15, 11, 12, 12, 13, 5]), 14, 0, 8)
    duel = Duel(d1, d2)
    duel.simulate(10)
