import math
from scipy.stats import norm #because its continuous 


def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the theoretical price of a European option.

    Parameters:
        S     : Current stock price
        K     : Strike price
        T     : Time to expiration in years (e.g. 90 days = 90/365)
        r     : Risk-free interest rate (e.g. 0.05 for 5%)
        sigma : Volatility of the underlying asset (e.g. 0.20 for 20%)
        option_type : "call" or "put"

    Returns:
        Theoretical option price (float)
    """

    # d1 and d2 are intermediate values the formula needs.
    # Think of d1 as "how far in the money are we, adjusted for time and vol"
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

    # d2 is d1 shifted back by one standard deviation over time
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        # N(d1), N(d2) = probability values from the normal distribution
        # Intuitively: probability the option ends up profitable
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)

    elif option_type == "put":
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        delta = norm.cdf(d1) - 1 

    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    vega = S * norm.pdf(d1) * math.sqrt(T)

    return {"price": round(option_price, 4), "delta" : round(delta, 4), "vega" : round(vega, 4)}


if __name__ == "__main__":
    # NVDA example: stock at $100, strike $110, 3 months out, 5% rate, 20% vol
    call_values = black_scholes(S=100, K=110, T=0.25, r=0.05, sigma=0.50, option_type="call")
    put_values  = black_scholes(S=100, K=110, T=0.25, r=0.05, sigma=0.50, option_type="put")

    print(f"Call price: ${call_values["price"]}\nCall delta: ${call_values["delta"]}")
    print(f"Put price: ${put_values["price"]}\nPut delta: ${put_values["delta"]}")
    print(f"Vega: ${call_values["vega"]}")
