"""Tests for utility functions."""

import pytest
from mypackage.utils import greet, format_result, is_even, factorial


class TestGreet:
    """Test suite for greet function."""

    def test_greet_normal(self):
        """Test greeting with normal name."""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_empty_string(self):
        """Test greeting with empty string raises ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")

    def test_greet_with_spaces(self):
        """Test greeting with name containing spaces."""
        assert greet("John Doe") == "Hello, John Doe!"


class TestFormatResult:
    """Test suite for format_result function."""

    def test_format_result_default_precision(self):
        """Test formatting with default precision."""
        assert format_result(3.14159) == "3.14"

    def test_format_result_custom_precision(self):
        """Test formatting with custom precision."""
        assert format_result(3.14159, precision=3) == "3.142"

    def test_format_result_integer(self):
        """Test formatting an integer."""
        assert format_result(42, precision=2) == "42.00"

    def test_format_result_zero_precision(self):
        """Test formatting with zero precision."""
        assert format_result(3.14159, precision=0) == "3"

    def test_format_result_invalid_type(self):
        """Test formatting with non-numeric value raises TypeError."""
        with pytest.raises(TypeError, match="Value must be a number"):
            format_result("not a number")

    def test_format_result_negative_precision(self):
        """Test formatting with negative precision raises ValueError."""
        with pytest.raises(ValueError, match="Precision must be non-negative"):
            format_result(3.14, precision=-1)


class TestIsEven:
    """Test suite for is_even function."""

    def test_is_even_true(self):
        """Test even numbers return True."""
        assert is_even(2) is True
        assert is_even(0) is True
        assert is_even(-4) is True

    def test_is_even_false(self):
        """Test odd numbers return False."""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(-5) is False

    def test_is_even_non_integer(self):
        """Test non-integer input raises TypeError."""
        with pytest.raises(TypeError, match="Number must be an integer"):
            is_even(2.5)


class TestFactorial:
    """Test suite for factorial function."""

    def test_factorial_zero(self):
        """Test factorial of 0."""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of 1."""
        assert factorial(1) == 1

    def test_factorial_positive(self):
        """Test factorial of positive numbers."""
        assert factorial(5) == 120
        assert factorial(3) == 6
        assert factorial(4) == 24

    def test_factorial_negative(self):
        """Test factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)

    def test_factorial_non_integer(self):
        """Test factorial of non-integer raises TypeError."""
        with pytest.raises(TypeError, match="Input must be an integer"):
            factorial(3.5)
