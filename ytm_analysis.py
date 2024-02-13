from scipy.optimize import newton

def calculate_ytm(price, face_value, coupon_rate, years_to_maturity, frequency=1):
    """
    Calculate the Yield to Maturity (YTM) of a bond.
    :param price: Current market price of the bond
    :param face_value: Face value of the bond
    :param coupon_rate: Annual coupon rate as a decimal
    :param years_to_maturity: Number of years until bond matures
    :param frequency: Number of coupon payments per year
    :return: The YTM as a decimal
    """
    annual_coupon = coupon_rate * face_value
    coupon_payment = annual_coupon / frequency
    periods = years_to_maturity * frequency
    
    def ytm_func(r):
        total_payments = sum(coupon_payment / ((1 + r/frequency) ** t) for t in range(1, periods + 1))
        final_payment = face_value / ((1 + r/frequency) ** periods)
        return total_payments + final_payment - price
    
    return newton(ytm_func, coupon_rate)

