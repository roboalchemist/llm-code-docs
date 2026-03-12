# Source: https://ably.com/docs/ai-transport/messaging/completion-and-cancellation.md

# Completion and cancellation

AI responses streamed using the [message-per-response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) or [message-per-token](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md) pattern do not require explicit completion signals to function. Subscribers receive tokens as they arrive and can render them progressively. However, some applications benefit from explicitly signalling when a response is complete, or allowing users to cancel an in-progress response.

## Benefits of completion and cancellation signals

Explicit completion and cancellation signals are useful when your application needs to:

- Detect whether a response is still in progress after reconnection, so clients can distinguish between a completed response and one that is still streaming
- Finalize UI state when a response ends, such as removing typing indicators or enabling input controls
- Allow users to abort a response mid-stream, stopping generation and saving compute resources
- Coordinate multiple content parts within a single response, where downstream logic depends on knowing when each part is finished

## Signal completion

Use [operation metadata](https://ably.com/docs/messages/updates-deletes.md#append-operation-metadata) to signal that a content part or response is complete. Operation metadata is a set of key-value pairs carried on each append or update operation. Subscribers can inspect this metadata to determine the current phase of a message.

### Content-part completion

When streaming content using the [message-per-response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) pattern, signal that a content part is complete by appending an empty string with a metadata marker. The empty append does not change the message's data, but the metadata signals to subscribers that no more content follows for this message.

This keeps the entire content lifecycle (create, stream, done) within a single Ably message:

<Code>

#### Javascript

```
const channel = realtime.channels.get('ai:your-channel-name');

// Publish initial message
const { serials: [msgSerial] } = await channel.publish({ name: 'response', data: '' });

// Stream tokens
for await (const event of stream) {
  if (event.type === 'token') {
    channel.appendMessage({
      serial: msgSerial,
      data: event.text
    }, {
      metadata: { phase: 'streaming' }
    });
  }
}

// Signal content-part completion with an empty append
channel.appendMessage({
  serial: msgSerial,
  data: ''
}, {
  metadata: { phase: 'done' }
});
```

#### Python

```
channel = realtime.channels.get('ai:your-channel-name')

# Publish initial message
message = Message(name='response', data='')
result = await channel.publish(message)
msg_serial = result.serials[0]

# Stream tokens
async for event in stream:
    if event['type'] == 'token':
        channel.append_message(
            serial=msg_serial,
            data=event['text'],
            metadata={'phase': 'streaming'}
        )

# Signal content-part completion with an empty append
channel.append_message(
    serial=msg_serial,
    data='',
    metadata={'phase': 'done'}
)
```

#### Java

```
Channel channel = realtime.channels.get("ai:your-channel-name");

// Publish initial message
CompletableFuture<PublishResult> publishFuture = new CompletableFuture<>();
channel.publish("response", "", new Callback<PublishResult>() {
    @Override
    public void onSuccess(PublishResult result) {
        publishFuture.complete(result);
    }

    @Override
    public void onError(ErrorInfo reason) {
        publishFuture.completeExceptionally(AblyException.fromErrorInfo(reason));
    }
});
String msgSerial = publishFuture.get().serials[0];

// Stream tokens
for (Event event : stream) {
    if (event.getType().equals("token")) {
        MessageMetadata metadata = new MessageMetadata();
        metadata.put("phase", "streaming");
        channel.appendMessage(msgSerial, event.getText(), metadata);
    }
}

// Signal content-part completion with an empty append
MessageMetadata metadata = new MessageMetadata();
metadata.put("phase", "done");
channel.appendMessage(msgSerial, "", metadata);
```

</Code>

<Aside data-type="note">
The completion append does not need to be awaited. Appends to the same message serial are delivered in order, so the completion marker is guaranteed to arrive after all previous tokens for that content part.
</Aside>

### Response-level completion

A single AI response may span multiple content parts, each represented as a separate Ably message with its own stream of appends. To signal that the entire response is complete, publish a discrete message after all content parts are finished. Subscribers can use this as a cue to finalize the response in the UI.

<Code>

#### Javascript

```
// After all content parts are done, signal response-level completion
await channel.publish({
  name: 'response-end',
  data: '',
  extras: {
    headers: {
      responseId: 'resp_abc123'
    }
  }
});
```

#### Python

```
# After all content parts are done, signal response-level completion
await channel.publish(Message(
    name='response-end',
    data='',
    extras={
        'headers': {
            'responseId': 'resp_abc123'
        }
    }
))
```

#### Java

```
// After all content parts are done, signal response-level completion
JsonObject extras = new JsonObject();
JsonObject headers = new JsonObject();
headers.addProperty("responseId", "resp_abc123");
extras.add("headers", headers);

channel.publish(new Message("response-end", "", new MessageExtras(extras)));
```

</Code>

<Aside data-type="note">
Await all pending append operations before publishing the response-level completion message. Appends to the same message serial are always delivered in order regardless of whether you await the acknowledgment, but create and append operations issued without awaiting the acknowledgment can race to be accepted by Ably. Without awaiting, the completion message could arrive before the last content token.
</Aside>

### Detect completion from history

When [hydrating client state](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md#hydration) from history, inspect `version.metadata` on each message to determine whether a content part was fully completed or is still in progress. If the most recent operation's metadata carries your completion marker, the content part is done. If it carries a streaming marker or no marker, the stream may still be active.

<Code>

#### Javascript

```
const channel = realtime.channels.get('ai:your-channel-name');

await channel.subscribe((message) => {
  // ...handle message actions as normal...
});

let page = await channel.history({ untilAttach: true });

while (page) {
  for (const message of page.items) {
    const phase = message.version?.metadata?.phase;

    if (phase === 'done') {
      // Content part is complete, render as final
    } else {
      // Content part may still be streaming, listen for live appends
    }
  }
  page = page.hasNext() ? await page.next() : null;
}
```

#### Python

```
channel = realtime.channels.get('ai:your-channel-name')

await channel.subscribe(on_message)

page = await channel.history(until_attach=True)

while page:
    for message in page.items:
        phase = getattr(message.version, 'metadata', {}).get('phase')

        if phase == 'done':
            # Content part is complete, render as final
            pass
        else:
            # Content part may still be streaming, listen for live appends
            pass

    page = await page.next() if page.has_next() else None
```

#### Java

```
Channel channel = realtime.channels.get("ai:your-channel-name");

channel.subscribe(message -> { /* handle message actions as normal */ });

PaginatedResult<Message> page = channel.history(new Param("untilAttach", "true"));

while (page != null) {
    for (Message message : page.items()) {
        String phase = message.version != null && message.version.metadata != null
            ? message.version.metadata.get("phase")
            : null;

        if ("done".equals(phase)) {
            // Content part is complete, render as final
        } else {
            // Content part may still be streaming, listen for live appends
        }
    }
    page = page.hasNext() ? page.next() : null;
}
```

</Code>

<Aside data-type="important">
Operation metadata is last-write-wins. Each operation's `version.metadata` overwrites all previous values on the message rather than merging with them. The metadata visible on a message in history reflects only the most recent operation. This is what makes the empty-append-with-completion-marker pattern work: the final append sets `phase: 'done'`, and that is what persists on the message.
</Aside>

## Cancel a response

Cancellation allows users to stop an in-progress response. The subscriber publishes a cancellation message on the channel, and the publisher stops generating and flushes any pending operations.

### How it works

1. The subscriber publishes a cancellation message on the channel with a response ID identifying the response to cancel.
2. The publisher receives the cancellation message, stops generating, and flushes any pending append operations.
3. The publisher optionally publishes a confirmation message to signal clean shutdown to other subscribers.

### Publish a cancellation request

The subscriber sends a cancellation message with a `responseId` in the message [extras](https://ably.com/docs/messages.md#properties) to identify which response to cancel:

<Code>

#### Javascript

```
const channel = realtime.channels.get('ai:your-channel-name');

// Send cancellation request for a specific response
await channel.publish({
  name: 'cancel',
  data: '',
  extras: {
    headers: {
      responseId: 'resp_abc123'
    }
  }
});
```

#### Python

```
channel = realtime.channels.get('ai:your-channel-name')

# Send cancellation request for a specific response
await channel.publish(Message(
    name='cancel',
    data='',
    extras={
        'headers': {
            'responseId': 'resp_abc123'
        }
    }
))
```

#### Java

```
Channel channel = realtime.channels.get("ai:your-channel-name");

// Send cancellation request for a specific response
JsonObject extras = new JsonObject();
JsonObject headers = new JsonObject();
headers.addProperty("responseId", "resp_abc123");
extras.add("headers", headers);

channel.publish(new Message("cancel", "", new MessageExtras(extras)));
```

</Code>

### Handle cancellation

The publisher subscribes for cancellation messages and stops generation when one arrives. After stopping, flush any pending append operations before optionally publishing a confirmation message:

<Code>

#### Javascript

```
const channel = realtime.channels.get('ai:your-channel-name');

// Track pending appends for flushing
const pendingAppends = [];

// Listen for cancellation requests
await channel.subscribe('cancel', async (message) => {
  const responseId = message.extras?.headers?.responseId;

  // Stop generation for the matching response
  stopGeneration(responseId);

  // Flush any pending appends before confirming
  await Promise.all(pendingAppends);

  // Optionally confirm cancellation to all subscribers
  await channel.publish({
    name: 'cancelled',
    data: '',
    extras: {
      headers: {
        responseId
      }
    }
  });
});
```

#### Python

```
channel = realtime.channels.get('ai:your-channel-name')

# Track pending appends for flushing
pending_appends = []

# Listen for cancellation requests
async def on_cancel(message):
    response_id = message.extras.get('headers', {}).get('responseId')

    # Stop generation for the matching response
    stop_generation(response_id)

    # Flush any pending appends before confirming
    await asyncio.gather(*pending_appends)

    # Optionally confirm cancellation to all subscribers
    await channel.publish(Message(
        name='cancelled',
        data='',
        extras={
            'headers': {
                'responseId': response_id
            }
        }
    ))

await channel.subscribe('cancel', on_cancel)
```

#### Java

```
Channel channel = realtime.channels.get("ai:your-channel-name");

// Listen for cancellation requests
channel.subscribe("cancel", message -> {
    JsonObject headers = message.extras.asJsonObject().get("headers").getAsJsonObject();
    String responseId = headers != null ? headers.get("responseId").getAsString() : null;

    // Stop generation for the matching response
    stopGeneration(responseId);

    // Flush any pending appends before confirming
    flushPendingAppends();

    // Optionally confirm cancellation to all subscribers
    JsonObject confirmExtras = new JsonObject();
    JsonObject confirmHeaders = new JsonObject();
    confirmHeaders.addProperty("responseId", responseId);
    confirmExtras.add("headers", confirmHeaders);

    channel.publish(new Message("cancelled", "", new MessageExtras(confirmExtras)));
});
```

</Code>

<Aside data-type="note">
Cancellation is fire-and-forget. No acknowledgment round-trip is needed between the subscriber and publisher. The optional confirmation message is a convenience for other subscribers to update their UI, not a required handshake.
</Aside>

<Aside data-type="further-reading">
- Learn about the [message-per-response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) and [message-per-token](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md) token streaming patterns
- Use [online status](https://ably.com/docs/ai-transport/sessions-identity/online-status.md) to detect agent availability via presence
- Use [correlation metadata](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md#publishing-with-metadata) to match responses to their requests
</Aside>

## Related Topics

- [Accepting user input](https://ably.com/docs/ai-transport/messaging/accepting-user-input.md): Enable users to send prompts to AI agents over Ably with verified identity and message correlation.
- [Tool calls](https://ably.com/docs/ai-transport/messaging/tool-calls.md): Stream tool call execution visibility to users, enabling transparent AI interactions and generative UI experiences.
- [Human-in-the-loop](https://ably.com/docs/ai-transport/messaging/human-in-the-loop.md): Implement human-in-the-loop workflows for AI agents using Ably capabilities and claims to ensure authorized users approve sensitive tool calls.
- [Chain of thought](https://ably.com/docs/ai-transport/messaging/chain-of-thought.md): Stream chain-of-thought reasoning from thinking models in AI applications
- [Citations](https://ably.com/docs/ai-transport/messaging/citations.md): Attach source citations to AI responses using message annotations

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
