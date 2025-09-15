# Research Agent (TypeScript)

A TypeScript reimplementation of the Python research agent using the official `@openai/agents` SDK and Exa search. Provides a simple CLI chat interface; the agent searches the web and replies in Chinese.

## Prerequisites

- Node.js 22+
- pnpm 9+
- OpenAI API key (`OPENAI_API_KEY`)
- Exa API key (`EXA_API_KEY`)

Use the repo-level `.env` (copy from `.env.example` if needed) and add:

```
OPENAI_API_KEY=...
EXA_API_KEY=...
```

The app loads `../.env` relative to `research-agent-ts/src` so it reuses the repo root `.env`.

## Install

```bash
cd research-agent-ts
pnpm install
```

## Run (chat CLI)

```bash
pnpm dev
```

- You’ll see a prompt like: `Research Assistant chat. Type empty line to exit.`
- Type your message (English queries recommended for search); the agent replies in Chinese.
- Press Enter on an empty line to exit.

## Build

```bash
pnpm build
pnpm start
```

## Project Structure

```
research-agent-ts/
├── src/
│   ├── index.ts          # CLI chat; Agent + Exa tool
│   └── instructions.md   # System instructions template (Chinese output)
├── tsconfig.json
├── package.json
└── README.md
```
