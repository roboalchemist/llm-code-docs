# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/decrby.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/decrby.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/decrby.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/decrby.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/decrby.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/decrby.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/decrby.md

# DECRBY

> Decrement the integer value of a key by a given number.

If a key does not exist, it is initialized as 0 before performing the operation. An error is returned if the key contains a value of the wrong type or contains a string that can not be represented as integer.

## Arguments

<ParamField body="key" type="string" required>
  The key to decrement.
</ParamField>

<ParamField body="decrementBy" type="integer" required>
  The amount to decrement by.
</ParamField>

## Response

<ResponseField type="integer" required>
  The value at the key after the decrementing.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.set("key", 6);
  await redis.decrby("key", 4);
  // returns 2
  ```
</RequestExample>
