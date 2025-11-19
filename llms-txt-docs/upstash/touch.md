# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/touch.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/touch.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/touch.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/touch.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/touch.md

# TOUCH

> Alters the last access time of one or more keys

## Arguments

<ParamField body="keys" type="...string[]" required>
  One or more keys.
</ParamField>

## Response

<ResponseField type="integer" required>
  The number of keys that were touched.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.touch("key1", "key2", "key3");
  ```
</RequestExample>
