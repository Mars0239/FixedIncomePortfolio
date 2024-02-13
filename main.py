# Import the previously defined modules
from interest_rate_models import CoxIngersollRossModel
from credit_risk_models import MertonModel
from ytm_analysis import calculate_ytm
from dcf_models import calculate_dcf
from portfolio_optimization import optimize_portfolio
import matplotlib.pyplot as plt

def main():
    print("Fixed Income Portfolio Analysis")
    print("Choose the analysis you want to perform:")
    print("1. Interest Rate Model (CIR)")
    print("2. Credit Risk Model (Merton)")
    print("3. Yield to Maturity (YTM)")
    print("4. Discounted Cash Flow (DCF)")
    print("5. Portfolio Optimization")
    choice = input("Enter your choice (1-5): ")


    
    if choice == '1':
        print("\nInterest Rate Model (Cox-Ingersoll-Ross) selected.")
        print("This model simulates the future evolution of interest rates.")
        print("Please provide parameters for the model:\n")

        print("Initial short rate (r0): The starting level of the interest rate.")
        r0 = float(input("Enter initial short rate (r0), e.g., 1 for 1%: "))

        print("\nSpeed of mean reversion (k): This parameter controls how quickly the interest rate reverts to the mean level.")
        k = float(input("Enter speed of mean reversion (k), e.g., 2: "))

        print("\nLong-term mean level (theta): The level to which the interest rate reverts over time.")
        theta = float(input("Enter long-term mean level (theta), e.g., 3 for 3%: "))

        print("\nVolatility of interest rate (sigma): This parameter controls the degree of fluctuation in the interest rates.")
        sigma = float(input("Enter volatility of interest rate (sigma), e.g., 4: "))
    
        print("\nTime horizon for the simulation (T): The total time period for the interest rate simulation, in years.")
        T = float(input("Enter the time horizon for the simulation (T, in years), e.g., 5: "))
    
        print("\nNumber of steps in the simulation: This determines how many data points will be simulated within the time horizon.")
        steps = int(input("Enter the number of steps in the simulation, e.g., 12: "))
    
        cir_model = CoxIngersollRossModel(r0, k, theta, sigma)
        rates = cir_model.simulate_short_rate(T, steps)

        plt.figure(figsize=(10, 6))
        plt.plot(rates)
        plt.title("Simulated Interest Rate Path - Cox-Ingersoll-Ross Model")
        plt.xlabel("Time Steps")
        plt.ylabel("Interest Rate")
        plt.show()
        print("\nSimulated short rate path:")
        for rate in rates:
            print(rate)
        print("\nSimulated short rate path (first few rates):")
        print(rates[:min(10, len(rates))])  
            
    elif choice == '2':
        print("\nCredit Risk Model (Merton) selected.")
        print("This model estimates the default probability of a firm based on its asset value, debt level, and other factors.")
        print("Please provide parameters for the Merton model:\n")

        print("Current total value of the firm's assets: This is the market value of all assets owned by the firm.")
        asset_value = float(input("Enter the current total value of the firm's assets, e.g., 1000000 for 1M: "))
        
        print("\nTotal value of the firm's debt/liabilities: The total amount of debt the firm needs to repay.")
        debt_value = float(input("Enter the total value of the firm's debt/liabilities, e.g., 500000 for 500K: "))
        
        print("\nRisk-free interest rate: The interest rate of a risk-free asset, typically government bonds.")
        risk_free_rate = float(input("Enter the risk-free interest rate as a decimal, e.g., 0.03 for 3%: "))
        
        print("\nVolatility of the firm's assets: This measures the degree of variation of the asset values.")
        sigma_asset = float(input("Enter the volatility of the firm's assets as a decimal, e.g., 0.2 for 20%: "))
        
        print("\nTime to maturity of the debt: The time until the firm's debt reaches its maturity date, in years.")
        time_to_maturity = float(input("Enter the time to maturity of the debt (in years), e.g., 5: "))
        
        merton_model = MertonModel(asset_value, debt_value, risk_free_rate, sigma_asset, time_to_maturity)
        default_probability = merton_model.calculate_default_probability()

        print(f"\nCalculated default probability: {default_probability:.4f}")
        
    elif choice == '3':
        print("\nYield to Maturity (YTM) Analysis selected.")
        print("This analysis calculates the total return anticipated on a bond if the bond is held until its maturity date.")
        print("Please provide parameters for the YTM calculation:\n")
        
        print("Current market price of the bond: The price at which the bond is currently trading in the market.")
        price = float(input("Enter the current market price of the bond, e.g., 950 for $950: "))
        
        print("\nFace value of the bond: The amount the bond issuer will pay the bondholder at maturity.")
        face_value = float(input("Enter the face value of the bond, e.g., 1000 for $1000: "))
        
        print("\nAnnual coupon rate: The interest rate the bond issuer will pay on the face value of the bond, expressed as a percentage.")
        coupon_rate = float(input("Enter the annual coupon rate as a decimal, e.g., 0.05 for 5%: "))
        
        print("\nNumber of years until the bond matures: The time remaining until the bond's maturity date.")
        years_to_maturity = float(input("Enter the number of years until the bond matures, e.g., 10: "))
        
        print("\nNumber of coupon payments per year: Indicates how often interest payments are made.")
        frequency = int(input("Enter the number of coupon payments per year, e.g., 2 for semi-annually: "))

        ytm = calculate_ytm(price, face_value, coupon_rate, years_to_maturity, frequency)
        
        print(f"\nCalculated Yield to Maturity (YTM): {ytm:.4f}")
        
    elif choice == '4':
        print("\nDiscounted Cash Flow (DCF) Analysis selected.")
        print("This analysis estimates the value of an investment based on its expected future cash flows, adjusted for the time value of money.")
        print("Please provide parameters for the DCF calculation:\n")

        print("Number of expected cash flows: This includes all future cash inflows and outflows associated with the investment.")
        cash_flows_count = int(input("Enter the number of expected cash flows, e.g., 5 for five years of cash flows: "))
        
        cash_flows = []
        for i in range(cash_flows_count):
            print(f"\nCash flow for year {i + 1}: Enter the net cash flow for year {i + 1}. Use negative values for outflows.")
            cash_flow = float(input(f"Enter cash flow for year {i + 1}, e.g., 100 for $100 inflow or -50 for $50 outflow: "))
            cash_flows.append(cash_flow)

        print("\nDiscount rate: The rate used to discount future cash flows back to their present value. Reflects the investment's risk and the time value of money.")
        discount_rate = float(input("Enter the discount rate as a decimal, e.g., 0.1 for 10%: "))
        dcf_value = calculate_dcf(cash_flows, discount_rate)
        
        print(f"\nCalculated DCF Value: {dcf_value:.2f}")
        
    elif choice == '5':
        print("\nPortfolio Optimization selected.")
        print("This section helps you to find the optimal weights of assets in your portfolio to maximize the Sharpe ratio.")
        num_assets = int(input("\nEnter the number of assets in the portfolio: "))
        
        print("\nFor each asset, you will enter its expected return. This is the mean return you expect to receive.")
        returns = []
        for i in range(num_assets):
            asset_return = float(input(f"Enter the expected return for asset {i + 1} as a decimal (e.g., 0.1 for 10%): "))
            returns.append(asset_return)
        
        print("\nEnter the covariance matrix for the asset returns.")
        print("The covariance matrix represents the covariance between returns of the assets.")
        print("For a portfolio with 2 assets, enter 4 values: var1 covar12 covar21 var2")
        cov_matrix = []
        for i in range(num_assets):
            row = input(f"Enter row {i + 1} of the covariance matrix, separated by spaces: ").split()
            cov_matrix.append([float(x) for x in row])
        
        risk_free_rate = float(input("\nEnter the risk-free rate as a decimal (e.g., 0.03 for 3%). This is the return of a risk-free asset: "))
        
        optimal_weights = optimize_portfolio(returns, cov_matrix, risk_free_rate)
        
        print("\nOptimal asset weights:")
        for i, weight in enumerate(optimal_weights):
            print(f"Asset {i + 1}: {weight:.4f}")
        
    else:
        print("Invalid choice. Please select a number between 1-5.")

if __name__ == "__main__":
    main()
