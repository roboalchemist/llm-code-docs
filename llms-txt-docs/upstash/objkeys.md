# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/objkeys.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/objkeys.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/objkeys.md

# JSON.OBJKEYS

> Return the keys in the object that`s referenced by path.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path of the array.
</ParamField>

## Response

<ResponseField type="string[][]" required>
  The keys of the object at the path.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const keys = await redis.json.objkeys("key", "$.path");
  ```
</RequestExample>
