# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/type.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/type.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/type.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/type.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TYPE

> Get the type of a key.

## Arguments

<ParamField body="key" type="str" required>
  The key to get.
</ParamField>

## Response

<ResponseField type="str" required>
  The type of the key.

  One of `string` | `list` | `set` | `zset` | `hash` | `none`
</ResponseField>

<RequestExample>
  ```py Example theme={"system"}
  redis.set("key1", "Hello")

  assert redis.type("key1") == "string"

  redis.lpush("key2", "Hello")

  assert redis.type("key2") == "list"

  assert redis.type("non-existent-key") == "none"
  ```
</RequestExample>
