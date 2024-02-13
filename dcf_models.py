def calculate_dcf(cash_flows, discount_rate):
    """
    Calculate the Discounted Cash Flow (DCF) value of an investment.
    :param cash_flows: List of expected cash flows, where cash_flows[0] is the initial investment amount
                       and cash_flows[1:] are the cash flows in subsequent periods.
    :param discount_rate: The discount rate to apply to future cash flows.
    :return: The DCF value of the investment.
    """
    dcf_value = sum(cash_flow / ((1 + discount_rate) ** i) for i, cash_flow in enumerate(cash_flows))
    return dcf_value
