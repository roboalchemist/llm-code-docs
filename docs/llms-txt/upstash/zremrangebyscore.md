# Source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyscore.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebyscore.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ZREMRANGEBYSCORE

> Remove all members in a sorted set between the given scores.

## Arguments

<ParamField body="key" type="str" required>
  The key of the sorted set
</ParamField>

<ParamField body="min" type="str | float" required>
  The minimum score to remove.
</ParamField>

<ParamField body="min" type="str | float" required>
  The maximum score to remove.
</ParamField>

## Response

<ResponseField type="int" required>
  The number of elements removed from the sorted set.
</ResponseField>

<RequestExample>
  ```py Example theme={"system"}
  redis.zremrangebyscore("key", 2, 5)
  ```
</RequestExample>
