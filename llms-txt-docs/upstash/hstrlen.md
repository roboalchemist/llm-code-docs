# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hstrlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hstrlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hstrlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hstrlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hstrlen.md

# HSTRLEN

> Returns the string length of a value in a hash.

## Arguments

<ParamField body="key" type="string" required>
  The key of the hash.
</ParamField>

<ParamField body="field" type="string" required>
  The name of the field.
</ParamField>

## Response

<ResponseField type="integer" required>
  `0` if the hash or field does not exist. Otherwise the length of the string.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const length = await redis.hstrlen("key", "field")
  ```
</RequestExample>
