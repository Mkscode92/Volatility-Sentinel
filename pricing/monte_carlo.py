import numpy as np
import math 
def monte_carlo_price(S, K, T, r, sigma, option_type="call", num_simulations=10000):
    """
    Price a European option using Monte Carlo simulation.
    Simulate `num_simulations` possible end prices for the stock,
    calculate the payoff for each, discount back to present value.
    """
    Z = np.random.standard_normal(num_simulations)
    end_prices = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option_type == "call": 
            payoffs = np.maximum(end_prices - K, 0)
    elif option_type == "put":
            payoffs = np.maximum(K - end_prices, 0) 
    
    #discounting the average payoff to get the price 
    price = math.exp(-r * T) * float(payoffs.mean())

    return {f'price_{option_type}': round(price, 4)}

if __name__ == "__main__":
    price_call_monte = monte_carlo_price(S=100, K=110, T=0.25, r=0.05, sigma=0.20, option_type="call")
    price_put_monte = monte_carlo_price(S=100, K=110, T=0.25, r=0.05, sigma=0.20, option_type="put")

    print("\nMonte Carlo\n")
    print(f"Call price: ${price_call_monte["price_call"]}")
    print(f"Put price: ${price_put_monte["price_put"]}")







