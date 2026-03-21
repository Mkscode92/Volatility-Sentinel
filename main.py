from pricing.monte_carlo import monte_carlo_price
from pricing.black_scholes import black_scholes

#testing shenanigans 
if __name__ == "__main__":
    price_call_monte = monte_carlo_price(S=100, K=110, T=0.25, r=0.05, sigma=0.20, option_type="call")
    price_put_monte = monte_carlo_price(S=100, K=110, T=0.25, r=0.05, sigma=0.20, option_type="put")

    call_values = black_scholes(S=100, K=110, T=0.25, r=0.05, sigma=0.20, option_type="call")
    put_values = black_scholes(S=100, K=110, T=0.25, r=0.05, sigma=0.20, option_type="put")

    print("Black Scholes\n")
    print(f"Call price: ${call_values["price"]}\nCall delta: ${call_values["delta"]}")
    print(f"Put price: ${put_values["price"]}\nPut delta: ${put_values["delta"]}")
    print(f"Vega: ${call_values["vega"]}")

    print("\nMonte Carlo\n")
    print(f"Call price: ${price_call_monte["price_call"]}")
    print(f"Put price: ${price_put_monte["price_put"]}")