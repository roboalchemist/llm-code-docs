# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/keys.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/keys.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/keys.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/keys.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/keys.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/keys.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/keys.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/keys.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/keys.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/keys.md

# KEYS

> Returns all keys matching pattern.

<Warning>
  This command may block the DB for a long time, depending on its size. We advice against using it in production. Use [SCAN](/redis/sdks/ts/commands/generic/scan) instead.
</Warning>

## Arguments

<ParamField body="match" type="string" required>
  A glob-style pattern. Use `*` to match all keys.
</ParamField>

## Response

<ResponseField type="string[]" required>
  Array of keys matching the pattern.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const keys = await redis.keys("prefix*");
  ```

  ```ts Match All theme={"system"}
  const keys = await redis.keys("*");
  ```
</RequestExample>
