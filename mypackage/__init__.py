"""
MyPackage - an awesome scientific tool for data manipulations
"""

import pkgutil
import sys

# Shortcut imports
from mypackage.calculator import CalculatorMain, CalculatorAwesome, CalculatorRandom
from mypackage.printer import PrinterMain

__all__ = [
    "__version__",
    "version_info",
    "CalculatorMain",  # same as import shortcut
    "CalculatorAwesome",
    "CalculatorRandom",
    "PrinterMain",
]


# MyPackage version
__version__ = (pkgutil.get_data(__package__, "VERSION") or b"").decode("ascii").strip()
version_info = tuple(int(v) if v.isdigit() else v for v in __version__.split("."))


# Check minimum required Python version
if sys.version_info < (3, 11):
    print(f"Scrapy {__version__} requires Python 3.11+")
    sys.exit(1)


del pkgutil
del sys
