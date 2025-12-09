"""Calculator module with basic arithmetic operations."""


class Calculator:
    """A simple calculator class."""

    def __init__(self, initial_value=0):
        """Initialize calculator with an optional initial value."""
        self.value = initial_value

    def add(self, x):
        """Add a number to the current value."""
        self.value += x
        return self.value

    def subtract(self, x):
        """Subtract a number from the current value."""
        self.value -= x
        return self.value

    def multiply(self, x):
        """Multiply the current value by a number."""
        self.value *= x
        return self.value

    def divide(self, x):
        """Divide the current value by a number."""
        if x == 0:
            raise ValueError("Cannot divide by zero")
        self.value /= x
        return self.value

    def reset(self):
        """Reset the calculator value to zero."""
        self.value = 0
        return self.value

    def get_value(self):
        """Get the current value."""
        return self.value
