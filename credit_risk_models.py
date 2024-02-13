import numpy as np
from scipy.stats import norm

class MertonModel:
    def __init__(self, asset_value, debt_value, risk_free_rate, sigma_asset, time_to_maturity):
        """
        Initialize the Merton model for credit risk assessment.
        :param asset_value: Current total value of the firm's assets
        :param debt_value: Total value of the firm's debt/liabilities
        :param risk_free_rate: Risk-free interest rate
        :param sigma_asset: Volatility of the firm's assets
        :param time_to_maturity: Time to maturity of the debt
        """
        self.asset_value = asset_value
        self.debt_value = debt_value
        self.risk_free_rate = risk_free_rate
        self.sigma_asset = sigma_asset
        self.time_to_maturity = time_to_maturity

    def calculate_default_probability(self):
        """
        Calculate the probability of default using the Merton model.
        :return: Probability of default
        """
        d1 = (np.log(self.asset_value / self.debt_value) + (self.risk_free_rate + (self.sigma_asset ** 2) / 2) * self.time_to_maturity) / (self.sigma_asset * np.sqrt(self.time_to_maturity))
        d2 = d1 - self.sigma_asset * np.sqrt(self.time_to_maturity)
        default_probability = norm.cdf(-d2)
        return default_probability
