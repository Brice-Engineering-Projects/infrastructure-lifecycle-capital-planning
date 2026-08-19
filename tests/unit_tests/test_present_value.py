"""Test present value calculations."""

import pytest
from infrastructure_capital_planning.economics.present_value import (
    pv_single_cash_flow,
    pv_uniform_recurring_series,
    pv_escalating_recurring_series,
)

def test_pv_single_cash_flow():
    assert pytest.approx(pv_single_cash_flow(100, 0.05, 1), 0.01) == 95.24

def test_pv_uniform_recurring_series():
    assert pytest.approx(pv_uniform_recurring_series(100, 0.05, 3), 0.01) == 272.32

def test_pv_escalating_recurring_series():
    assert pytest.approx(pv_escalating_recurring_series(100, 0.02, 0.05, 3), 0.01) == 268.24
