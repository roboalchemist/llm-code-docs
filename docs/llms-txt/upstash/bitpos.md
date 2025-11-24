# Source: https://upstash.com/docs/redis/sdks/ts/commands/bitmap/bitpos.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/bitmap/bitpos.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/bitmap/bitpos.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/bitmap/bitpos.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/bitmap/bitpos.md

# BITPOS

> Find the position of the first set or clear bit (bit with a value of 1 or 0) in a Redis string key.

## Arguments

<ParamField body="key" type="string" required>
  The key to search in.
</ParamField>

<ParamField body="bit" type="0 | 1" required>
  The key to store the result of the operation in.
</ParamField>

<ParamField body="start" type="number">
  The index to start searching at.
</ParamField>

<ParamField body="end" type="number">
  The index to stop searching at.
</ParamField>

## Response

<ResponseField type="integer" required>
  The index of the first occurrence of the bit in the string.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
   await redis.bitpos("key", 1);
  ```

  ```ts With Range theme={"system"}
   await redis.bitpos("key", 1, 5, 20);
  ```
</RequestExample>
