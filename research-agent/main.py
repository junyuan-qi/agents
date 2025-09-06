import asyncio
import os
import time
from typing import Any

from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
from exa_py import Exa
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt

# Load environment variables
load_dotenv("../.env")

# Initialize Exa client
exa = Exa(api_key=os.getenv("EXA_API_KEY"))
current_datetime = time.strftime("%Y-%m-%d %H:%M")


@function_tool
def exa_web_search(query: str) -> Any:
    """Perform a search query on the web with Exa, and retrieve relevant web data."""
    return exa.search_and_contents(query=query, type="auto", highlights=True)


async def main() -> None:
    console = Console()

    # Display welcome message
    console.print(
        Panel.fit(
            "[bold blue]Research Assistant[/bold blue]\nPowered by Exa Search API",
            title="🔍 Welcome",
        )
    )

    query = Prompt.ask("\n[bold cyan]Enter your research query[/bold cyan]")

    # Create research agent with web search capabilities
    agent = Agent(
        name="Research Assistant",
        instructions=(
            f"You are a helpful research assistant that can search the web for "
            f"information using the exa_web_search tool when needed. "
            f"After reviewing initial results, decide on follow-up searches to gather "
            f"more information, performing two to three rounds and up to ten if "
            f"necessary. Provide comprehensive, well-structured responses in markdown, "
            f"and answer in Chinese. Current date and time: {current_datetime}"
        ),
        tools=[exa_web_search],
    )

    # Show processing message
    with console.status("[bold green]Researching your query...", spinner="dots"):
        result = await Runner.run(agent, query, max_turns=10)

    # Display results with rich formatting
    console.print(
        Panel.fit(
            Markdown(result.final_output),
            title="Research Results",
            border_style="green",
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
