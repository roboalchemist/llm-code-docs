# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/flushdb.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushdb.md

# FLUSHDB

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
  await redis.flushdb();
  ```

  ```ts Async theme={"system"}
  await redis.flushdb({async: true})
  ```
</RequestExample>
