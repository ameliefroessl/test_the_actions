"""Tests for the Calculator class."""

import pytest
from mypackage.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    def test_initial_value_default(self):
        """Test calculator initializes with zero by default."""
        calc = Calculator()
        assert calc.get_value() == 0

    def test_initial_value_custom(self):
        """Test calculator initializes with custom value."""
        calc = Calculator(10)
        assert calc.get_value() == 10

    def test_add(self):
        """Test addition operation."""
        calc = Calculator(5)
        result = calc.add(3)
        assert result == 8
        assert calc.get_value() == 8

    def test_subtract(self):
        """Test subtraction operation."""
        calc = Calculator(10)
        result = calc.subtract(4)
        assert result == 6
        assert calc.get_value() == 6

    def test_multiply(self):
        """Test multiplication operation."""
        calc = Calculator(5)
        result = calc.multiply(3)
        assert result == 15
        assert calc.get_value() == 15

    def test_divide(self):
        """Test division operation."""
        calc = Calculator(10)
        result = calc.divide(2)
        assert result == 5.0
        assert calc.get_value() == 5.0

    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        calc = Calculator(10)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(0)

    def test_reset(self):
        """Test reset operation."""
        calc = Calculator(100)
        calc.add(50)
        result = calc.reset()
        assert result == 0
        assert calc.get_value() == 0

    def test_chained_operations(self):
        """Test multiple operations in sequence."""
        calc = Calculator(10)
        calc.add(5)
        calc.multiply(2)
        calc.subtract(10)
        calc.divide(2)
        assert calc.get_value() == 10.0
