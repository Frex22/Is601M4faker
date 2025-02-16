"""
Parametrized tests for the Operations class.
"""

import pytest
from app.operations import Operations  # Adjust this import if needed

def test_addition(a, b, operation, expected):
    """
    Test that addition of a and b returns the expected sum.
    """
    result = Operations.addition(a, b)
    assert result == expected

def test_subtraction(a, b, operation, expected):
    """
    Test that subtraction of b from a returns the expected difference.
    """
    result = Operations.subtraction(a, b)
    assert result == expected

def test_multiplication(a, b, operation, expected):
    """
    Test that multiplication of a and b returns the expected product.
    """
    result = Operations.multiplication(a, b)
    assert result == expected

def test_division(a, b, operation, expected):
    """
    Test that division of a by b returns the expected quotient.
    """
    result = Operations.division(a, b)
    assert result == expected

def test_division_by_zero():
    """
    Test that dividing by zero raises a ValueError with the correct message.
    """
    with pytest.raises(ValueError, match="Division By zero is not allowed."):
        Operations.division(5, 0)
