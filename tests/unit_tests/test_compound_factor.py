"""Unit tests for the compound_factor function."""

import pytest
from infrastructure_capital_planning.economics.compound_factor import compound_factor


def test_compound_factor():
    # Test with a positive rate and period
    assert pytest.approx(compound_factor(0.05, 1), 0.0001) == 1.05
    assert pytest.approx(compound_factor(0.05, 2), 0.0001) == 1.1025

    # Test with a zero rate
    assert compound_factor(0, 1) == 1.0
    assert compound_factor(0, 5) == 1.0

    # Test with a negative rate
    assert pytest.approx(compound_factor(-0.05, 1), 0.0001) == 0.95
    assert pytest.approx(compound_factor(-0.05, 2), 0.0001) == 0.9025

    # Test with a zero period
    assert compound_factor(0.05, 0) == 1.0
