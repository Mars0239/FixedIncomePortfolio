import numpy as np
from scipy.optimize import minimize

def portfolio_return(weights, returns):
    return np.dot(weights, returns)

def portfolio_volatility(weights, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

def optimize_portfolio(returns, cov_matrix, risk_free_rate):
    num_assets = len(returns)
    
    # Objective function (negative Sharpe ratio)
    def min_func_sharpe(weights, returns, cov_matrix, risk_free_rate):
        # 计算组合回报
        port_return = portfolio_return(weights, returns)
        # 计算组合波动率
        port_volatility = portfolio_volatility(weights, cov_matrix)
        # 计算夏普比率
        sharpe_ratio = (port_return - risk_free_rate) / port_volatility
        # 最小化负夏普比率
        return -sharpe_ratio

    # 约束条件：所有权重之和等于1
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    
    # 权重范围在0和1之间
    bounds = tuple((0, 1) for asset in range(num_assets))
    
    # 初始权重猜测
    initial_weights = num_assets * [1. / num_assets,]
    
    # 最小化负夏普比率
    result = minimize(min_func_sharpe, initial_weights, args=(returns, cov_matrix, risk_free_rate), method='SLSQP', bounds=bounds, constraints=constraints)
    
    return result.x
