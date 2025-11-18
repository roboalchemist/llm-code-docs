# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/numincrby.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/numincrby.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/numincrby.md

# JSON.NUMINCRBY

> Increment the number value stored at `path` by number.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path of the array.
</ParamField>

<ParamField body="increment" type="number" required>
  The number to increment by.
</ParamField>

## Response

<ResponseField type="integer[]" required>
  The new value after incrementing
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const newValue = await redis.json.numincrby("key", "$.path.to.value", 2);
  ```
</RequestExample>
