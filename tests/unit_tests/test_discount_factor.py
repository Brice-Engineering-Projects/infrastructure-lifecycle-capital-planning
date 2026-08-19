"""Unit tests for discount factor calculations"""

import pytest
from infrastructure_capital_planning.economics.discount_factor import discount_factor

def test_discount_factor():
    # Test with a positive rate and period
    assert pytest.approx(discount_factor(0.05, 1), 0.0001) == 0.95238
    assert pytest.approx(discount_factor(0.05, 2), 0.0001) == 0.90703

    # Test with a zero rate
    assert discount_factor(0, 1) == 1.0
    assert discount_factor(0, 5) == 1.0

    # Test with a negative rate
    assert pytest.approx(discount_factor(-0.05, 1), 0.0001) == 1.05263
    assert pytest.approx(discount_factor(-0.05, 2), 0.0001) == 1.10803

    # Test with a zero period
    assert discount_factor(0.05, 0) == 1.0
