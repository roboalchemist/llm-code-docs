# Source: https://upstash.com/docs/redis/sdks/ts/commands/pubsub/publish.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/pubsub/publish.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/publish.md

# Source: https://upstash.com/docs/qstash/api/publish.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/pubsub/publish.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/pubsub/publish.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/publish.md

# Source: https://upstash.com/docs/qstash/api/publish.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/pubsub/publish.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/pubsub/publish.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/publish.md

# Source: https://upstash.com/docs/qstash/api/publish.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/pubsub/publish.md

# PUBLISH

> Publish a message to a channel

## Arguments

<ParamField body="channel" type="string" required>
  The channel to publish to.
</ParamField>

<ParamField body="message" type="TMessage">
  The message to publish.
</ParamField>

## Response

<ResponseField type="integer" required>
  The number of clients who received the message.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const listeners = await redis.publish("my-channel", "my-message");
  ```
</RequestExample>
