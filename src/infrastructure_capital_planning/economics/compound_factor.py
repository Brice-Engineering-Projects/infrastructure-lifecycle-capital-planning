"""Calculate the compound factor for a given rate and period."""

def compound_factor(rate: float, period: int) -> float:
    """Calculate the compound factor for a given rate and period."""
    return (1 + rate) ** period
