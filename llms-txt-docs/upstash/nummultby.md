# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/nummultby.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/nummultby.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/nummultby.md

# JSON.NUMMULTBY

> Multiply the number value stored at `path` by number.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path of the array.
</ParamField>

<ParamField body="multiply" type="number" required>
  The number to multiply by.
</ParamField>

## Response

<ResponseField type="integer[]" required>
  The new value after multiplying
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const newValue = await redis.json.nummultby("key", "$.path.to.value", 2);
  ```
</RequestExample>
