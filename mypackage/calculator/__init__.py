"""
Base class for calculators

See documentation in docs/topics/calculator.rst
"""


class CalculatorMain:
    """Calculator class created from init!
    """
    # Constructor
    def __init__(self, name: str = 'CalculatorMainName'):
        self.name = name
        return

    # Repeat my number
    def repeat_my_number(self, number: int | float) -> list[int | float]:
        return [number] * 5


# Imports from Calculator main
from mypackage.calculator.awesomulator import CalculatorAwesome
from mypackage.calculator.randomulator import CalculatorRandom
