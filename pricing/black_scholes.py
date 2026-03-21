import math
from scipy.stats import norm #because its continuous stat 200 reference heh


def black_scholes(S, K, T, r, sigma, option_type="call"):
    #Calculate the theoretical price of a European option.
    # d1 and d2 are intermediate values the formula needs.
    # Think of d1 as "how far in the money are we, adjusted for time and vol"
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        # N(d1), N(d2) = probability values from the normal distribution
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
    call_values = black_scholes(S=100, K=110, T=0.25, r=0.05, sigma=0.50, option_type="call")
    put_values  = black_scholes(S=100, K=110, T=0.25, r=0.05, sigma=0.50, option_type="put")

    print(f"Call price: ${call_values["price"]}\nCall delta: ${call_values["delta"]}")
    print(f"Put price: ${put_values["price"]}\nPut delta: ${put_values["delta"]}")
    print(f"Vega: ${call_values["vega"]}")
