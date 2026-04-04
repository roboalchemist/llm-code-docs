# Source: https://mastra.ai/reference/ai-sdk/handle-chat-stream

# handleChatStream()

Framework-agnostic handler for streaming agent chat in AI SDK-compatible format. Use this function directly when you need to handle chat streaming outside Hono or Mastra's own [apiRoutes](https://mastra.ai/docs/server/custom-api-routes) feature.

`handleChatStream()` returns a `ReadableStream` that you can wrap with [`createUIMessageStreamResponse()`](https://ai-sdk.dev/docs/reference/ai-sdk-ui/create-ui-message-stream-response).

Use [`chatRoute()`](https://mastra.ai/reference/ai-sdk/chat-route) if you want to create a chat route inside a Mastra server.

## Usage example

Next.js App Router example:

```typescript
import { handleChatStream } from '@mastra/ai-sdk'
import { createUIMessageStreamResponse } from 'ai'
import { mastra } from '@/src/mastra'

export async function POST(req: Request) {
  const params = await req.json()
  const stream = await handleChatStream({
    mastra,
    agentId: 'weatherAgent',
    params,
  })
  return createUIMessageStreamResponse({ stream })
}
```

## Parameters

**mastra** (`Mastra`): The Mastra instance containing registered agents.

**agentId** (`string`): The ID of the agent to use for chat.

**params** (`ChatStreamHandlerParams`): Parameters for the chat stream, including messages and optional resume data.

**params.messages** (`UIMessage[]`): Array of messages in the conversation.

**params.resumeData** (`Record<string, any>`): Data for resuming a suspended agent execution. Requires \`runId\` to be set.

**params.runId** (`string`): The run ID. Required when \`resumeData\` is provided.

**params.providerOptions** (`Record<string, Record<string, unknown>>`): Provider-specific options passed to the language model (e.g. \`{ openai: { reasoningEffort: "high" } }\`). Merged with \`defaultOptions.providerOptions\`, with \`params\` taking precedence.

**params.requestContext** (`RequestContext`): Request context to pass to the agent execution.

**defaultOptions** (`AgentExecutionOptions`): Default options passed to agent execution. These are merged with params, with params taking precedence.

**sendStart** (`boolean`): Whether to send start events in the stream. (Default: `true`)

**sendFinish** (`boolean`): Whether to send finish events in the stream. (Default: `true`)

**sendReasoning** (`boolean`): Whether to include reasoning steps in the stream. (Default: `false`)

**sendSources** (`boolean`): Whether to include source citations in the stream. (Default: `false`)