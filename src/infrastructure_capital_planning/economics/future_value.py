"""Future value calculations."""

def fv_single_cash_flow(present_value: float, interest_rate: float, periods: int) -> float:
    """
    Calculate the future value of a single present cash flow.

    Parameters:
    present_value (float): The amount of money in the present.
    interest_rate (float): The interest rate (as a decimal).
    periods (int): The number of periods until the cash flow occurs.

    Returns:
    float: The future value of the present cash flow.
    """
    return present_value * ((1 + interest_rate) ** periods)

def fv_multiple_cash_flows(cash_flows: list, interest_rate: float) -> float:
    """
    Calculate the future value of multiple present cash flows.

    Parameters:
    cash_flows (list): A list of tuples, each containing (present_value, periods).
    interest_rate (float): The interest rate (as a decimal).

    Returns:
    float: The total future value of the present cash flows.
    """
    total_fv = 0.0
    for present_value, periods in cash_flows:
        total_fv += fv_single_cash_flow(present_value, interest_rate, periods)
    return total_fv

def fv_uniform_recurring_series(payment: float, interest_rate: float, periods: int) -> float:
    """
    Calculate the future value of a uniform recurring series of cash flows.

    Parameters:
    payment (float): The amount of each recurring payment.
    interest_rate (float): The interest rate (as a decimal).
    periods (int): The number of periods for the recurring payments.

    Returns:
    float: The future value of the uniform recurring series.
    """
    if interest_rate == 0:
        return payment * periods
    else:
        return payment * (((1 + interest_rate) ** periods - 1) / interest_rate)

def fv_escalating_recurring_series(initial_payment: float, escalation_rate: float, interest_rate: float, periods: int) -> float:
    """
    Calculate the future value of an escalating recurring series of cash flows.

    Parameters:
    initial_payment (float): The amount of the first payment.
    escalation_rate (float): The rate at which payments escalate (as a decimal).
    interest_rate (float): The interest rate (as a decimal).
    periods (int): The number of periods for the recurring payments.

    Returns:
    float: The future value of the escalating recurring series.
    """
    total_fv = 0.0
    for n in range(periods):
        payment = initial_payment * ((1 + escalation_rate) ** n)
        total_fv += fv_single_cash_flow(payment, interest_rate, periods - n)
    return total_fv
