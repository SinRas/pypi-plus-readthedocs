"""
Random calculator functionalitites.

See documentation in docs/topics/calculator.rst
"""

import numpy as np


class CalculatorRandom:
    """Random calculator.
    """
    # Constructor
    def __init__(self, name: str = 'CalculatorRandomName'):
        self.name = name
        return

    # Random repeat my number
    def random_repeat_my_number(self, number: int | float) -> list[int | float]:
        n_repeats = np.random.randint(1, 30)
        return [number] * n_repeats

    # Make it random
    def randomize(self, number: int | float) -> float:
        return np.random.rand()
