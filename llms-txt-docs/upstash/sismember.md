# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/sismember.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/set/sismember.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/sismember.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/set/sismember.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/sismember.md

# SISMEMBER

> Check if a member exists in a set

## Arguments

<ParamField body="key" type="string" required>
  The key of the set to check.
</ParamField>

<ParamField body="member" type="TMember">
  The member to check for.
</ParamField>

## Response

<ResponseField type="0 | 1" required>
  `1` if the member exists in the set, `0` if not.
</ResponseField>

<RequestExample>
  ```ts Example  theme={"system"}
  await redis.sadd("set", "a", "b", "c"); 
  const isMember =  await redis.sismember("set", "a");
  console.log(isMember); // 1
  ```
</RequestExample>
