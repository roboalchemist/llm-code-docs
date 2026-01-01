# Source: https://braintrust.dev/docs/integrations/sdk-integrations/vercel.md

# Vercel

Braintrust integrates with [Vercel](https://vercel.com) in two ways: through the **Vercel AI SDK** for code-based tracing, and through the **Vercel Marketplace** for dashboard-based observability.

Choose your integration method based on your needs:

| Method                 | Best for                                                     | Setup                         |
| ---------------------- | ------------------------------------------------------------ | ----------------------------- |
| **Vercel AI SDK**      | Fine-grained control over tracing, selective instrumentation | Install packages + add code   |
| **Vercel Marketplace** | Quick setup, automatic tracing of all AI calls               | Configure in Vercel dashboard |

## Trace with Vercel AI SDK

The Braintrust SDK provides native support for the [Vercel AI SDK](https://sdk.vercel.ai/docs/ai-sdk-core), automatically tracing AI calls with full input/output logging, metrics, and tool execution.

### Setup

Install the Braintrust SDK alongside the Vercel AI SDK. The Braintrust SDK supports Vercel AI SDK v3, v4, v5, and v6.

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add braintrust ai
  # npm
  npm install braintrust ai
  ```
</CodeGroup>

Then use `wrapAISDK` to wrap the Vercel AI SDK functions (`generateText`, `streamText`, `generateObject`, `streamObject`).

```typescript title="trace-vercel-ai-sdk.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { initLogger, wrapAISDK } from "braintrust";
import * as ai from "ai";
import { openai } from "@ai-sdk/openai";

initLogger({
  projectName: "My AI Project",
  apiKey: process.env.BRAINTRUST_API_KEY,
});

const { generateText } = wrapAISDK(ai);

async function main() {
  // This will automatically log the request, response, and metrics to Braintrust
  const { text } = await generateText({
    model: openai("gpt-5-mini"),
    prompt: "What is the capital of France?",
  });
  console.log(text);
}

main().catch(console.error);
```

### Trace tools calls

`wrapAISDK` automatically traces tool call suggestions from the LLM and the tool execution results.

```typescript title="trace-vercel-ai-sdk-tools.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { initLogger, wrapAISDK } from "braintrust";
import * as ai from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";

initLogger({
  projectName: "Tool Tracing",
  apiKey: process.env.BRAINTRUST_API_KEY,
});

const { generateText } = wrapAISDK(ai);

async function main() {
  // Tool executions are automatically wrapped and traced
  const { text } = await generateText({
    model: openai("gpt-5-mini"),
    prompt: "What's the weather like in San Francisco?",
    tools: {
      getWeather: {
        description: "Get weather for a location",
        inputSchema: z.object({
          location: z.string().describe("The city name"),
        }),
        execute: async ({ location }: { location: string }) => {
          // This execution will appear as a child span
          return {
            location,
            temperature: 72,
            conditions: "sunny",
          };
        },
      },
    },
  });

  console.log(text);
}

main().catch(console.error);
```

### Stream tool responses

You can also use `streamText` for streaming responses with tool calls. Streaming creates `doStream` child spans (as explained above) for each LLM call:

```typescript title="trace-vercel-ai-sdk-streaming.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { initLogger, wrapAISDK } from "braintrust";
import * as ai from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";

initLogger({
  projectName: "Streaming Tool Tracing",
  apiKey: process.env.BRAINTRUST_API_KEY,
});

const { streamText } = wrapAISDK(ai);

async function main() {
  const result = streamText({
    model: openai("gpt-5-mini"),
    prompt: "What is 127 multiplied by 49?",
    tools: {
      calculate: {
        description: "Perform a mathematical calculation",
        inputSchema: z.object({
          operation: z.enum(["add", "subtract", "multiply", "divide"]),
          a: z.number(),
          b: z.number(),
        }),
        execute: async ({ operation, a, b }) => {
          switch (operation) {
            case "add": return a + b;
            case "subtract": return a - b;
            case "multiply": return a * b;
            case "divide": return b !== 0 ? a / b : 0;
          }
        },
      },
    },
    maxToolRoundtrips: 2,
  });

  for await (const delta of result.textStream) {
    process.stdout.write(delta);
  }
}

main().catch(console.error);
```

### Add metadata

To attach custom metadata to your `wrapAISDK` traces, wrap your AI calls in a parent span using `traced`. The `wrapAISDK` function automatically creates child spans for AI SDK calls, and you attach your metadata to the parent span:

```typescript title="trace-with-span-metadata.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { initLogger, wrapAISDK, traced, currentSpan } from "braintrust";
import * as ai from "ai";
import { openai } from "@ai-sdk/openai";

initLogger({
  projectName: "My AI Project",
  apiKey: process.env.BRAINTRUST_API_KEY,
});

const { generateText } = wrapAISDK(ai);

async function generateWithContext(userId: string, prompt: string) {
  // Create a parent span to hold metadata
  return traced(
    async (span) => {
      // Fetch user context or compute metadata
      const userTier = await getUserTier(userId);

      // wrapAISDK creates a child span automatically for this call
      const { text } = await generateText({
        model: openai("gpt-5-mini"),
        prompt,
      });

      // Attach metadata to the parent span (not the AI SDK's child span)
      span.log({
        input: prompt,
        output: text,
        metadata: {
          userId,
          userTier,
          timestamp: new Date().toISOString(),
        },
      });

      return text;
    },
    { name: "generate-with-context", type: "function" }
  );
}

async function getUserTier(userId: string): Promise<string> {
  // Simulated async operation
  return "premium";
}

async function main() {
  const text = await generateWithContext("user-123", "What is the capital of France?");
  console.log(text);
}

main().catch(console.error);
```

This creates a span hierarchy where your parent span contains the metadata, and the AI SDK call appears as a child span with its own metrics and details.

This approach is useful when you need to:

* Add custom metadata like user IDs, session IDs, or feature flags.
* Compute metadata based on async operations (e.g., fetching user context).
* Add metadata conditionally based on the response.
* Group multiple AI calls under a single parent span with shared metadata.

<Note>
  If you're using the Vercel AI SDK with OpenTelemetry tracing (not `wrapAISDK`), you can use the native `experimental_telemetry.metadata` parameter instead. See the [OpenTelemetry integration guide](/integrations/sdk-integrations/opentelemetry#vercel-ai-sdk) for details.
</Note>

### Multi-round tool interactions

When using tools, the AI SDK often makes multiple LLM calls to complete the task. Braintrust automatically creates nested spans to give you visibility into each step:

* **Parent span**: `generateText`, `streamText`, `generateObject`, or `streamObject` - represents the overall operation
* **Child spans**: `doGenerate` or `doStream` - one span for each individual LLM call during the operation
* **Tool spans**: Tool executions appear as separate spans showing inputs and outputs

This nested structure helps you understand:

* How many LLM calls were needed to complete the task
* What each LLM call received and returned
* The complete flow of tool calls and responses

For example, a `generateText` call that uses tools might produce this span hierarchy:

* `generateText` (parent)
  * `doGenerate` (1st LLM call - decides to use tool)
  * `getWeather` (tool execution)
  * `doGenerate` (2nd LLM call - uses tool result to form response)

### Trace agents

The AI SDK's Agent classes (`Agent`, `Experimental_Agent`, `ToolLoopAgent`) are automatically wrapped and traced when using `wrapAISDK`.

```typescript title="trace-vercel-ai-sdk-agent.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { initLogger, wrapAISDK } from "braintrust";
import * as ai from "ai";
import { openai } from "@ai-sdk/openai";

initLogger({
  projectName: "Agent Tracing",
  apiKey: process.env.BRAINTRUST_API_KEY,
});

const { Experimental_Agent: Agent } = wrapAISDK(ai);

async function main() {
  // Agent methods are automatically traced
  const agent = new Agent({
    model: openai("gpt-5-mini"),
    system: "You are a helpful assistant.",
  });

  // Both generate() and stream() are traced
  const result = await agent.generate({
    prompt: "What is the capital of France?",
  });

  console.log(result.text);
}

main().catch(console.error);
```

## Trace with Vercel Marketplace

The Vercel Marketplace integration provides automatic tracing for all AI calls in your Vercel applications with minimal setup. No package installation required.

### Setup

1. Visit the [Vercel Marketplace listing](https://vercel.com/integrations/braintrust) and select **Install**.
2. Create or link your Braintrust account.
3. Select a plan (Free or Pro) and create a project name.
4. Select **Add Drain** to configure trace collection.

### Configure log drain

In the **Add Drain** panel:

1. Select **Traces** and **Next**.
2. Choose which Vercel projects to trace (**All Projects** or specific projects).
3. Set the sampling rate for trace collection.

### Enable OpenTelemetry

In your Next.js project, create an `instrumentation.ts` file and call `registerOtel`. See the [Vercel OpenTelemetry docs](https://vercel.com/docs/otel#initialize-otel) for details.

## Resources

* [Vercel AI SDK documentation](https://sdk.vercel.ai/docs)
* [Vercel Marketplace integration](https://vercel.com/integrations/braintrust)
* [Vercel OpenTelemetry docs](https://vercel.com/docs/otel)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt