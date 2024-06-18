"""
Base class for printing

See documentation in docs/topics/printer.rst
"""

from typing import Any
from icecream import ic


class PrinterMain:
    """Printer class made in init!
    """
    # Constructor
    def __init__(self, name: str = 'PrinterMainName'):
        self.name = name
        return

    # Repeat my number
    def shout(self, number: Any) -> None:
        msg = f"SHOUT!!!: {number}"
        ic(msg)
        return
