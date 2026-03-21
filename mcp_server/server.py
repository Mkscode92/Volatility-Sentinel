from mcp.server.fastmcp import FastMCP
from pricing.black_scholes import black_scholes
from pricing.monte_carlo import monte_carlo_price

mcp = FastMCP("Volatility Sentinel")

@mcp.tool()
def run_black_scholes(S: float, K: float, T: float, r: float, sigma: float, option_type: str = "call") -> dict:
    """
    Calculate theoretical option price using Black-Scholes.
    Returns price, delta, and vega.
    """
    # YOUR CODE HERE — one line

@mcp.tool()
def run_monte_carlo(S: float, K: float, T: float, r: float, sigma: float, option_type: str = "call", num_simulations: int = 10000) -> dict:
    """
    Price an option using Monte Carlo simulation.
    """
    # YOUR CODE HERE — one line

if __name__ == "__main__":
    mcp.run()
