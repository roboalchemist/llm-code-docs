# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/mset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/mset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/mset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/mset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/mset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/mset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/mset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/mset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/mset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/mset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/mset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/mset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/mset.md

# MSET

> Set multiple keys in one go.

For billing purposes, this counts as a single command.

## Arguments

<ParamField body="params" type="Record<string, TValue>" required>
  An object where the keys are the keys to set, and the values are the values to set.
</ParamField>

## Response

<ResponseField type="string" required>
  "OK"
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.mset({
      key1: 1,
      key2: "hello",
      key3: { a: 1, b: "hello" },
  });
  ```
</RequestExample>
