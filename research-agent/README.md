# Research Agent

A Python research assistant agent that can search the web for information using the Exa search API and OpenAI agents framework.
The assistant conducts multi-round searches to deepen its understanding and returns results in Chinese.

## Overview

This research agent leverages the power of web search to provide comprehensive information on various topics. It's built using:

- **Exa API**: For advanced web search capabilities with semantic understanding
- **OpenAI Agents Framework**: For intelligent agent behavior and function calling
- **Python 3.13**: Modern Python with type safety and performance improvements

## Installation

### Prerequisites

- Python 3.13 or higher
- An Exa API key (get one at [exa.ai](https://exa.ai))
- OpenAI API key

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd research-agent
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Set up environment variables:
   ```bash
   cp ../.env.example ../.env
   # Edit ../.env with your API keys:
   # EXA_API_KEY=your_exa_api_key_here
   # OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Run the research agent:

```bash
uv run python main.py
```

You will be prompted for a query, and the assistant will perform several rounds of web search before summarizing the findings in Chinese.

### Example Output

The agent will return comprehensive search results with:
- Relevant web content
- Highlighted key information
- Source links and metadata

## Dependencies

- **exa-py**: Web search API client
- **openai-agents**: OpenAI agents framework for function calling
- **python-dotenv**: Environment variable management
- **socksio**: SOCKS proxy support

### Development Dependencies

- **ruff**: Code linting and formatting
- **mypy**: Static type checking

## Development

### Environment

This project uses Python 3.13 with uv for dependency management. The virtual environment is automatically managed by uv.

### Code Quality

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and code formatting, and [MyPy](https://mypy.readthedocs.io/) for type checking.

#### Running the linter

```bash
# Run Ruff linter
uv run ruff check

# Run Ruff formatter
uv run ruff format

# Run MyPy type checker
uv run mypy .
```

#### Configuration

- **Ruff**: Configured in `pyproject.toml` with line length of 88 characters, targeting Python 3.13
- **MyPy**: Configured for Python 3.13 with strict type checking enabled

### Project Structure

```
research-agent/
├── main.py              # Main application entry point
├── pyproject.toml       # Project configuration and dependencies
├── README.md           # This file
└── .python-version     # Python version specification (3.13)
```