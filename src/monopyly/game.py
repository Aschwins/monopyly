import numpy as np


def double_dice(n_rolls=1):
    d1 = np.random.randint(1, 7, size=n_rolls)
    d2 = np.random.randint(1, 7, size=n_rolls)
    return d1 + d2


