# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hlen.md

# HLEN

> Returns the number of fields contained in the hash stored at key.

## Arguments

<ParamField body="key" type="string" required>
  The key of the hash.
</ParamField>

## Response

<ResponseField type="integer" required>
  How many fields are in the hash.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.hset("key", {
    id: 1,
    username: "chronark",
    });
  const fields = await redis.hlen("key");
  console.log(fields); // 2
  ```
</RequestExample>
