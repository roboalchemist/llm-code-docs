# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hexists.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hexists.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hexists.md

# HEXISTS

> Checks if a field exists in a hash.

## Arguments

<ParamField body="key" type="string" required>
  The key to get.
</ParamField>

<ParamField body="field" type="string" required>
  The field to check.
</ParamField>

## Response

<ResponseField type="integer" required>
  `1` if the hash contains `field`. `0` if the hash does not contain `field`, or `key` does not exist.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.hset("key", "field", "value");
  const exists = await redis.hexists("key", "field");

  console.log(exists); // 1
  ```
</RequestExample>
