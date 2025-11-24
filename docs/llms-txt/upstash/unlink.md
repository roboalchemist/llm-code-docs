# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/unlink.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/unlink.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/unlink.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/unlink.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/unlink.md

# UNLINK

> Removes the specified keys. A key is ignored if it does not exist.

## Arguments

<ParamField body="keys" type="...string[]" required>
  One or more keys to unlink.
</ParamField>

## Response

<ResponseField type="integer" required>
  The number of keys that were unlinked.
</ResponseField>

<RequestExample>
  ```ts Basic theme={"system"}
  await redis.unlink("key1", "key2");
  ```

  ```ts Array theme={"system"}
  // in case you have an array of keys
  const keys = ["key1", "key2"];
  await redis.unlink(...keys)

  ```
</RequestExample>
