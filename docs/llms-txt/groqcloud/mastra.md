# Source: https://console.groq.com/docs/mastra

---
description: Learn how to use Mastra with Groq to build production-ready AI agents, multi-step workflows, and MCP servers with built-in memory, observability, and deployment tools.
title: Mastra + Groq: Build Production AI Agents &amp; Workflows - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Mastra + Groq: Build Production AI Agents & Workflows](#mastra--groq-build-production-ai-agents--workflows)

[Mastra](https://mastra.ai) is a TypeScript framework for building production-ready AI applications with agents, workflows, and tools. Combined with Groq's fast inference, you can build sophisticated AI systems with built-in memory, observability, MCP support, and deployment capabilities.

**Key Features:**

* **Agent Framework:** Build intelligent agents with tools, memory, and guardrails
* **Workflow Engine:** Create multi-step workflows with branching, parallel execution, and error handling
* **MCP Support:** Both create MCP servers and connect to them as a client
* **Built-in Memory:** Thread-based memory with conversation history and semantic recall
* **RAG Integration:** Chunking, embedding, vector search, and retrieval out of the box
* **Observability:** AI tracing, logging, and monitoring with multiple exporters
* **Production Ready:** Deploy to any platform with built-in server and deployment tools

## [Quick Start](#quick-start)

#### [1\. Create a new Mastra project:](#1-create-a-new-mastra-project)

curl

```
npx create-mastra@latest my-app
cd my-app
```

#### [2\. Install Groq integration:](#2-install-groq-integration)

curl

```
npm install @ai-sdk/groq
```

#### [3\. Set your Groq API key:](#3-set-your-groq-api-key)

curl

```
export GROQ_API_KEY="your-groq-api-key"
```

#### [4\. Create your first Groq-powered agent:](#4-create-your-first-groqpowered-agent)

TypeScript

```
import { Agent } from '@mastra/core';
import { createGroq } from '@ai-sdk/groq';

const groq = createGroq({
  apiKey: process.env.GROQ_API_KEY,
});

export const researchAgent = new Agent({
  name: 'Research Assistant',
  instructions: 'You are a helpful research assistant that provides accurate, well-sourced information.',
  model: {
    provider: groq,
    name: 'llama-3.3-70b-versatile',
    toolChoice: 'auto',
  },
});
```

#### [5\. Use the agent:](#5-use-the-agent)

TypeScript

```
import { Mastra } from '@mastra/core';
import { researchAgent } from './mastra/agents';

const mastra = new Mastra({
  agents: { researchAgent },
});

const result = await mastra
  .getAgent('researchAgent')
  .generate('What are the latest developments in AI inference optimization?');

console.log(result.text);
```

## [Advanced Examples](#advanced-examples)

### [Agent with Tools](#agent-with-tools)

Create agents that can use tools with Groq's fast inference:

TypeScript

```
import { Agent } from '@mastra/core';
import { createTool } from '@mastra/core/tools';
import { createGroq } from '@ai-sdk/groq';
import { z } from 'zod';

const groq = createGroq({ apiKey: process.env.GROQ_API_KEY });

const weatherTool = createTool({
  id: 'get_weather',
  description: 'Get current weather for a location',
  inputSchema: z.object({
    location: z.string().describe('City name'),
  }),
  execute: async ({ context }) => {
    // API call to weather service
    return `Weather in ${context.location}: 72°F, sunny`;
  },
});

export const weatherAgent = new Agent({
  name: 'Weather Assistant',
  instructions: 'You help users get weather information.',
  model: {
    provider: groq,
    name: 'llama-3.3-70b-versatile',
  },
  tools: { weatherTool },
});
```

### [Multi-Step Workflows](#multistep-workflows)

Build complex workflows with Groq-powered steps:

TypeScript

```
import { Workflow, Step } from '@mastra/core';
import { z } from 'zod';

const searchStep = new Step({
  id: 'search',
  execute: async ({ context }) => {
    // Search for information
    return { results: ['result1', 'result2', 'result3'] };
  },
});

const analyzeStep = new Step({
  id: 'analyze',
  execute: async ({ context, mastra }) => {
    const agent = mastra.getAgent('researchAgent');
    const analysis = await agent.generate(
      `Analyze these search results: ${context.results.join(', ')}`
    );
    return { analysis: analysis.text };
  },
});

const summarizeStep = new Step({
  id: 'summarize',
  execute: async ({ context, mastra }) => {
    const agent = mastra.getAgent('researchAgent');
    const summary = await agent.generate(
      `Summarize this analysis: ${context.analysis}`
    );
    return { summary: summary.text };
  },
});

export const researchWorkflow = new Workflow({
  name: 'research-workflow',
  triggerSchema: z.object({
    query: z.string(),
  }),
});

researchWorkflow
  .step(searchStep)
  .then(analyzeStep)
  .then(summarizeStep)
  .commit();
```

### [Agent with Memory](#agent-with-memory)

Add conversation memory to your agents:

TypeScript

```
import { Agent } from '@mastra/core';
import { createGroq } from '@ai-sdk/groq';

const groq = createGroq({ apiKey: process.env.GROQ_API_KEY });

export const chatAgent = new Agent({
  name: 'Chat Assistant',
  instructions: 'You are a helpful assistant that remembers context.',
  model: {
    provider: groq,
    name: 'llama-3.3-70b-versatile',
  },
  enableMemory: true,
});

// Use with thread-based memory
const result = await chatAgent.generate(
  'What did we discuss earlier?',
  {
    threadId: 'user-123',
    resourceId: 'conversation-1',
  }
);
```

### [Creating an MCP Server](#creating-an-mcp-server)

Build your own MCP server with Mastra:

TypeScript

```
import { MCPServer } from '@mastra/mcp';
import { createTool } from '@mastra/core/tools';
import { z } from 'zod';

const notesTool = createTool({
  id: 'create_note',
  description: 'Create a new note',
  inputSchema: z.object({
    title: z.string(),
    content: z.string(),
  }),
  execute: async ({ context }) => {
    // Save note to database
    return `Note created: ${context.title}`;
  },
});

export const mcpServer = new MCPServer({
  name: 'Notes Server',
  version: '1.0.0',
  tools: { notesTool },
});

// Start the server
await mcpServer.start();
```

### [Connecting to MCP Servers](#connecting-to-mcp-servers)

Use external MCP servers in your agents:

TypeScript

```
import { Agent } from '@mastra/core';
import { MCPClient } from '@mastra/mcp';
import { createGroq } from '@ai-sdk/groq';

const groq = createGroq({ apiKey: process.env.GROQ_API_KEY });

const exaClient = new MCPClient({
  name: 'exa',
  serverUrl: `https://mcp.exa.ai/mcp?exaApiKey=${process.env.EXA_API_KEY}`,
});

const exaTools = await exaClient.getTools();

export const searchAgent = new Agent({
  name: 'Search Agent',
  instructions: 'You help users search the web for information.',
  model: {
    provider: groq,
    name: 'llama-3.3-70b-versatile',
  },
  tools: exaTools,
});
```

## [Agent Features](#agent-features)

### [Streaming Responses](#streaming-responses)

Stream agent responses for real-time feedback:

TypeScript

```
const stream = await researchAgent.stream(
  'Explain quantum computing',
  { threadId: 'user-123' }
);

for await (const chunk of stream) {
  if (chunk.type === 'text-delta') {
    process.stdout.write(chunk.textDelta);
  }
}
```

### [Agent Networks](#agent-networks)

Create multi-agent systems with supervisor patterns:

TypeScript

```
import { Agent } from '@mastra/core';

const researcher = new Agent({ /* ... */ });
const writer = new Agent({ /* ... */ });
const editor = new Agent({ /* ... */ });

const supervisor = new Agent({
  name: 'Supervisor',
  model: { provider: groq, name: 'llama-3.3-70b-versatile' },
});

const result = await supervisor.network({
  agents: [researcher, writer, editor],
  prompt: 'Write a research article about AI',
  maxTurns: 5,
});
```

### [Guardrails](#guardrails)

Add safety checks to agent outputs:

TypeScript

```
import { Agent } from '@mastra/core';

export const safeAgent = new Agent({
  name: 'Safe Agent',
  model: { provider: groq, name: 'llama-3.3-70b-versatile' },
  guardrails: {
    input: [
      {
        check: (input: string) => !input.includes('harmful'),
        message: 'Input contains harmful content',
      },
    ],
    output: [
      {
        check: (output: string) => output.length < 1000,
        message: 'Output too long',
      },
    ],
  },
});
```

## [Workflow Features](#workflow-features)

### [Parallel Execution](#parallel-execution)

Run multiple steps simultaneously:

TypeScript

```
workflow
  .parallel([step1, step2, step3])
  .then(combineResults)
  .commit();
```

### [Conditional Branching](#conditional-branching)

Add conditional logic to workflows:

TypeScript

```
workflow
  .step(checkCondition)
  .branch({
    when: (context) => context.needsApproval,
    then: [requestApproval, processApproval],
    else: [autoProcess],
  })
  .commit();
```

### [Error Handling](#error-handling)

Handle errors gracefully:

TypeScript

```
const step = new Step({
  id: 'risky-operation',
  execute: async ({ context }) => {
    // Operation that might fail
  },
  retryConfig: {
    maxRetries: 3,
    delayMs: 1000,
  },
});
```

## [Deployment](#deployment)

Mastra provides deployment tools for various platforms:

curl

```
# Deploy to Vercel
npm run mastra deploy -- --platform vercel

# Deploy to Cloudflare Workers
npm run mastra deploy -- --platform cloudflare

# Deploy to AWS Lambda
npm run mastra deploy -- --platform aws-lambda
```

Or use the built-in server:

TypeScript

```
import { Mastra } from '@mastra/core';
import { agents } from './mastra/agents';
import { workflows } from './mastra/workflows';

const mastra = new Mastra({
  agents,
  workflows,
});

const server = mastra.getServer();

server.listen(3000, () => {
  console.log('Mastra server running on port 3000');
});
```

**Challenge:** Build a multi-agent research system that uses Groq for fast inference, coordinates multiple specialized agents (researcher, analyst, writer), maintains conversation memory, and generates comprehensive reports with proper citations!

## [Additional Resources](#additional-resources)

* [Mastra Documentation](https://mastra.ai/en/docs)
* [Mastra Examples](https://mastra.ai/en/examples)
* [Mastra API Reference](https://mastra.ai/en/reference)
* [Mastra MCP Server Guide](https://mastra.ai/en/reference/tools/mcp-server)
* [Mastra GitHub](https://github.com/mastra-ai/mastra)
* [Groq with Vercel AI SDK](https://sdk.vercel.ai/providers/ai-sdk-providers/groq)