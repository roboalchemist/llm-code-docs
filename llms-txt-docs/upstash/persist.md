# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/persist.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/persist.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/persist.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/persist.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/persist.md

# PERSIST

> Remove any timeout set on the key.

## Arguments

<ParamField body="key" type="string" required>
  The key to persist
</ParamField>

## Response

<ResponseField type="integer" required>
  `1` if the timeout was removed, `0` if `key` does not exist or does not have an associated timeout.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.persist(key);
  ```
</RequestExample>
