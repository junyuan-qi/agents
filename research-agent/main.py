import asyncio
import os
import time
from typing import Any

from agents import Agent, function_tool, run_demo_loop
from dotenv import load_dotenv
from exa_py import Exa

# Load environment variables
load_dotenv("../.env")

# Initialize Exa client
exa = Exa(api_key=os.getenv("EXA_API_KEY"))
current_datetime = time.strftime("%Y-%m-%d %H:%M")


@function_tool
def exa_web_search(query: str) -> Any:
    """Perform a search query on the web with Exa, and retrieve relevant web data."""
    return exa.search_and_contents(query=query, type="auto", highlights=True)


def load_prompt_from_file(file_path: str, variables: dict[str, Any]) -> str:
    """Load a prompt template from disk and substitute {{var}} placeholders.

    Raises if the file is missing or unreadable.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Instructions file not found: {file_path}") from e
    except OSError as e:
        raise OSError(f"Failed to read instructions file: {file_path}") from e

    for key, value in variables.items():
        content = content.replace(f"{{{{{key}}}}}", str(value))
    return content


async def main() -> None:
    # Create research agent with web search capabilities
    prompt_file_path = os.path.join(os.path.dirname(__file__), "instructions.md")
    instructions = load_prompt_from_file(
        prompt_file_path,
        {"current_datetime": current_datetime},
    )
    agent = Agent(
        name="Research Assistant",
        instructions=instructions,
        tools=[exa_web_search],
    )

    await run_demo_loop(agent)


if __name__ == "__main__":
    asyncio.run(main())
