# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/smembers.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/set/smembers.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/set/smembers.md

# SMEMBERS

> Return all the members of a set

## Arguments

<ParamField body="key" type="string" required>
  The key of the set.
</ParamField>

## Response

<ResponseField type="TMember[]" required>
  The members of the set.
</ResponseField>

<RequestExample>
  ```ts Example  theme={"system"}
  await redis.sadd("set", "a", "b", "c"); 
  const members =  await redis.smembers("set");
  console.log(members); // ["a", "b", "c"]
  ```
</RequestExample>
