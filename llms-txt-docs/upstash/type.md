# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/type.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/type.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/type.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/type.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/type.md

# JSON.TYPE

> Report the type of JSON value at `path`.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path of the value.
</ParamField>

## Response

<ResponseField type="(string | null)[]" required>
  The type of the value at `path` or `null` if the value does not exist.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const myType = await redis.json.type("key", "$.path.to.value");
  ```
</RequestExample>
