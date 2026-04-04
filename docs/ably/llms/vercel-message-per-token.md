# Source: https://ably.com/docs/ai-transport/guides/vercel-ai-sdk/vercel-message-per-token.md

# Guide: Stream Vercel AI SDK responses using the message-per-token pattern

This guide shows you how to stream AI responses from the [Vercel AI SDK](https://ai-sdk.dev/docs/ai-sdk-core/generating-text) over Ably using the [message-per-token pattern](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md). Specifically, it implements the [explicit start/stop events approach](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md#explicit-events), which publishes each response token as an individual message, along with explicit lifecycle events to signal when responses begin and end.

Using Ably to distribute tokens from the Vercel AI SDK enables you to broadcast AI responses to thousands of concurrent subscribers with reliable message delivery and ordering guarantees, ensuring that each client receives the complete response stream with all tokens delivered in order. This approach decouples your AI inference from client connections, enabling you to scale agents independently and handle reconnections gracefully.

<Aside data-type="further-reading">
To discover other approaches to token streaming, including the [message-per-response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) pattern, see the [token streaming](https://ably.com/docs/ai-transport/token-streaming.md) documentation.
</Aside>

## Prerequisites

To follow this guide, you need:

- Node.js 20 or higher
- A Vercel AI Gateway API key
- An Ably API key

Useful links:

- [Vercel AI Gateway documentation](https://vercel.com/docs/ai-gateway)
- [Vercel AI SDK documentation](https://ai-sdk.dev/docs)
- [Ably JavaScript SDK getting started](https://ably.com/docs/getting-started/javascript.md)

Create a new Node project, which will contain the publisher and subscriber code:

<Code>

### Shell

```
mkdir ably-vercel-message-per-token && cd ably-vercel-message-per-token
npm init -y
```

</Code>

Install the required packages using NPM:

<Code>

### Shell

```
npm install ai@^6 ably@^2
```

</Code>

<Aside data-type="note">
This guide uses version 6.x of the AI SDK. You can use any model from any [supported provider](https://ai-sdk.dev/providers/ai-sdk-providers) by specifying it as a string (e.g., `'openai/gpt-4o'`, `'anthropic/claude-sonnet-4'`). Some details of interacting with the SDK may differ if using a different major version.
</Aside>

Export your Vercel AI Gateway API key to the environment, which will be used later in the guide by the Vercel AI SDK:

<Code>

### Shell

```
export AI_GATEWAY_API_KEY="your_api_key_here"
```

</Code>

## Step 1: Get a streamed response from Vercel AI SDK

Initialize the Vercel AI SDK and use [`streamText`](https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-text) to stream model output as a series of events.

Create a new file `agent.mjs` with the following contents:

<Code>

### Javascript

```
import { streamText } from 'ai';

// Process each streaming event
function processEvent(event) {
  console.log(JSON.stringify(event));
  // This function is updated in the next sections
}

// Create streaming response from Vercel AI SDK
async function streamVercelResponse(prompt) {
  const result = streamText({
    model: 'openai/gpt-4o',
    prompt: prompt,
  });

  // Iterate through streaming events using fullStream
  for await (const event of result.fullStream) {
    processEvent(event);
  }
}

// Usage example
streamVercelResponse("Tell me a short joke");
```

</Code>

### Understand Vercel AI SDK streaming events

The Vercel AI SDK's [`streamText`](https://ai-sdk.dev/docs/ai-sdk-core/generating-text#streamtext) function provides a [`fullStream`](https://ai-sdk.dev/docs/ai-sdk-core/generating-text#fullstream-property) property that returns all stream events. Each event includes a `type` property which describes the event type. A complete text response can be constructed from the following event types:

- [`text-start`](https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol#text-start-part): Signals the start of a text response. Contains an `id` to correlate subsequent events.

- [`text-delta`](https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol#text-delta-part): Contains a single text token in the `text` field. These events represent incremental text chunks as the model generates them.

- [`text-end`](https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol#text-end-part): Signals the completion of a text response.

The following example shows the event sequence received when streaming a response:

<Code>

#### Json

```
// 1. Stream initialization
{"type":"start"}
{"type":"start-step","request":{...}}
{"type":"text-start","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","providerMetadata":{...}}

// 2. Text tokens stream in as delta events
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":"Why"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" don't"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" skeleton"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":"s"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" fight"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" each"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" other"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":"?\n\n"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":"They"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" don't"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" have"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" the"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":" guts"}
{"type":"text-delta","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","text":"!"}

// 3. Stream completion
{"type":"text-end","id":"msg_0cc4da489ab9d4d101696f97d7c9548196a04f71d10a3a4c99","providerMetadata":{...}}
{"type":"finish-step","finishReason":"stop","usage":{"inputTokens":12,"outputTokens":15,"totalTokens":27,"reasoningTokens":0,"cachedInputTokens":0},"providerMetadata":{...}}
{"type":"finish","finishReason":"stop","totalUsage":{"inputTokens":12,"outputTokens":15,"totalTokens":27,"reasoningTokens":0,"cachedInputTokens":0}}
```

</Code>

<Aside data-type="note">
This is only an illustrative example for a simple "text in, text out" use case and may not reflect the exact sequence of events that you observe from the Vercel AI SDK. The SDK also supports other event types such as `reasoning-delta` for chain-of-thought reasoning, `tool-call` for function calling, and `error` for handling failures. For complete details on all event types and their properties, see [Vercel AI SDK fullStream reference](https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-text#full-stream).
</Aside>

## Step 2: Publish streaming events to Ably

Publish Vercel AI SDK streaming events to Ably to reliably and scalably distribute them to subscribers.

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

### Map Vercel AI SDK streaming events to Ably messages

Choose how to map [Vercel AI SDK streaming events](#understand-streaming-events) to Ably [messages](https://ably.com/docs/messages.md). You can choose any mapping strategy that suits your application's needs. This guide uses the following pattern as an example:

- `start`: Signals the beginning of a response
- `token`: Contains the incremental text content for each delta
- `stop`: Signals the completion of a response

Update your `agent.mjs` file to initialize the Ably client and update the `processEvent()` function to publish events to Ably:

<Code>

#### Javascript

```
// Track response ID across events
let responseId = null;

// Process each streaming event and publish to Ably
function processEvent(event) {
  switch (event.type) {
    case 'text-start':
      // Capture response ID from text-start event
      responseId = event.id;

      // Publish start event with response ID
      channel.publish({
        name: 'start',
        extras: {
          headers: { responseId }
        }
      });
      break;

    case 'text-delta':
      // Publish each text delta as a token
      channel.publish({
        name: 'token',
        data: event.text,
        extras: {
          headers: { responseId }
        }
      });
      break;

    case 'text-end':
      // Publish stop event when stream completes
      channel.publish({
        name: 'stop',
        extras: {
          headers: { responseId }
        }
      });
      break;
  }
}
```

</Code>

This implementation:

- Captures the `responseId` from the `text-start` event
- Publishes a `start` event at the beginning of the response
- Filters for `text-delta` events and publishes them as `token` events
- Publishes a `stop` event when the response completes using the `text-end` event
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

- [Message per response](https://ably.com/docs/ai-transport/guides/vercel-ai-sdk/vercel-message-per-response.md): Stream tokens from the Vercel AI SDK over Ably in realtime using message appends.
- [Human-in-the-loop](https://ably.com/docs/ai-transport/guides/vercel-ai-sdk/vercel-human-in-the-loop.md): Implement human approval workflows for AI agent tool calls using the Vercel AI SDK and Ably with role-based access control.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
