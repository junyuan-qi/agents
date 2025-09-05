import os
import time
from typing import Any

from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
from exa_py import Exa

# Load environment variables
load_dotenv('../.env')

# Initialize Exa client
exa = Exa(api_key=os.getenv("EXA_API_KEY"))
current_datetime = time.strftime("%Y-%m-%d %H:%M")


@function_tool
def exa_web_search(query: str) -> Any:
    """Perform a search query on the web with Exa, and retrieve relevant web data."""
    return exa.search_and_contents(query=query, type='auto', highlights=True)


# Create research agent with web search capabilities
agent = Agent(
    name="Research Assistant",
    instructions=(
        f"You are a helpful research assistant that can search the web for "
        f"information using the exa_web_search tool when needed. "
        f"Current date and time: {current_datetime}"
    ),
    tools=[exa_web_search]
)


# Run the agent
result = Runner.run_sync(agent, "Today's top news headlines of China")
print(result.final_output)
