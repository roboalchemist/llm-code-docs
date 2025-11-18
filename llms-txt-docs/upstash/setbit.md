# Source: https://upstash.com/docs/redis/sdks/ts/commands/bitmap/setbit.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/bitmap/setbit.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/bitmap/setbit.md

# SETBIT

> Set a single bit in a string.

## Arguments

<ParamField body="key" type="string" required>
  The key of the bitset
</ParamField>

<ParamField body="offset" type="integer" required>
  Specify the offset at which to set the bit.
</ParamField>

<ParamField body="value" type="0 | 1" required>
  The bit to set
</ParamField>

## Response

<ResponseField type="0 | 1" required>
  The original bit value stored at offset.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const originalBit = await redis.setbit(key, 4, 1);
  ```
</RequestExample>
