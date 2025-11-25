# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/randomkey.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/randomkey.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/randomkey.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/randomkey.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/randomkey.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/randomkey.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/randomkey.md

# RANDOMKEY

> Returns a random key from database

## Arguments

No arguments

## Response

<ResponseField type="string" required>
  A random key from database, or `null` when database is empty.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const key = await redis.randomkey();
  ```
</RequestExample>
