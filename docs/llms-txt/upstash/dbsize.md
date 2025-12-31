# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/server/dbsize.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/server/dbsize.md

# DBSIZE

> Count the number of keys in the database.

## Arguments

This command has no arguments

## Response

<ResponseField type="integer" required>
  The number of keys in the database
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const keys = await redis.dbsize();
  console.log(keys) // 20
  ```
</RequestExample>
