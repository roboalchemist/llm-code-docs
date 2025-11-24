# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/srem.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/set/srem.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/srem.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/set/srem.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/srem.md

# SREM

> Remove one or more members from a set

## Arguments

<ParamField body="key" type="string" required>
  The key of the set to remove the member from.
</ParamField>

<ParamField body="members" type="...TMember[]">
  One or more members to remove from the set.
</ParamField>

## Response

<ResponseField type="integer" required>
  How many members were removed
</ResponseField>

<RequestExample>
  ```ts Example  theme={"system"}
  await redis.sadd("set", "a", "b", "c"); 
  const removed = await redis.srem("set", "a", "b", "d");
  console.log(removed); // 2
  ```
</RequestExample>
