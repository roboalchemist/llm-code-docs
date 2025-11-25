# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zpopmax.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zpopmax.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zpopmax.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zpopmax.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zpopmax.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zpopmax.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zpopmax.md

# ZPOPMAX

> Removes and returns up to count members with the highest scores in the sorted set stored at key.

## Arguments

<ParamField body="key" type="string" required>
  The key of the sorted set
</ParamField>

## Response

<ResponseField body="count" type="integer">
  The number of elements removed. Defaults to 1.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const popped = await redis.zpopmax("key", 4);
  ```
</RequestExample>
