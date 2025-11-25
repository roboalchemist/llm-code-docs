# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/objlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/objlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/objlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/objlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/objlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/objlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/objlen.md

# JSON.OBJLEN

> Report the number of keys in the JSON object at `path` in `key`.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path of the object.
</ParamField>

## Response

<ResponseField type="integer[]" required>
  The number of keys in the objects.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const lengths = await redis.json.objlen("key", "$.path");
  ```
</RequestExample>
