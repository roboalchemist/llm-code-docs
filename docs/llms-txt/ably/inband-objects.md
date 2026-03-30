# Source: https://ably.com/docs/liveobjects/inband-objects.md

# Inband Objects

<If lang="javascript">
  <Aside data-type='public-preview'>
  LiveObjects JavaScript is in Public Preview. We are committed to supporting the LiveObjects Javascript API and welcome adoption and feedback.

  **Building with LiveObjects?** Help shape its future by [sharing your use case](https://44qpp.share.hsforms.com/2fZobHQA1ToyRfB9xqZYQmQ).
  </Aside>
</If>
<If lang="swift">
  <Aside data-type='experimental'>
  LiveObjects Swift is currently Experimental. Its features are still in development and subject to rapid change.

  **Building with LiveObjects?** Help shape its future by [sharing your use case](https://44qpp.share.hsforms.com/2fZobHQA1ToyRfB9xqZYQmQ).
  </Aside>
</If>
<If lang="java">
  <Aside data-type='experimental'>
  LiveObjects Java is currently Experimental. Its features are still in development and subject to rapid change.

  **Building with LiveObjects?** Help shape its future by [sharing your use case](https://44qpp.share.hsforms.com/2fZobHQA1ToyRfB9xqZYQmQ).
  </Aside>
</If>

Inband objects enables clients to subscribe to LiveObjects updates in realtime, even on platforms that don't yet have a native LiveObjects Realtime client implementation.

<Aside data-type='note'>
If you're using LiveObjects from one of the the following languages, then use the LiveObjects plugin which has dedicated support for all LiveObjects features:

* [JavaScript/TypeScript](https://ably.com/docs/liveobjects/quickstart/javascript.md)
* [Swift](https://ably.com/docs/liveobjects/quickstart/swift.md)
* [Java](https://ably.com/docs/liveobjects/quickstart/java.md)

</Aside>

Inband objects works by delivering changes to channel objects as regular channel messages, similar to [inband occupancy](https://ably.com/docs/channels/options.md#occupancy).

<Aside data-type='usp'>
Scalable message fanout

Inband object updates are delivered as regular channel messages through Ably's [horizontally scalable architecture](https://ably.com/docs/platform/architecture/platform-scalability.md), so LiveObjects state changes can be distributed to any number of subscribers simultaneously.
</Aside>

## Enable Inband Objects

To enable inband objects, use the `objects` [channel parameter](https://ably.com/docs/channels/options.md#objects) when getting a channel:

<Code>

### Javascript

```
// When getting a channel instance
const channelOpts = { params: { objects: 'objects' } };
const channel = realtime.channels.get('my-channel', channelOpts);

// Or using setOptions on an existing channel
await channel.setOptions({ params: { objects: 'objects' } });
```

</Code>

<Aside data-type='important'>
Clients require the `channel-metadata` [capability](https://ably.com/docs/auth/capabilities.md) to receive inband objects updates.
</Aside>

## Subscribe to updates

When using inband objects, the client will receive special `[meta]objects` messages whenever the objects on the channel are updated. These messages provide a snapshot of the current set of objects on the channel.

<Aside data-type='note'>
If there is a high rate of updates to the channel objects the inband messages are throttled. However, the client is guaranteed to receive a sequence of inband messages after the last change occurs so that the latest data is always available.
</Aside>

[Subscribe](https://ably.com/docs/api/realtime-sdk/channels.md#subscribe) to `[meta]objects` messages like you would any other message on the channel. For convenience, use a message name filter to only receive messages with the name `[meta]objects` in your listener:

<Code>

### Javascript

```
// Subscribe to [meta]objects messages
channel.subscribe('[meta]objects', (message) => {
  const { syncId, nextCursor, object } = message.data;
  console.log("Received inband objects message:", syncId, nextCursor, JSON.stringify(message.data));
});
```

</Code>

## Message Format

Inband objects messages are sent as a sequence of messages, where each message contains a snapshot of a single object on the channel. Taken together, a set of messages belonging to the same sequence describes the complete set of objects on the channel.

Each inband objects message has a message `name` of `[meta]objects`.

The message `data` is a JSON object with the following top-level properties:

| Property | Description |
| -------- | ----------- |
| `syncId` | A unique ID for this sequence. All messages with the same `syncId` are part of the same sequence of messages which describes the complete set of the objects on the channel. |
| `nextCursor` | A cursor for the next message in the sequence, or `undefined` if this is the last message in the sequence. |
| `object` | A JSON representation of the object included in the message. |

The shape of the `object` is the same as the response format of an object when listing them via the [REST API](https://ably.com/docs/liveobjects/rest-api-usage.md#fetching-objects-list-values).

## Related Topics

* [Batch operations](https://ably.com/docs/liveobjects/batch.md): Group multiple objects operations into a single channel message to apply grouped operations atomically and improve performance.
* [Lifecycle events](https://ably.com/docs/liveobjects/lifecycle.md): Understand lifecycle events for Objects, LiveMap and LiveCounter to track synchronization events and object deletions.
* [Typing](https://ably.com/docs/liveobjects/typing.md): Type objects on a channel for type safety and code autocompletion.
* [Object storage](https://ably.com/docs/liveobjects/storage.md): Learn about LiveObjects object storage.
* [Using the REST API](https://ably.com/docs/liveobjects/rest-api-usage.md): Learn how to work with Ably LiveObjects using the REST API

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
