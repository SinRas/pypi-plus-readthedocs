"""
Awesome calculator functionalitites.

See documentation in docs/topics/calculator.rst
"""


class CalculatorAwesome:
    """Awesome calculator with extra functionalities
    """
    # Constructor
    def __init__(self, name: str = 'CalculatorAwesomeName'):
        self.name = name
        return

    # Awesome repeat my number
    def awesome_repeat_my_number(self, number: int | float) -> list[int | float]:
        return [number] * 12

    # Make it awesome
    def awesomize(self, number: int | float) -> int | float:
        return number**2
