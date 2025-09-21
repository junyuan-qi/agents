# Agents

This repository is dedicated to developing and experimenting with multiple personal agents to assist with various tasks. The goal is to create, test, and compare different agent frameworks and implementations for productivity, creativity, and personal management.

## Planned Agents

- **Writing Agent**: Assists with drafting, editing, and organizing written content.
- **Time Management Agent**: Helps schedule tasks, set reminders, and optimize daily routines.
- **Brainstorming Agent**: Facilitates idea generation and creative thinking sessions.
- **Other Agents**: Additional agents for research, learning, automation, and more.

## Agent Frameworks

Both agents run on the OpenAI Agent SDK, giving them a shared runtime for
tooling, memory, and safety policies. `research-agent` (Python) wires the SDK
into a CLI loop with project-specific prompts, and `research-agent-ts`
implements the same flow in TypeScript for parity. We plan to evaluate other
frameworks (LangChain, AutoGen, Haystack, etc.) alongside the SDK in future
experiments.

## Repository Structure

- Each agent will have its own directory with documentation, code, and usage instructions.
- Framework-specific experiments will be organized for easy comparison.

## Getting Started

1. Clone the repository:
	```bash
	git clone https://github.com/junyuan-qi/agents.git
	```
2. Explore agent directories for setup and usage instructions.
3. Refer to individual agent README files for details.

## Contributing

Feel free to suggest new agent ideas, frameworks, or improvements via issues or pull requests.

## License

[MIT License](LICENSE)
