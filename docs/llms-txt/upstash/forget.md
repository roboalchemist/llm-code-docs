# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/forget.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/forget.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/forget.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/forget.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/forget.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/forget.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/forget.md

# JSON.FORGET

> Delete a key from a JSON document.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path to forget.
</ParamField>

## Response

<ResponseField type="integer" required>
  How many paths were deleted.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.json.forget("key", "$.path.to.value");
  ```
</RequestExample>
