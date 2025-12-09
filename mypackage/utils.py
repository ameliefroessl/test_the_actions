"""Utility functions for the package."""


def greet(name):
    """Return a greeting message."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


def format_result(value, precision=2):
    """Format a numeric result with specified precision."""
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if precision < 0:
        raise ValueError("Precision must be non-negative")
    return f"{value:.{precision}f}"


def is_even(number):
    """Check if a number is even."""
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")
    return number % 2 == 0


def factorial(n):
    """Calculate factorial of a non-negative integer."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
