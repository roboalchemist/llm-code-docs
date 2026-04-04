# Source: https://docs.augmentcode.com/cli/sdk-typescript.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TypeScript SDK

> Build custom integrations and agents using the Auggie TypeScript SDK.

## About

The Auggie TypeScript SDK provides a programmatic interface to Auggie for building custom integrations and agents in Node.js and TypeScript applications.

The SDK offers two main interfaces:

1. **Agent Interaction (ACP)** - Launch and communicate with a local Auggie agent process
2. **AI SDK Provider** - Use Augment as a language model provider with Vercel's AI SDK (API-only, no local installation required)

## Installation

```sh  theme={null}
npm install @augmentcode/auggie-sdk
```

## Agent Interaction (ACP)

**⚠️ Requires Local Auggie Installation**

The Agent Interaction interface allows you to launch Auggie in ACP mode and communicate bidirectionally. This requires a local Auggie installation.

## Usage

### Basic Initialization

```typescript  theme={null}
import { Auggie } from "@augmentcode/auggie-sdk";

// Simple initialization
const client = await Auggie.create({
  model: "sonnet4.5"
});

// Send a prompt
const response = await client.prompt("What files are in the current directory?");
console.log(response);

// Close the connection
await client.close();
```

### Full Configuration

```typescript  theme={null}
import { Auggie } from "@augmentcode/auggie-sdk";

const client = await Auggie.create({
  // Path to Auggie executable (default: "auggie")
  auggiePath: "/path/to/auggie",

  // Working directory for the Auggie process (default: process.cwd())
  workspaceRoot: "/path/to/workspace",

  // Eg: "haiku4.5" | "gpt-5" | "sonnet4.5" | "sonnet4"
  model: "sonnet4.5",

  // Allow codebase indexing (default: true)
  allowIndexing: true,

  // API key for authentication (optional, sets AUGMENT_API_TOKEN)
  apiKey: "your-api-key",

  // API URL (optional, sets AUGMENT_API_URL)
  apiUrl: "https://api.augmentcode.com",

  // Custom tools to provide to Auggie (optional)
  tools: {
    // Your custom tools here
  },

  // Rule file paths (optional)
  rules: ["/path/to/rules.md"],

  // Additional CLI arguments to pass to the Auggie process (optional)
  cliArgs: ["--quiet", "--max-turns=10"]
});

// Use the client
const response = await client.prompt("Your question here");
console.log(response);

await client.close();
```

### Advanced CLI Arguments

The `cliArgs` option allows you to pass additional command-line arguments directly to the Auggie CLI process. These arguments are appended after all SDK-generated flags, allowing you to use advanced configurations or experimental flags not exposed through standard SDK options.

```typescript  theme={null}
import { Auggie } from "@augmentcode/auggie-sdk";

// Pass custom CLI flags
const client = await Auggie.create({
  model: "sonnet4.5",
  cliArgs: ["--quiet", "--max-turns=10"]
});

// Arguments can use either format:
// 1. Separate flag and value: ["--retry-timeout", "60"]
// 2. Combined with equals: ["--retry-timeout=60"]
const client2 = await Auggie.create({
  model: "sonnet4.5",
  cliArgs: ["--shell=bash", "--allow-indexing"]
});
```

**Note:** Since `cliArgs` are appended after SDK-generated flags, they can override default values when the CLI uses a last-value-wins strategy. Refer to `auggie --help` for available CLI flags.

## Output Modes

The TypeScript SDK supports multiple output modes to fit different use cases:

### String Response (Default)

By default, the SDK returns the complete agent response as a string:

```typescript  theme={null}
const client = await Auggie.create({ model: "sonnet4.5" });
const response = await client.prompt("What files are in the current directory?");
console.log(response); // Full response as string
```

### Answer-Only Mode

Get only the final answer after all tool calls complete, excluding intermediate reasoning:

```typescript  theme={null}
const finalAnswer = await client.prompt(
  "List all TypeScript files in this project",
  { isAnswerOnly: true }
);
// Returns only the final response after tool execution
```

### Streaming Mode

Listen to real-time updates as the agent processes your request:

```typescript  theme={null}
client.onSessionUpdate((event) => {
  switch (event.update.sessionUpdate) {
    case "agent_message_chunk":
      if (event.update.content.type === "text") {
        process.stdout.write(event.update.content.text);
      }
      break;
    case "tool_call":
      console.log(`\nTool: ${event.update.title}`);
      break;
    case "tool_call_update":
      console.log("Output:", event.update.rawOutput);
      break;
  }
});

const response = await client.prompt("Your question here");
```

## Custom Tools

The TypeScript SDK supports **ai-sdk compatible tools**, allowing you to extend Auggie with custom functionality. You can provide tools that the agent can call during execution.

### Creating a Custom Tool

Here's an example of a custom weather tool:

```typescript  theme={null}
import { Auggie } from "@augmentcode/auggie-sdk";
import { tool } from "ai";
import { z } from "zod";

// Define a custom tool
const weather_tool = tool({
  name: "get_weather",
  description: "Get the weather in a location",
  inputSchema: z.object({
    location: z.string().describe("The location to get the weather for"),
  }),
  execute: ({ location }) => {
    console.log(`\n Weather tool called for location: ${location}`);
    return `The weather in ${location} is sunny.`;
  },
});

// Initialize Auggie with the custom tool
const client = await Auggie.create({
  model: "sonnet4.5",
  tools: {
    get_weather: weather_tool,
  },
});

// The agent can now use the weather tool
const response = await client.prompt("What's the weather like in San Francisco?");
console.log(response);

await client.close();
```

### Key Points

* **ai-sdk Compatible**: Tools follow the [Vercel AI SDK](https://sdk.vercel.ai/docs) tool format
* **Zod Schemas**: Use Zod for input validation and type safety
* **Automatic Discovery**: The agent automatically discovers and uses available tools when relevant
* **Multiple Tools**: Pass multiple tools in the `tools` object

### Tool Structure

Each tool requires:

* `name` - Unique identifier for the tool
* `description` - Clear description of what the tool does (helps the agent decide when to use it)
* `inputSchema` - Zod schema defining the tool's input parameters
* `execute` - Function that implements the tool's logic

## AI SDK Provider (Vercel AI SDK)

**✅ No Local Auggie Required - API Only**

The AI SDK Provider allows you to use Augment as a language model provider with [Vercel's AI SDK](https://sdk.vercel.ai/docs). This interface only requires API credentials and works without a local Auggie installation.

### Features

* Compatible with `generateText`, `streamText`, and other AI SDK functions
* Full support for tool calling (function calling) with automatic execution
* Multi-turn conversations with context retention
* Streaming responses for real-time output
* Works with API credentials only (no local Auggie installation needed)

### Quick Start

```typescript  theme={null}
import { AugmentLanguageModel, resolveAugmentCredentials } from "@augmentcode/auggie-sdk";
import { generateText } from "ai";

// Resolve credentials from environment or ~/.augment/session.json
const credentials = await resolveAugmentCredentials();

// Create the Augment language model
const model = new AugmentLanguageModel("claude-sonnet-4-5", credentials);

// Use with AI SDK functions
const { text } = await generateText({
  model,
  prompt: "Explain TypeScript in one sentence.",
});

console.log(text);
```

### Streaming Responses

```typescript  theme={null}
import { streamText } from "ai";

const { textStream } = await streamText({
  model,
  prompt: "Write a haiku about coding.",
});

for await (const chunk of textStream) {
  process.stdout.write(chunk);
}
```

### Tool Calling

```typescript  theme={null}
import { generateText, tool, stepCountIs } from "ai";
import { z } from "zod";

const weatherTool = tool({
  description: "Get the weather in a location",
  inputSchema: z.object({
    location: z.string().describe("The location to get the weather for"),
  }),
  execute: async ({ location }) => {
    return `The weather in ${location} is sunny.`;
  },
});

const { text } = await generateText({
  model,
  tools: { weather: weatherTool },
  stopWhen: stepCountIs(5),
  prompt: "What's the weather like in San Francisco?",
});
```

### Multi-turn Conversations

```typescript  theme={null}
const messages = [
  { role: "user" as const, content: "What's 2+2?" },
];

const response1 = await generateText({ model, messages });
messages.push({ role: "assistant" as const, content: response1.text });
messages.push({ role: "user" as const, content: "Multiply that by 3" });

const response2 = await generateText({ model, messages });
console.log(response2.text); // "12"
```

### Authentication

The AI SDK Provider uses the same authentication methods as the rest of the SDK:

1. **Environment Variables** - Set `AUGMENT_API_TOKEN` and `AUGMENT_API_URL`
2. **Session File** - Use credentials from `~/.augment/session.json` (created by `auggie login`)
3. **Direct Credentials** - Pass credentials directly to `AugmentLanguageModel`

```typescript  theme={null}
// Option 1: Auto-resolve from environment or session file
const credentials = await resolveAugmentCredentials();
const model = new AugmentLanguageModel("claude-sonnet-4-5", credentials);

// Option 2: Pass credentials directly
const model = new AugmentLanguageModel("claude-sonnet-4-5", {
  apiKey: "your-api-key",
  apiUrl: "https://api.augmentcode.com",
});
```
