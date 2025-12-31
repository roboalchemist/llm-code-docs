# Source: https://docs.augmentcode.com/cli/sdk-typescript.md

# TypeScript SDK

> Build custom integrations and agents using the Auggie TypeScript SDK.

## About

The Auggie TypeScript SDK provides a programmatic interface to Auggie for building custom integrations and agents in Node.js and TypeScript applications.

## Installation

```sh  theme={null}
npm install @augmentcode/auggie-sdk
```

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
  rules: ["/path/to/rules.md"]
});

// Use the client
const response = await client.prompt("Your question here");
console.log(response);

await client.close();
```

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
