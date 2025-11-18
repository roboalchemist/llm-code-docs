# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hkeys.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hkeys.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hkeys.md

# HKEYS

> Return all field names in the hash stored at key.

## Arguments

<ParamField body="key" type="string" required>
  The key of the hash.
</ParamField>

## Response

<ResponseField type="string[]" required>
  The field names of the hash
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.hset("key", {
    id: 1,
    username: "chronark",
    });
  const fields = await redis.hkeys("key");
  console.log(fields); // ["id", "username"]
  ```
</RequestExample>
