# Research Agent (TypeScript)

A TypeScript reimplementation of the Python research agent using the OpenAI Agents JS SDK and Exa search. The assistant performs web searches and synthesizes results in Chinese.

## Prerequisites

- Node.js 18+
- pnpm 9+
- OpenAI API key (`OPENAI_API_KEY`)
- Exa API key (`EXA_API_KEY`)

Use the existing repo-level `.env` (copy from `.env.example` if needed) and add:

```
OPENAI_API_KEY=...
EXA_API_KEY=...
```

## Install

```bash
cd research-agent-ts
pnpm install
```

## Run (dev)

```bash
pnpm dev
```

You’ll get an interactive prompt. Type a query in English; the agent will use the `exa_web_search` tool and respond in Chinese.

## Build

```bash
pnpm build
pnpm start
```

## Project Structure

```
research-agent-ts/
├── src/
│   ├── index.ts            # CLI runner and agent wiring
│   ├── instructions.md     # System instruction template
│   └── tools/
│       └── exa.ts          # Exa web search tool (def + impl)
├── tsconfig.json
├── package.json
└── README.md
```

