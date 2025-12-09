"""A simple Python package for demonstration."""

from .calculator import Calculator
from .utils import greet, format_result, is_even, factorial

__version__ = "0.1.0"
__all__ = ["Calculator", "greet", "format_result", "is_even", "factorial"]
