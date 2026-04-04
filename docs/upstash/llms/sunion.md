# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/sunion.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/set/sunion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SUNION

> Return the union between sets

## Arguments

<ParamField body="keys" type="*List[str]" required>
  The keys of the sets to perform the union operation on.
</ParamField>

## Response

<ResponseField type="set[str]" required>
  The resulting set
</ResponseField>

<RequestExample>
  ```py Example  theme={"system"}
  redis.sadd("key1", "a", "b", "c")

  redis.sadd("key2", "c", "d", "e")

  assert redis.sunion("key1", "key2") == {"a", "b", "c", "d", "e"}
  ```
</RequestExample>
