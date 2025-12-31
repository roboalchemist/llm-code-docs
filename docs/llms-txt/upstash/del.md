# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/del.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/del.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/del.md

# JSON.DEL

> Delete a key from a JSON document.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path to delete
</ParamField>

## Response

<ResponseField type="integer" required>
  How many paths were deleted.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.json.del("key", "$.path.to.value");
  ```
</RequestExample>
