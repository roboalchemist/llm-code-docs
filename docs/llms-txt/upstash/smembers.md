# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/smembers.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/set/smembers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SMEMBERS

> Return all the members of a set

## Arguments

<ParamField body="key" type="str" required>
  The key of the set.
</ParamField>

## Response

<ResponseField type="set[str]" required>
  The members of the set.
</ResponseField>

<RequestExample>
  ```py Example  theme={"system"}
  redis.sadd("set", "a", "b", "c"); 
  assert redis.smembers("set") == {"a", "b", "c"}
  ```
</RequestExample>
