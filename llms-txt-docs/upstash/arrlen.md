# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/arrlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/arrlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/arrlen.md

# JSON.ARRLEN

> Report the length of the JSON array at `path` in `key`.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path of the array.
</ParamField>

## Response

<ResponseField type="integer[]" required>
  The length of the array.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const length = await redis.json.arrlen("key", "$.path.to.array");
  ```
</RequestExample>
