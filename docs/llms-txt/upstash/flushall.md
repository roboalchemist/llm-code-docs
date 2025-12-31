# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushall.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushall.md

# FLUSHALL

<Warning>
  Deletes all keys permanently. Use with caution!
</Warning>

## Arguments

<ParamField body="async" type="boolean">
  Whether to perform the operation asynchronously.
  Defaults to synchronous.
</ParamField>

<RequestExample>
  ```ts Sync theme={"system"}
  await redis.flushall();
  ```

  ```ts Async theme={"system"}
  await redis.flushall({async: true})
  ```
</RequestExample>
