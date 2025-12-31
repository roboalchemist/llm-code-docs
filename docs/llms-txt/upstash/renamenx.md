# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/renamenx.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/renamenx.md

# RENAMENX

> Rename a key if it does not already exist.

## Arguments

<ParamField body="source" type="string" required>
  The original key.
</ParamField>

<ParamField body="destination" type="string" required>
  A new name for the key.
</ParamField>

## Response

<ResponseField type="0 | 1" required>
  `1` if key was renamed, `0` if key was not renamed.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const renamed = await redis.renamenx("old", "new");
  ```
</RequestExample>
