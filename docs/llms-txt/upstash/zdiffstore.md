# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zdiffstore.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zdiffstore.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zdiffstore.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zdiffstore.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zdiffstore.md

# ZDIFFSTORE

> Writes the difference between sets to a new key.

## Arguments

<ParamField body="destination" type="string" required>
  The key to write the difference to.
</ParamField>

<ParamField body="keys" type="integer" required>
  How many keys to compare.
</ParamField>

<ParamField body="keys" type="...string[]" required>
  The keys to compare.
</ParamField>

## Response

<ResponseField required>
  The number of elements in the resulting set.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const values = await redis.zdiffstore("destination", 2, "key1", "key2");
  ```
</RequestExample>
