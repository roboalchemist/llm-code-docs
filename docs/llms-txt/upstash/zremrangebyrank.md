# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebyrank.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyrank.md

# ZREMRANGEBYRANK

> Remove all members in a sorted set between the given ranks.

## Arguments

<ParamField body="key" type="string" required>
  The key of the sorted set
</ParamField>

<ParamField body="min" type="number" required>
  The minimum rank to remove.
</ParamField>

<ParamField body="max" type="number" required>
  The maximum rank to remove.
</ParamField>

## Response

<ResponseField type="integer" required>
  The number of elements removed from the sorted set.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.zremrangebyrank("key", 4, 20)
  ```
</RequestExample>
