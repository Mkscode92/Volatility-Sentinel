import asyncio
import sys
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()

async def run_agent(user_question):
    client = MultiServerMCPClient(
        {
            "volatility_sentinel": {
                "command": sys.executable,
                "args": ["-m", "mcp_server.server"],
                "transport": "stdio",
            }
        }
    )
    tools = await client.get_tools()

    llm = ChatAnthropic(
        model="claude-sonnet-4-6",
        temperature=0.0,
    )
    agent = create_react_agent(llm, tools)

    response = await agent.ainvoke({"messages": user_question})
    print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(run_agent(
        "NVDA is trading at $100. What is the theoretical call option price "
        "with a strike of $110, 3 months to expiry, 5% risk-free rate, "
        "and 20% volatility? Use both Black-Scholes and Monte Carlo."
    ))
