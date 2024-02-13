import numpy as np
import matplotlib.pyplot as plt

class CoxIngersollRossModel:
    def __init__(self, r0, k, theta, sigma):
        self.r0 = r0
        self.k = k
        self.theta = theta
        self.sigma = sigma

    def simulate_short_rate(self, T, steps):
        dt = T / steps
        rates = [self.r0]
        for _ in range(steps - 1):
            rt = rates[-1]
            dr = self.k * (self.theta - rt) * dt + self.sigma * np.sqrt(max(rt, 0)) * np.random.normal() * np.sqrt(dt)
            rates.append(rt + dr)
        return rates
