import dotenv from 'dotenv';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import { z } from 'zod';
import Exa from 'exa-js';
import { Agent, run, tool, user } from '@openai/agents';
import readline from 'readline/promises';
import { stdin as input, stdout as output } from 'node:process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load env from repo root (../.env relative to this file in dist/src)
dotenv.config({ path: path.resolve(__dirname, '../../.env') });

function nowLocal(): string {
  const d = new Date();
  const pad = (n: number) => n.toString().padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

async function loadInstructions(): Promise<string> {
  const file = path.resolve(__dirname, 'instructions.md');
  const raw = await fs.readFile(file, 'utf-8');
  return raw.split('{{current_datetime}}').join(nowLocal());
}

async function main() {
  if (!process.env.OPENAI_API_KEY) {
    throw new Error('Missing OPENAI_API_KEY');
  }
  if (!process.env.EXA_API_KEY) {
    throw new Error('Missing EXA_API_KEY');
  }

  const instructions = await loadInstructions();

  // Exa client
  const exa = new Exa(process.env.EXA_API_KEY);

  // Minimal tool per @openai/agents docs
  const exaWebSearch = tool({
    name: 'exa_web_search',
    description: 'Perform a web search via Exa and return relevant results',
    parameters: z.object({ query: z.string() }),
    execute: async (input) => {
      return exa.searchAndContents(input.query, { text: { maxCharacters: 3000 } });
    },
  });

  const agent = new Agent({
    name: 'Research Assistant',
    instructions,
    tools: [exaWebSearch],
  });

  // CLI chat loop similar to examples/basic/chat.ts
  const rl = readline.createInterface({ input, output });
  console.log('Research Assistant chat. Type empty line to exit.');

  let history: any[] = [];
  while (true) {
    const line = await rl.question('You: ');
    if (!line.trim()) break;

    const turnInput = [...history, user(line)];
    const result: any = await run(agent, turnInput);
    const text = result?.finalOutput ?? '';
    console.log(`Agent: ${text}`);
    history = result?.state?.history ?? turnInput;
  }
  rl.close();
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
