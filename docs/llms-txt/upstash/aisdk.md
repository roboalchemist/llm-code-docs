# Source: https://upstash.com/docs/workflow/integrations/aisdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel AI SDK

<Note>
  This feature is not yet available in
  [workflow-py](https://github.com/upstash/workflow-py). See our
  [Roadmap](/workflow/roadmap) for feature parity plans and
  [Changelog](/workflow/changelog) for updates.
</Note>

<Card title="GitHub Repository" icon="github" href="https://github.com/upstash/workflow-js/blob/main/examples/nextjs/app/vercel-ai-sdk/route.ts" horizontal>
  You can find the project source code which uses real APIs on Github.
</Card>

Upstash Workflow integrates with the Vercel AI SDK to provide durable and reliable AI applications. This allows you to:

* Build resilient AI applications with automatic retries
* Manage AI operations with workflow steps
* Implement tools and function calling with durability
* Handle errors gracefully across your AI operations
* Handle long-running AI operations with extended timeouts

This guide will walk you through setting up and implementing AI features using Upstash Workflow's durability guarantees with Vercel AI SDK's capabilities.

## Prerequisites

Before getting started, make sure you have:

* An OpenAI API key
* Basic familiarity with Upstash Workflow and Vercel AI SDK
* Vercel AI SDK version 4.0.12 or higher (required for ToolExecutionError handling)

## Installation

Install the required packages:

<CodeGroup>
  ```bash npm theme={"system"}
  npm install @ai-sdk/openai ai zod
  ```

  ```bash pnpm theme={"system"}
  pnpm install @ai-sdk/openai ai zod
  ```

  ```bash bun theme={"system"}
  bun install @ai-sdk/openai ai zod
  ```
</CodeGroup>

## Implementation

### Creating OpenAI client

AI SDKs (Vercel AI SDK, OpenAI SDK etc.) uses the client's default fetch implementation to make API requests, but allows you to provide a custom fetch implementation.

In the case of Upstash Workflow, we need to use the `context.call` method to make HTTP requests. We can create a custom fetch implementation that uses `context.call` to make requests. By using `context.call`, Upstash Workflow is the one making the HTTP request and waiting for the response, even if it takes too long to receive response from the LLM.

The following code snippet can also be generalized to work with other LLM SDKs, such as Anthropic or Google.

```typescript {18-24} theme={"system"}
import { createOpenAI } from '@ai-sdk/openai';
import { HTTPMethods } from '@upstash/qstash';
import { WorkflowAbort, WorkflowContext } from '@upstash/workflow';

export const createWorkflowOpenAI = (context: WorkflowContext) => {
  return createOpenAI({
    compatibility: "strict",
    fetch: async (input, init) => {
      try {
        // Prepare headers from init.headers
        const headers = init?.headers
          ? Object.fromEntries(new Headers(init.headers).entries())
          : {};

        // Prepare body from init.body
        const body = init?.body ? JSON.parse(init.body as string) : undefined;

        // Make network call
        const responseInfo = await context.call("openai-call-step", {
          url: input.toString(),
          method: init?.method as HTTPMethods,
          headers,
          body,
        });

        // Construct headers for the response
        const responseHeaders = new Headers(
          Object.entries(responseInfo.header).reduce((acc, [key, values]) => {
            acc[key] = values.join(", ");
            return acc;
          }, {} as Record<string, string>)
        );

        // Return the constructed response
        return new Response(JSON.stringify(responseInfo.body), {
          status: responseInfo.status,
          headers: responseHeaders,
        });
      } catch (error) {
        if (error instanceof WorkflowAbort) {
          throw error
        } else {
          console.error("Error in fetch implementation:", error);
          throw error; // Rethrow error for further handling
        }
      }
    },
  });
};
```

### Using OpenAI client to generate text

Now that we've created the OpenAI client, we can use it to generate the text.

For that, we're going to create a new workflow endpoint that uses the payload as prompt to generate text using the OpenAI client.

```typescript {8, 16-20} theme={"system"}
import { serve } from "@upstash/workflow/nextjs";
import { WorkflowAbort } from '@upstash/workflow';
import { generateText, ToolExecutionError } from 'ai';

import { createWorkflowOpenAI } from './model';

export const { POST } = serve<{ prompt: string }>(async (context) => {
  const openai = createWorkflowOpenAI(context);

  // Important: Must have a step before generateText
  const prompt = await context.run("get prompt", async () => {
    return context.requestPayload.prompt;
  });

  try {
    const result = await generateText({
      model: openai('gpt-3.5-turbo'),
      maxTokens: 2048,
      prompt,
    });

    await context.run("text", () => {
      console.log(`TEXT: ${result.text}`);
      return result.text;
    });
    
  } catch (error) {    
    if (error instanceof ToolExecutionError && error.cause instanceof WorkflowAbort) {
      throw error.cause;
    } else {
      throw error;
    }
  }
});
```

We can either [run the app locally](/workflow/howto/local-development) or deploy it. Once the app is running, we can trigger the workflow using the following code:

```ts  theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  body: { "prompt": "How is the weather in San Francisco around this time?" }
});
```

The workflow will execute, and we can view the logs in [the Workflow dashboard](/workflow/howto/monitor):

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/without-tool.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=67020a90a3c074458dc673b548de501f" alt="Workflow logs in dashboard" data-og-width="2172" width="2172" data-og-height="600" height="600" data-path="img/qstash-workflow/ai-sdk/without-tool.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/without-tool.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=eb661b008f69cbcb8a531a25687aa3b6 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/without-tool.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=e388763ee91488cf272ca7bc5f72a906 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/without-tool.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=5c8883aca9f4e3a9a93876ee5255f691 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/without-tool.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=945cf3bccb336c17fbfd2d24306dc808 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/without-tool.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=5d656092b0a76ce1b8cca0d0d7eb747d 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/without-tool.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=1b7e3c54fa46a632aca1ee8886076def 2500w" />
</Frame>

### Advanced Implementation with Tools

Tools allow the AI model to perform specific actions during text generation. You can learn more about tools in the [Vercel AI SDK documentation](https://sdk.vercel.ai/docs/ai-sdk-core/tools-and-tool-calling).

When using tools with Upstash Workflow, each tool execution must be wrapped in a workflow step.

<Info>
  The `maxSteps` parameter must be greater than 1 when using tools to allow the model to process tool results and generate final responses. See the [tool steps documentation](https://sdk.vercel.ai/docs/ai-sdk-core/tools-and-tool-calling#tool-steps) for detailed explanation.
</Info>

```typescript {24-30, 33} theme={"system"}
import { z } from 'zod';
import { serve } from "@upstash/workflow/nextjs";
import { WorkflowAbort } from '@upstash/workflow';
import { generateText, ToolExecutionError, tool } from 'ai';

import { createWorkflowOpenAI } from './model';

export const { POST } = serve<{ prompt: string }>(async (context) => {
  const openai = createWorkflowOpenAI(context);

  const prompt = await context.run("get prompt", async () => {
    return context.requestPayload.prompt;
  });

  try {
    const result = await generateText({
      model: openai('gpt-3.5-turbo'),
      tools: {
        weather: tool({
          description: 'Get the weather in a location',
          parameters: z.object({
            location: z.string().describe('The location to get the weather for'),
          }),
          execute: ({ location }) => context.run("weather tool", () => {
	        // Mock data, replace with actual weather API call
            return {
              location,
              temperature: 72 + Math.floor(Math.random() * 21) - 10,
            };
          })
        }),
      },
      maxSteps: 2,
      prompt,
    });
    
    await context.run("text", () => {
      console.log(`TEXT: ${result.text}`);
      return result.text;
    });
  } catch (error) {
    if (error instanceof ToolExecutionError && error.cause instanceof WorkflowAbort) {
      throw error.cause;
    } else {
      throw error;
    }
  }
});
```

When called with the same prompt as above, we will see the following logs:

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/with-tool.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=feaa22e98e9bd424f67a06494c00715c" data-og-width="2172" width="2172" data-og-height="790" height="790" data-path="img/qstash-workflow/ai-sdk/with-tool.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/with-tool.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=2e3b6f135b6f59bf6aa07524d998befd 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/with-tool.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=a7da726a229ee05b06ae19e4a3e449ff 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/with-tool.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=43e20af5a05b5d6786928097d40a4e96 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/with-tool.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8dc2fb669846aaa6e783b7042c7e9fed 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/with-tool.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=4d042557b569a795cb3330ca43358eaf 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/ai-sdk/with-tool.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=04264f5ad160a798837b54e5c354b627 2500w" />
</Frame>

## Important Considerations

When using Upstash Workflow with the Vercel AI SDK, there are several critical requirements that must be followed:

### Step Execution Order

The most critical requirement is that `generateText` cannot be called before any workflow step. Always have a step before `generateText`. This could be a step which gets the prompt:

<CodeGroup>
  ```typescript ❌ Wrong {4} theme={"system"}
  export const { POST } = serve<{ prompt: string }>(async (context) => {
    const openai = createWorkflowOpenAI(context);

    // Will throw "prompt is undefined"
    const result = await generateText({
      model: openai('gpt-3.5-turbo'),
      prompt: context.requestPayload.prompt
    });
  });
  ```

  ```typescript ✅ Correct {3-7} theme={"system"}
  export const { POST } = serve<{ prompt: string }>(async (context) => {
    const openai = createWorkflowOpenAI(context);

    // Get prompt in a step first
    const prompt = await context.run("get prompt", async () => {
      return context.requestPayload.prompt;
    });

    const result = await generateText({
      model: openai('gpt-3.5-turbo'),
      prompt
    });
  });
  ```
</CodeGroup>

### Error Handling Pattern

You must use the following error handling pattern exactly as shown. The conditions and their handling should not be modified:

```typescript {3-9} theme={"system"}
try {
  // Your generation code
} catch (error) {    
  if (error instanceof ToolExecutionError && error.cause instanceof WorkflowAbort) {
    throw error.cause;
  } else {
    throw error;
  }
}
```

### Tool Implementation

When implementing tools:

* Each tool's `execute` function must be wrapped in a `context.run()` call
* Tool steps should have descriptive names for tracking
* Tools must follow the same error handling pattern as above

Example:

```typescript  theme={"system"}
execute: ({ location }) => context.run("weather tool", () => {
  // Mock data, replace with actual weather API call
  return {
    location,
    temperature: 72 + Math.floor(Math.random() * 21) - 10,
  };
})
```
