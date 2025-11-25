# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/clear.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/clear.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/clear.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/clear.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/clear.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/clear.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/clear.md

# JSON.CLEAR

> Clear container values (arrays/objects) and set numeric values to 0.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path to clear
</ParamField>

## Response

<ResponseField type="integer[]" required>
  How many values were cleared.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.json.clear("key");
  ```

  ```ts With path theme={"system"}
  await redis.json.clear("key", "$.my.key");
  ```
</RequestExample>
