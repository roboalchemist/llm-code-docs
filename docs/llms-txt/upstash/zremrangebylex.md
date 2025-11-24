# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebylex.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebylex.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebylex.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebylex.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebylex.md

# ZREMRANGEBYLEX

> Remove all members in a sorted set between the given lexicographical range.

## Arguments

<ParamField body="key" type="string" required>
  The key of the sorted set
</ParamField>

<ParamField body="min" type="string" required>
  The minimum lexicographical value to remove.
</ParamField>

<ParamField body="max" type="string" required>
  The maximum lexicographical value to remove.
</ParamField>

## Response

<ResponseField type="integer" required>
  The number of elements removed from the sorted set.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.zremrangebylex("key", "alpha", "omega")
  ```
</RequestExample>
