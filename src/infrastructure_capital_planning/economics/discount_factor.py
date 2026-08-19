"""Discount factor calculations for economic analysis"""

def discount_factor(rate: float, period: int) -> float:
    """Calculate the discount factor for a given rate and period."""
    return 1 / (1 + rate) ** period
