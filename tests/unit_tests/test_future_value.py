"""Unit tests for future value calculations."""

import pytest
from infrastructure_capital_planning.economics.future_value import (
    fv_single_cash_flow,
    fv_multiple_cash_flows,
    fv_uniform_recurring_series,
    fv_escalating_recurring_series,
)

def test_fv_single_cash_flow():
    assert pytest.approx(fv_single_cash_flow(100, 0.05, 1), 0.01) == 105.00

def test_fv_multiple_cash_flows():
    cash_flows = [(100, 1), (200, 2)]
    assert pytest.approx(fv_multiple_cash_flows(cash_flows, 0.05), 0.01) == 315.25

def test_fv_uniform_recurring_series():
    assert pytest.approx(fv_uniform_recurring_series(100, 0.05, 3), 0.01) == 315.25

def test_fv_escalating_recurring_series():
    assert pytest.approx(fv_escalating_recurring_series(100, 0.05, 0.02, 3), 0.01) == 321.55
