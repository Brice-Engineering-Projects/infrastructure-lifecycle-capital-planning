"""
Module for calculating the present value of future cash flows.
"""

def pv_single_cash_flow(future_value: float, discount_rate: float, periods: int) -> float:
    """
    Calculate the present value of a single future cash flow.

    Parameters:
    future_value (float): The amount of money in the future.
    discount_rate (float): The discount rate (as a decimal).
    periods (int): The number of periods until the cash flow occurs.

    Returns:
    float: The present value of the future cash flow.
    """
    return future_value / ((1 + discount_rate) ** periods)

def pv_multiple_cash_flows(cash_flows: list, discount_rate: float) -> float:
    """
    Calculate the present value of multiple future cash flows.

    Parameters:
    cash_flows (list): A list of tuples, each containing (future_value, periods).
    discount_rate (float): The discount rate (as a decimal).

    Returns:
    float: The total present value of the future cash flows.
    """
    total_pv = 0.0
    for future_value, periods in cash_flows:
        total_pv += pv_single_cash_flow(future_value, discount_rate, periods)
    return total_pv

def pv_uniform_recurring_series(payment: float, discount_rate: float, periods: int) -> float:
    """
    Calculate the present value of a uniform recurring series of cash flows.

    Parameters:
    payment (float): The amount of each recurring payment.
    discount_rate (float): The discount rate (as a decimal).
    periods (int): The number of periods for the recurring payments.

    Returns:
    float: The present value of the uniform recurring series.
    """
    if discount_rate == 0:
        return payment * periods
    else:
        return payment * ((1 - (1 + discount_rate) ** -periods) / discount_rate)

def pv_escalating_recurring_series(initial_payment: float, escalation_rate: float, discount_rate: float, periods: int) -> float:
    """
    Calculate the present value of an escalating recurring series of cash flows.

    Parameters:
    initial_payment (float): The amount of the first payment.
    escalation_rate (float): The rate at which payments escalate (as a decimal).
    discount_rate (float): The discount rate (as a decimal).
    periods (int): The number of periods for the recurring payments.

    Returns:
    float: The present value of the escalating recurring series.
    """
    total_pv = 0.0
    for period in range(periods):
        future_value = initial_payment * ((1 + escalation_rate) ** period)
        total_pv += pv_single_cash_flow(future_value, discount_rate, period + 1)
    return total_pv
