# Source: https://ably.com/docs/ai-transport/guides/langgraph/langgraph-message-per-token.md

# Guide: Stream LangGraph responses using the message-per-token pattern

This guide shows you how to stream AI responses from [LangGraph](https://docs.langchain.com/oss/javascript/langgraph/overview) over Ably using the [message-per-token pattern](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md). Specifically, it implements the [explicit start/stop events approach](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md#explicit-events), which publishes each response token as an individual message, along with explicit lifecycle events to signal when responses begin and end.

Using Ably to distribute tokens from LangGraph enables you to broadcast AI responses to thousands of concurrent subscribers with reliable message delivery and ordering guarantees, ensuring that each client receives the complete response stream with all tokens delivered in order. This approach decouples your AI inference from client connections, enabling you to scale agents independently and handle reconnections gracefully.

<Aside data-type="further-reading">
To discover other approaches to token streaming, including the [message-per-response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) pattern, see the [token streaming](https://ably.com/docs/ai-transport/token-streaming.md) documentation.
</Aside>

## Prerequisites

To follow this guide, you need:

- Node.js 20 or higher
- An Anthropic API key
- An Ably API key

Useful links:

- [LangGraph documentation](https://docs.langchain.com/oss/javascript/langgraph/overview)
- [Ably JavaScript SDK getting started](https://ably.com/docs/getting-started/javascript.md)

Create a new NPM package, which will contain the publisher and subscriber code:

<Code>

### Shell

```
mkdir ably-langgraph-example && cd ably-langgraph-example
npm init -y
```

</Code>

Install the required packages using NPM:

<Code>

### Shell

```
npm install @langchain/langgraph@^0.2 @langchain/anthropic@^0.3 @langchain/core@^0.3 ably@^2
```

</Code>

<Aside data-type="note">
This guide uses LangGraph with the Anthropic provider and Claude Sonnet 4.5 model. LangGraph supports [multiple model providers](https://js.langchain.com/docs/integrations/chat/) including OpenAI, Google, and others. The streaming approach shown in this guide works with any LangChain-compatible model.
</Aside>

Export your Anthropic API key to the environment, which will be used later in the guide by the Anthropic SDK:

<Code>

### Shell

```
export ANTHROPIC_API_KEY="your_api_key_here"
```

</Code>

## Step 1: Get a streamed response from LangGraph

Initialize LangGraph with a simple graph that uses Claude to respond to prompts, and use [`stream`](https://docs.langchain.com/oss/javascript/langgraph/streaming) with `streamMode: "messages"` to stream model tokens.

Create a new file `agent.mjs` with the following contents:

<Code>

### Javascript

```
import { ChatAnthropic } from "@langchain/anthropic";
import { StateGraph, Annotation, START, END } from "@langchain/langgraph";

// Initialize the model
const model = new ChatAnthropic({ model: "claude-sonnet-4-5" });

// Define state with message history
const StateAnnotation = Annotation.Root({
  messages: Annotation({
    reducer: (x, y) => x.concat(y),
    default: () => [],
  }),
});

// Build and compile a simple graph
const graph = new StateGraph(StateAnnotation)
  .addNode("agent", async (state) => {
    const response = await model.invoke(state.messages);
    return { messages: [response] };
  })
  .addEdge(START, "agent")
  .addEdge("agent", END);

const app = graph.compile();

// Stream response tokens
async function streamLangGraphResponse(prompt) {
  const stream = await app.stream(
    { messages: [{ role: "user", content: prompt }] },
    { streamMode: "messages" }
  );

  for await (const [messageChunk, metadata] of stream) {
    console.log(messageChunk.content || "(empty)");
  }
}

// Usage example
streamLangGraphResponse("Tell me a short joke");
```

</Code>

### Understand LangGraph streaming

LangGraph's [`stream`](https://docs.langchain.com/oss/javascript/langgraph/streaming) method with `streamMode: "messages"` streams LLM tokens from your graph. The stream returns tuples of `[messageChunk, metadata]` where:

- `messageChunk`: Contains the token content in the `content` field. These represent incremental text chunks as the model generates them.

- `metadata`: Contains metadata about the stream, including the `langgraph_node` where the LLM is invoked and any associated tags.

The following example shows the message chunks received when streaming a response. Each event is a tuple of `[messageChunk, metadata]`:

<Code>

#### Json

```
// 1. Stream initialization (empty content with model metadata)
[{"lc":1,"type":"constructor","id":["langchain_core","messages","AIMessageChunk"],"kwargs":{"content":"","additional_kwargs":{"model":"claude-sonnet-4-5-20250929","id":"msg_01SPbpi5P7CkNqgxPT2Ne9u5","type":"message","role":"assistant"},"tool_call_chunks":[],"usage_metadata":{"input_tokens":12,"output_tokens":1,"total_tokens":13},"id":"msg_01SPbpi5P7CkNqgxPT2Ne9u5"}},{"langgraph_step":1,"langgraph_node":"agent","langgraph_triggers":["branch:to:agent"]}]

// 2. Empty content chunk
[{"lc":1,"type":"constructor","id":["langchain_core","messages","AIMessageChunk"],"kwargs":{"content":"","additional_kwargs":{},"tool_call_chunks":[],"id":"msg_01SPbpi5P7CkNqgxPT2Ne9u5"}},{"langgraph_step":1,"langgraph_node":"agent"}]

// 3. Text tokens stream in
[{"lc":1,"type":"constructor","id":["langchain_core","messages","AIMessageChunk"],"kwargs":{"content":"Why","additional_kwargs":{},"tool_call_chunks":[],"id":"msg_01SPbpi5P7CkNqgxPT2Ne9u5"}},{"langgraph_step":1,"langgraph_node":"agent"}]
[{"lc":1,"type":"constructor","id":["langchain_core","messages","AIMessageChunk"],"kwargs":{"content":" don't scientists trust atoms?\n\nBecause","additional_kwargs":{},"tool_call_chunks":[],"id":"msg_01SPbpi5P7CkNqgxPT2Ne9u5"}},{"langgraph_step":1,"langgraph_node":"agent"}]
[{"lc":1,"type":"constructor","id":["langchain_core","messages","AIMessageChunk"],"kwargs":{"content":" they make up everything!","additional_kwargs":{},"tool_call_chunks":[],"id":"msg_01SPbpi5P7CkNqgxPT2Ne9u5"}},{"langgraph_step":1,"langgraph_node":"agent"}]

// 4. Stream completion (empty content with stop reason and final usage)
[{"lc":1,"type":"constructor","id":["langchain_core","messages","AIMessageChunk"],"kwargs":{"content":"","additional_kwargs":{"stop_reason":"end_turn","stop_sequence":null},"usage_metadata":{"input_tokens":0,"output_tokens":17,"total_tokens":17},"id":"msg_01SPbpi5P7CkNqgxPT2Ne9u5"}},{"langgraph_step":1,"langgraph_node":"agent"}]
```

</Code>

<Aside data-type="note">
This is only an illustrative example for a simple "text in, text out" use case and may not reflect the exact sequence of messages that you observe from LangGraph. LangGraph also supports more complex graphs with multiple nodes, tools, and conditional edges. For complete details on streaming modes, see [LangGraph streaming documentation](https://docs.langchain.com/oss/javascript/langgraph/streaming).
</Aside>

## Step 2: Publish streaming events to Ably

Publish LangGraph streaming events to Ably to reliably and scalably distribute them to subscribers.

This implementation follows the [explicit start/stop events pattern](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md#explicit-events), which provides clear response boundaries.

### Initialize the Ably client

Add the Ably client initialization to your `agent.mjs` file:

<Code>

#### Javascript

```
import Ably from 'ably';

// Initialize Ably Realtime client
const realtime = new Ably.Realtime({
  key: 'your-api-key',
  echoMessages: false
});

// Create a channel for publishing streamed AI responses
const channel = realtime.channels.get('your-channel-name');
```

</Code>

The Ably Realtime client maintains a persistent connection to the Ably service, which allows you to publish tokens at high message rates with low latency.

<Aside data-type="note">
Set [`echoMessages`](https://ably.com/docs/api/realtime-sdk/types.md#client-options) to `false` on the agent's Ably client to prevent the agent from receiving its own streamed tokens, avoiding billing for [echoed messages](https://ably.com/docs/pub-sub/advanced.md#echo).
</Aside>

### Map LangGraph streaming events to Ably messages

Choose how to map [LangGraph streaming events](#understand-streaming-events) to Ably [messages](https://ably.com/docs/messages.md). You can choose any mapping strategy that suits your application's needs. This guide uses the following pattern as an example:

- `start`: Signals the beginning of a response
- `token`: Contains the incremental text content for each delta
- `stop`: Signals the completion of a response

Update your `agent.mjs` file to initialize the Ably client and update the `streamLangGraphResponse()` function to publish streaming tokens to Ably:

<Code>

#### Javascript

```
// Track response ID across events
let responseId = null;

// Create streaming response from LangGraph
async function streamLangGraphResponse(prompt) {
  const input = {
    messages: [{ role: "user", content: prompt }],
  };

  // Stream tokens using messages mode
  const stream = await app.stream(input, { streamMode: "messages" });

  for await (const [messageChunk, metadata] of stream) {
    // Capture response ID from the first message chunk
    if (!responseId && messageChunk?.id) {
      responseId = messageChunk.id;

      // Publish start event with response ID
      channel.publish({
        name: 'start',
        extras: {
          headers: { responseId }
        }
      });
    }

    // Extract token content
    const content = messageChunk?.content;
    if (content) {
      channel.publish({
        name: 'token',
        data: content,
        extras: {
          headers: { responseId }
        }
      });
    }
  }

  // Publish stop event
  channel.publish({
    name: 'stop',
    extras: {
      headers: { responseId }
    }
  });
}
```

</Code>

This implementation:

- Captures the `responseId` from the first message chunk's `id` field
- Publishes a `start` event when the response ID is captured
- Streams tokens from the graph using `streamMode: "messages"`
- Extracts the `content` from each message chunk and publishes it as a `token` event
- Publishes a `stop` event when streaming completes
- All published events include the `responseId` in message [`extras`](https://ably.com/docs/messages.md#properties) to allow the client to correlate events relating to a particular response

<Aside data-type="note">
This implementation publishes Ably messages without `await` to maximize throughput. Ably maintains message ordering even without awaiting each publish. For more information, see [Publishing tokens](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md#publishing).
</Aside>

Run the publisher to see tokens streaming to Ably:

<Code>

#### Shell

```
node agent.mjs
```

</Code>

## Step 3: Subscribe to streaming tokens

Create a subscriber that receives the streaming events from Ably and reconstructs the response.

Create a new file `client.mjs` with the following contents:

<Code>

### Javascript

```
import Ably from 'ably';

// Initialize Ably Realtime client
const realtime = new Ably.Realtime({ key: 'your-api-key' });

// Get the same channel used by the publisher
const channel = realtime.channels.get('your-channel-name');

// Track responses by ID
const responses = new Map();

// Handle response start
await channel.subscribe('start', (message) => {
  const responseId = message.extras?.headers?.responseId;
  console.log('\n[Response started]', responseId);
  responses.set(responseId, '');
});

// Handle tokens
await channel.subscribe('token', (message) => {
  const responseId = message.extras?.headers?.responseId;
  const token = message.data;

  // Append token to response
  const currentText = responses.get(responseId) || '';
  responses.set(responseId, currentText + token);

  // Display token as it arrives
  process.stdout.write(token);
});

// Handle response stop
await channel.subscribe('stop', (message) => {
  const responseId = message.extras?.headers?.responseId;
  const finalText = responses.get(responseId);

  console.log('\n[Response completed]', responseId);
});

console.log('Subscriber ready, waiting for tokens...');
```

</Code>

Run the subscriber in a separate terminal:

<Code>

### Shell

```
node client.mjs
```

</Code>

With the subscriber running, run the publisher in another terminal. The tokens stream in realtime as the AI model generates them.

## Step 4: Stream with multiple publishers and subscribers

Ably's [channel-oriented sessions](https://ably.com/docs/ai-transport/sessions-identity.md#connection-oriented-vs-channel-oriented-sessions) enables multiple AI agents to publish responses and multiple users to receive them on a single channel simultaneously. Ably handles message delivery to all participants, eliminating the need to implement routing logic or manage state synchronization across connections.

### Broadcasting to multiple subscribers

Each subscriber receives the complete stream of tokens independently, enabling you to build collaborative experiences or multi-device applications.

Run a subscriber in multiple separate terminals:

<Code>

#### Shell

```
# Terminal 1
node client.mjs

# Terminal 2
node client.mjs

# Terminal 3
node client.mjs
```

</Code>

All subscribers receive the same stream of tokens in realtime.

### Publishing concurrent responses

The implementation uses `responseId` in message [`extras`](https://ably.com/docs/messages.md#properties) to correlate tokens with their originating response. This enables multiple publishers to stream different responses concurrently on the same [channel](https://ably.com/docs/channels.md), with each subscriber correctly tracking all responses independently.

To demonstrate this, run a publisher in multiple separate terminals:

<Code>

#### Shell

```
# Terminal 1
node agent.mjs

# Terminal 2
node agent.mjs

# Terminal 3
node agent.mjs
```

</Code>

All running subscribers receive tokens from all responses concurrently. Each subscriber correctly reconstructs each response separately using the `responseId` to correlate tokens.

## Next steps

- Learn more about the [message-per-token pattern](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md) used in this guide
- Learn about [client hydration strategies](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md#hydration) for handling late joiners and reconnections
- Understand [sessions and identity](https://ably.com/docs/ai-transport/sessions-identity.md) in AI enabled applications
- Explore the [message-per-response pattern](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) for storing complete AI responses as single messages in history

## Related Topics

- [Message per response](https://ably.com/docs/ai-transport/guides/langgraph/langgraph-message-per-response.md): Stream tokens from LangGraph over Ably in realtime using message appends.
- [Human-in-the-loop](https://ably.com/docs/ai-transport/guides/langgraph/langgraph-human-in-the-loop.md): Implement human approval workflows for AI agent tool calls using LangGraph and Ably with role-based access control.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
