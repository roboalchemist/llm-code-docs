# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/toggle.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/toggle.md

# JSON.TOGGLE

> Toggle a boolean value stored at `path`.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path of the boolean.
</ParamField>

## Response

<ResponseField type="boolean" required>
  The new value of the boolean.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const bool = await redis.json.toggle("key", "$.path.to.bool");
  ```
</RequestExample>
