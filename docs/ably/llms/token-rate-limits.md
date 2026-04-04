# Source: https://ably.com/docs/ai-transport/token-streaming/token-rate-limits.md

# Token streaming limits

LLM token streaming introduces high-rate or bursty traffic patterns to your application, with some models outputting upwards of 150 distinct events (that is, tokens or response deltas) per second. Output rates can vary unpredictably over the lifetime of a response stream, and you have limited control over third-party model behaviour. AI Transport provides functionality to help you stay within your [rate limits](https://ably.com/docs/platform/pricing/limits.md) while delivering a great experience to your users.

Ably's limits divide into two categories:

1. Limits relating to usage across an account, such as the total number of messages sent in a month, or the aggregate instantaneous message rate across all connections and channels
2. Limits relating to the capacity of a single resource, such as a connection or a channel

Limits in the first category exist to provide protection in the case of accidental spikes or deliberate abuse. Provided that your package is sized correctly for your use-case, these limits should not be hit as a result of valid traffic.

The limits in the second category, however, cannot be increased arbitrarily and exist to protect the integrity of the service. The limits associated with individual connections or channels can be relevant to LLM token streaming use-cases. The following sections discuss these limits in particular.

## Message-per-response

The [message-per-response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) pattern includes automatic rate limit protection. AI Transport prevents a single response stream from reaching the message rate limit for a connection by rolling up multiple appends into a single published message:

1. Your agent streams tokens to the channel at the model's output rate
2. Ably publishes the first token immediately, then automatically rolls up subsequent tokens on receipt
3. Clients receive the same content, delivered in fewer discrete messages

By default, Ably delivers a single response stream at 25 messages per second or the model output rate, whichever is lower. This means you can publish two simultaneous response streams on the same channel or connection with any [Ably package](https://ably.com/docs/platform/pricing.md#packages), because each stream uses half of the [connection inbound message rate](https://ably.com/docs/platform/pricing/limits.md#connection). Ably charges for the number of published messages, not for the number of streamed tokens.

### Configure rollup behaviour

Ably concatenates all appends for a single response that are received during the rollup window into one published message. You can specify the rollup window for a particular connection by setting the `appendRollupWindow` [transport parameter](https://ably.com/docs/api/realtime-sdk.md#client-options). This allows you to determine how much of the connection message rate can be consumed by a single response stream and control your consumption costs.

| `appendRollupWindow` | Maximum message rate for a single response |
|---|---|
| 0ms | Model output rate |
| 20ms | 50 messages/s |
| 40ms *(default)* | 25 messages/s |
| 100ms | 10 messages/s |
| 500ms *(max)* | 2 messages/s |

The following example code demonstrates establishing a connection to Ably with `appendRollupWindow` set to 100ms:

<Code>

#### Javascript

```
const ably = new Ably.Realtime(
  {
    key: 'your-api-key',
    transportParams: { appendRollupWindow: 100 }
  }
);
```

#### Python

```
ably = AblyRealtime(
    key='your-api-key',
    transport_params={'appendRollupWindow': 100}
)
```

#### Java

```
ClientOptions options = new ClientOptions();
options.key = "your-api-key";
options.transportParams = Map.of("appendRollupWindow", "100");
AblyRealtime ably = new AblyRealtime(options);
```

</Code>

<Aside data-type="important">
If you configure the `appendRollupWindow` to allow a single response to use more than your [connection inbound message rate](https://ably.com/docs/platform/pricing/limits.md#connection) then you will see [limit enforcement](https://ably.com/docs/platform/pricing/limits.md#hitting) behaviour if you stream tokens faster than the allowed message rate.
</Aside>

## Message-per-token

The [message-per-token](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md) pattern requires you to manage rate limits directly. Each token publishes as a separate message, so high-speed model output can cause per-connection or per-channel rate limits to be hit, as well as consuming overall message allowances quickly.

To stay within limits:

- Calculate your headroom by comparing your model's peak output rate against your package's [connection inbound message rate](https://ably.com/docs/platform/pricing/limits.md#connection)
- Account for concurrency by multiplying peak rates by the maximum number of simultaneous streams your application supports
- If required, batch tokens in your agent before publishing to the SDK, reducing message count while maintaining delivery speed
- Enable [server-side batching](https://ably.com/docs/messages/batch.md#server-side) to reduce the number of messages delivered to your subscribers

If your application requires higher message rates than your current package allows, [contact Ably](https://ably.com/contact) to discuss options.

## Next steps

- Review [Ably platform limits](https://ably.com/docs/platform/pricing/limits.md) to understand rate limit thresholds for your package
- Learn about the [message-per-response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md) pattern for automatic rate limit protection
- Learn about the [message-per-token](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md) pattern for fine-grained control

## Related Topics

- [Overview](https://ably.com/docs/ai-transport/token-streaming.md): Learn about token streaming with Ably AI Transport, including common patterns and the features provided by the Ably solution.
- [Message per response](https://ably.com/docs/ai-transport/token-streaming/message-per-response.md): Stream individual tokens from AI models into a single message over Ably.
- [Message per token](https://ably.com/docs/ai-transport/token-streaming/message-per-token.md): Stream individual tokens from AI models as separate messages over Ably.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
