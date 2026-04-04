# Source: https://mastra.ai/reference/ai-sdk/handle-network-stream

# handleNetworkStream()

> **Deprecated:** Agent networks are deprecated and will be removed in a future release. Use the [supervisor pattern](https://mastra.ai/docs/agents/supervisor-agents) with `agent.stream()` or `agent.generate()` instead. See the [migration guide](https://mastra.ai/guides/migrations/network-to-supervisor) to upgrade.

Framework-agnostic handler for streaming network execution in AI SDK-compatible format. Use this function directly when you need to handle network streaming outside Hono or Mastra's own [apiRoutes](https://mastra.ai/docs/server/custom-api-routes) feature.

`handleNetworkStream()` returns a `ReadableStream` that you can wrap with [`createUIMessageStreamResponse()`](https://ai-sdk.dev/docs/reference/ai-sdk-ui/create-ui-message-stream-response).

Use [`networkRoute()`](https://mastra.ai/reference/ai-sdk/network-route) if you want to create a network route inside a Mastra server.

## Usage example

Next.js App Router example:

```typescript
import { handleNetworkStream } from '@mastra/ai-sdk'
import { createUIMessageStreamResponse } from 'ai'
import { mastra } from '@/src/mastra'

export async function POST(req: Request) {
  const params = await req.json()
  const stream = await handleNetworkStream({
    mastra,
    agentId: 'routingAgent',
    params,
  })
  return createUIMessageStreamResponse({ stream })
}
```

## Parameters

**mastra** (`Mastra`): The Mastra instance to use for agent lookup and execution.

**agentId** (`string`): The ID of the routing agent to execute as a network.

**params** (`NetworkStreamHandlerParams`): The request parameters containing messages and execution options. Includes \`messages\` (required) and any AgentExecutionOptions like \`memory\`, \`maxSteps\`, \`runId\`, etc.

**defaultOptions** (`AgentExecutionOptions`): Default options passed to agent execution. These are merged with params, with params taking precedence.